import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Set up your Gmail SMTP credentials
sender_email = 'YOUR_EMAIL'
sender_password = 'YOUR_PASSWORD'

# Set up the email details
recipient_email = 'RECIPIENT_EMAIL'
subject = 'Email subject'
message = 'Email body'

# Create the email message
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = recipient_email
msg['Subject'] = subject
msg.attach(MIMEText(message, 'plain'))

# Set up the SMTP server and send the email
with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.starttls()
    smtp.login(sender_email, sender_password)
    smtp.send_message(msg)

# Validate email 
import re

def validate_email(email):
    # Regular expression pattern for email validation
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

    # Use the pattern to match the email
    if re.match(pattern, email):
        return True
    else:
        return False

# Example usage
email = input("Enter an email address: ")
if validate_email(email):
    print("Valid email")
else:
    print("Invalid email")
