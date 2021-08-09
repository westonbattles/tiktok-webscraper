from setuptools import setup

setup(
    name='tiktokscraper',
    version='0.1.0',
    description='A simple webscraper for tiktok data',
    long_description = 'file: README.md',
    long_description_content_type = 'text/markdown',
    url='https://github.com/westonbattles/tiktok-webscraper',
    author='Weston Battles',
    author_email='westonb.work@gmail.com',
    license='MIT',
    packages=['tiktokscraper'],
    
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3'
    ],
)