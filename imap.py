import smtplib

# A configuração IMAP server para receber e-mails
import imaplib
import email
import os
import base64
from email import utils
from email import message
from email.header import decode_header


# checking the e-mail count from the lastest e-mail count
with open('BotEmail\log.txt', 'r') as file:
    # this object receive the last e-mail count value
    last_email_count = int(file.readlines()[-1].strip())
    file.close()

# oppening the imap server
mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login('botmailunilink@gmail.com', 'fhpgvqamrqrbpijw')

# checking currently e-mail count
mail.select(mailbox='inbox', readonly=True)
status, count = mail.status('INBOX', "(MESSAGES)")
total_emails = int(count[0].decode("utf-8").split()[2][:-1])
mail.mesg_conversion = False

# If there's new messagens, then proceed : 
if total_emails > last_email_count:
    for num in range(last_email_count+1, total_emails+1):
        result, data = mail.fetch(str(num), '(RFC822)')
        raw_email = data[0][1]
        email_message = email.message_from_bytes(raw_email)

        # Get the sender, subject, and body of the email
        sender = email.utils.parseaddr(email_message['From'])[1]
        subject = decode_header(email_message['Subject'])[0][0].decode()
        body = ''

        if email_message.is_multipart():
            for part in email_message.walk():
                content_type = part.get_content_type()
                if content_type == 'text/plain':
                    body = part.get_payload(decode=True).decode('utf-8')
        else:
            body = email_message.get_payload(decode=True).decode('utf-8')

        # Compose the reply email
        reply_email = email.message.EmailMessage()
        reply_email['From'] = 'botmailunilink@gmail.com'
        reply_email['To'] = sender
        reply_email['Subject'] = f"Re: {subject}"
        reply_email['In-Reply-To'] = email_message['Message-ID']
        reply_email['References'] = email_message['Message-ID']
        reply_email.set_content('Olá, recebemos sua mensagem. Por favor, solicito para que aguarde o retorno do responsável, para que possamos responder suas perguntas.')

        # Send the reply email
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp_server:
            smtp_server.starttls()
            smtp_server.login('botmailunilink@gmail.com', 'fhpgvqamrqrbpijw')
            smtp_server.send_message(reply_email)

    # Update the log file with the latest email count
    with open('BotEmail\log.txt', 'a') as log_file:
        log_file.write(f"{total_emails}\n")