from utils import download_all

def build_component(name):
    print 'Building module:%s' % name
    config_module = __import__("components.%s.config" % name, fromlist="components")
    download_all(config_module.DOWNLOADS)
