"""Contient les requetes en base de données des demandes
"""
from sqlalchemy.orm.session import Session
from sqlalchemy import and_
from app.dao.schema import DemandeBase
from app.dao.models import DbDemande
from app.dao.hash import Hash
import datetime as dt

def create_demande(db: Session, request: DemandeBase):
    new_demande = DbDemande(
        destinataire = request.destinataire,
        expediteur = request.expediteur,
        password = request.password, #Hash.bcrypt(request.password),
        sujet = request.sujet,
        message = request.message,
        mois = request.mois,
        jour = request.jour,
        heure = request.heure,
        minutes = request.minutes,
        est_envoye = request.est_envoye
    )
    db.add(new_demande)
    db.commit()
    db.refresh(new_demande)
    return new_demande


def get_all_demandes(db: Session):
    return db.query(DbDemande).all()

def get_demande(db: Session, id:int):
    # Handle any exceptions
    return db.query(DbDemande).filter(DbDemande.id == id).first()

def get_demande_to_send(db: Session):
    now = dt.datetime.now()
    month = now.month
    day = now.day
    hour_of_now = now.hour
    minutes_of_now = now.minute

    demandes = db.query(DbDemande).filter(DbDemande.est_envoye == False).filter(DbDemande.mois <= month).filter(DbDemande.jour <= day).filter(DbDemande.heure <= hour_of_now).filter(DbDemande.minutes <= minutes_of_now).all()
    return demandes



def update_demande(db: Session, id: int, request: DemandeBase):
    demande = db.query(DbDemande).filter(DbDemande.id == id)
    # Handle any exceptions
    demande.update({
        DbDemande.destinataire: request.destinataire,
        DbDemande.expediteur: request.expediteur,
        DbDemande.password: Hash.bcrypt(request.password),
        DbDemande.sujet: request.sujet,
        DbDemande.message: request.message,
        DbDemande.mois: request.mois,
        DbDemande.jour: request.jour,
        DbDemande.heure: request.heure,
        DbDemande.minutes: request.minutes,
        DbDemande.est_envoye: request.est_envoye
    })
    db.commit()
    return 'ok'

def delete_demande(db: Session, id: int):
    demande = db.query(DbDemande).filter(DbDemande.id == id).first()
    # Handle any exceptions
    db.delete(demande)
    db.commit()
    return 'ok'