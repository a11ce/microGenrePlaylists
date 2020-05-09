import spotipy
import spotipy.util

SPOTIFY_SCOPE = "playlist-read-private playlist-modify-private playlist-modify-public"


def main():
    spotifyUser = input("Enter your spotify username: ")
    genre = "dark jazz"
    sp, newPl = spotifySetup(spotifyUser, genre)
    escapedGenre = "genre:" + genre
    #print(escapedGenre)
    results = sp.search(q=escapedGenre, type='track')
    for track in results['tracks']['items']:
        sp.user_playlist_add_tracks(spotifyUser, newPl, [track['uri']])


def spotifySetup(uName, genre):
    global sp
    global newPl
    global SPOTIFY_USERNAME
    SPOTIFY_USERNAME = uName

    token = spotipy.util.prompt_for_user_token(uName, SPOTIFY_SCOPE)
    sp = spotipy.Spotify(token)
    newPl = sp.user_playlist_create(uName, genre)['uri']
    return sp, newPl


if __name__ == "__main__":
    main()
