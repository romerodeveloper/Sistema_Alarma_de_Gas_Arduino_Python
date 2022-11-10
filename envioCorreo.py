import smtplib
from email.message import EmailMessage


class Correo:
    
    email_subject = "ALERTA DE HOGAR"
    sender_email_address = "nstiromero@poligran.edu.co"
    receiver_email_address = "desarrollador.romero@gmail.com"
    email_smtp = "smtp.office365.com"
    email_password = "*****"

    @classmethod
    def Generar(cls):
        message = EmailMessage()
        message['Subject'] = cls.email_subject
        message['From'] = cls.sender_email_address
        message['To'] = cls.receiver_email_address
        message.set_content("Lo sentimos pero su casa se esta incendiando!")
        server = smtplib.SMTP(cls.email_smtp, '587')
        server.ehlo()
        server.starttls()
        server.login(cls.sender_email_address, cls.email_password)
        server.send_message(message)
        server.quit()


