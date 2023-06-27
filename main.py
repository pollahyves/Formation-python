# Youtube Downloader

# module pytube

from pytube import YouTube

url="https://www.youtube.com/watch?v=n9GImjHkLmE"

def on_download_process(stream,chunk,bytes_remaining):
    byte_downloaded= stream.filesize - bytes_remaining
    percent = byte_downloaded*100/stream.filesize
    
    print("progression du telechargement: "+str(int(percent))+"%")

youtube_vdeo = YouTube(url)

youtube_vdeo.register_on_progress_callback(on_download_process)

print("TITLE: ",youtube_vdeo.title)

print("NB VUE: ",youtube_vdeo.views)

stream = youtube_vdeo.streams.get_highest_resolution()
print("Telechargement....")
stream.download()
print("OK")