# -*- coding: utf-8 -*-

import logging
import logging.config
import traceback
import sys
from slack import Slack
from sqs import Sqs

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    slack = Slack()
    sqs = Sqs()

    try:
        for loop_count in range(0, 10):
            response = sqs.send_message(loop_count)
            logger.info(response)

            return event

    except Exception as e:
        slack.send_message('test:' + traceback.format_exc(sys.exc_info()[2]), "#error")
        logger.error(traceback.format_exc(sys.exc_info()[2]))
