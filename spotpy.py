import spotipy
import json
import webbrowser

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

username = ''
clientID = ''
clientSecret = ''
redirectURI = 'https://www.google.de'

# Create OAuth Object
oauth_object = spotipy.SpotifyOAuth(clientID,clientSecret,redirectURI)
# Create token
token_dict = oauth_object.get_access_token()
token = token_dict['access_token']
# Create Spotify Object
spotifyObject = spotipy.Spotify(auth=token)

user = spotifyObject.current_user()
# To print the response in readable format.
print(json.dumps(user,sort_keys=True, indent=4))



try:
    text = reader.read()
    searchQuery = text
    searchResults = spotifyObject.search(searchQuery,1,0,"track")
    tracks_dict = searchResults['tracks']
    tracks_items = tracks_dict['items']
    song = tracks_items[0]['external_urls']['spotify']
    print("Song has opened in browser.")


finally:
    GPIO.cleanup()
