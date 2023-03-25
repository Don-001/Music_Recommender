# -*- coding: UTF-8 -*-
"""
Python-Flask webapp to recommender music to it's users.
"""
from website import create_app

app = create_app()


#def register():
   # if request.method == 'GET':
        # render the registration form template
     #   return render_template('register.html')
   # elif request.method == 'POST':
    #    email = request.form['email']
       # if not validate_email(email):
            # if the email is invalid, re-render the form with an error message
      #      return render_template('register.html', error='Invalid email address')
   # else:
            # continue with registration process
            # return a success message or redirect to a different page
      #  return "Registration successful"

if __name__ == '__main__':  # Script executed directly (instead of via import)?
        app.run(debug=True)  # Launch built-in web server and run this Flask webapp