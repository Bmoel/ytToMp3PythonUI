import subprocess as subp;

def runYoutubeDl(url: str):
    subp.run(['youtube-dl','-x', url]);