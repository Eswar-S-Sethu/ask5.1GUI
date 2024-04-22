import RPi.GPIO as GPIO
import tkinter as tk

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
red_pin=17
green_pin=18
blue_pin=24
GPIO.setup(red_pin,GPIO.OUT)
GPIO.setup(green_pin,GPIO.OUT)
GPIO.setup(blue_pin,GPIO.OUT)



def turn_off_all():
    GPIO.output(red_pin,GPIO.LOW)
    GPIO.output(green_pin,GPIO.LOW)
    GPIO.output(blue_pin,GPIO.LOW)

def turn_on_led(led_pin):
    GPIO.output(led_pin,GPIO.HIGH)

def select_led(led_pin):
    turn_off_all() 
    turn_on_led(led_pin)


root=tk.Tk()
root.title('gui_led')
root.geometry('300x300')

radio = tk.IntVar()
colorInput=tk.StringVar()


def selection():  
   selection =str(radio.get())
   if(selection=='1'):
       select_led(red_pin)
   elif(selection=='2'):
       select_led(green_pin)
   elif(selection=='3'):
       select_led(blue_pin)

   

  
R1 = tk.Radiobutton(root, text="RED LED", variable=radio, value=1,  
                  command=selection)  
R1.pack( anchor = tk.W )  
  
R2 = tk.Radiobutton(root, text="GREEN LED", variable=radio, value=2,  
                  command=selection)  
R2.pack( anchor = tk.W )  
  
R3 = tk.Radiobutton(root, text="BLUE LED", variable=radio, value=3,  
                  command=selection)  
R3.pack( anchor = tk.W)  

def submitInfo():
    colorInput=str(inputLine.get())
    print(colorInput)
    if(colorInput=='RED'):
        select_led(red_pin)
    elif(colorInput=='GREEN'):
        select_led(green_pin)
    elif(colorInput=='BLUE'):
        select_led(blue_pin)


inputLabel=tk.Label(root,text='Enter color name (RED,GREEN, BLUE):')
inputLabel.pack()
inputLine=tk.Entry(root,textvariable=colorInput)
inputLine.pack()
submitBtn=tk.Button(root,command=submitInfo,text='submit')
submitBtn.pack()

exitButton=tk.Button(root,command=root.destroy,text='Exit')
exitButton.pack()
root.mainloop()

GPIO.cleanup()
