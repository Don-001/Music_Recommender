#import re
#from flask import Flask
#from models import db, User

#def validate_email(email):
  #  """
   # Validate the email address using a regular expression.
  #  Returns True if the email is valid, False otherwise.
  #  """
  #  pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
  #  return re.match(pattern, email) is not None
