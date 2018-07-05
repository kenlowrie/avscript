from setuptools import setup
from sys import version_info

setup(name='avscript',
      version='0.3.8',
      description='Audio/Visual Script Parser',
      url='https://github.com/kenlowrie/avscript',
      author='Ken Lowrie',
      author_email='ken@kenlowrie.com',
      license='Apache',
      packages=['avscript', 'avscript.avs'],
      install_requires=['pylib_kenl380'],
      entry_points = {
        'console_scripts': ['avscript=avscript.avscript_md:av_parse_file',
                            'avscript{}=avscript.avscript_md:av_parse_file'.format(version_info.major),
                            'mkavscript=avscript.mkavscript_md:mkavscript_md',
                            'mkavscript{}=avscript.mkavscript_md:mkavscript_md'.format(version_info.major),
        ],
      },
      include_package_data=True,
      zip_safe=False)
