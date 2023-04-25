# A biblioteca SMTP é utilizada para enviar e-mails
import smtplib

# Setando configurações do servidor SMTP
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('botmailunilink@gmail.com', 'fhpgvqamrqrbpijw')

"""
# Configurando o email que será enviado
from_email = 'seu_email@gmail.com'
to_email = 'email_destinatario@example.com'
subject = 'Assunto do e-mail'
message = 'Conteúdo do e-mail'

msg = f'Subject: {subject}\n\n{message}'
"""

server.sendmail(from_email, to_email, msg)
server.quit()