from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DATETIME
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

SQLALCHEMY_DATABASE_URL = "Conception_logiciel_projet/app/database.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)

Base = declarative_base()

class MyTable(Base):
    __tablename__ = "mes_demandes"

    id = Column(Integer, primary_key=True, index=True)
    destinataire = Column(String(80))
    expediteur = Column(String(80))
    sujet = Column(String(100))
    contenu = Column(String(10000))
    date_envoi = Column(DateTime(timezone=True))
    etat = Column()

Base.metadata.create_all(bind=engine)