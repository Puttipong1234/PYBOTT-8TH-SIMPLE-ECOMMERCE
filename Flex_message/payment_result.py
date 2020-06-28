success_bubble_msg = {
  "type": "flex",
  "altText": "Flex Message",
  "contents": {
    "type": "bubble",
    "direction": "ltr",
    "header": {
      "type": "box",
      "layout": "vertical",
      "contents": [
        {
          "type": "box",
          "layout": "vertical",
          "flex": 5,
          "contents": [
            {
              "type": "image",
              "url": "https://firebasestorage.googleapis.com/v0/b/pybott-8th.appspot.com/o/%E2%80%94Pngtree%E2%80%94mobilepayment_4999544.png?alt=media&token=2dde96f8-e133-413e-85fe-68c3a01468da",
              "margin": "none",
              "align": "center",
              "size": "md",
              "aspectMode": "fit"
            },
            {
              "type": "text",
              "text": "เตรียมจัดส่ง",
              "margin": "lg",
              "size": "sm",
              "align": "center",
              "weight": "bold",
              "color": "#000000"
            },
            {
              "type": "text",
              "text": "กรุณารอสินค้า 2-5 วันทำการ",
              "margin": "none",
              "size": "lg",
              "align": "center",
              "weight": "bold",
              "color": "#0D0CB5"
            }
          ]
        }
      ]
    },
    "body": {
      "type": "box",
      "layout": "vertical",
      "contents": [
        {
          "type": "separator"
        },
        {
          "type": "box",
          "layout": "horizontal",
          "margin": "lg",
          "contents": [
            {
              "type": "box",
              "layout": "vertical",
              "flex": 7,
              "contents": [
                {
                  "type": "text",
                  "text": "SUCCESS!!",
                  "size": "md",
                  "align": "center",
                  "weight": "bold",
                  "color": "#00C73C"
                },
                {
                  "type": "text",
                  "text": "การชำระเงินเสร็จสิ้น",
                  "size": "xs",
                  "align": "center",
                  "weight": "bold"
                },
                {
                  "type": "text",
                  "text": "ขอขอบพระคุณที่ใช้บริการ",
                  "size": "xs",
                  "align": "center",
                  "weight": "bold"
                }
              ]
            }
          ]
        },
        {
          "type": "box",
          "layout": "vertical",
          "margin": "lg",
          "contents": [
            {
              "type": "button",
              "action": {
                "type": "message",
                "label": "ยกเลิกรายการทั้งหมด",
                "text": "ยกเลิกรายการทั้งหมด"
              },
              "color": "#BDFFAE",
              "height": "sm",
              "style": "secondary"
            },
            {
              "type": "separator",
              "margin": "md"
            }
          ]
        }
      ]
    },
    "footer": {
      "type": "box",
      "layout": "horizontal",
      "contents": [
        {
          "type": "box",
          "layout": "horizontal",
          "spacing": "xxl",
          "contents": [
            {
              "type": "box",
              "layout": "vertical",
              "flex": 8,
              "margin": "md",
              "contents": [
                {
                  "type": "text",
                  "text": "ติดตามเราได้ที่ FB: PYBOTT",
                  "margin": "sm",
                  "size": "xs",
                  "align": "center",
                  "gravity": "center",
                  "weight": "bold"
                },
                {
                  "type": "text",
                  "text": "https://www.facebook.com/Pybott/",
                  "margin": "none",
                  "size": "xxs",
                  "align": "center",
                  "gravity": "center",
                  "weight": "bold"
                }
              ]
            }
          ]
        }
      ]
    },
    "styles": {
      "header": {
        "backgroundColor": "#BDFFAE"
      },
      "footer": {
        "backgroundColor": "#F0F0F0",
        "separatorColor": "#000000"
      }
    }
  }
}

unsuccess_bubble_msg = {
  "type": "flex",
  "altText": "Flex Message",
  "contents": {
    "type": "bubble",
    "direction": "ltr",
    "header": {
      "type": "box",
      "layout": "vertical",
      "contents": [
        {
          "type": "box",
          "layout": "vertical",
          "flex": 5,
          "contents": [
            {
              "type": "image",
              "url": "https://firebasestorage.googleapis.com/v0/b/pybott-8th.appspot.com/o/%E2%80%94Pngtree%E2%80%94mobilepayment_4999544.png?alt=media&token=2dde96f8-e133-413e-85fe-68c3a01468da",
              "margin": "none",
              "align": "center",
              "size": "md",
              "aspectMode": "fit"
            },
            {
              "type": "text",
              "text": "CARD NUMBER",
              "margin": "lg",
              "size": "sm",
              "align": "center",
              "weight": "bold",
              "color": "#000000"
            },
            {
              "type": "text",
              "text": "0123456789999",
              "margin": "none",
              "size": "lg",
              "align": "center",
              "weight": "bold",
              "color": "#0D0CB5"
            }
          ]
        }
      ]
    },
    "body": {
      "type": "box",
      "layout": "vertical",
      "contents": [
        {
          "type": "separator"
        },
        {
          "type": "box",
          "layout": "horizontal",
          "margin": "lg",
          "contents": [
            {
              "type": "box",
              "layout": "vertical",
              "flex": 7,
              "contents": [
                {
                  "type": "text",
                  "text": "NOT SUCCESS",
                  "size": "md",
                  "align": "center",
                  "weight": "bold",
                  "color": "#FF0000"
                },
                {
                  "type": "text",
                  "text": "ขออภัยคะ เกิดข้อผิดพลาดทางทางชำระเงิน ",
                  "size": "xs",
                  "align": "center",
                  "weight": "bold"
                },
                {
                  "type": "text",
                  "text": "กรุณาตรวจสอบบัญชีของท่านอีกครั้ง",
                  "size": "xs",
                  "align": "center",
                  "weight": "bold"
                }
              ]
            }
          ]
        },
        {
          "type": "box",
          "layout": "vertical",
          "margin": "lg",
          "contents": [
            {
              "type": "button",
              "action": {
                "type": "message",
                "label": "ยกเลิกรายการทั้งหมด",
                "text": "ยกเลิกรายการทั้งหมด"
              },
              "color": "#CED5FF",
              "height": "sm",
              "style": "secondary"
            },
            {
              "type": "separator",
              "margin": "md"
            }
          ]
        }
      ]
    },
    "footer": {
      "type": "box",
      "layout": "horizontal",
      "contents": [
        {
          "type": "box",
          "layout": "horizontal",
          "spacing": "xxl",
          "contents": [
            {
              "type": "box",
              "layout": "vertical",
              "flex": 8,
              "margin": "md",
              "contents": [
                {
                  "type": "text",
                  "text": "ติดตามเราได้ที่ FB: PYBOTT",
                  "margin": "sm",
                  "size": "xs",
                  "align": "center",
                  "gravity": "center",
                  "weight": "bold"
                },
                {
                  "type": "text",
                  "text": "https://www.facebook.com/Pybott/",
                  "margin": "none",
                  "size": "xxs",
                  "align": "center",
                  "gravity": "center",
                  "weight": "bold"
                }
              ]
            }
          ]
        }
      ]
    },
    "styles": {
      "header": {
        "backgroundColor": "#AECCFF"
      },
      "footer": {
        "backgroundColor": "#F0F0F0",
        "separatorColor": "#000000"
      }
    }
  }
}