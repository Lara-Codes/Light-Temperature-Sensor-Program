import RPi.GPIO as GPIO 
import time 
import os 

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT) 
GPIO.setup(18, GPIO.OUT) 
def light():
  tempfile = open("/sys/bus/w1/devices/28-00044a3d8eff/w1_slave")
  tempfile_text=tempfile.read()
  currentTime = time.strftime('%x%X%Z')
  tempfile.close()
  tempC = float(tempfile_text.split("\n")[1].split("t=")[1])/1000
  tempF = tempC*9.0/5.0+32
  
  if tempC<25:
    GPIO.output(18, False)
    GPIO.output(17, True)
    
  if tempC>25:
    GPIO.output(17, False)
    GPIO.output(18, True)
  
  return[currentTime, tempC, tempF]

light()
print(light())
  
