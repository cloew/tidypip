from distutils.core import setup

setup(name='tidypip',
      version='0.1.1',
      description="",
      author='Chris Loew',
      author_email='cloew123@gmail.com',
      packages=['tidypip',
                'tidypip.args',
                'tidypip.commands',
                'tidypip.packages'],
      install_requires=['kao_command'],
      scripts=['tidypip/scripts/tidypip']
     )