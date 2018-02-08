from setuptools import setup

setup(name='gpapi',
      version='0.4.2',
      description='Unofficial python api for google play',
      url='https://github.com/NoMore201/googleplay-api',
      author='NoMore201',
      author_email='domenico.iezzi.201@gmail.com',
      license='MIT',
      packages=['gpapi'],
      package_data={'gpapi': ['device.properties']},
      install_requires=['pycryptodome',
                        'protobuf',
                        'requests'])
