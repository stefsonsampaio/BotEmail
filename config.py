import getpass

radr = input("Adrees to log int to") # Email para checar e enviar mensagens
smtpserver = onput("SMTP server domain: ") #Servidor smpt da conta
smtpserverport = input("SMTP server port [587]: ") # Porta do servidor SMTP 

if not smtpserverport or smtpserverport == "":
    smtpserverport = 587
pwd = getpass.getpass("Account password: ") # Senha da conta
sadr = input("Trusted addresses to receive from: ") # Endereço para receber comandos
check_freq = 5

