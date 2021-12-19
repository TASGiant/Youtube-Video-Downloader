from pytube import YouTube
import os
from pathlib import Path
print("Input Video URL :")
link = input("")
url = YouTube(link)
print("downloading...")
video = url.streams.get_highest_resolution()
path_to_download_folder = str(os.path.join(Path.home(), "C:\\Users\\Public\\Videos"))
video.download(path_to_download_folder)
print("downloaded!")
