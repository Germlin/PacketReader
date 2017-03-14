from setuptools import setup
import codecs

with codecs.open('README.rst', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='PacketReader',
    version='1.0.0',
    description='Python Pcap Parser',
    long_description=long_description,
    author='Yue',
    author_email='linyue92@outlook.com',
    url='https://github.com/Reuynil/PacketReader',
    license='MIT',
    packages=['PacketReader'],
    classifiers=[
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
    ],
)
