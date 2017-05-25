# -*- coding: utf-8 -*-

import logging
import logging.config
from slack import Slack
import traceback
import sys
import os

logger = logging.getLogger()
logger.setLevel(logging.INFO)




def main(event, context):
    slack = Slack()

    try:
        print('aaaaa')

    except Exception as e:
        slack.sendMessage('test:' + traceback.format_exc(sys.exc_info()[2]), "#error")
        logger.error(traceback.format_exc(sys.exc_info()[2]))


def lambda_handler(event, context):
    """
    :param event:
    :param context:
    :return:
    """
    logger.setLevel(logging.INFO)
    main(event, context)
    return {
        'message': 'done'
    }

if __name__ == '__main__':
    logging.config.fileConfig("logging.conf")
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    event = {}
    main(event, None)