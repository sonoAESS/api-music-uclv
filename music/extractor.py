from .models import Musica

def llenar():
    ficherodb=open('mp3.txt',encoding='utf-8').readlines()

    for song in ficherodb:
        song=song.strip()
        sprefix=song.removeprefix('https://visuales.uclv.cu/MP3s/').replace('_',' ')
        arr=sprefix.split('/')
        artist=arr[0]
        titulo=arr.pop().removesuffix('.mp3')
        album=''
        if(len(arr)>1):
            album=arr[1]
        Song=Musica(link=song,artista=artist,title=titulo,album=album,)
        Song.save()


                            