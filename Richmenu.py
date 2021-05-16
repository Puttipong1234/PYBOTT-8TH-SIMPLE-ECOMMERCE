
richdata = {
  "size": {
    "width": 2500,
    "height": 1686
  },
  "selected": True,
  "name": "PYBOTT-8TH",
  "chatBarText": "> เมนูหลัก <",
  "areas": [
    {
      "bounds": {
        "x": 42,
        "y": 42,
        "width": 2433,
        "height": 814
      },
      "action": {
        "type": "message",
        "text": "มีอะไรขายบ้าง"
      }
    },
    {
      "bounds": {
        "x": 42,
        "y": 864,
        "width": 784,
        "height": 784
      },
      "action": {
        "type": "message",
        "text": "ยกเลิกรายการทั้งหมด"
      }
    },
    {
      "bounds": {
        "x": 843,
        "y": 869,
        "width": 576,
        "height": 775
      },
      "action": {
        "type": "message",
        "text": "พร้อมเพย์"
      }
    },
    {
      "bounds": {
        "x": 1432,
        "y": 864,
        "width": 636,
        "height": 767
      },
      "action": {
        "type": "message",
        "text": "บัตรเครดิค"
      }
    },
    {
      "bounds": {
        "x": 2089,
        "y": 856,
        "width": 386,
        "height": 788
      },
      "action": {
        "type": "message",
        "text": "อินเตอร์เน็ต แบงค์กิ้ง"
      }
    }
  ]
}


from config import CHANNEL_ACCESS_TOKEN #
channel_access_token = CHANNEL_ACCESS_TOKEN
Image_File_Path = "resource\\richmenu.png"
import json

import requests



def RegisRich(Rich_json,channel_access_token):

    url = 'https://api.line.me/v2/bot/richmenu'

    Rich_json = json.dumps(Rich_json)

    Authorization = 'Bearer {}'.format(channel_access_token)


    headers = {'Content-Type': 'application/json; charset=UTF-8',
    'Authorization': Authorization}

    response = requests.post(url,headers = headers , data = Rich_json)

    print(str(response.json()['richMenuId']))

    return str(response.json()['richMenuId'])

def CreateRichMenu(ImageFilePath,Rich_json,channel_access_token):


    richId = RegisRich(Rich_json = Rich_json,channel_access_token = channel_access_token)

    url = ' https://api-data.line.me/v2/bot/richmenu/{}/content'.format(richId)
    # https://api-data.line.me/v2/bot/richmenu/richmenu-88c05ef6921ae53f8b58a25f3a65faf7/content

    Authorization = 'Bearer {}'.format(channel_access_token)

    headers = {'Content-Type': 'image/jpeg',
    'Authorization': Authorization}

    img = open(ImageFilePath,'rb').read()

    response = requests.post(url,headers = headers , data = img)

    print(response.json())


CreateRichMenu(ImageFilePath=Image_File_Path,Rich_json=richdata,channel_access_token=channel_access_token)
