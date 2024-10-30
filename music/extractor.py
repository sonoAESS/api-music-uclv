from django.core.exceptions import ValidationError
from models import Song

def fillSongs():
    songsSave = []
    
    with open('mp3.txt', encoding='utf-8') as f:
        songLines = f.readlines()

    for songLine in songLines:
        songLine = songLine.strip()
        stripped_prefix = songLine.removeprefix('https://visuales.uclv.cu/MP3s/').replace('_', ' ')
        arr = stripped_prefix.split('/')
        
        if len(arr) < 1:
            continue  # Skip if there's no valid data
        
        artist = arr[0]
        title = arr.pop().removesuffix('.mp3')
        album = arr[1] if len(arr) > 1 else ''

        # Validate fields before saving
        if artist and title:  # Ensure that both artist and title are present
            songsSave.append(Song(link=songLine, artist=artist, title=title, album=album))

    # Bulk create all songs at once
    Song.objects.bulk_create(songsSave)