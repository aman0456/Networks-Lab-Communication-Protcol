from graphics import *
from time import sleep

interimTime = 0.1

def makeSignal(s, bitTime):
	win = GraphWin("Communication", 1300, 700)
	rect = Rectangle(Point(0, 0), Point(1300, 700))
	rect.draw(win)
	rect.setFill("blue")
	sleep(bitTime)
	for bit in s:
		rect.setFill("yellow")
		sleep(interimTime)
		if bit == '1':
			rect.setFill("green")
		else:
			rect.setFill("red")
		sleep(bitTime)
	rect.setFill("yellow")
	sleep(interimTime)
	rect.setFill("blue")
	sleep(bitTime)
	win.close()
