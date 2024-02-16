import re

def main():
    print(parse(input("HTML: ")))

def parse(s):
    # Define the regular expression pattern to find the YouTube URL in src attribute
    pattern = r'src="(?:https?:)?//(?:www\.)?youtube\.com/embed/([^"]+)"'

    # Search for the pattern in the input HTML
    match = re.search(pattern, s)

    if match:
        # Extract the video ID from the first capturing group
        video_id = match.group(1)

        # Convert the video ID to the shorter youtu.be format
        short_youtube_url = f"https://youtu.be/{video_id}"

        return short_youtube_url
    else:
        # If no YouTube URL is found, return None
        return None

if __name__ == "__main__":
    main()
