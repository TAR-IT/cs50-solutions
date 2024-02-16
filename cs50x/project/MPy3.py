
# MPy3 - a YouTube-to-mp3-converter
from lib import ffmpeg, meta
from decouple import config
from pytube import YouTube, exceptions
import subprocess
import sys
import os
import re


# default download directory ".\Downloads" - change to your needs
DEFAULT_DOWNLOAD_DIRECTORY = config("DEFAULT_DOWNLOAD_DIRECTORY", default="./Downloads")


def main():
    while True:
        # Check if FFmpeg is installed, if not ask to install it
        if not ffmpeg.check_install():
            ffmpeg.ask_install()
            sys.exit(0)

        # If URL and download location are used in command line arguments, use them
        if len(sys.argv) == 3:
            url = sys.argv[1]
            download_location = sys.argv[2]
        elif len(sys.argv) == 2:
            # If only URL is provided, use it and ask for the download location
            url = sys.argv[1]
            download_location = input("\nEnter download location (or press Enter for the default directory): ")
            download_location = download_location if download_location else DEFAULT_DOWNLOAD_DIRECTORY
        else:
            # Else try to ask for URL and download location
            url = get_valid_url()
            download_location = input("\nEnter download location (or press Enter for the default directory): ")
            download_location = download_location if download_location else DEFAULT_DOWNLOAD_DIRECTORY

        mp4_file = download_to_mp4(url, download_location)
        convert_to_mp3(mp4_file)

        repeat = input("\nDo you want to download another file? (y/yes or q/quit to exit): ").lower()
        if repeat in ["q", "quit"]:
            sys.exit(0)
            

def get_valid_url():
    while True:
        try:
            url = input("\nURL: ")
            if url.lower() in ['q', 'quit']:
                sys.exit(0)
            video = YouTube(url)  # Try creating a YouTube object with the input URL
            return url
        except exceptions.VideoUnavailable:
            print("\nError: The YouTube video is unavailable.")
        except Exception as e:
            print(f"\nError: {e}.")


def download_to_mp4(url, download_location):
    # Take URL and download
    video = YouTube(url)
    print(f"""
          Title: {video.title}
          Length: {video.length} seconds
          """)

    # Get the best available video stream with a flashing dot
    print("\nGetting highest bitrate stream available...")
    stream = video.streams.get_audio_only()
    print("\nStream found.")

    # Clean the video title to remove invalid characters for use as a file name
    print("\nCleaning title from invalid characters...")
    cleaned_title = re.sub(r'[<>:"/\\|?*]', "", video.title)
    print(f"\nCleaned Title: {cleaned_title}")

    # Download video to the specified location
    print(f"\nDownloading file to '{download_location}'...")
    os.makedirs(download_location, exist_ok=True)
    file_path = os.path.join(download_location, f"{cleaned_title}.mp4")
    stream.download(output_path=download_location, filename=f"{cleaned_title}.mp4")
    print(f"\nThe file has been downloaded successfully to {file_path}.")

    return file_path


def convert_to_mp3(mp4_file):
    mp3_file = mp4_file.replace('.mp4', '.mp3')

    # Convert video to MP3 using FFmpeg
    print(f"\nConverting file to MP3 using FFmpeg...")
    subprocess.run(['ffmpeg', '-i', mp4_file, '-q:a', '0', '-map', 'a', mp3_file],
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(f"\nThe file has been converted to MP3 successfully: {mp3_file}")

    # Fetch Discogs metadata
    discogs_metadata = meta.get_meta(os.path.basename(mp3_file).replace('.mp3', ''))

    if discogs_metadata:
        print("\nDiscogs Metadata:")
        for key, value in discogs_metadata.items():
            print(f"{key}: {value}")

        # Attach Discogs metadata to the downloaded file
        meta.attach_meta(mp3_file, discogs_metadata)

    # Delete the original video file if needed
    print(f"\nDeleting old file...")
    os.remove(mp4_file)
    print(f"\nDone!")

    return mp3_file


if __name__ == "__main__":
    main()
