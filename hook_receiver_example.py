#!/usr/bin/python3

from flask import Flask, abort, request

listener = Flask(__name__)


@listener.route("/mobiledevice_inventory", methods=["POST"])
def main():
    hook_status = None
    try:
        jamf_id = str(request.json["event"]["jssID"])
        webhook_id = str(request.json["webhook"]["id"])
        webhook_event = str(request.json["webhook"]["webhookEvent"])
    except KeyError:
        hook_status = "Error"
        abort(400)
    hook_status = "Success"

    # Do something here with the data

    return {
        "status": hook_status,
        "webhook_id": webhook_id,
        "event": webhook_event,
        "jamf_id": jamf_id,
    }


if __name__ == "__main__":
    listener.run()
