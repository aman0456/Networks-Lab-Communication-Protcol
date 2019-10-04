from sendSignal import makeSignal
from encode import encode

bitTime = 1
message=""

def senderOriginal(s):
	global message
	message = s
	s = appendCRC(s)
	makeSignal(s, bitTime)

def senderResponse(s):
	global message
	if s == "0":
		makeSignal(message + encode(message), bitTime)
		return False
	else:
		return True

def makeError(s, errors):
	s = list(s)
	for error in errors:
		if s[error] == '1':
			s[error] = '0'
		else:
			s[error] = '1'
	return ''.join(s)


if __name__== "__main__":
	#First Message
	timer = float(raw_input("Please enter the bit rate you would like: "))
	bitTime = timer
	message = raw_input("Please enter the message that you want to transmit: ")
	errors = raw_input("Please enter the indices of the errors: ").split()
	for i in range(len(errors)):
		errors[i] = int(errors[i])
	suffix = encode(message)
	errorMes = makeError(message, errors)
	makeSignal(errorMes+suffix, bitTime)
	while True:
		response = raw_input("Please give us the message received from the receiver: ")
		if senderResponse(response):
			break

	#Second Message
	timer = float(raw_input("Please enter the bit rate you would like: "))
	bitTime = timer
	message = raw_input("Please enter the message that you want to transmit: ")
	errors = raw_input("Please enter the indices of the errors: ").split()
	for i in range(len(errors)):
		errors[i] = int(errors[i])
	suffix = encode(message)
	errorMes = makeError(message, errors)
	makeSignal(errorMes+suffix, bitTime)
	while True:
		response = raw_input("Please give us the message received from the receiver: ")
		if senderResponse(response):
			break