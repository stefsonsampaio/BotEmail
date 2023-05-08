import time

# lib to find log.txt file
import os
import sys

import smtplib

# IMAP configuration
import imaplib
import email
import base64
from email import utils
from email import message
from email.header import decode_header

# PDF sender configuration
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

# Make program run infinitally
while True:
    # use this in case you make a .exe app from this program with pyinstaller to find log.txt file' path
    """""""""
    caminho_executavel = sys.executable
    caminho_executavel_dir = os.path.dirname(caminho_executavel)
    caminho_log = os.path.join(caminho_executavel_dir, 'log.txt')
    """""""""

    # checking the e-mail count from the lastest e-mail count
    with open('log.txt path', 'r') as file:
        # this object receive the last e-mail count value
        last_email_count = int(file.readlines()[-1].strip())
        file.close()

    # oppening the imap server
    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    mail.login('youremail@example.com', 'yourpassword')

    # checking currently e-mail count
    mail.select(mailbox='inbox', readonly=True)
    status, count = mail.status('INBOX', "(MESSAGES)")
    total_emails = int(count[0].decode("utf-8").split()[2][:-1])
    mail.mesg_conversion = False

    # If there's new messagens, then proceed : 
    if total_emails > last_email_count:
        # read only last email to optmize program
        result, data = mail.fetch(str(total_emails), '(RFC822)')
        raw_email = data[0][1]

        # Get the sender, subject, and body of the email
        email_message = email.message_from_bytes(raw_email)
        sender = email.utils.parseaddr(email_message['From'])[1]
        subject = decode_header(email_message['Subject'])[0][0]

        # decode subject in case it has accent or symbols
        if isinstance(subject, bytes):
            subject = subject.decode()
        body = ''

        # decode email's body in case it has accent or symbols
        # you can use email's body to create conditions to answer the e-mail
        if email_message.is_multipart():
            for part in email_message.walk():
                content_type = part.get_content_type()
                if content_type == 'text/plain':
                    body = part.get_payload(decode=True).decode('utf-8')
        else:
            body = email_message.get_payload(decode=True).decode('utf-8')

        # Compose the reply email
        reply_email = email.message.EmailMessage()
        reply_email['From'] = 'youremail@example.com'
        reply_email['To'] = sender
        reply_email['Subject'] = f"Re: {subject}"
        reply_email['In-Reply-To'] = email_message['Message-ID'] # In-Reply-To make the email be send as a reply
        reply_email['References'] = email_message['Message-ID']

        # Make some conditions to differente responses
        if "pdfpath" in subject.lower(): # this condition can send a pdf file in attachment
            reply_email.set_content('your message body')

            # Turns the reply_email into multipart text, so it can support pdf file
            reply_email.make_mixed()
            reply_email.attach(MIMEText('', 'plain'))

            # Encoding PDF file with base64
            with open('pdfpath.pdf', 'rb') as pdf_file: # 'rb' read the pdf file as "binary word"
                pdf_content = pdf_file.read()

            # Creating an object in attach
            pdf_attachment = MIMEApplication(pdf_content, _subtype='pdf')
            pdf_attachment.add_header('Content-Disposition', 'attachment', filename='LGPD.pdf')

            # Add attachment to email
            reply_email.attach(pdf_attachment)
        else: # email without pdf file
            reply_email.set_content('your message body.')

        # Send the reply email
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp_server:
            smtp_server.starttls()
            smtp_server.login('youremail@example.com', 'yourpassword')
            smtp_server.send_message(reply_email)
            print("Message sent!")
            smtp_server.quit()

        # Update the log file with the latest email count
        with open(caminho_log, 'w') as log_file:
            log_file.write(f"{total_emails}\n")
    else:
        print("Not new messages.")
    
    # Make program pause 5 seconds
    time.sleep(5)