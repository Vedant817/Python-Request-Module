import requests

# Streaming helps in knowing that how much file is downloaded and how much file is to be downloaded.
url = 'https://www.pagalwrold.com/siteuploads/files/sfd7/3089/Save%20Your%20Tears%20-%20The%20Weeknd(PagalWorld).mp3'
r = requests.get(url, stream=True)
fp = open('Save Your Tears.mp3', 'wb')
fp.write(r.content)
fp.close()
# To print how much is downloaded, use r.header, and we can add progress bar using different third party libraries.
