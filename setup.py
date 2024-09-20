import setuptools

setuptools.setup(
    name='nxo-omega-prime',
    version='1.0.0',
    author='KOSASIH',
    author_email='kosasihg88@gmail.com',
    description='The Future of Decentralized Communication and Data Exchange.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/KOSASIH/nxo-omega-prime',
    packages=setuptools.find_packages(),
    install_requires=[
        'cryptography==43.0.1',
        'fabric==2.5.0',
        'docker==4.4.0'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache 2.0 License',
        'Operating System :: OS Independent'
    ],
    python_requires='>=3.8'
)
