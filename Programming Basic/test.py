import urllib2  
website='https://www.allyourmusic.com'  
try:  
    response = urllib2.urlopen(website)  
    if response.code==200:  
        print("site exists!")  
    else:  
        print("site doesn't exists!")  
except urllib2.HTTPError:  
    print(e.code)  
except urllib2.URLError:  
    print(e.args)