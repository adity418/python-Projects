from datetime import datetime
import wave
import pyaudio
from tkinter import *
import time

def update_time():
    current_time = time.strftime("%H:%M:%S %p")
    time_label.config(text=current_time)
    time_label.after(1000, update_time)



def set_alarm():
    alarm_hour = int(hour.get())
    alarm_minute = int(min.get())
    alarm_seconds = int(sec.get())
    print("Setting up alarm..")
    while True:
        now = datetime.now()
        current_hour = now.hour
        current_minute = now.minute
        current_seconds = now.second
        if (alarm_hour == current_hour) and (alarm_minute == current_minute) and (alarm_seconds == current_seconds):
            print("Wake Up!")
            play_alarm_sound('alarm.wav')
            break

def play_alarm_sound(sound_file):
    wf = wave.open(sound_file, 'rb')
    p = pyaudio.PyAudio()
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)
    data = wf.readframes(1024)
    while data:
        stream.write(data)
        data = wf.readframes(1024)
    stream.stop_stream()
    stream.close()
    p.terminate()

clock = Tk()
clock.title("Aditya Alarm Clock")
clock.geometry("400x250")

time_label = Label(clock, font=("Arial", 20), fg="black", bg="white")
time_label.pack(pady=20)

update_time()

addTime = Label(clock, text="Hour   Min    Sec", font=60)
addTime.place(x=150)

setYourAlarm = Label(clock, text="When to wake you up", fg="blue", relief="solid", font=("Helevetica", 7, "bold"))
setYourAlarm.place(x=0, y=29)

hour = StringVar()
min = StringVar()
sec = StringVar()

hourTime = Entry(clock, textvariable=hour, bg="pink", width=15)
hourTime.place(x=110, y=60)
minTime = Entry(clock, textvariable=min, bg="pink", width=15)
minTime.place(x=150, y=60)
secTime = Entry(clock, textvariable=sec, bg="pink", width=15)
secTime.place(x=200, y=60)

submit = Button(clock, text="Set Alarm", fg="Red", width=10, command=set_alarm)
submit.place(x=110, y=90)

clock.mainloop()
