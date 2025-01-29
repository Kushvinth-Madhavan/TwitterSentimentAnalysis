# setup.py
from setuptools import setup, find_packages

setup(
    name="twitter-sentiment-analysis",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        'tweepy==4.14.0',
        'textblob==0.17.1',
        'python-dotenv==1.0.0',
        'pandas==2.0.0',
        'nltk==3.8.1',
    ],
    author="Kushvinth Madhavan",
    author_email="kushvinthmadhavan@gmail.com",
    description="A Twitter sentiment analysis tool using TextBlob",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Kushvinth-Madhavan/twitter-sentiment-analysis",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
