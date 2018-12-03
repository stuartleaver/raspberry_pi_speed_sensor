import RPi.GPIO as GPIO

# Configure the Pi to use the BCM (Broadcom pin names, rather than the pin positions
GPIO.setmode(GPIO.BCM)

sensor_one = 4

GPIO.setup(sensor_one, GPIO.IN)

broken_count = 0 # Record the number of times the beam is broken

is_beam_broken = False # Record if the beam is currently broken

try:
	while True:
		if(GPIO.input(sensor_one) == False):
			if(is_beam_broken == False):
				is_beam_broken = True

				broken_count += 1

				print("Beam broken %d time(s)" % (broken_count))
		else:
			is_beam_broken = False
finally:
	print("Ending")
	GPIO.cleanup()
