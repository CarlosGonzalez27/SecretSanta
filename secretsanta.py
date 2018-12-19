from twilio.rest import Client
import random

#local variables contains the list of names, numbers, and authentication keys needed to use twilio you must have a localvariables.py with these variables to use this script
import localvariables as loc


client = Client(loc.account_sid, loc.auth_token)
''' names, exchange, and numbers are all string lists. Names and exchange contain the names of people participating in the gift exchange. Numbers is a string list with
the numbers of those individuals. '''
names = loc.names
exchange = loc.exchange
numbers = loc.numbers

if __name__ == "__main__":	
	'''This randomly shuffles the names in the exchange list'''
	for x in range(10):
		random.shuffle(exchange)

	'''This file will keep a log of the names incase anyone loses their text'''	
	openfile = open('santaexchangelog.txt', "w")


		
	while len(exchange) > 0:
		'''Used to make sure two people using the same phone to receive a text dont get themselves'''
		if names[0] == loc.samephone1 and exchange[0] == loc.samephone2 or names[0] == loc.samephone2 and exchange[0] == loc.samephone1:
			random.shuffle(exchange)
		elif exchange[0] != names[0] and exchange[len(exchange)-1] != names[len(names)-1]:
			'''Used to make sure the first person and the last person on our lists is not assigned themselves'''
			tonumber = numbers.pop(0)
			receiving = names.pop(0)
			if receiving == loc.spanishspeaker:
				'''Sends spanish message for any spanish speaker'''
				thismessage = ('******************\nEste es Papá Noel. \nNecesito tu ayuda para darle un regalo a ' + exchange.pop(0) + ' este año. \nGracias ' + spanishspeaker+ '. Feliz Navidad!\n')
			else:
				thismessage = ( '******************\nA message from Santa: \nI need your help with gifting ' + exchange.pop(0) + " this year. \n Thank you " + receiving + '!\n Merry Christmas!!\n')
			

			'''Twilios code used to send SMS'''
			message = client.messages \
							.create(
								 body= thismessage ,
								 from_= loc.localnumber,
								 to= tonumber
							 )

			print(message.sid)
			
			openfile.write(thismessage)
			
		else:
		
			random.shuffle(exchange)
			
	openfile.close()