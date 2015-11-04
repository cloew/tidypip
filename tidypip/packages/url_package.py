import posixpath

class UrlPackage:
    """ Represents a package specified as a Url """
    
    def __init__(self, url):
        """ Initialize with the url """
        if ':' in url:
            self.url = url
        else:
            self.url = posixpath.join('git+git://github.com', url)
        
    @property
    def installAs(self):
        """ Return the string to use to Install the package via pip """
        return self.url
        
    def forRequirements(self, versions):
        """ Return the text to use for adding to the Requirements file """
        return self.url