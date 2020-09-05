import smtplib
from email.message import EmailMessage


# Attach html to mail
EMAIL_ADDRESS = "mymusicwebsite7@gmail.com"
EMAIL_PASS = "hwvpfblqisuzajxk"
GMAIL = "smtp.gmail.com"

msg = EmailMessage()

msg["From"] = EMAIL_ADDRESS
dest_email = input("Enter destination e-mail: ")
msg["To"] = dest_email
msg["Subject"] = input("Enter subject: ")

msg.set_content('This is a plain text email')
msg.add_alternative("""\
<!DOCTYPE html>
<html lang="en">
    <body>
        <h1 style="color:SlateGray;">This is an HTML Email!</h1>
    </body>
</html>
""", subtype="html")

with smtplib.SMTP_SSL(GMAIL, 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASS)
    smtp.send_message(msg)
