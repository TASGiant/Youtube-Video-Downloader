import tkinter as tk
from tkinter import *
from tkinter import messagebox, filedialog
from pytube import YouTube

root = tk.Tk()
root.geometry("650x280")
root.resizable(False, False)
root.title("TAS YouTube Video Downloader")


def widgets():
    head_label = Label(root, text="YouTube video download", padx=15, pady=15, fg="red")
    head_label.grid(row=1, column=1, pady=10, padx=5, columnspan=3)
    link_label = Label(root, text="Video link : ", pady=5, padx=5)
    link_label.grid(row=2, column=0, pady=5, padx=5)
    root.linkText = Entry(root, width=35, textvariable=video_link, font="Arial 14")
    root.linkText.grid(row=2, column=1, pady=5, padx=5, columnspan=2)
    destination_label = Label(root, text="path : ", padx=5, pady=9)
    destination_label.grid(row=3, column=0, pady=5, padx=5)
    root.destinationText = Entry(root, width=27, textvariable=download_Path, font="Arial 14")
    root.destinationText.grid(row=3, column=1, padx=5, pady=5)
    brows_b = Button(root, text="Browse", command=Browse, width=10, pady=10, padx=10, relief=GROOVE, font="Georgia, 13")
    brows_b.grid(row=3, column=2, pady=1, padx=1)
    download_b = Button(root, text="Download Video", width=10, command=Download, pady=10, padx=15, relief=GROOVE,
                        font="Georgia, 13")
    download_b.grid(row=4, column=1, pady=20, padx=20)


def Browse():
    download_directory = filedialog.askdirectory(initialdir="YOUR DIRECTORY PATH", title="Save Video")
    download_Path.set(download_directory)


def Download():
    youtube_link = video_link.get()
    download_folder = download_Path.get()
    get_video = YouTube(youtube_link)
    video_stream = get_video.streams.first()
    video_stream.download(download_folder)
    messagebox.showinfo("SUCCESSFULLY", "DOWNLOADED AND SAVED IN\n" + download_folder)


video_link = StringVar()
download_Path = StringVar()
widgets()
root.mainloop()
