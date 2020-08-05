import json
import requests
import smtplib
from socket import gaierror
from email.message import EmailMessage

from app import config

class Notifier(object):
    def notify():
        raise NotImplemented


class EmailNotifier(Notifier):
    def __init__(self, target_email):
        self.target_email = target_email

    def notify(self, notification):
        fromaddr = self.target_email
        msg = EmailMessage()
        msg['Subject'] = 'Notification'
        msg['From'] = config.ADMIN_EMAIL 
        msg['To'] = self.target_email
        msg['Msg'] = notification

        try:
            with smtplib.SMTP(config.SMTP_HOST, config.SMTP_PORT) as server:
                server.login(config.SMTP_USERNAME, config.SMTP_PASSWORD)
                server.send_message(msg)
                server.quit()
        except (gaierror, ConnectionRefusedError):
            print('Failed to connect to the server. Bad connection settings?')
        except smtplib.SMTPServerDisconnected:
            print('Failed to connect to the server. Wrong user/password?')
        except smtplib.SMTPException as e:
            print('SMTP error occurred: ' + str(e))


class HTTPNotifier(Notifier):
    def __init__(self, target_url):
        self.target_url = target_url

    def notify(self, notification):
        requests.post(
            self.target_url, 
            data=json.dumps({'notification': notification}), 
            headers={'Content-Type': 'application/json'}
        )


registered_notifiers = []

if config.EMAIL_BACKEND:
    registered_notifiers.append(EmailNotifier(config.EMAIL_BACKEND))

if config.HTTP_BACKEND:
    registered_notifiers.append(HTTPNotifier(config.HTTP_BACKEND))