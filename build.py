import utils

DEPENDENCIES = [
    'http://downloads.sourceforge.net/project/boost/boost/1.53.0/boost_1_53_0.tar.bz2',
    'ftp://ftp.gmplib.org/pub/gmp/gmp-5.1.1.tar.bz2',
    'http://www.mpfr.org/mpfr-current/mpfr-3.1.1.tar.bz2',
    'https://gforge.inria.fr/frs/download.php/31640/CGAL-4.1.tar.bz2'
]


def download_dependencies():

    for dependency in DEPENDENCIES:
        utils.download(dependency)

download_dependencies()