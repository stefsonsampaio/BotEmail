import smtplib

# A configuração IMAP server para receber e-mails
import imaplib
import email
import os
import base64
from email import utils
from email import message
from email.header import decode_header

mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login('botmailunilink@gmail.com', 'fhpgvqamrqrbpijw')

mail.list()
mail.select(mailbox='inbox', readonly=True) # selecionando caixa de entrada
mail.mesg_conversion = False

result, mail_id = mail.search(None, 'ALL') # pesquisando por "TUDO", None significar que não quero filtrar nada

for num in mail_id[0].split():
    resultado, dados = mail.fetch(num, '(RFC822)')
    
    # obtendo o corpo da mensagem
    message = email.message_from_bytes(dados[0][1])

    # obtendo o remetente
    sender = utils.parseaddr(message['From'])[1]

    # obtendo o assunto
    subject = decode_header(message['Subject'])[0][0]

    # obterndo o corpo do email
    if message.is_multipart():
        for part in message.walk():
            content_type = part.get_content_type()
            if content_type == 'text/plain':
                body = part.get_payload(decode=True).decode('utf-8')


    # imprimindo a informação do e-mail
    print('De : ', sender)
    print('Assunto : ', subject)
    print('Corpo : ', body)
    print('--------------------------')

"""""""""""""""
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('botmailunilink@gmail.com', 'fhpgvqamrqrbpijw')

##Configurando o email que será enviado
from_email = 'botmailunilink@gmail.com'
to_email = sender
assunto = 'Resposta padrao'
resposta = 'Ola, recebemos sua mensagem. Por favor, entre em contato com suporte2 ou aguarde um retorno...'

email_resposta = f'Subject: {assunto}\n\n{resposta}'

server.sendmail(from_email, to_email, email_resposta)
server.quit()
"""""""""""""""