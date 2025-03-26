try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name='pyuhmegle',
      version='1.07',
      description='Python API for Uhmegle webchat',
      long_description='Python API for Uhmegle webchat. \
                        Usage: https://github.com/holdentheplanet/pyuhmegle',
      author='Holden Moore',
      author_email='holdenchristianmoore@gmail.com',
      url='https://github.com/holdentheplanet',
      license='MIT',
      packages=[ 'pyuhmegle' ],
      install_requires=[ 'mechanize' ],
      classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX',
        'Topic :: Communications :: Chat',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet :: WWW/HTTP :: Browsers'
      ],
      zip_safe=False)
