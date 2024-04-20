from pytube import YouTube
import tkinter as tk
from tkinter import filedialog

def download_from_youtube(url , url_path):
    try:
        yt = YouTube(url)
        stream =yt.streams.filter(progressive=True ,file_extension ="mp4")
        highest_res_stream = stream.get_highest_resolution()
        highest_res_stream.download(output_path=save_directory)
        print("Video Downloaded")
    except Exception as e:
        print(e)
        
def open_file_dialog():
    folder = filedialog.askdirectory()
    if folder:
        print(f"Selected folder : {folder}")
    return folder

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    
    video_url = input("Enter your url here: ")
    save_directory = open_file_dialog()
    
    
    if not save_directory:
        print("Invalid save location")
    else:
        print("Download Started...")
        download_from_youtube(video_url , save_directory)
    
    