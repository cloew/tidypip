from .pip_versions import PipVersions
from subprocess import call, check_output

class PipWrapper:
    """ Helper class to manage calling the proper Pip command """
    
    def __init__(self, pipCmd=None):
        """ Initialize with the pip command to call """
        if pipCmd is None:
            pipCmd = 'pip'
        self.pipCmd = pipCmd
    
    def install(self, packages):
        """ Install the given packages """
        args = [self.pipCmd, 'install'] + [package.installAs for package in packages]
        print(args)
        # call(args)
        
    def versions(self):
        """ Return the current version information """
        freezeInfo = check_output(['pip', 'freeze'], universal_newlines=True)
        versions = {}
        for packageInfo in freezeInfo.split('\n'):
            packageInfo = packageInfo.strip()
            if packageInfo != '' and '==' in packageInfo:
                package, version = packageInfo.split('==')
                versions[package] = version
                
        return PipVersions(versions)