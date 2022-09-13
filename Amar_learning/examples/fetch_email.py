# Fetch Outlook Emails
# pip install imap-tools
from imap_tools import MailBox as Email
from imap_tools import MailMessageFlags
# Fetch all unseen mails
with Email("https://mail.google.com/").login("amarnathreddy0201@gmail.com", "Amar@eee201", "INBOX") as EmailBox:
    mails = [m.mail for m in EmailBox.fetch(mark_seen=False)]
    #EmailBox.flag(mails, MailMessageFlags.SEEN, True)
    for email in mails:
        print("From : {}".format(email.from_))
        print("Subject:", email.subject)
        print("Body:", email.text)