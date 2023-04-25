# A configuração IMAP server para receber e-mails
import imaplib
import email
from email import utils
from email import message
from email.header import decode_header

mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login('botmailunilink@gmail.com', 'fhpgvqamrqrbpijw')

mail.select('inbox') # selecionando caixa de entrada
mail.mesg_conversion = False

result, data = mail.search(None, 'ALL')

for num in data[0].split():
    result, data = mail.fetch(num, '(RFC822)')
    
    # obtendo o corpo da mensagem
    message = email.message_from_bytes(data[0][1])

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