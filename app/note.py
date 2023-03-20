from . import schemas, models
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status, APIRouter, Response
from .database import get_db

router = APIRouter()

# [...] get all records
@router.get('/')
def get_notes(db: Session = Depends(get_db), limit: int = 10, page: int = 1, search: str = ''):
    skip = (page - 1) * limit

    notes = db.query(models.Note).filter(
        models.Note.title.contains(search)).limit(limit).offset(skip).all()
    return {'status': 'success', 'results': len(notes), 'notes': notes}


# [...] create record
@router.post('/', status_code=status.HTTP_201_CREATED)
def create_note(payload: schemas.NoteBaseSchema, db: Session = Depends(get_db)):
    new_note = models.Note(**payload.dict()) #We created an instance of the SQLAlchemy model
    db.add(new_note) # only registers a transaction operation without communicating it to the database.
    db.commit() #the .commit() method will be called to persist the data permanently in the database
    db.refresh(new_note) # get an up-to-date version of the newly-created record.
    return {"status": "success", "note": new_note}

# [...] edit record
@router.patch('/{noteId}')
def update_note(noteId: str, payload: schemas.NoteBaseSchema, db: Session = Depends(get_db)):
    # In the code below, we created the database query by chaining
    # the .query() and .filter() methods. After that, we evoked
    # the .first() method to return the first record that matches
    # our query.
    note_query = db.query(models.Note).filter(models.Note.id == noteId)
    db_note = note_query.first()

    if not db_note:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'No note with this id: {noteId} found')
    update_data = payload.dict(exclude_unset=True)
    # Next, we called the .dict() method on the payload JSON object
    # and assigned the result to the update_data variable before
    # passing it to the .update() method.
    note_query.filter(models.Note.id == noteId).update(update_data,
                                                       synchronize_session=False)
    db.commit()
    # Finally, we called the .commit() method to persist the data in
    # the database and returned the updated record to the client.
    db.refresh(db_note)
    return {"status": "success", "note": db_note}


# [...] get single record
@router.get('/{noteId}')
def get_post(noteId: str, db: Session = Depends(get_db)):
    note = db.query(models.Note).filter(models.Note.id == noteId).first()
    if not note:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"No note with this id: {id} found")
    return {"status": "success", "note": note}


# [...] delete record
@router.delete('/{noteId}')
def delete_post(noteId: str, db: Session = Depends(get_db)):
    # The fifth and final path operation function will perform a DELETE
    # operation to remove a single record from the database. When a
    # DELETE request is made to the /api/notes/{noteId} endpoint,
    # FastAPI will evoke this route controller to remove the record
    # that matches the query.
    note_query = db.query(models.Note).filter(models.Note.id == noteId)
    note = note_query.first()
    # The route handler will first query the database to check if a
    # record with that ID exists before the .delete() method will be
    # called to remove that record from the database.
    if not note:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'No note with this id: {id} found')
    note_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

