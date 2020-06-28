from flask import Flask, request, abort
from fuzzywuzzy import fuzz
from firebase import firebase

from config import DATABASE_URI
DATABASE_PRODUCT = "PRODUCT_DB"
DATABASE_USER = "USER_DB"
firebase = firebase.FirebaseApplication(DATABASE_URI, None)

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
    
    if not firebase.get(DATABASE_USER+"/"+UID,None):
        data = {
            "session" : "None",
            "shoping_data" : "None"
        }
        firebase.patch(DATABASE_USER+"/"+UID + "/",data)
    
    user_session = firebase.get(DATABASE_USER+"/"+UID,None)["session"]
    
    if user_session == "None":
        if MESSAGE_FROM_USER == "มีอะไรขายบ้าง" or fuzz.ratio(MESSAGE_FROM_USER,"มีอะไรขายบ้าง") > 70:
            
            data = {
            "session" : "เลือกซื้อสินค้า",
            "shoping_data" : "None"
            }
            user_session = firebase.patch(DATABASE_USER+"/"+UID,data)
            
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text=formatter(DICT=update_product())))
    
    elif user_session == "เลือกซื้อสินค้า":
        if MESSAGE_FROM_USER in firebase.get(DATABASE_PRODUCT,None).keys():
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text="กรุณาเลือกวิธีการชำระเงิน"))
            
            data = {
            "session" : "เลือกวิธีการชำระเงิน",
            "shoping_data" : [{
                    "สินค้า" : MESSAGE_FROM_USER,
                    "payment_data" : "None"
                }]
            }
            firebase.patch(DATABASE_USER+"/"+UID,data)
    
    elif user_session == "เลือกวิธีการชำระเงิน":
        if MESSAGE_FROM_USER == "พร้อมเพย์":
            # สร้าง charge บน omise
            # update payment data
            # สร้าง qr code ขึ้นมา
            
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text="กรุณาแสกน qr code จากลิงค์"))
            
        elif MESSAGE_FROM_USER == "บัตรเครดิต":
            # สร้าง charge บน omise
            # update payment data
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text="กรุณาระบุข้อมูลบัตร"))
            
        elif MESSAGE_FROM_USER == "อินเตอร์เน็ต แบงค์กิ้ง":
            # สร้าง charge บน omise
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text="กรุณากดที่ลิงค์ด้านล่างเพื่อเข้าสู่ระบบจ่ายเงิน อินเตอร์เน็ตแบงค์กิ้ง"))
            

@handler.add(MessageEvent , message=StickerMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token, StickerSendMessage(package_id='1', sticker_id='1'))


if __name__ == "__main__":
    app.run(port=8080)