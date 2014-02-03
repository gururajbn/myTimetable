#! /usr/bin/env python
import datetime
import os
currentDay= datetime.datetime.now().strftime("%A")[:3].lower()

def displyTimeTable(indicator,day):
	if day=='sun':
		print " NO CLASS ON SUNDAY"
		return
	t=0
	today=time_table[day[:3]]
	print '''\"TIME                         '''+indicator+day[:3].upper()+'''\"
-----------------------------------'''
	for i in today:
		print time[t]+'  |'+subjects[i]+'|'
		t+=1
	print '-----------------------------------'
	return 

week=['sun','mon','tue','wed','thu','fri','sat']

time={	0:'08:00 AM',
		1:'09:00 AM',
		2:'10:30 AM',
		3:'11:30 AM',
		4:'12:30 PM',
		5:'02:30 PM',
		6:'03:30 PM',
	}

subjects={	0:"        FREE           ",
			1:"    Comp Graphics      ",
			2:"    Comp Networks      ",
			3:"Object  Design Modeling",
			4:"Artificial Intelligence",
			5:"Advance Data Structures",
			6:"Mini Project assessment",

		}

time_table= {	
				'mon':[3,3,0,2,4],
				'tue':[0,0,0,1,2,5,5],
				'wed':[1,5,0,2,3],
				'thu':[1,1,0,3,2],
				'fri':[4,4,5],
				'sat':[0,4],
			}	

for i in range (0,7):
	if week[i]==currentDay:
		displyTimeTable('*',week[i])
		break

while True:
	if raw_input(">>")=='':
		i+=1
		displyTimeTable('~',week[i%7])
	else:
		break


