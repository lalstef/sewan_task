from app.config import EMAIL_BACKEND, HTTP_BACKEND


class Notifier(object):
	def dispatch_notification():
		raise NotImplemented


class EmailNotifier(Notifier):
	def __init__(self, target_email):
		self.target_email = target_email

	def notify(self, notification):
		pass


class HTTPNotifier(Notifier):
	def __init__(self, target_url):
		self.target_url = target_url

	def notify(self, notification):
		pass


registered_notifiers = []

if EMAIL_BACKEND:
	registered_notifiers.append(EmailNotifier(EMAIL_BACKEND))

if HTTP_BACKEND:
	registered_notifiers.append(HTTPNotifier(HTTP_BACKEND))