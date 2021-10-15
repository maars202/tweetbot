from setuptools import setup
INSTALL_REQUIRES = [
      'selenium',
      'pandas'
]
setup(name='tweetbot',
    version='0.1',
    description='Twitter bot for extract information from twitter based on number of tweets needed and search query string',
    url='http://example.com',
    author='Maaruni',
    author_email='maarunip.2020@scis.smu.edu.sg',
    license='GPL',
    packages=['tweetbot'],
    zip_safe=False,
)