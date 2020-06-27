from firebase import firebase # import module from pip install .....
from config import DATABASE_URI
DATABASE_PRODUCT = "PRODUCT_DB"
DATABASE_USER = "USER_DB"
firebase = firebase.FirebaseApplication(DATABASE_URI, None)

def formatter(DICT):
    res = ""
    res += "รายการ   ราคา   เหลืออยู่ \n"
    for key,value in DICT.items():
        รายการ = value["ชื่อ"]
        ราคา = value["ราคา"]
        เหลืออยู่ = value["จำนวนที่เหลืออยู่"]
        res += "{}   {}   {} \n".format(รายการ,ราคา,เหลืออยู่)
    
    return res

def formatter_column(DICT):
    LIST = []
    for key,value in DICT.items():
        # list[list[element]]
        data = [value["ชื่อ"],value["ราคา"],value["จำนวนที่เหลืออยู่"]]
        LIST.append(data)
    
    # a = [li[0] for li in LIST]
    # b = [li[1] for li in LIST]
    # c = [li[2] for li in LIST]
    
    return LIST

def process_product(command):
    คำสั่ง = command
    if คำสั่ง == "":
        
        ชื่อสินค้า = input("กรุณาระบุชื่อสินค้า  ")
        ราคาสินค้า = int(input("กรุณาระบุราคาสินค้า  "))
        จำนวนที่เหลืออยู่ของสินค้า = int(input("กรุณาระบุจำนวนที่เหลืออยู่ของสินค้า  "))
        # จำนวนที่ขายไปแล้วของสินค้า = int(input("กรุณาระบุจำนวนที่ขายไปแล้วของสินค้า  "))

        สินค้า = {
                    "ชื่อ":ชื่อสินค้า,
                    "ราคา":ราคาสินค้า,
                    "จำนวนที่เหลืออยู่":จำนวนที่เหลืออยู่ของสินค้า,
                    # "จำนวนที่ขายไปแล้ว":จำนวนที่ขายไปแล้วของสินค้า
                }
        
        #save to firebase
        firebase.patch(DATABASE_PRODUCT+"/"+ชื่อสินค้า,สินค้า)
        
        return สินค้า
            
    elif คำสั่ง.lower().strip(" ") == "all":
        all_products = firebase.get(DATABASE_PRODUCT,None)
        print(all_products)
        return True
        # None == False
    else:
        print("ท่านได้ออกจากคำสั่งเรียบร้อย ขอขอบพระคุณที่ใช้บริการ")
        return False

def update_product():
    all_products = firebase.get(DATABASE_PRODUCT,None)
    return all_products


def add_product(name,price,count):
    ชื่อสินค้า = name
    ราคาสินค้า = price
    จำนวนที่เหลืออยู่ของสินค้า = count
    # จำนวนที่ขายไปแล้วของสินค้า = int(input("กรุณาระบุจำนวนที่ขายไปแล้วของสินค้า  "))

    สินค้า = {
                "ชื่อ":ชื่อสินค้า,
                "ราคา":ราคาสินค้า,
                "จำนวนที่เหลืออยู่":จำนวนที่เหลืออยู่ของสินค้า,
                # "จำนวนที่ขายไปแล้ว":จำนวนที่ขายไปแล้วของสินค้า
            }
    
    #save to firebase
    firebase.patch(DATABASE_PRODUCT+"/"+ชื่อสินค้า,สินค้า)

import PySimpleGUI as sg    

if __name__ == '__main__':
    
    # headings = ['รายการ', 'ราคา', 'จำนวนที่เหลือ']
    # header =  [[sg.Text('  ')] + [sg.Text(h) for h in headings]]
    
    datas = formatter_column(DICT=update_product())
    
    input_row = [[sg.Text(' '+"รายการ",size=(20,1)),sg.Text(' '+"ราคา",size=(10,1)),sg.Text(' '+"เหลืออยู่",size=(10,1))]]
    
    for i in datas:
        a = [sg.Text(' '+i[0],size=(20,1)),sg.Text(' '+str(i[1]),size=(10,1)),sg.Text(' '+str(i[2]),size=(10,1))]
        input_row.append(a)  
               
    
    # tab1_layout =  [[sg.Multiline(formatter(update_product()),key="product_list",disabled=True)]]                
    tab1_layout =  [[sg.Column(layout=input_row)]]               

    tab2_layout = [[sg.T('เพิ่มรายการสินค้า')],  
                [sg.T('ชื่อสินค้า')],    
                [sg.In(key='in_name')],
                [sg.T('ราคา')],    
                [sg.In(key='in_price')],
                [sg.T('จำนวน')],    
                [sg.In(key='in_count')],
                [sg.Button('เพิ่ม')]]    

    layout = [[sg.TabGroup([[sg.Tab('สินค้าทั้งหมด', tab1_layout,key="product_list"), sg.Tab('เพิ่มสินค้า', tab2_layout)]])],[sg.Button('อัพเดตสินค้า'),sg.Button('EXIT')]]    

    window = sg.Window('Application เพิ่มสินค้า', layout, default_element_size=(60,30))    

    while True:    
        event, values = window.read()    
        # print("Event : " + event )    
        # print("Values : " + str(values) )   
        
        if event == "เพิ่ม":
            add_product(name=values["in_name"],price=values["in_price"],count=values["in_count"])
        
        elif event == "อัพเดตสินค้า":
            window.close()
            
            all_prod = formatter(update_product())
            datas = formatter_column(DICT=update_product())
    
            input_row = [[sg.Text(' '+"รายการ",size=(20,1)),sg.Text(' '+"ราคา",size=(10,1)),sg.Text(' '+"เหลืออยู่",size=(10,1))]]
            
            for i in datas:
                a = [sg.Text(' '+i[0],size=(20,1)),sg.Text(' '+str(i[1]),size=(10,1)),sg.Text(' '+str(i[2]),size=(10,1))]
                input_row.append(a) 
            
            # cloumn ไม่สามารถ update ได้ ต้องสร้างใหม่จาก Layout เท่านั้น ปิดแล้วเปิดใหม่
            
            tab11_layout =  [[sg.Column(layout=input_row)]]               

            tab22_layout = [[sg.T('เพิ่มรายการสินค้า')],  
                        [sg.T('ชื่อสินค้า')],    
                        [sg.In(key='in_name')],
                        [sg.T('ราคา')],    
                        [sg.In(key='in_price')],
                        [sg.T('จำนวน')],    
                        [sg.In(key='in_count')],
                        [sg.Button('เพิ่ม')]]
            
            layout1 = [[sg.TabGroup([[sg.Tab('สินค้าทั้งหมด', tab11_layout,key="product_list"), sg.Tab('เพิ่มสินค้า', tab22_layout)]])],[sg.Button('อัพเดตสินค้า'),sg.Button('EXIT')]]    

            window = sg.Window('Application เพิ่มสินค้า', layout1, default_element_size=(60,30))
            
            # window["product_list"](visible=False)
            # all_prod = formatter_column(update_product())
            # window["product_column"](all_prod)
        
        if event == "EXIT":           # always,  always give a way out!    
            window.close()
            break  









# while True:
    
#     คำสั่ง = input("กรุณากด ENTER เพื่อเพิ่มสินค้า \n พิมพ์ all เพื่อดูสินค้าทั้งหมด \n พิมพ์ q เพื่อออกจากคำสั่ง")
#     ผลลัพธ์ = process_product(command=คำสั่ง)
#     if not ผลลัพธ์:
#         # store catalog ไว้บน firebase database
#         break
    
#     elif isinstance(ผลลัพธ์,dict):
#         catalog.append(ผลลัพธ์)