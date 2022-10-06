from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'Slack Messanger Client using Incoming Webhooks'
LONG_DESCRIPTION = 'This is a simple package that helps send Slack Messages via Incoming Webhook URLs'

setup(
    name="slack-messenger",
    version=VERSION,
    author="Louis Tadman",
    author_email="<noreply@louistadman.com>",
    url="https://github.com/LouieT/slack-messenger",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=["requests==2.*", "datetime==*", "calendar==*"],
    keywords=['python', 'Slack', "Messenger"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)