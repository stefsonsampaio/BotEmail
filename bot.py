import imapclient as IC

server = IC.IMAPClient('imap.gmail.com') # settando o servidor IMAP

server.login('suporteunilink@gmail.com', 'gigevpnbcyphyzsn') # logando o email

server.select_folder('INBOX') # seleciona um arquivo de emails, no caso, caixa de entrada

server.search(['UNSEEN']) # seleciona os emails não vistos
# nesse momento ele traz apenas números. Prox passo : utilizar os numeros para trazer os corpos dos emails

