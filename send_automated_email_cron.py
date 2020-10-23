if __name__ == "__main__":

	# cron settings # m h  dom mon dow   command
 					# */10 * * * *
	import os
	import json
	import django

	os.environ.setdefault("DJANGO_SETTINGS_MODULE", "interview.settings.dev")
	django.setup()

	from api.v1.email import helpers
	helpers.email_report()