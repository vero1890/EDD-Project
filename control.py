import RPi.GPIO as GPIO
import time

right = 4
middle = 27
left = 23

kick_array = [0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, ]
snare_array = [0, 0, 1, ]
hat_array = [0, 0, 1, ]
bongo_array = [0, 0, 1, ]

def setup():
  GPIO.setmode(GPIO.BCM)  # Numbers GPIOs by physical location
  GPIO.setup(left, GPIO.OUT)
  GPIO.setup(middle, GPIO.OUT)
  GPIO.setup(right, GPIO.OUT)
  GPIO.output(left, GPIO.LOW)
  GPIO.output(middle, GPIO.LOW)
  GPIO.output(right, GPIO.LOW)



def destroy():
  GPIO.output(left, GPIO.LOW)
  GPIO.output(middle, GPIO.LOW)
  GPIO.output(right, GPIO.LOW)
  GPIO.cleanup()  # Release resource


if __name__ == '__main__':  # Program start from here
  setup()
  try:
    loop()
  except KeyboardInterrupt:
    destroy()
