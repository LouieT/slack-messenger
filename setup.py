from setuptools import setup, find_packages

VERSION = '0.1.0'
DESCRIPTION = 'Slack Messanger Client using Incoming Webhooks'
LONG_DESCRIPTION = 'This is a simple package that helps send Slack Messages via Incoming Webhook URLs'

setup(
    name="slack_messenger",
    version=VERSION,
    author="Louis Tadman",
    author_email="<noreply@louistadman.com>",
    url="https://github.com/LouieT/slack-messenger",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
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
    ]
)
