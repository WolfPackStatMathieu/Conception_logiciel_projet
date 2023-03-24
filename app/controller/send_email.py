from app.dao import db_demande
from app.dao.schema import DemandeBase
import smtplib
from app.dao.database import get_db
from app.router import demande_get
from app.router import demande_post

def send_email(demande: DemandeBase):
    # Create SMTP connection
    smtp_server = "smtp-mail.outlook.com"
    port = 587 # StartTLS
    sender_email = demande.expediteur
    sender_password = demande.password
    recipient_email = demande.destinataire


    with smtplib.SMTP(smtp_server, port) as connection:
        connection.starttls()
        connection.login(user = sender_email,password= sender_password)
        connection.sendmail(
            from_addr= sender_email
            ,to_addrs= recipient_email
            ,msg=f'{demande.sujet}\n\n{demande.message}')


        # connection.login(user=, password=)


