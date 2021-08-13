from pytube import YouTube #to install required Youtube Module "pip install pytube"
link = input("Enter youtbe video Url:") 
yt = YouTube(link)
videos=yt.streams.all() # this will disply available stream format available for above url
video=list(enumerate(videos)) #to index all all the format in list

for i in video:
    print(i) # this will print all available formats for video

print("enter desired format to download")
dn_option = int(input(" Enter the option: ")) #to ask user in which format videos to be downloaded
dn_video= videos[dn_option]
dn_video.download() #to download video

print("downloaded youtube video sucessfully") #to print acknowledgement
