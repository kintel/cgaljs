import os

NAME = 'gmp'
VERSION = '5.1.1'
DOWNLOADS = ['ftp://ftp.gmplib.org/pub/gmp/gmp-%s.tar.bz2' % VERSION]
SOURCE_DIR = 'gmp-%s' % VERSION
CONFIGURE_CMD = 'emconfigure ./configure --disable-assembly'
MAKE_CMD = 'emmake make -j4'
CONFIG_PATCHES = [
    {
        'file': 'config.h',
        'patch': 'config.h.patch'
    }
]
ARTIFACTS =  {
    'includes': [{
                     'source':'gmp-%s' % VERSION,
                     'name':'gmp'
                 }],
    'libs': [{
                     'source': os.path.join('gmp-%s' % VERSION, '.libs', 'libgmp.so'),
                     'name':'libgmp.so'
                 }]
}

