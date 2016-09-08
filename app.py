from flask import Flask, request, make_response
from flask_restful import Resource, Api
import os
from spark.rooms import Room
from spark.messages import Message
from spark.session import Session
from spark.webhooks import Webhook

app = Flask(__name__)
api = Api(app)
app.secret_key = 'CHANGEME'

REGISTERED = False


class Status(Resource):

    def get(self):
        return {"status": "ok"}


class SparkWebHook(Resource):
    """
    A Resource template for our Spark Webhook
    """

     # Create your responses here as a dictionary
    response_dict = dict()


    # This will be used for health checks at '/
    def get(self):
        return {'info': 'SparkWebhook',
                'detail': self.response_dict,
                'registered': REGISTERED}

    # Receive a post request
    def post(self):

        # Extract the data key from the POST request

        # Determine the message ID that triggered the webhook

        # Retrieve the message based on ID
        # https://github.com/imapex/spark-python/blob/master/spark/messages.py

        # Conditional to test if we need to respond (if it's in our response_map)

        # Determine Room the message was received in

        # Send Message to room

        # Send response code to the caller
        return {'status': 'processed'}


class RegisterWebhook(Resource):

    def post(self):

        # Register our webhook
        session = Session('https://api.ciscospark.com', os.getenv("SPARK_TOKEN"))
        webhook = Webhook()
        webhook.targetUrl = request.url_root + '/api/spark'
        webhook.resource = 'messages'
        webhook.event = 'created'
        resp = webhook.create(session)
        if resp.ok:
            REGISTERED = True


# Register our resource classes as endpoints to our API
api.add_resource(Status, '/')
api.add_resource(SparkWebHook, '/api/spark')
api.add_resource(RegisterWebhook, '/api/spark/register')


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')