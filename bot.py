import imapclient as IC
import imaplib as IL
import pyzmail

server = IC.IMAPClient('imap.gmail.com') # settando o servidor IMAP

server.login('suporteunilink@gmail.com', 'gigevpnbcyphyzsn') # logando o email

server.select_folder('INBOX') # seleciona um arquivo de emails, no caso, caixa de entrada

uids = server.search(['ALL']) # seleciona os emails não vistos
# nesse momento ele traz apenas números. Prox passo : utilizar os numeros para trazer os corpos dos emails

IL.MAXLINE = 1000000

rawmsgs = server.fetch(uids, ['BODY[]'])
msg = pyzmail.PyzMessage.factory(rawmsgs)

assunto = msg.get_subject()
remetente = msg.get_adresses('from')
destinatario = msg.get_adresses('to')
em_copia = msg.get.adresses('cc')

print(assunto)