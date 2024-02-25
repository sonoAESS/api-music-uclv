a='https://visuales.uclv.cu/MP3s/Joaquin_Sabina/19_Dias_y_500_Noches/02 19 dias y 500 noches.mp3'
a=a.removeprefix('https://visuales.uclv.cu/MP3s/')
arr=a.split('/')

expSearch=a.replace('/',' ').replace('_',' ')
titulo=arr.pop()
artist=arr[0].replace('_',' ')

print(titulo.removesuffix('.mp3'))