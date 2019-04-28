#Actual problem: Start at: http://py4e-data.dr-chuck.net/known_by_Bailley.html
#Find the link at position 18 (the first name is 1). Follow that link.
#Repeat this process 7 times. The answer is the last name that you retrieve.
#Hint: The first character of the name of the last page that you will load is: I

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()

soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('a')

position = input('Enter position: ')
position = int(position)
position = position - 1 # to take into account 0,1,2 ...
count = input('Enter count: ') # desired amount of cycle repetitions
count = int(count)

meter = 0 # for 0 repetitions of the cycle
meter = int(meter)

while count != meter :

    print('TAG:', tags[position])
    print('URL:', tags[position].get('href', None))
    print('Contents:', tags[position].contents[0])
    print('Attrs:', tags[position].attrs)
    meter = meter + 1

    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    url = tags[position].get('href', None)
    print(url)
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup('a')
    print('break', meter, count)
