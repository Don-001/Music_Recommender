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

#def validate_login(username, password):
     # query the database to find a user with the given username and password
   # user = User.query.filter_by(username=username, password=password).first()

    # check if a user was found
  #  if user is not None:
        # if the username and password are valid, return True
   #     return True
    
    # if the username and password are invalid, return False
   # else:
    #    return False