from sendSignal import makeSignal
from decode import decode

bitTime = 1

def sendAck(b):
	if b:
		makeSignal("1", bitTime)
	else:
		makeSignal("0", bitTime)

def decodeAtReceiver(s):
	if (len(s)<16):
		print("Incorrect input sequence")
		return
	decoded = decode(s)
	if decoded != False:
		print ("Message has been receieved correctly!")
		print 
		print ("Message is " + decoded)
		print
		sendAck(True)
		return True
	else:
		print("Unrecoverable error detected in message")
		print
		sendAck(False)
		return False


if __name__=="__main__":
	#first time 
	while True:
		st = raw_input("Please input the receieved data: ")
		if st == "!" :
			sendAck(False)
		elif st == ">":
			sendAck(True)
		elif decodeAtReceiver(st):
			break
	#second time
	while True:
		st = raw_input("Please input the receieved data: ")
		if st == "!" :
			sendAck(False)
		elif st == ">":
			sendAck(True)
		elif decodeAtReceiver(st):
			break