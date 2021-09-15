import PySimpleGUI as sg
import webbrowser

sg.theme("DarkBlue2")

MainMenu =[[sg.Text("MAJOR BEATS", font = "Times 100")],
           [sg.Text("BY MAJOR MUSIC", font = "Times 50")]]

Genre1 =[[sg.Text("This is the Chill Music Genre, It has only Chill Music", font = "Times 30")],
         [sg.Text("Chill Beats To Quarantine To:", font = "Times 20"), sg.Button("Go To Song", font = "20", key='Chill1')]]

Genre2 =[[sg.Text("This is the Rock/HardRock Genre, It has only Rock/HardRock Music", font = "Times 30")],
         [sg.Text("Metallica, Eye Of The Beholder:", font = "Times 20"), sg.Button("Go To Song", font = "20", key='Rock1')],
         [sg.Text("Metallica, Master Of Puppets:", font = "Times 20"), sg.Button("Go To Song", font = "20", key='Rock2')]]

Genre3 =[[sg.Text("This is the Pop Music Genre, It has only Pop Music", font = "Times 30")],
         [sg.Text("Uptown Funk:", font = "Times 20"), sg.Button("Go To Song", font = "20", key='Pop1')],
         [sg.Text("Havana:", font = "Times 20"), sg.Button("Go To Song", font = "20", key='Pop2')]]

layout =[[sg.Column(MainMenu, key='-COL1-'), sg.Column(Genre1, visible = False, key='-COL2-'), sg.Column(Genre2, visible = False, key='-COL3-'), sg.Column(Genre3, visible = False, key='-COL4-')],
         [sg.Button('MAIN MENU'), sg.Button('Chill Music'), sg.Button('Rock/HardRock'), sg.Button('Pop Music')]]

window = sg.Window("Spotify", layout)

while True:
    event, values = window.read(timeout = 10)
    if event == 'Chill Music':
        window['-COL2-'].update(visible=True)
        window['-COL1-'].update(visible=False)
        window['-COL3-'].update(visible=False)
        window['-COL4-'].update(visible=False)
    if event == 'MAIN MENU':
        window['-COL2-'].update(visible=False)
        window['-COL1-'].update(visible=True)
        window['-COL3-'].update(visible=False)
        window['-COL4-'].update(visible=False)
    if event == 'Rock/HardRock':
        window['-COL2-'].update(visible=False)
        window['-COL1-'].update(visible=False)
        window['-COL3-'].update(visible=True)
        window['-COL4-'].update(visible=False)
    if event == 'Pop Music':
        window['-COL2-'].update(visible=False)
        window['-COL1-'].update(visible=False)
        window['-COL3-'].update(visible=False)
        window['-COL4-'].update(visible=True)
    if event == 'Chill1':
        webbrowser.open(r'www.youtube.com/watch?v=rA56B4JyTgI')
    if event == 'Rock1':
        webbrowser.open(r'www.youtube.com/watch?v=ioZeYpab3no')
    if event == 'Pop1':
        webbrowser.open(r'www.youtube.com/watch?v=OPf0YbXqDm0')
    if event == 'Pop2':
        webbrowser.open(r'www.youtube.com/watch?v=HCjNJDNzw8Y')
    if event == 'Rock2':
        webbrowser.open(r'www.youtube.com/watch?v=xnKhsTXoKCI')
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
