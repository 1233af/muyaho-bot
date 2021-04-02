import requests
import youtube_dl
import zipfile
import shutil

# url = 'https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip'
# r = requests.get(url, allow_redirects=True)
# open('ffmpeg.zip', 'wb').write(r.content)

zipfile.ZipFile('ffmpeg.zip').extractall('.//ffmpeg')

# shutil.move('/')