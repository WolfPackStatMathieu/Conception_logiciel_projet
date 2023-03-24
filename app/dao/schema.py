from pydantic import BaseModel

class DemandeBase(BaseModel):
    id = int
    destinataire = str
    expediteur = str
    password = str
    sujet = str
    message = str
    mois = int
    jour = int
    heure = int
    minutes = int
    est_envoye = bool