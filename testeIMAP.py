import imaplib
import email
import smtplib
from email.mime.text import MIMEText

# Configuração IMAP server para receber e-mails
mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login('botmailunilink@gmail.com', 'fhpgvqamrqrbpijw')
mail.select('inbox')

# Buscando o último e-mail
result, data = mail.search(None, 'ALL')
latest_email_id = data[0].split()[-1]
result, data = mail.fetch(latest_email_id, "(RFC822)")
raw_email = data[0][1]

# Decodificando o e-mail
email_message = email.message_from_bytes(raw_email)

# Obtendo informações do e-mail
sender_email = email.utils.parseaddr(email_message['From'])[1]
recipient_email = email.utils.parseaddr(email_message['To'])[1]
subject = email_message['Subject']

# Preparando a resposta
response = MIMEText('Sua mensagem de resposta aqui')
response['To'] = sender_email
response['Subject'] = 'Re: ' + subject
response['In-Reply-To'] = email_message['Message-ID']
response['References'] = email_message['Message-ID']

# Enviando a resposta usando SMTP
smtp = smtplib.SMTP('smtp.gmail.com', 587)
smtp.ehlo()
smtp.starttls()
smtp.login('botmailunilink@gmail.com', 'fhpgvqamrqrbpijw')
smtp.sendmail(recipient_email, sender_email, response.as_string())
smtp.quit()