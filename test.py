import PySimpleGUI as sg
import sqlite3
conn = sqlite3.connect('chemDemo.db')
c = conn.cursor()

# Create the Window
isVis = True
lib = {
"hydrogen" : {'src':'./hydrogen.png'},
"oxygen" : {'src':'./Oxygen.png'},
"water" : {'src':'./Water.png'},
"iron" : {'src':'./iron.png'},
"sodium" : {'src':'./sodium.png'},
"nitrogen" : {'src':'./Nitrogen.png'},
"carbon" : {'src':'./carbon.png'},
"h2o" : {'src':'./h2o.png'},
}
sg.theme('LightGreen3')	# Add a touch of color
selected = 0
selectedArr =["",""]
layout = [
            [sg.Button(key='hydrogen',image_filename=lib['hydrogen']['src'],border_width=0),sg.Button(key='oxygen',image_filename=lib['oxygen']['src'],border_width=0),sg.Button(key='iron',image_filename=lib['iron']['src'],border_width=0),sg.Button(key='sodium',image_filename=lib['sodium']['src'],border_width=0),sg.Button(key='carbon',image_filename=lib['carbon']['src'],border_width=0)],
            [sg.Text("Elements:")],
            [sg.Button(key='-TESTER-',visible=False, image_filename=lib["oxygen"]['src'] ,size=(5,5)),sg.Text('+',visible=False,key= '+Test'),sg.Button(key='-TESTER2-',visible=False,image_filename=lib["oxygen"]['src'],size=(5,5))],
            [sg.Text("Result:")],
            # [sg.Button(key='-TESTER3-',visible=False, image_filename=lib["oxygen"]['src'] ,size=(5,5)),sg.Button(key='-TESTER4-',visible=False, image_filename=lib["oxygen"]['src'] ,size=(5,5))],
            [sg.Button(key='-TESTER3-',visible=False, image_filename=lib["oxygen"]['src'] ),sg.Button(key='-TESTER4-',visible=False, image_filename=lib["oxygen"]['src'] ,size=(5,5))],


            # [sg.Text('File Save Location', size=(15, 1)), sg.Input(size=(30,1)), sg.FolderBrowse()],
            [sg.Button('Test'),sg.Button('Reset'), sg.Button('Close')] ]

window = sg.Window('Diet Program Generator', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    print(event)
    if event in (None, 'Close'):	# if user closes window or clicks cancel
        break
    if event == 'Reset':
        window['-TESTER-'].update(visible=False)
        window['-TESTER2-'].update(visible=False)
        window['-TESTER3-'].update(visible=False)
        window['-TESTER4-'].update(visible=False)

        window['+Test'].update(visible=False)
        selected = 0
    elif event == 'Test':
        if(selected==2):
            selectedArr.sort()
            c.execute('SELECT * FROM reactions WHERE elem1=? AND elem2 = ?',(selectedArr[0],selectedArr[1]))
            comp = c.fetchone()
            if(comp):
                print(comp[0])
                window['-TESTER3-'].update(image_filename=lib[comp[2]]['src'], visible=True)
                if(comp[3]!='emp'):
                    window['-TESTER4-'].update(image_filename=lib[comp[3]]['src'], visible=True)
            else:
                print('failed')
                sg.popup('No known combination of these elements')
        else:
            sg.popup('Please select two elements first')
    elif(event in lib.keys()):
        if(selected == 0):
            window['-TESTER-'].update(image_filename=lib[event]['src'], visible=True)
            window['+Test'].update(visible=True)
            selectedArr[0]=event
            selected=1
        else:
            window['-TESTER2-'].update(image_filename=lib[event]['src'], visible=True)
            selected=2
            selectedArr[1]=event
