# slack-messenger

## Description

The **slack-messenger** is a simple package that helps send Slack Messages via Incoming Webhook URLs. For more information on how to create 
a Slack App, and how to generate an incoming webhook URL please read the official Slack documentation on [sending messages using Incoming Webhooks](https://api.slack.com/messaging/webhooks).

[![Downloads](https://pepy.tech/badge/slack-messenger)](https://pepy.tech/project/slack-messenger)
[![Downloads](https://pepy.tech/badge/slack-messenger/month)](https://pepy.tech/project/slack-messenger)
[![Supported Versions](https://img.shields.io/pypi/pyversions/requests.svg)](https://pypi.org/project/requests)

## How to use slack-messenger

```python
from slack_messenger import SlackMessenger

# Create the SlackMessenger object with your Incoming Webhook URL
url = "https://hooks.slack.com/services/<rest-of-the-webhook>"
sm = SlackMessenger(slackbot_webhook_url=url)

# Create your message, you can use the usual formatting and layout blocks available from Slack
message = "Hello Slack :alert-emoji:, this is sent from `slack messenger`"

# The 'send_slack_msg' method will return a tuple with the first item boolean to represent if sending
# the message was successful and the second item as a string of text indicating if the message was 
# successfully sent or failed along with the message content and error message in the event of failure.
message_success, response_msg = sm.send_slack_msg(message=message)
print(f"SUCCESS: {message_success}  RESPONSE MSG: {response_msg}")

# If you wish to include a slack formatted date and timestamp in your message you can call the below
# method to return the slack date and include it in your message body
slack_date = sm.get_slack_formatted_date_num_time_secs()
```

## Installing slack-messenger

Requests is available on PyPI:

```console
$ python -m pip install slack-messenger
```
