import os
import urllib2

DOWNLOADS_DIRECTORY = "downloads"

def download(url, filename=None):

    if filename is None:
        filename = url.split('/')[-1]

    filename = os.path.join(DOWNLOADS_DIRECTORY, filename)

    if not os.path.exists(DOWNLOADS_DIRECTORY):
        os.makedirs(DOWNLOADS_DIRECTORY)

    u = urllib2.urlopen(url)
    localFile = open(filename, 'w')
    localFile.write(u.read())
    localFile.close()


download("ftp://ftp.gmplib.org/pub/gmp/gmp-5.1.1.tar.bz2")