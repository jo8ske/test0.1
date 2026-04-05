import requests
from config import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET

def get_token():
    url = "https://accounts.spotify.com/api/token"
    data = {"grant_type": "client_credentials"}

    response = requests.post(
        url,
        data=data,
        auth=(SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET)
    )

    return response.json()["access_token"]


def get_track_name(spotify_url: str) -> str:
    token = get_token()

    track_id = spotify_url.split("/")[-1].split("?")[0]

    url = f"https://api.spotify.com/v1/tracks/{track_id}"

    headers = {"Authorization": f"Bearer {token}"}

    data = requests.get(url, headers=headers).json()

    name = data["name"]
    artist = data["artists"][0]["name"]

    return f"{artist} - {name}"
