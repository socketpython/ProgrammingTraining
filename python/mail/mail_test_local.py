import smtplib


# run this in cmd - python -m smtpd -c DebuggingServer -n localhost:1025
EMAIL_ADDRESS = "mymusicwebsite7@gmail.com"
EMAIL_PASS = "hwvpfblqisuzajxk"

with smtplib.SMTP('localhost', 1025) as smtp:
    subject = input("Enter subject: ")
    body = input("Enter text: ")
    dest_email = input("Enter destination e-mail: ")

    msg = f"Subject: {subject}\n\n{body}"

    smtp.sendmail(EMAIL_ADDRESS, dest_email, msg)
