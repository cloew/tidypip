from subprocess import call

class PipWrapper:
    """ Helper class to manage calling the proper Pip command """
    
    def install(self, packages):
        """ Install the given packages """
        call(['pip', 'install'] + packages)