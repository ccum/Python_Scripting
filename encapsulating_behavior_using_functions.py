#!/usr/bin/env python
def gather_info():
	height = float(raw_input("What is your height? "))
	weight = float(raw_input("What is your weight? "))
	unit = raw_input("Are your measurements in metric or imperal units? ").lower().strip()
	return (height,weight,unit)

def calculate_bmi(height,weight,unit):
	if unit == 'metric':
		bmi= weight/(height**2)
	else:
		bmi= 703* (weight/(height**2))
	print("Your BMI is %s" % bmi)

while True:
	height,weight,unit = gather_info()
	if unit.startswith('i'):
		calculate_bmi(height,weight,'imperal')
	elif unit.startswith('m'):
		calculate_bmi(height,weight,'metric')
	else:
		print ("error: Unknowm measurement System")




