from flask import Flask, request, abort
from fuzzywuzzy import fuzz

from product_app import update_product , formatter
from config import CHANNEL_ACCESS_TOKEN , CHANNEL_SECRET

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)

line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(CHANNEL_SECRET)


@app.route("/home")
def home():
    return "Hello World"

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    
    REPLY_TOKEN = event.reply_token #เก็บ reply token
    MESSAGE_FROM_USER = event.message.text #เก็บ ข้อความที่ user ส่งมา
    UID = event.source.user_id #เก็บ user id
    
    if MESSAGE_FROM_USER == "มีอะไรขายบ้าง" or fuzz.ratio(MESSAGE_FROM_USER,"มีอะไรขายบ้าง") > 70:
        
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=formatter(DICT=update_product())))

@handler.add(MessageEvent , message=StickerMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token, StickerSendMessage(package_id='1', sticker_id='1'))


if __name__ == "__main__":
    app.run(port=8080)