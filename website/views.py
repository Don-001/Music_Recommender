from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


views = Blueprint('views', __name__)

# Spotify API credentials
client_id = 'your_client_id'
client_secret = 'your_client_secret'
redirect_uri = 'http://localhost:5000/callback'

# Authenticate with Spotify API
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


@views.route('/search', methods= ['POST', 'GET'])
@login_required
def search():  
    if request.method == 'POST':
    # Get search query from form data
        query = request.form.get['query']

    # Search for track on Spotify
        results = sp.search(q=query, type='track', limit=1)

    # Extract track URI from search results
        track_uri = results['tracks']['items'][0]['uri']

    # Generate Spotify player widget HTML code
        player_html = f'<iframe src="https://open.spotify.com/embed/track/{track_uri.split(":")[2]}" width="300" height="380" frameborder="0" allowtransparency="true" allow="encrypted-media"></iframe>'

    # Render player widget in Flask template
    #return render_template("player.html", user=current_user)
    return render_template("search.html", user=current_user)
