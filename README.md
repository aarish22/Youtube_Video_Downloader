# 📥 YouTube Video Downloader

## About the Project

This project is a Python-based YouTube video downloader that allows users to download videos in the highest resolution available. The application uses the `pytube` library for downloading videos and `tkinter` for creating a graphical user interface (GUI) to select the download directory.

## Features

- **High-Resolution Downloads**: Downloads the video in the highest resolution available in MP4 format.
- **User-Friendly Interface**: Uses `tkinter` to provide a simple GUI for selecting the download directory.
- **Error Handling**: Gracefully handles errors during the download process.

## Technologies Used

- **Python**: The core programming language used for the project.
- **pytube**: For accessing and downloading YouTube videos.
- **tkinter**: For creating the GUI to select the download directory.

## How It Works

1. **Enter YouTube URL**: The user is prompted to enter the URL of the YouTube video they wish to download.
2. **Select Download Directory**: A file dialog opens, allowing the user to select the directory where the video will be saved.
3. **Download Video**: The video is downloaded in the highest resolution available to the selected directory.

## Usage

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/aarish22/Youtube_Video_Downloader.git
    cd youtube-video-downloader
    ```

2. **Install Dependencies**:
    Ensure you have `pytube` and `tkinter` installed. If not, install them using:
    ```bash
    pip install pytube3
    ```

3. **Run the Script**:
    ```bash
    python youtube.py
    ```

4. **Follow the Prompts**:
    - Enter the YouTube video URL when prompted.
    - Select the download directory through the GUI file dialog.

## Example

```plaintext
Enter your URL here: https://www.youtube.com/watch?v=dQw4w9WgXcQ
Selected folder: /Users/username/Downloads
Download Started...
Video Downloaded
```

[![Watch the video](https://github.com/aarish22/Youtube_Video_Downloader/blob/main/Converter.py%20-%20Pdf%20to%20Audio%20using%20Python%20-%20Visual%20Studio%20Code%202024-04-22%2023-22-35.mp4)]
