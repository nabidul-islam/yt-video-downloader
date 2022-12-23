from pytube import YouTube
link = input("Enter your youtude url : ")
yt = YouTube(link)
print(yt.title)
videos = yt.streams.all()

video = list(enumerate(videos))

for i in video:
    print(i)

print ("enter the desired option to download the format")

dn_option = int(input("enter the option : "))

dn_video = videos[dn_option]
dn_video.download()

print("Downloaded successfully")
print("Downloaded successfully")