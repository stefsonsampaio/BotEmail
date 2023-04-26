# A biblioteca SMTP é utilizada para enviar e-mails
import smtplib

# Setando configurações do servidor SMTP
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('botmailunilink@gmail.com', 'fhpgvqamrqrbpijw')


# Configurando o email que será enviado
from_email = 'botmailunilink@gmail.com'
to_email = 'suporte2@unilinktransportes.com.br'
subject = 'Assunto do e-mail'
message = 'Conteudo do e-mail'

msg = f'Subject: {subject}\n\n{message}'


server.sendmail(from_email, to_email, msg)
server.quit()