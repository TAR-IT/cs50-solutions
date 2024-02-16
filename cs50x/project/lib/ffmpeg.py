# script for checking/installing ffmpeg
import subprocess
import sys


def main():
    if not check_install():
        ask_install()


def check_install():
    try:
        # Use 'where' command on Windows to check for the existence of ffmpeg
        if sys.platform.startswith('win'):
            subprocess.run(['where', 'ffmpeg'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
        else:
            # Use 'which' command on Unix-like systems
            subprocess.run(['which', 'ffmpeg'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
    except subprocess.CalledProcessError:
        return False
    return True

 
def install_windows():
    try:
        subprocess.run(['winget', '--version'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
    except subprocess.CalledProcessError:
        print("Error: 'winget' not found. Please make sure it's available on your system or manually install ffmpeg using your package manager.")
        sys.exit(1)

    try:
        subprocess.run(['winget', 'install', 'ffmpeg'], check=True)
        print("FFmpeg has been installed successfully. Please restart your terminal to make use of the changes, otherwise the script does not work.")
    except subprocess.CalledProcessError:
        print("Error installing FFmpeg. Please install it manually.")
        sys.exit(1)


def install_linux():
    try:
        subprocess.run(['sudo', 'apt-get', 'install', '-y', 'ffmpeg'], check=True)
        print("FFmpeg has been installed successfully. Please restart your terminal to make use of the changes, otherwise the script does not work.")
    except subprocess.CalledProcessError:
        print("Error installing FFmpeg. Please install it manually using your package manager.")
        sys.exit(1)


def install_macos():
    try:
        subprocess.run(['/usr/bin/ruby', '-e', '$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)'], check=True)
        subprocess.run(['brew', 'install', 'ffmpeg'], check=True)
        print("FFmpeg has been installed successfully. Please restart your terminal to make use of the changes, otherwise the script does not work.")
    except subprocess.CalledProcessError:
        print("Error installing FFmpeg. Please install it manually.")
        sys.exit(1)


def ask_install():
    response = input("FFmpeg is not installed. Do you want to install it automatically? (y/n): ").strip().lower()
    if response == 'y':
        if sys.platform.startswith('win'):
            install_windows()
        elif sys.platform.startswith('linux'):
            install_linux()
        elif sys.platform.startswith('darwin'):
            install_macos()
        else:
            print("Unsupported operating system.")
            sys.exit(1)
    else:
        print("FFmpeg is required for this script. Please install it manually.")
        sys.exit(1)


if __name__ == "__main__":
    main()
