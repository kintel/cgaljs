NAME = 'mpfr'
VERSION = '3.1.1'
DOWNLOADS = ['http://www.mpfr.org/mpfr-current/mpfr-%s.tar.bz2' % VERSION]
SOURCE_DIR = 'mpfr-%s' % VERSION
CONFIGURE_CMD = 'emconfigure ./configure --with-gmp-include={includes}/gmp --with-gmp-lib={libs}/libgmp.so'
MAKE_CMD = 'emmake make -j4'
CONFIG_PATCHES = [
    {
        'file': 'configure',
        'patch': 'configure.patch'
    }
]
ARTIFACTS =  {
    'includes': [{
                     'source':'mpfr-%s/src' % VERSION,
                     'name':'mpfr'
                 }],
    'libs': [{
                 'source': 'mpfr-%s/src/.libs/libmpfr.so' % VERSION,
                 'name':'libmpfr.so'
             }]
}





