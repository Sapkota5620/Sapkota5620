import requests #getting content of TED TALK PAGE
from bs4 import BeautifulSoup #WEB SCRAPING
import re # Regular Expression pattern matching
import sys # for argument parsing

# Exception Handling
'''
if len(sys.argv) > 1:
    url = sys.argv[1]
else:
    sys.exit("Error: Please enter the TED TALK URL")
'''
url = "https://www.ted.com/talks/iseult_gillespie_the_myth_of_narcissus_and_echo"
# url

r = requests.get(url)
print("Download about to start")

soup = BeautifulSoup(r.content,'lxml')
result = ""
for val in soup.findAll("script"):
    if(re.search("talkPage.init", str(val))) is not None:
        result = str(val)

result_mp4 = re.search("(?P<url>https?://[^\s] +)(mp4)", result).group("url")
mp4_url = result_mp4.split('"')[0]

print("Downloading video from ..........." + mp4_url)

file_name = mp4_url.split("/")[len(mp4_url.split("/")) - 1].split('?')[0]

print("Storing video in ...." + file_name)

r = requests.get(mp4_url)

with open(file_name, 'wb') as f:
    f.write(r.content)
# Alternate method
# urlretrieve(mp4_url, file_name)


