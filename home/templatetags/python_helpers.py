import time
import string
from django.template import Library
from django.utils.safestring import mark_safe

register = Library()

def format_time(value, arg=None):
	try:
		value = time.strptime(value, "%H:%M:%S")
	except:
		pass
	value = time.strftime("%I:%M %p", value).lower()
	value = string.lstrip(value, "0")
	return value
register.filter(format_time)
