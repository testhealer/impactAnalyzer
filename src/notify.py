import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_notification(email_recipient, pr_title, impacted_tests):
    email_sender = 'your_email@example.com'
    email_password = 'your_email_password'

    msg = MIMEMultipart()
    msg['From'] = email_sender
    msg['To'] = email_recipient
    msg['Subject'] = f"Impact Analysis for PR: {pr_title}"

    body = f"The following test cases might be impacted by the PR titled '{pr_title}':\n" + "\n".join(impacted_tests)
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.example.com', 587)
    server.starttls()
    server.login(email_sender, email_password)
    text = msg.as_string()
    server.sendmail(email_sender, email_recipient, text)
    server.quit()

if __name__ == "__main__":
    send_notification('test_owner@example.com', 'Fix login issue in user module', ['Test login functionality'])
