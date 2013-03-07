NAME = 'boost'
VERSION = '1.53.0'
DOWNLOADS = ['http://downloads.sourceforge.net/project/boost/boost/%s/boost_%s.tar.bz2' %
            tuple([VERSION, VERSION.replace('.', '_')])]
ARTIFACTS =  {
        'includes': [{
            'source':'boost_%s/boost' % VERSION.replace('.', '_'),
            'name':'boost'
        }]
    }


