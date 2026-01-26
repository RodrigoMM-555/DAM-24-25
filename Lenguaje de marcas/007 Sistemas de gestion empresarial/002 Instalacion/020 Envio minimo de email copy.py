import smtplib
from email.message import EmailMessage
import os

SMTP_SERVER = "smtp.gmx.com"
SMTP_PORT = 587          # 587 = STARTTLS, 465 = SSL
SMTP_USER = "menendez.rodrigo555@gmx.es"
SMTP_PASS = "2KXXDQ7BL5P7PSEJD47J"

msg = EmailMessage()
msg["From"] = "menendez.rodrigo555@gmx.es"
msg["To"] = "menendez.rodrigo555@gmx.es"
msg["Subject"] = "Esto es un ejercicio de clase"
msg.set_content("Hola esto es una prueba de envio de email desde Python")

with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as smtp:
    smtp.starttls()
    smtp.login(SMTP_USER, SMTP_PASS)
    smtp.send_message(msg)

print("Email sent")
