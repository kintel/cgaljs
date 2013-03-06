import os
import urllib2

DOWNLOADS_DIRECTORY = "downloads"

def download_all(urls):
    for url in urls:
        download(url)


def download(url, filename=None):

    if filename is None:
        filename = url.split('/')[-1]

    filename = os.path.join(DOWNLOADS_DIRECTORY, filename)
    print 'Downloading:%s to:%s' % tuple([url, filename])

    if os.path.isfile(filename):
        print 'Already downloaded'
        return

    if not os.path.exists(DOWNLOADS_DIRECTORY):
        os.makedirs(DOWNLOADS_DIRECTORY)

    u = urllib2.urlopen(url)
    localFile = open(filename, 'w')
    localFile.write(u.read())
    localFile.close()
    print 'Download completed'


