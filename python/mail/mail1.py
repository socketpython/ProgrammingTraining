import smtplib
from email.message import EmailMessage
import imghdr


# Attach image to mail
EMAIL_ADDRESS = "mymusicwebsite7@gmail.com"
EMAIL_PASS = "hwvpfblqisuzajxk"
GMAIL = "smtp.gmail.com"

msg = EmailMessage()

msg["From"] = EMAIL_ADDRESS
dest_email = input("Enter destination e-mail: ")
msg["To"] = dest_email
msg["Subject"] = input("Enter subject: ")
msg.set_content(input("Enter text: "))

files = ["img/tony_stark.webp"]

for file in files:
    with open(file, "rb") as f:
        file_data = f.read()
        file_type = imghdr.what(f.name)
        file_name = f.name

    msg.add_attachment(file_data, maintype="image", subtype=file_type, filename=file_name)

with smtplib.SMTP_SSL(GMAIL, 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASS)
    smtp.send_message(msg)
