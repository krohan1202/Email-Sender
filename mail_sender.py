import os
import smtplib
import imghdr
from email.message import EmailMessage

# Use environment variables
EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

msg = EmailMessage()
msg['Subject'] = "Dark html"
msg['From'] = EMAIL_ADDRESS
msg['To'] = "Enter receiver's email"
msg.set_content('Trying to send html text')

msg.add_alternative('''\
<!DOCTYPE html>
<html>
<body>
    <h3 style="color: orange;">This is the image</h3>
</html>    
''', subtype="html")

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:

    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)
    print("Email sent.")
