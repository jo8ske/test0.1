import yt_dlp

def search_youtube(query: str) -> str:
    with yt_dlp.YoutubeDL({'quiet': True}) as ydl:
        info = ydl.extract_info(f"ytsearch:{query}", download=False)
        return info['entries'][0]['webpage_url']
