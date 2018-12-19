
from twilio.rest import Client
import random
import localvariables as loc


client = Client(loc.account_sid, loc.auth_token)
recepientname = 'Enter a name here' #must enter your own value
recepientnumber = 'Enter a number here'#must enter your own value


if __name__ == "__main__":	
	'''opens file containing log'''
	readfile = open('santaexchangeloc.txt', 'r')
	thisline = readfile.readline()
	line = []
	thismessage = ''
	while thisline != '':
		line.append(thisline)
		'''Reads file until it reaches the line containing "Thank you (the name of person receiving)!", 
		and saves the text they should have received'''
		if 'Thank you ' +recepientname+'!' in thisline:
			thisline = readfile.readline()
			line.append(thisline)
			'''Formats the text so that it can be sent out to the new person receiving it'''
			newline = line[len(line):len(line)-6:-1]
			newline.reverse()
			for x in newline:
				thismessage += x

			thisline = ''
		else:
			thisline = readfile.readline()
	'''Twilio code for sending sms'''
	message = client.messages \
					.create(
						 body= thismessage ,
						 from_= loc.localnumber,
						 to= recepientnumber
					 )

	print(message.sid)
			

			

		

	readfile.close()