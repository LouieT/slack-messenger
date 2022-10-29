from pathlib import Path
from setuptools import setup, find_packages

VERSION = '0.1.2'
DESCRIPTION = 'Slack Messanger Client using Incoming Webhooks'

directory = Path(__file__).parent
LONG_DESCRIPTION = (directory / "README.md").read_text()

setup(
    name="slack_messenger",
    version=VERSION,
    author="Louis Tadman",
    author_email="<noreply@louistadman.com>",
    url="https://github.com/LouieT/slack-messenger",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=["requests==2.*"],
    keywords=['python', 'Slack', "Messenger"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3 :: Only",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
    project_urls={
        "Documentation": "https://github.com/LouieT/slack-messenger",
        "Source": "https://github.com/LouieT/slack-messenger",
    },
)
