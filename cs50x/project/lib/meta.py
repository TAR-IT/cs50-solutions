# script for fetching metadata using the Discogs API
from mutagen.id3 import ID3, TIT2, TPE1, TDRC
from decouple import config
import discogs_client

def main():
    get_meta()
    attach_meta()


def get_meta(title):
    try:
        # Access the environment variable - or set user token manually
        user_token = config("DISCOGS_USER_TOKEN", default="")

        # Initialize Discogs client with the user token
        discogs = discogs_client.Client('MPy3.py', user_token=user_token)

        # Search for releases based on the video title
        search_results = discogs.search(title, type='release')

        if search_results:
            # Take the first result
            release = search_results[0]

            metadata = {
                'title': release.title,
                'artist': release.artists[0].name if release.artists else '',
                'year': release.year,
                # TODO: Add more meta tags
            }
            return metadata
        else:
            print("\nNo Discogs results found.")
            return None
    except Exception as e:
        print(f"\nError fetching Discogs metadata: {e}")
        return None

def attach_meta(file_path, metadata):
    try:
        audio = ID3(file_path.replace('.mp4', '.mp3'))
        audio.add(TIT2(encoding=3, text=metadata['title']))
        audio.add(TPE1(encoding=3, text=metadata['artist']))
        audio.add(TDRC(encoding=3, text=str(metadata['year'])))
        # TODO: Add more meta tags
        audio.save()
        print("\nMetadata attached to the file.")
    except Exception as e:
        print(f"\nError attaching metadata to the file: {e}")

if __name__ == "__main__":
    main()
