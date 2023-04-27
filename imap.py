import smtplib

# A configuração IMAP server para receber e-mails
import imaplib
import email
import os
import base64
from email import utils
from email import message
from email.header import decode_header


# Vendo na lista de log, quantos e-mails tinha na ultima vez que o programa rodou
# TODO : Se agora tiver mais emails que a ultima linha do log, rodas o programa de envio de resposta.
with open('BotEmail\log.txt', 'r') as file:
    linha = file.readlines()
    file.close()

# Esse objeto recebe o valor da ultima linha do arquivo log
ultima_linha = int(linha[-1].strip())

mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login('botmailunilink@gmail.com', 'fhpgvqamrqrbpijw')

# gerando uma lista com os ids dos emails
mail.list()

# selecionando caixa de entrada
status, count = mail.select(mailbox='inbox', readonly=True) 

# armazenando a quantidade de emails
total = int(count[0])
mail.mesg_conversion = False

# pesquisando por 'TUDO', None significar que não quero filtrar nada
result, mail_id = mail.search(None, 'ALL') 

# TODO: Se a ultima linha do arquivo log indicar que temos um novo email, o asked_for permite que recebamos os valores de destinatario e etc
asked_for = False
if total > ultima_linha:
    asked_for = True
    print("Mensagem de resposta enviada.")
else:
    print("Nenhuma mensagem foi enviada.")

if asked_for == True:
    for num in mail_id[0].split():
        resultado, dados = mail.fetch(num, '(RFC822)')
        
        # obtendo o corpo da mensagem
        message = email.message_from_bytes(dados[0][1])

        # obtendo o remetente
        sender = utils.parseaddr(message['From'])[1]

        # obtendo o assunto
        subject = decode_header(message['Subject'])[0][0]

        # decodificando o corpo da mensagem
        if message.is_multipart():
            for part in message.walk():
                content_type = part.get_content_type()
                if content_type == 'text/plain':
                    body = part.get_payload(decode=True).decode('utf-8')

        """""""""
        # imprimindo a informação do e-mail
        print('De : ', sender)
        print('Assunto : ', subject)
        print('Corpo : ', body)
        print('--------------------------')
        """""""""
# Salvando memória
mail.close()

if asked_for == True:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('botmailunilink@gmail.com', 'fhpgvqamrqrbpijw')

    ##Configurando o email que será enviado
    from_email = 'botmailunilink@gmail.com'
    to_email = sender
    assunto = 'Resposta padrão'
    resposta = 'Olá, recebemos sua mensagem. Por favor, solicito para que aguarde o retorno do responsável, para que possamos responder suas perguntas.'

    email_resposta = f'Subject: {assunto}\n\n{resposta}'

    server.sendmail(from_email, to_email, email_resposta.format(to_email, from_email, resposta).encode('utf-8'))

    # Salvando memória
    server.quit()


# Essa função foi criada para armazenar quantos e-mails tinham na caixa de entrada na ultima vez que o programa rodou
# Objetivo : Com file.read, eu descubro quando o email receber novos emails e assim consigo gerar uma condição para responder o e-mail
with open('BotEmail\log.txt', 'a') as file:
    file.write(str(total))
    file.write("\n")
    file.close()
