import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
in1, in2, in3, in4, in5= 4, 17, 27, 20, 21
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(in3, GPIO.OUT)
GPIO.setup(in4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(in5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
pwm1=GPIO.PWM(in2, 100)
pwm2=GPIO.PWM(in3, 100)

def myCallback(pin):
  if (pin==20):
    pwm1.start(0)
    for dc in range(51):
      pwm1.ChangeDutyCycle(2*dc)
      sleep(.01)
    for dc in range(51):
      pwm1.ChangeDutyCycle(100-2*dc)
      sleep(.01)
  if(pin==21):
    pwm2.start(0)
    for dc in range(51):
      pwm2.ChangeDutyCycle(2*dc)
      sleep(.01)
    for dc in range(51):
      pwm2.ChangeDutyCycle(100-2*dc)
      sleep(.01)
    

GPIO.add_event_detect(in4, GPIO.RISING, callback=myCallback, bouncetime=500)
GPIO.add_event_detect(in5, GPIO.RISING, callback=myCallback, bouncetime=500)


try:
  while True:
    GPIO.output(in1,1)
    sleep(.5)
    GPIO.output(in1,0)
    sleep(.5)
except KeyboardInterrupt:
	print("\nExiting")
finally:
    GPIO.cleanup()

