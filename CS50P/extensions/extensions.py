def get_media_type(filename):
    media_types = {
        '.gif': 'image/gif',
        '.jpg': 'image/jpeg',
        '.jpeg': 'image/jpeg',
        '.png': 'image/png',
        '.pdf': 'application/pdf',
        '.txt': 'text/plain',
        '.zip': 'application/zip'
    }

    ext = filename.lower().rsplit('.', 1)[-1].strip()

    if not ext or ('.' + ext) not in media_types:
        return 'application/octet-stream'

    return media_types['.' + ext]

def main():
    filename = input("Enter the name of the file: ")
    media_type = get_media_type(filename)
    print(media_type)

if __name__ == "__main__":
    main()