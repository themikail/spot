# To access Spotipy
import spotipy
# To View the API response
import json
# To open our song in our default browser
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

while True:
    print("Welcome, " + user['display_name'])
    print("0 - Exit")
    print("1 - Search for a Song")
    text = reader.read()
    choice = reader.read()

    if choice == 1:
        # Get the Song Name.
        searchQuery = text
        # Search for the Song.
        searchResults = spotifyObject.search(searchQuery, 1, 0, "track")
        # Get required data from JSON response.
        tracks_dict = searchResults['tracks']
        tracks_items = tracks_dict['items']
        song = tracks_items[0]['external_urls']['spotify']
        # Open the Song in Web Browser
        webbrowser.open(song)
        print('Song has opened in your browser.')
    elif choice == 0:
        break
    else:
        print("Enter valid choice.")
