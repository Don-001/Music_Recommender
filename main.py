# -*- coding: UTF-8 -*-
"""
Python-Flask webapp to recommender music to it's users.
"""
from website import create_app

app = create_app()




if __name__ == '__main__':  # Script executed directly (instead of via import)
        app.run(debug=True)  # Launch built-in web server and run this Flask webapp