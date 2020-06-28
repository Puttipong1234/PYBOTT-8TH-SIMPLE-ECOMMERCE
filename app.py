from flask import Flask, request, abort
from fuzzywuzzy import fuzz
from firebase import firebase

from OmisePython.credit_card import create_token , create_charge
from OmisePython.internet_banking import net_banking_create_source_and_charge
from OmisePython.promptpay import promptpay

from config import DATABASE_URI , OMISE_PUBLIC_KEY , OMISE_SECRET_KEY
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
    
    if MESSAGE_FROM_USER == "ยกเลิกคำสั่ง":
        data = {
            "session" : "None",
            "shoping_data" : "None"
        }
        firebase.patch(DATABASE_USER+"/"+UID + "/",data)
    
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
            "shoping_data" : {
                    "สินค้า" : MESSAGE_FROM_USER,
                    "ราคา" : firebase.get(DATABASE_PRODUCT+"/"+MESSAGE_FROM_USER,None)["ราคา"],
                    "payment_data" : "None"
                }
            }
            firebase.patch(DATABASE_USER+"/"+UID+"/",data)
    
    elif user_session == "เลือกวิธีการชำระเงิน":
        if MESSAGE_FROM_USER == "พร้อมเพย์":
            # สร้าง charge บน omise
            # update payment data
            # สร้าง qr code ขึ้นมา
            ราคาสินค้า = firebase.get(DATABASE_USER+"/"+UID+"/shoping_data",None)["ราคา"]
            charge_id , qr_code_url = promptpay(amount=int(ราคาสินค้า),currency="thb",OMISE_SECRET_KEY=OMISE_SECRET_KEY)
            
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text="กรุณาแสกน qr code เพื่อชำระสินค้า ที่ลิงค์ \n" + str(qr_code_url)))
            
            data = {
                    "charge_id" : charge_id,
                    "status" : "pending"
                }
            firebase.patch(DATABASE_USER+"/"+UID+"/"+MESSAGE_FROM_USER + "/shoping_data/payment_data/",data)
            
            data = firebase.get(DATABASE_USER+"/"+UID,None)
            data["session"] = "รอชำระเงิน_พร้อมเพย์"
            firebase.patch(DATABASE_USER+"/"+UID,data)
            
        elif MESSAGE_FROM_USER == "บัตรเครดิต":
            
            # สร้าง charge บน omise
            # update payment data
            
            Example_input_for_user1 = TextSendMessage(text="กรุณาระบุข้อมูลบัตร (ตามตัวอย่างดังนี้)")
            Example_input_for_user2 = TextSendMessage(text="ชื่อบัตร,เลขบัตร,วันหมดอายุ")
            Example_input_for_user3 = TextSendMessage(text="BUMBIN ARAUPORN,4242424242424242,02/23")
            Exampl_Image = ImageSendMessage(original_content_url="https://p3.isanook.com/hi/0/ud/277/1388224/2.jpg",
                                            preview_image_url="https://p3.isanook.com/hi/0/ud/277/1388224/2.jpg")
            
            msgs = [Example_input_for_user1,Example_input_for_user2,Example_input_for_user3,Exampl_Image]
            
            line_bot_api.reply_message(
                event.reply_token,
                messages=msgs)
            
            data = firebase.get(DATABASE_USER+"/"+UID,None)
            data["session"] = "รับข้อมูลบัตรเครดิต"
            firebase.patch(DATABASE_USER+"/"+UID,data)
            
        elif MESSAGE_FROM_USER == "อินเตอร์เน็ต แบงค์กิ้ง":
            
            ราคาสินค้า = firebase.get(DATABASE_USER+"/"+UID+"/shoping_data",None)["ราคา"]
            charge_id , authorize_uri = net_banking_create_source_and_charge(amount=int(ราคาสินค้า),
                                                                             currency="thb",
                                                                             return_uri="https://www.facebook.com/groups/586940368917146/?__tn__=-U",
                                                                             _type="internet_banking_ktb",
                                                                             OMISE_SECRET_KEY=OMISE_SECRET_KEY)
            
            msg1 = TextSendMessage(text="กรุณากดที่ลิงค์ด้านล่างเพื่อเข้าสู่ระบบจ่ายเงิน อินเตอร์เน็ตแบงค์กิ้ง")
            msg2 = TextSendMessage(text=authorize_uri)
            
            # สร้าง charge บน omise
            line_bot_api.reply_message(
                event.reply_token,
                messages=[msg1,msg2])
            
            data = {
                    "charge_id" : charge_id,
                    "status" : "pending"
                }
            firebase.patch(DATABASE_USER+"/"+UID+"/"+MESSAGE_FROM_USER + "/shoping_data/payment_data/",data)

            data = firebase.get(DATABASE_USER+"/"+UID,None)
            data["session"] = "รอชำระเงิน_อินเตอร์เน็ตแบงค์กิ้ง"
            firebase.patch(DATABASE_USER+"/"+UID,data)

    elif user_session == "รับข้อมูลบัตรเครดิต":
        
        ชื่อสินค้า = firebase.get(DATABASE_USER+"/"+UID+"/shoping_data",None)["สินค้า"]
        ราคาสินค้า = int(firebase.get(DATABASE_USER+"/"+UID+"/shoping_data",None)["ราคา"])*100
        
        as_list = MESSAGE_FROM_USER.split(",")
        name = as_list[0].strip(" ")
        number = as_list[1].strip(" ")
        ex_month , ex_year = as_list[2].split("/")
        
        token_id = create_token(name=name,
                                number=number,
                                expiration_month=ex_month.strip(" "),
                                expiration_year=ex_year.strip(" "),
                                OMISE_KEY_PUBLIC=OMISE_PUBLIC_KEY)
        
        status = create_charge(description="ค่าใช้จ่ายสำหรับ {}".format(ชื่อสินค้า),
                                  amount=ราคาสินค้า,
                                  currency="thb",
                                  token_id=token_id)
        
        print(status)
        
        if status == "successful":
        
            line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text="ชำระเงินเรียบร้อย กรุณารอรับสินค้า 2-5 วันนะคะ"))
            
            data = firebase.get(DATABASE_USER+"/"+UID,None)
            data["session"] = "None"
            firebase.patch(DATABASE_USER+"/"+UID,data)
        
        else :
            
            Example_input_for_user0 = TextSendMessage(text="เกิดข้อผิดพลาด กรุณากรอกข้อมูลบัตรใหม่อีกครั้งคะ")
            Example_input_for_user1 = TextSendMessage(text="กรุณาระบุข้อมูลบัตร (ตามตัวอย่างดังนี้)")
            Example_input_for_user2 = TextSendMessage(text="ชื่อบัตร,เลขบัตร,วันหมดอายุ")
            Example_input_for_user3 = TextSendMessage(text="BUMBIN ARAUPORN,4242424242424242,02/23")
            
            msgs = [Example_input_for_user0,Example_input_for_user1,Example_input_for_user2,Example_input_for_user3]
            
            line_bot_api.reply_message(
                    event.reply_token,
                    messages=msgs)
            
            data = firebase.get(DATABASE_USER+"/"+UID,None)
            data["session"] = "รับข้อมูลบัตรเครดิต"
            firebase.patch(DATABASE_USER+"/"+UID,data)

    elif "รอชำระเงิน" in user_session:
        line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text="กรุณาชำระเงินก่อนการทำรายการใหม่คะ หรือ กดปุ่มยกเลิกคำสั่ง เพื่อยกเลิกการสั่งซื้อสินค้าทั้งหมด"))
        
        
    

@handler.add(MessageEvent , message=StickerMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token, StickerSendMessage(package_id='1', sticker_id='1'))


if __name__ == "__main__":
    app.run(port=8000)