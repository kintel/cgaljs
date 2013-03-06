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


def build_component(name, includes_dir, libs_dir, working_dir=None):

    try:
        component = __import__("components.%s.config" % name, fromlist="components")
    except:
        print "No such component:%s" % name
        return

    print 'Building version:%s of component:%s ' % tuple([component.VERSION, component.NAME])

    if not working_dir:
        working_dir = get_default_working_dir(name)

    clean_component(name)

    #Download and untar required bits
    for download_url in component.DOWNLOADS:
        download_file_path = download(download_url, get_download_dir(working_dir))
        untar(download_file_path, get_source_dir(working_dir))

    # TODO Patch source
    # TODO Configure
    # TODO Patch any generated config or headers
    # TODO Build

    # Copy artifacts to given destination
    try:
        for include in component.ARTIFACTS['includes']:
            source = os.path.join(get_source_dir(working_dir), include['source'])
            destination = os.path.join(includes_dir, include['name'])
            shutil.copytree(source, destination)
    except:
        print "Component did not produce any includes"

    try:
        for lib in component.ARTIFACTS['libs']:
            pass
    except:
        print "Component did not produce any libs"

    print "Completed building component:%s" % name
    print "********************************************************************************************************"


def clean_component(name, working_dir=None):
    if not working_dir:
        working_dir = get_default_working_dir(name)

    # Don't remove downloads as they could take a while
    print "Cleaning component:%s" % name
    shutil.rmtree(get_source_dir(working_dir))





