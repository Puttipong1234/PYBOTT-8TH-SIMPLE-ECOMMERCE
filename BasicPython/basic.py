# text = "Hello World" # string
# number = 1 # integer
# _float = 1.10 #float

# ราคาหนังสือ = 500 
# ราคาสมุด = 50
# จำนวนหนังสือที่สั่งซื้อ = int(input("ท่านต้องการสั่งซื้อหนังสือจำนวนกี่เล่มดีคะ?\t : ")) #10 "10"
# จำนวนสมุดที่สั่งซื้อ = int(input("ท่านต้องการสั่งซื้อสมุดจำนวนกี่เล่มดีคะ?\t : "))

#ซื้อหนังสือ + สมุด
# ราคารวม = ราคาหนังสือ + ราคาสมุด

# print(ราคารวม)

# ลูกค้าสั่ง หนังสือ 3 เล่ม สมุด 2 เล่ม 
# ราคารวม = ราคาหนังสือ*จำนวนหนังสือที่สั่งซื้อ + ราคาสมุด*จำนวนสมุดที่สั่งซื้อ
# print(ราคารวม)
# หากต้องการแสดงผลเป็น "ท่านได้สั่งซื้อสินค้ารวมทั้งสิ้น xxxx บาท "
# print("ท่านได้สั่งซื้อสินค้ารวมทั้งสิ้น " + str(ราคารวม) +" บาท")
# print("ท่านได้สั่งซื้อสินค้ารวมทั้งสิ้น {} บาท".format(str(ราคารวม)) )

# print("Hello "*5)

#list คืออะไร

# สินค้า1 = "หนังสือเรียน"
# สินค้า2 = "สมุด"
# สินค้า3 = "ไม้บรรทัด"
# สินค้า4 = "ยางลบ"
#            0        1        2        3
# สินค้า = ["หนังสือเรียน","สมุด","ไม้บรรทัด",'ยางลบ']
# # append add สินค้าเข้าไปใหม่
# สินค้า.append("ดินสอ")
# print(สินค้า)
# # loop
# for each in สินค้า:
#     print("วันนี่เรามี {} ขายอยู่นะคะ สนใจไหมเอ่ย".format(each) )
# for index,each in enumerate(สินค้า):
#     print("{} วันนี่เรามี {} ขายอยู่นะคะ สนใจไหมเอ่ย".format(index,each) )

# # list pop , remove
# สินค้า.pop(0)
# print(สินค้า)
# สินค้า.remove("ไม้บรรทัด")
# print(สินค้า)

# สินค้า "ชื่อสินค้า" อย่างเดียว
# ชื่อ ราคา จำนวนที่เหลืออยู่ จำนวนที่ขายไปแล้ว
# ชื่อสินค้า = []
# ราคาสินค้า = []
# จำนวนที่เหลืออยู่ของสินค้า = []
# จำนวนที่ขายไปแล้วของสินค้า = []

# dictionary 
#           key       value
สินค้า1 = {
            "ชื่อ":"หนังสือเรียน อนุบาล 3",
            "ราคา":250,
            "จำนวนที่เหลืออยู่":10,
            "จำนวนที่ขายไปแล้ว":20
        }

สินค้า2 = {
            "ชื่อ":"หนังสือเรียน ประถม",
            "ราคา":150,
            "จำนวนที่เหลืออยู่":5,
            "จำนวนที่ขายไปแล้ว":10,
            "ขายโดย" : "PYBOTT"
        }

สินค้า3 = {
            "ชื่อ":"หนังสือเรียน มัธยม",
            "ราคา":350,
            "จำนวนที่เหลืออยู่":55,
            "จำนวนที่ขายไปแล้ว":50,
            "ขายโดย" : "ลุงวิศวกร"
        }

# print(สินค้า1)
# สินค้า1["ขายโดย"] = "PYBOTT"
# print(สินค้า1)

# catalog = [สินค้า1,สินค้า2]
# print(catalog)
# catalog.append(สินค้า3)
# print(catalog)

# สร้าง dictionary ของสินค้า4 ที่มีการรับค่ามาจาก User 4 ค่า 
# ชื่อ ราคา จำนวนที่เหลืออยู่ จำนวนที่ขายไปแล้ว
# ชื่อ = input("")
# print สินค้า4 ผลลัพธ์ออกมา 
# {'ชื่อ': 'xxxxx', 'ราคา': xxxx, 'จำนวนที่เหลืออยู่': xx, 'จำนวนที่ขายไปแล้ว': xx}

# ชื่อสินค้า = input("กรุณาระบุชื่อสินค้า  ")
# ราคาสินค้า = int(input("กรุณาระบุราคาสินค้า  "))
# จำนวนที่เหลืออยู่ของสินค้า = int(input("กรุณาระบุจำนวนที่เหลืออยู่ของสินค้า  "))
# จำนวนที่ขายไปแล้วของสินค้า = int(input("กรุณาระบุจำนวนที่ขายไปแล้วของสินค้า  "))

# สินค้า4 = {
#             "ชื่อ":ชื่อสินค้า,
#             "ราคา":ราคาสินค้า,
#             "จำนวนที่เหลืออยู่":จำนวนที่เหลืออยู่ของสินค้า,
#             "จำนวนที่ขายไปแล้ว":จำนวนที่ขายไปแล้วของสินค้า
#         }

# print(สินค้า4)

# count = 0
# while count < 5:   #boolean True False
#     print("วนซ้ำครั้งที่  " + str(count)) 
#     count += 1

# count = 0
# while True:   #boolean True False
#     print("วนซ้ำครั้งที่  " + str(count)) 
#     count += 1
    
#     if count > 5:
#         print("count > 5 need to break")
#         break

catalog = [] 

def process_product(command):
    คำสั่ง = command
    if คำสั่ง == "":
        
        ชื่อสินค้า = input("กรุณาระบุชื่อสินค้า  ")
        ราคาสินค้า = int(input("กรุณาระบุราคาสินค้า  "))
        จำนวนที่เหลืออยู่ของสินค้า = int(input("กรุณาระบุจำนวนที่เหลืออยู่ของสินค้า  "))
        จำนวนที่ขายไปแล้วของสินค้า = int(input("กรุณาระบุจำนวนที่ขายไปแล้วของสินค้า  "))

        สินค้า = {
                    "ชื่อ":ชื่อสินค้า,
                    "ราคา":ราคาสินค้า,
                    "จำนวนที่เหลืออยู่":จำนวนที่เหลืออยู่ของสินค้า,
                    "จำนวนที่ขายไปแล้ว":จำนวนที่ขายไปแล้วของสินค้า
                }
        
        return สินค้า
            
    elif คำสั่ง.lower().strip(" ") == "all":
        print(catalog)
        return True
        # None == False
    else:
        print("ท่านได้ออกจากคำสั่งเรียบร้อย ขอขอบพระคุณที่ใช้บริการ")
        return False

while True:
    
    คำสั่ง = input("กรุณากด ENTER เพื่อเพิ่มสินค้า \n พิมพ์ all เพื่อดูสินค้าทั้งหมด \n พิมพ์ q เพื่อออกจากคำสั่ง")
    ผลลัพธ์ = process_product(command=คำสั่ง)
    if not ผลลัพธ์:
        # store catalog ไว้บน firebase database
        break
    
    elif isinstance(ผลลัพธ์,dict):
        catalog.append(ผลลัพธ์)