import PySimpleGUI as sg
import datetime
import os

Hour = datetime.datetime.now().hour - 12
Minute = datetime.datetime.now().minute
Second = datetime.datetime.now().second
Stop = False
isSet = False
Stop2 = False
isSet2 = False

if Minute < 10:
	Minute = "0"+str(Minute)

if Second < 10:
        Second = "0"+str(Second)

layout=[
    [sg.Text("Real Time:", font = "Times 25")],
[sg.Text(str(Hour)+" : "+str(Minute)+" : "+str(Second), font = "Times 25", key = '-TEXT-')],
[sg.Text("Alarm Time:", font = "Times 25")],
[sg.Text("Hour: ", font = "Times 25"), sg.Listbox(values=['12','11','10','09','08','07','06','05','04','03','02','01'], size=(5, 1), key = 'Hour'),
 sg.Text("Minute: ", font = "Times 25"), sg.Listbox(values=['59','58','57','56','55','54','53','52','51','50','49','48','47','46','45','44','43','42','41','40','39','38','37','36','35','34','33','32','31','30','29','28','27','26','25','24','23','22','21','20','19','18','17','16','15','14','13','12','11','10','09','08','07','06','05','04','03','02','01','00'], size=(5, 1), key = 'Minute'),
 sg.Text("Second: ", font = "Times 25"), sg.Listbox(values=['59','58','57','56','55','54','53','52','51','50','49','48','47','46','45','44','43','42','41','40','39','38','37','36','35','34','33','32','31','30','29','28','27','26','25','24','23','22','21','20','19','18','17','16','15','14','13','12','11','10','09','08','07','06','05','04','03','02','01','00'], size=(5, 1), key = 'Second'),
 sg.Text("Am or Pm: ", font = "Times 25"),sg.Listbox(values=['Am', 'Pm'], size=(5, 1), key = 'AmPm')],
[sg.Text("Hour: ", font = "Times 25"), sg.Listbox(values=['12','11','10','09','08','07','06','05','04','03','02','01'], size=(5, 1), key = 'Hour2'),
 sg.Text("Minute: ", font = "Times 25"), sg.Listbox(values=['59','58','57','56','55','54','53','52','51','50','49','48','47','46','45','44','43','42','41','40','39','38','37','36','35','34','33','32','31','30','29','28','27','26','25','24','23','22','21','20','19','18','17','16','15','14','13','12','11','10','09','08','07','06','05','04','03','02','01','00'], size=(5, 1), key = 'Minute2'),
 sg.Text("Second: ", font = "Times 25"), sg.Listbox(values=['59','58','57','56','55','54','53','52','51','50','49','48','47','46','45','44','43','42','41','40','39','38','37','36','35','34','33','32','31','30','29','28','27','26','25','24','23','22','21','20','19','18','17','16','15','14','13','12','11','10','09','08','07','06','05','04','03','02','01','00'], size=(5, 1), key = 'Second2'),
 sg.Text("Am or Pm: ", font = "Times 25"),sg.Listbox(values=['Am', 'Pm'], size=(5, 1), key = 'AmPm2')],
[sg.Button("Set Alarm", font = "Times 25")]]

window = sg.Window('Alarm Clock', layout)

i = 0

while True:
        event, values = window.read(timeout = 10)
        if event == sg.WIN_CLOSED:
                break
        if event == 'Set Alarm':
                AlarmHour = values['Hour']
                AlarmMinute = values['Minute']
                AlarmSecond = values['Second']
                AlarmAmPm = values['AmPm']
                AlarmHour2 = values['Hour2']
                AlarmMinute2 = values['Minute2']
                AlarmSecond2 = values['Second2']
                AlarmAmPm2 = values['AmPm2']
                alarmHour = int(AlarmHour[0])
                alarmMinute = int(AlarmMinute[0])
                alarmSecond = int(AlarmSecond[0])
                amPm = AlarmAmPm[0]
                alarmHour2 = int(AlarmHour2[0])
                alarmMinute2 = int(AlarmMinute2[0])
                alarmSecond2 = int(AlarmSecond2[0])
                amPm2 = AlarmAmPm2[0]
                isSet = True
                isSet2 = True
                if(amPm == "Pm"):
                        alarmHour = alarmHour + 12
                if(amPm2 == "Pm"):
                        alarmHour2 = alarmHour2 + 12
        if isSet == True:
                if(alarmHour == datetime.datetime.now().hour and alarmMinute == datetime.datetime.now().minute and alarmSecond == datetime.datetime.now().second):
                        if not Stop:
                                print("Wake up lazy")
                                os.system("C:/Users/lachl/Desktop/Python_Projects_and_Recordings/WakeUpClaps.m4a")
                                Stop = True
        if isSet2 == True:
                if(alarmHour2 == datetime.datetime.now().hour and alarmMinute2 == datetime.datetime.now().minute and alarmSecond2 == datetime.datetime.now().second):
                        if not Stop2:
                                print("Wake up lazy")
                                os.system("C:/Users/lachl/Desktop/Python_Projects_and_Recordings/WakeUpClaps.m4a")
                                Stop2 = True
        if Stop:
                Stop = False
                isSet = False
        if Stop2:
                Stop2 = False
                isSet2 = False
        Hour = datetime.datetime.now().hour - 12
        Minute = datetime.datetime.now().minute
        Second = datetime.datetime.now().second

        if Minute < 10:
                Minute = "0"+str(Minute)

        if Second < 10:
                Second = "0"+str(Second)

        window['-TEXT-'].update(str(Hour)+" : "+str(Minute)+" : "+str(Second))
