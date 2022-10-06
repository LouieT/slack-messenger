"""
    This is a simple package that helps send Slack Messages via Incoming Webhook URLs

    Use this guide to understand the formatting of Slack messages  https://api.slack.com/reference/surfaces/formatting

    Created By: Louis Tadman
"""

import requests
import datetime
import calendar


class SlackMessenger:

    def __init__(self, slackbot_webhook_url: str):

        self.slackbot_webhook_url = slackbot_webhook_url
        self.headers = {"Content-type": "application/json"}

    ##############################################################################
    @staticmethod
    def __escape_msg_text(message: str):
        """
            Slack uses &, <, and > as control characters for special parsing in text objects, so they must be
            converted to HTML entities if they're not used for their parsing purpose:
        """

        escaped_msg = str(message)

        escaped_msg\
            .replace("&", "&amp;")\
            .replace("<", "&lt;")\
            .replace(">", "&gt;")

        return escaped_msg

    ##############################################################################
    @staticmethod
    def get_slack_format_unix_timestamp():
        """
            For Slack date and time formats you need a unix timestamp to parse, check link for details
            https://api.slack.com/reference/surfaces/formatting#date-formatting
        """

        date = datetime.datetime.utcnow()
        return calendar.timegm(date.utctimetuple())

    ##############################################################################
    def get_slack_formatted_date_num_time_secs(self):
        unix_timestamp = self.get_slack_format_unix_timestamp()
        slack_date = "<!date^" + str(unix_timestamp) + "^ {date_num} {time_secs}|Err>"
        return slack_date

    ##############################################################################
    def send_slack_msg(self, message: str):
        """
            Send a message to the Slack channel webhook URL set in the __init__ method
        """

        message_success = True

        clean_msg = self.__escape_msg_text(message=message)
        msg_payload = {"text": clean_msg}

        response = requests.post(url=self.slackbot_webhook_url,
                                 headers=self.headers,
                                 json=msg_payload)

        http_status = response.status_code
        response_txt = response.text

        if http_status == 200:
            success_msg = f"Successfully sent message to Slack \nSLACK MSG: {clean_msg}"

        else:
            message_success = False
            error_msg = f"Error sending message to Slack \nHTTP STATUS: {http_status} \nERROR MSG: {response_txt}" \
                        f"\nSLACK MSG: {clean_msg}"

        return message_success
