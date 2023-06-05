# Welcome to Cloud Functions for Firebase for Python!
# To get started, simply uncomment the below code or create your own.
# Deploy with `firebase deploy`

from firebase_functions import https_fn
from firebase_admin import initialize_app, messaging
# from datetime import datetime

initialize_app()


@https_fn.on_request()
def hello_world_test(req: https_fn.Request) -> https_fn.Response:
    method = req.method
    if(method == 'POST'):
        request_json = req.get_json(silent=True)
        title = request_json['title']
        body = request_json['body']
        tokens = request_json['tokens']
        # nowTime = datetime.now()
        message = messaging.MulticastMessage(
            data={
                'click_action': 'FLUTTER_NOTIFICATION_CLICK', 
                'event_trigger_type': 'Batch', 
                'event_trigger_time': '2021-08-03T19:00:00+00:00'
                },
            tokens=tokens,
            notification=messaging.Notification(
                title=title,
                # body='{body} {nowTime}!'.format(body=body, nowTime=nowTime),
                body=body,
            )
        )
        response = messaging.send_multicast(message)
        print(response)
    return https_fn.Response("Hello world!")