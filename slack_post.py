# -*- coding: utf-8 -*-

import logging
import logging.config
import traceback
import sys
from slack import Slack
from sqs import Sqs

logger = logging.getLogger()
logger.setLevel(logging.INFO)
SLACK_MESSAGE = 'process_no:{val_process_no}'

def lambda_handler(event, context):
    slack = Slack()
    sqs = Sqs()

    try:
        message = sqs.get_message()
        if sqs.check_message(message):
            message_body = sqs.get_message_body(message)
            process_no = sqs.get_value(message_body,'process_no')

            slack.send_message(SLACK_MESSAGE.format(
                val_process_no = process_no
            ), "#notify")

            return event

        else:
            slack.send_message('no queue', "#notify")

    except Exception as e:
        slack.send_message('test:' + traceback.format_exc(sys.exc_info()[2]), "#error")
        logger.error(traceback.format_exc(sys.exc_info()[2]))
