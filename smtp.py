import smtplib

server = smtplib.SMTP('imap.gmail.com', 587)
server.starttls()
server.ehlo()
server.login('botmailunilink@gmail.com', 'fhpgvqamrqrbpijw')

text = """Primeiro teste concluído,
Um e-mail foi enviado com sucesso! 

-Stefson
"""
msg = smtplib.email.message.EmailMessage()
msg['from'] = 'botmailunilink@gmail.com'
msg["to"] = 'stefsonsampaio01@gmail.com'
msg["Subject"] = "Teste, projeto BotMail Unilink! "
msg.set_content(text)
res = server.send_message(msg)