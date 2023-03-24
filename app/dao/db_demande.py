from sqlalchemy.orm.session import Session
from app.dao.schema import DemandeBase
from app.dao.models import DbDemande
from app.dao.hash import Hash


def create_demande(db: Session, request: DemandeBase):
    new_demande = DbDemande(
        destinataire = request.destinataire,
        expediteur = request.expediteur,
        password = Hash.bcrypt(request.password),
        sujet = request.sujet,
        message = request.message,
        mois = request.mois,
        jour = request.jour,
        heure = request.minutes,
        est_envoye = request.est_envoye
    )
    db.add(new_demande)
    db.commit()
    db.refresh(new_demande)
    return new_demande


def get_all_demandes(db: Session):
    return db.query(DbDemande).all()

def get_demande(db: Session, id:int):
    return db.query(DbDemande).filter(DbDemande.id == id).first()