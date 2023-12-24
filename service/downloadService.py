import subprocess as subp;
import re;

YOUTUBE_PATTERN = '^(https?\:\/\/)?(www\.youtube\.com|youtu\.be)\/.+$';
INVALID_ERROR_MSG = 'Invalid Youtube URL';
DOWNLOAD_WALL = '--------------------------------';
DONE_DOWNLOADING = 'Download Successful';

def isValidYoutubeUrl(url: str) -> bool:
    return re.search(YOUTUBE_PATTERN, url);

def runYoutubeDl(url: str):
    if not isValidYoutubeUrl(url):
        print(INVALID_ERROR_MSG);
        return;
    print(DOWNLOAD_WALL);
    subp.run([
        'youtube-dl',
        '-x', 
        url, 
        '--audio-format',
        'mp3'
    ]);
    print(DONE_DOWNLOADING);
    print(DOWNLOAD_WALL);