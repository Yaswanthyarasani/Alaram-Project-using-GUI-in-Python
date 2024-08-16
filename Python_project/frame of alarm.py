#frame modules
from tkinter.ttk import *
from tkinter import *
#Pic Module
from PIL import ImageTk, Image
#datetime module
from datetime import datetime
from time import sleep
#pygame module
from pygame import mixer
import threading

#creation of the window
window=Tk()

#bg color assigning
bg_color="#ffffff"   #White total bg,(window)
bg_color1="#838B83"  #Grey  heading frame_line
bg_color2="#00FFFF"  #black  body frame_body
bg_color3="#ffffff"

#heading of the window
window.title("Alarm")

#length and breadth of the window
window.geometry('400x380')

#Bg Color fixing
window.configure(bg=bg_color)

#FRAMES Concept
frame_line=Frame(window, width=800, height=5,bg=bg_color1)
frame_line.grid(row=0,column=0)
  #frame body
frame_body=Frame(window, width=800,height=400,bg=bg_color3)
frame_body.grid(row=1,column=0)

#detailing of the window in the body part
 #opening the image in program
pic= Image.open('C:\\Users\\yeswanth\\OneDrive\\Desktop\\PYpro\\Clock1.png')
 #resize of the image
pic.resize((100,100))
 #loading the image and the modification
pic=ImageTk.PhotoImage(pic)
pic_label=Label(frame_body, height=100,image=pic,bg=bg_color3) #in this "bg" color, is bg color of pic
 #position of the image
pic_label.place(x=60,y=70)
#text alarm in body part
text_alarm=Label(frame_body,height=1,text="ALARM",font=('Ivy 25 bold'),bg=bg_color3)
text_alarm.place(x=53,y=30)
#text set time in body part
text_settime=Label(frame_body,height=1,text="Set Time",font=('Ivy 18 bold'),bg=bg_color3)
text_settime.place(x=245,y=20)
#text hrs and combo box
text_hrs=Label(frame_body,height=1,text="Hrs",font=('Ivy 15'),bg=bg_color3)
text_hrs.place(x=260,y=60)
hrs=Combobox(frame_body,width=3,font=('arial 15'))
hrs['values']=("01","02","03","04","05","06","07","08","09","10","11","12")
hrs.current(0)
hrs.place(x=300,y=60)

#text Mins
text_mins=Label(frame_body,height=1,text="Mins",font=('Ivy 15'),bg=bg_color3)
text_mins.place(x=248,y=120)
mins=Combobox(frame_body,width=3,font=('arial 15'))
mins['values']=("00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59")
mins.current(0)
mins.place(x=300,y=120)

#text secs
text_secs=Label(frame_body,height=1,text=("Secs"),font=('Ivy 15'),bg=bg_color3)
text_secs.place(x=247,y=180)
secs=Combobox(frame_body,width=3,font=('arial 15'))
secs['values']=("00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59")
secs.current(0)
secs.place(x=300,y=180)

#text AM/PM
text_period=Label(frame_body,height=1,text=("Period"),font=('Ivy 15'),bg=bg_color3)
text_period.place(x=233,y=240)
period=Combobox(frame_body,width=3,font=('arial 15'))
period['values']=("AM","PM")
period.current(0)
period.place(x=300,y=240)

#text Set date
text_setday=Label(frame_body,height=1,text="Set Day",font=('Ivy 16 bold'),bg=bg_color3)
text_setday.place(x=25,y=199)

#days 
text_day=Label(frame_body,height=1,text="Day",font=('Ivy 15'),bg=bg_color3)
text_day.place(x=25,y=240)
day=Combobox(frame_body,width=7,font=('arial 15'))
day['values']=("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
day.current(0)
day.place(x=80,y=240)

def activate_alarm():
  t= threading.Thread(target=time_alarm)
  t.start()

def deactivate_alarm():
    print('Deactivate alarm: ',selected.get())
    mixer.music.stop()

#activate and deactivate
 #activate
selected=IntVar()
activate=Radiobutton(frame_body,font=('arial 15'),value=1,text="Activate",bg=bg_color3,command=activate_alarm,variable=selected)
activate.place(x=60,y=290)

#Music for alarm
def sound_alarm():
    mixer.music.load('D://Python/Playsound/Kannuladha.mp3')
    print("music is playing")
    mixer.music.play()
    selected.set(0)
    deactivate=Radiobutton(frame_body,font=('arial 15'),value=2,text="Deactivate",bg=bg_color3,command=deactivate_alarm,variable=selected)
    deactivate.place(x=180,y=290)
def time_alarm():
    while True:
        control=selected.get()
        print(control)
        alarm_day=day.get()
        alarm_hr=hrs.get()
        alarm_min=mins.get()
        alarm_secs=secs.get()
        alarm_period=period.get()
        alarm_period=str(alarm_period).upper()

        now_time=datetime.now()
        
        day1=now_time.strftime("%A")
        hr1= now_time.strftime("%I")
        min1=now_time.strftime("%M")
        secs1=now_time.strftime("%S")
        period1=now_time.strftime("%p")

        if control==1:
            if alarm_day==day1:
                if alarm_period==period1:
                    if alarm_hr==hr1:
                        if alarm_min==min1:
                            if alarm_secs==secs1:
                                print("Time to take a break")
                                sound_alarm()
        sleep(1)

mixer.init()
#Opening of the window
window.mainloop()