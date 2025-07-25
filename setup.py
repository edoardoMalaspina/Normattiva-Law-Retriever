from setuptools import setup, find_packages

setup(
    name="lawtextfinder",
    version="0.1.0",
    description="A tool to find law texts from Normattiva",
    author="Your Name",
    packages=find_packages(),
    install_requires=[
        "attrs>=25.3.0",
        "beautifulsoup4>=4.13.4",
        "certifi>=2025.7.14",
        "cffi>=1.17.1",
        "charset-normalizer>=3.4.2",
        "exceptiongroup>=1.3.0",
        "h11>=0.16.0",
        "idna>=3.10",
        "outcome>=1.3.0.post0",
        "pycparser>=2.22",
        "PySocks>=1.7.1",
        "requests>=2.32.4",
        "selenium>=4.34.2",
        "sniffio>=1.3.1",
        "sortedcontainers>=2.4.0",
        "soupsieve>=2.7",
        "trio>=0.30.0",
        "trio-websocket>=0.12.2",
        "typing_extensions>=4.14.1",
        "urllib3>=2.5.0",
        "websocket-client>=1.8.0",
        "wsproto>=1.2.0"
    ],
    python_requires='>=3.6',
)
