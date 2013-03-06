import os
import shutil
from utils import download, untar

DOWNLOAD_DIR = "downloads"
SOURCE_DIR = "source"
BUILD_DIR = "build"


def get_default_working_dir(name):
    return os.path.join(os.getcwd(), BUILD_DIR, name)


def get_source_dir(path):
    return os.path.join(path, SOURCE_DIR)


def get_download_dir(path):
    return os.path.join(path, DOWNLOAD_DIR)


def build_component(name, working_dir=None):

    if not working_dir:
        working_dir = get_default_working_dir(name)

    config_module = __import__("components.%s.config" % name, fromlist="components")

    print 'Building version:%s of module:%s ' % tuple([config_module.VERSION, config_module.NAME])

    clean_component(name)

    #Download and untar required bits
    for download_url in config_module.DOWNLOADS:
        download_file_path = download(download_url, get_download_dir(working_dir))
        untar(download_file_path, get_source_dir(working_dir))

    # TODO Do the actual build steps if necessary

    #Done - copy any includes or libs we've built
    for include in config_module.INCLUDES:
        source = os.path.join(get_source_dir(working_dir), include['source'])
        destination = os.path.join(get_source_dir(working_dir), include['destination'])
        shutil.copytree(source, destination)

    print "Completed building component:%s" % name
    print "********************************************************************************************************"


def clean_component(name, working_dir=None):

    if not working_dir:
        working_dir = get_default_working_dir(name)

    # Don't remove downloads as they could take a while
    print "Cleaning component:%s" % name
    shutil.rmtree(get_source_dir(working_dir))





