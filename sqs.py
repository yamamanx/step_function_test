# -*- coding: utf-8 -*-


import os
import boto3
import json

class Sqs(object):
    def __init__(self):
        self.url = os.environ['SQS_URL']
        self.sqs_client = boto3.client('sqs')

    def send_message(self,process_no):
        queue_data = {}
        queue_data['process_no'] = process_no
        response = self.sqs_client.send_message(
            QueueUrl=self.url,
            MessageBody=json.dumps(queue_data)
        )
        return response

    def get_message(self):
        message = self.sqs_client.receive_message(
            QueueUrl=self.url,
            MaxNumberOfMessages=1
        )
        return message

    def check_message(self,message):
        return message.has_key('Messages')

    def get_receipt_handle(self,message):
        return message['ReceiptHandle']

    def delete_message(self,receipt_handle):
        response = self.sqs_client.delete_message(
            QueueUrl=self.url,
            ReceiptHandle=receipt_handle
        )
        return response

    def get_message_body(self,message):
        return json.loads(message['Body'])

    def get_value(self,message_body,key):
        return message_body[key]






