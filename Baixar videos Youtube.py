from pytube import YouTube


#Digite o link do video e local do destino
 
link = input("Digite o link do video que deseja baixar: ") #O  link do video
path = input("Digite o Diretório que deseja salvar o video : ") #Local onde o video será salvo
yt = YouTube(link)

#Mostra detalhe do video
print("Titulo: ", yt.title)
print("Tamanho do video: ", yt.length, "Segundos")
print("Avaliação do video: ", yt.rating)

#Usa maior resolução
ys = yt.streams.get_highest_resolution()

# Começa o Dowload do video

print("Baixando ...")
ys.download(path)
print("Download Completo!")