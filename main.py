import urllib
import urllib2
import webbrowser
import os

day = int(input("Enter Day:"))
month = int(input("Enter Month:"))
year = str(input("Enter Year: "))

if (day<10):
    day = str(0)+str(day)

if (month<10):
    month = str(0)+str(month)

date = str(day)+str(month)+str(year)
rl="http://epaper.jagran.com/epaperimages/"+date+"/varanasi/m-26vns-pg"
#raw link

# Making total links
def start():
    for i in range(1,40):
        gl=rl+str(i)+"-0.png"
        #good link
        fil = pd(gl)
        print ("Pic downloaded at " + gl)
        remove(fil)
    return
#downloading pics
def pd(url):
    file_name = url.split('/')[-1]
    urllib.urlretrieve(url,file_name)
    return file_name

#removing the false ones.
def remove(fpath):
    if (os.path.getsize(fpath)<3000L):
        os.remove(fpath)
        print ("Pic removed -> " + fpath)
    return


start()
