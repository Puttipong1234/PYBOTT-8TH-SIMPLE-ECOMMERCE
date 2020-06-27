import PySimpleGUI as sg      

sg.theme('SystemDefaultForReal')    # Keep things interesting for your users

layout = [[sg.Text('Name')],      
          [sg.Input(key='-IN1-')],  
          [sg.Text('Price')],      
          [sg.Input(key='-IN2-')],
          [sg.Text('count')],      
          [sg.Input(key='-IN3-')], 
          [sg.Button('Read'), sg.Exit()]]      

window = sg.Window('Window that stays open', layout)      

while True:                             # The Event Loop
    event, values = window.read() 
    print(event, values)       
    if event == sg.WIN_CLOSED or event == 'Exit':
        break      

window.close()