from dao.database import Base
from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer, String, Boolean

class DbDemande(Base):
    __tablename__ = 'demandes'
    id = Column(Integer, primary_key = True, index= True)
    destinataire = Column(String)
    expediteur = Column(String)
    password = Column(String)
    sujet = Column(String)
    message = Column(String)
    mois = Column(Integer)
    jour = Column(Integer)
    heure = Column(Integer)
    minutes = Column(Integer)
    est_envoye = Column(Boolean)