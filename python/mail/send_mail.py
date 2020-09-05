import smtplib


EMAIL_ADDRESS = "mymusicwebsite7@gmail.com"
EMAIL_PASS = "hwvpfblqisuzajxk"
GMAIL = "smtp.gmail.com"

with smtplib.SMTP(GMAIL, 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(EMAIL_ADDRESS, EMAIL_PASS)

    subject = input("Enter subject: ")
    body = input("Enter text: ")
    dest_email = input("Enter destination e-mail: ")

    msg = f"Subject: {subject}\n\n{body}"

    smtp.sendmail(EMAIL_ADDRESS, dest_email, msg)
