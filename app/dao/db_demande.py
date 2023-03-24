from sqlalchemy.orm.session import Session
from schema import DemandeBase
from models import DbDemande
from dao.hash import Hash


def create_demande(db: Session, request: DemandeBase):
    new_demande = DbDemande(
        destinataire = request.destinataire,
        expediteur = request.expediteur,
        password = Hash(request.password),
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