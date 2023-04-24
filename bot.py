def smtp_init():
    """
    Initialize SMTP connection
    """
    print("Initializing SMTP...")
    global sets = smtplib.SMTP(smtpserver, smtpserverport)
    c = s.starttls()[0] # O valor retornado do código
    if c is not 235:
        raise Exception('SMTP login failed: ' + str(c))
    print("Done. ")
    