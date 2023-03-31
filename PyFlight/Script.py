import os
from time import sleep
import random

os.system("clear")

print("PyFlight.")
print("""
	+------------------------+
	|Created by Shaunak Ghosh|
	|Date: 30/03/2023 14:40  |
	|Github: @shaunakg3      |
	+------------------------+
	\n
	""")
option = input("What would you like to simulate.\n[1] Air Traffic\n[2] Landings\n[3] Crash\n>>> ")

# Functions and Variables.
def AirTraffic(x, y):
	os.system("clear")
	print("Simulating...")
	sleep(1)
	print("✈ " + x + " flying at " + str(random.randint(200, 576)) + "mph Type: Boeing 747 Dreamliner")
	print("✈ " + y + " flying at " + str(random.randint(200, 450)) + "mph Type: Neo Airbus")
	degreesX = str(random.randint(0, 360))
	degreesY = str(random.randint(0, 360))
	sleep(3)
	print("✈ " + x + " flying " + degreesX + "°")
	print("✈ " + y + " flying " + degreesY + "°")
	sleep(3)
	if degreesX == degreesY:
		print("Crash between ✈ " + x + " and ✈ " + y + " predicted.")
		print("Terminating...")
		sleep(1)
	else:
		print("✈ " + x + " Succesfully landed at 0" + str(random.randint(1, 9)))
		print("✈ " + y + " Succesfully landed at 0" + str(random.randint(1, 9)))
		sleep(1)

def Landing(x, y):
	os.system("clear")
	print("Simulating...")
	sleep(1)
	print("✈ " + x + " flying at " + str(random.randint(100, 350)) + "mph Type: Cessna Aircraft")
	sleep(3)
	degreesX = str(random.randint(0, 360))
	runway = str(random.randint(1, 9))
	weather = random.randint(1, 3)
	print("✈ " + x + " flying " + degreesX + "°")
	sleep(3)
	print("✈ Runway 0" + runway + " Clear for landing. Location: " + y + ". Angle: " + degreesX)
	sleep(3)
	if weather == 1:
		print("✈ Runway 0" + runway + " weather status: Clear")
	elif weather == 2:
		print("✈ Runway 0" + runway + " weather status: Cloudy")
	elif weather == 3:
		print("✈ Runway 0" + runway + " weather status: Precipitation")
	sleep(1)
	print("✈ " + x + " Succesfully landed at Runway 0" + runway)

def Crash(x, y):
	os.system("clear")
	print("Simulating...")
	sleep(1)
	print("✈ " + x + " flying at " + str(random.randint(200, 576)) + "mph Type: Boeing 747 Dreamliner")
	print("✈ " + y + " flying at " + str(random.randint(200, 450)) + "mph Type: Neo Airbus")
	degrees = str(random.randint(0, 360))
	sleep(3)
	print("✈ " + x + " flying " + degrees + "°")
	print("✈ " + y + " flying " + degrees + "°")
	sleep(3)
	print("Crash between ✈ " + x + "band ✈ " + y + "bpredicted.")
	print("Terminating...")
	sleep(1)
	print("Mayday. Termination Failed.")
	sleep(1)
	print("A Crash Occurred.")
	sleep(1)

def CheckInputs():
	if option == "1":
		os.system("clear")
		a = input("What is the name of the first aircraft. Limit: 20 Characters.\n>>> ")
		print("Processing")
		sleep(1)
		b = input("What is the name of the second aircraft. Limit: 20 Characters.\n>>> ")
		print("Processing")
		sleep(1)
		aLength = len(a)
		bLength = len(b)
		if aLength + bLength >= 40:
			print("Too many characters. Try again.")
			sleep(1)
		else:
			AirTraffic(a, b)
	elif option == "2":
		os.system("clear")
		c = input("What is the name of the specified aircraft. Limit: 20 Characters.\n>>> ")
		print("Processing")
		sleep(1)
		d = input("What is the location of the airport.\n>>> ")
		print("Processing")
		sleep(1)
		cLength = len(c)
		if cLength >= 20:
			print("Too many characters. Try again.")
			sleep(1)
		else:
			Landing(c, d)
	elif option == "3":
		os.system("clear")
		e = input("What is the name of the first aircraft. Limit: 20 Characters.\n>>> ")
		print("Processing")
		sleep(1)
		f = input("What is the name of the second aircraft. Limit: 20 Characters.\n>>> ")
		print("Processing")
		sleep(1)
		eLength = len(e)
		fLength = len(f)
		if eLength + fLength >= 40:
			print("Too many characters. Try again.")
			sleep(1)
		else:
			Crash(e, f)

CheckInputs()