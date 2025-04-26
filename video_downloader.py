# Downloading YT video
from pytubefix import YouTube
from pytubefix.cli import on_progress

def downloader(url):
    yt = YouTube(url, on_progress_callback=on_progress)
    ys = yt.streams.get_highest_resolution()
    video_path = ys.download()

    return video_path