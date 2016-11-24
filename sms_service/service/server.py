# coding: utf-8

from concurrent import futures
import time

import grpc
from attackt.sms import SMSManager
from attackt.service.settings import (
    SMS_PORT,
    SMS_ACCOUNT_SID,
    SMS_ACCOUNT_TOKEN,
    SMS_SUB_ACCOUNT_SID,
    SMS_SUB_ACCOUNT_TOKEN,
    SMS_APP_ID,
)

import captcha_service_pb2 as pb

sms_manager = SMSManager(
    SMS_ACCOUNT_SID,
    SMS_ACCOUNT_TOKEN,
    SMS_SUB_ACCOUNT_SID,
    SMS_SUB_ACCOUNT_TOKEN,
    SMS_APP_ID,
)


class CaptchaService(pb.CaptchaServiceServicer):

    def __init__(self):
        pass

    def SendSMSCaptcha(self, request, context):
        sms_manager.send_auth_code(
            request.mobile, request.captcha, expired_minutes=request.expired_minutes,
            template_id=request.template_id,
        )
        return pb.SendSMSResponse(ret=1)

    def SendVoiceCaptcha(self, request, context):
        sms_manager.send_voice_code(request.mobile, request.captcha, request.play_times)
        return pb.SendVoiceResponse(ret=1)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb.add_CaptchaServiceServicer_to_server(CaptchaService(), server)
    server.add_insecure_port('[::]:{}'.format(SMS_PORT))
    server.start()

    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == "__main__":
    serve()
