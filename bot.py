from config import *
from smtp import *

def smtp_init():
    """
    Initialize SMTP connection
    """
    print("Initializing SMTP...")
    global s
    s = smtplib.SMTP(smtpserver, smtpserverport)
    c = s.starttls()[0] # O valor retornado do código
    if c != 235:
        raise Exception('SMTP login failed: ' + str(c))
    print("Done. ")

def get_unread():
    """
    Fetch unread emails
    """
    uids = server.search('UNSEEN')
    if not uids:
        return None
    else:
        print("Found %s unreads" % len(uids))
        return server.fetch(uids, ['BODY[]', 'FLAGS'])
    
def hello_world(lines):
    return "Hello, World! "

commands = {"hello" : hello_world}

def analyze_msg(raws, a):
    """
    Analyze message.  Determine if sender and command are valid.
    Return values:
    None: Sender is invalid or no text part
    False: Invalid command
    Otherwise:
    Array: message split by lines
    :type raws: dict
    """
    print("Analyzing message with uid " + str(a))
    msg = pm.factory(raws[a][b'BODY[]'])
    frm = msg.get_addresses('from')
    if frm[0][1] != sadr:
        print("Unread is from %s <%s> skipping" % (frm[0][0],
                                                   frm[0][1]))
        return None
    global subject
    if not subject.startswith("Re"):
        subject = "Re: " + msg.get_subject()
    print("subject is", subject)
    if msg.text_part is None:
        print("No text part, cannot parse")
        return None
    text = msg.text_part.get_payload().decode(msg.text_part.charset)
    cmds = text.replace('\r', '').split('\n')  # Remove any \r and split on \n
    if cmds[0] not in commands:
        print("Command %s is not in commands" % cmds[0])
        return False
    else:
        return cmds
    
def mail(text):
    """
    Print an email to console, then send it
    """
    print("This email will be sent: ")
    print(text)
    msg = email.message.EmailMessage()
    global subject
    msg["from"] = radr
    msg["to"] = sadr
    msg["Subject"] = subject
    msg.set_content(text)
    res = s.send_message(msg)
    print("Sent, res is", res)

