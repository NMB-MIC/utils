'''
A simple servo motor running
can rotate angle by a toggle
@auther suraphop bunsawat

changable 1 point
1. define pin number (pin = 13)
'''

#import tools
from tkinter import *
import RPi.GPIO as GPIO
import time

#define pin number
pin = 13
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.OUT)

#setup pwm
pwm = GPIO.PWM(pin, 100)
pwm.start(5)

class App:
    '''control servo motor'''	
    def __init__(self, master):
        '''create toggle'''
        frame = Frame(master)
        frame.pack()
        scale = Scale(frame, from_=0, to=180, 
              orient=HORIZONTAL, command=self.update)
        scale.grid(row=0)

    def update(self, angle):
        '''change angle'''
        duty = float(angle) / 10.0 + 2.5
        pwm.ChangeDutyCycle(duty)

#running program
root = Tk()
root.wm_title('Servo Control')
app = App(root)
root.geometry("200x50+0+0")
root.mainloop()