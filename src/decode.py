from encode import encode

messageLength = 0

def diff(a, b):
	ans = []
	for i in range(len(a)):
		if a[i] != b[i]:
			ans.append(i)
	return ans

def solver(l):
	mod4 = l[0]
	mod5 = l[1] - 4
	mod7 = l[2] - 9
	global messageLength
	index = mod4
	while index < messageLength:
		if index%5 == mod5 and index%7 == mod7:
			#print(index)
			return index
		index += 4
	return -1

def solver2(l, mod1, mod2):
	moda = l[0]
	modb = l[1]
	global messageLength
	index = moda
	while index < messageLength:
		if index%mod2 == modb:
			#print(index)
			return index
		index += mod1
	return -1

def decode(s):
	global messageLength
	messageLength = len(s) - 16
	suffix = s[-16:]
	receivedMessage = s[:-16]
	listMessage = list(receivedMessage)
	expectedSuffix = encode(receivedMessage)
	difference = diff(suffix, expectedSuffix)
#	print(difference)
	numberDiff = len(difference)
	if numberDiff == 0: #no error
		return receivedMessage
	if numberDiff == 3: #1 bit error
		index = solver(difference)
		if index == -1:
			return False
		else:
			if listMessage[index] == '0':
				listMessage[index] = '1'
			else:
				listMessage[index] = '0'
			return ''.join(listMessage)
	if numberDiff == 6: # 2 bit error with no common modulo
#		print('--------------')
#		print(numberDiff)
		four = difference[0:2]
		five = difference[2:4]
		seven = difference[4:6]
		# five[0] = five[0] - 4
		# five[1] = five[1] - 4
		# seven[0] = seven[0] - 9
		# seven[1] = seven[1] - 9
		for i in range(2):
			for j in range(2):
				if solver([four[0], five[i], seven[j]]) != -1 and solver([four[1], five[1-i], seven[1-j]]) != -1:
					index = solver([four[0], five[i], seven[j]])
					listMessage[index] = chr(48 +49 - ord(listMessage[index]))
					index = solver([four[1], five[1-i], seven[1-j]])
					listMessage[index] = chr(48 + 49 - ord(listMessage[index]))
					return ''.join(listMessage)
		return False
	if numberDiff == 4: # 2 bit error with a common modulo
		lostMod = 0
	#	print('-------------------')
		if difference[0] >= 4:
			lostMod = 4
			index1 = solver2([difference[0] - 4, difference[2] - 9], 5, 7)
			index2 = solver2([difference[1] - 4, difference[3] - 9], 5, 7)
			if ((index1 - index2)%4 == 0) and (index2 != -1) and (index1 != -1):
				listMessage[index1] = chr(48 +49 - ord(listMessage[index1]))
				listMessage[index2] = chr(48 +49 - ord(listMessage[index2]))
				return ''.join(listMessage)
			# print('-------------------')
			index1 = solver2([difference[0] - 4, difference[3] - 9], 5, 7)
			index2 = solver2([difference[1] - 4, difference[2] - 9], 5, 7)
			if ((index1 - index2)%4 == 0) and (index2 != -1) and (index1 != -1):
				listMessage[index1] = chr(48 +49 - ord(listMessage[index1]))
				listMessage[index2] = chr(48 +49 - ord(listMessage[index2]))
				return ''.join(listMessage)
			return False
			
		elif difference[3] < 9:
			
			lostMod = 7
			index1 = solver2([difference[0], difference[2] - 4], 4, 5)
			index2 = solver2([difference[1] , difference[3] - 4], 4, 5)
			if ((index1 - index2)%7 == 0) and (index2 != -1) and (index1 != -1):
				listMessage[index1] = chr(48 +49 - ord(listMessage[index1]))
				listMessage[index2] = chr(48 +49 - ord(listMessage[index2]))
				return ''.join(listMessage)
			index1 = solver2([difference[0], difference[3] - 4], 4, 5)
			index2 = solver2([difference[1] , difference[2] - 4], 4, 5)
			if ((index1 - index2)%7 == 0) and (index2 != -1) and (index1 != -1):
				listMessage[index1] = chr(48 +49 - ord(listMessage[index1]))
				listMessage[index2] = chr(48 +49 - ord(listMessage[index2]))
				return ''.join(listMessage)
			return False
		else:
			lostMod = 5
			index1 = solver2([difference[0], difference[2] - 9], 4, 7)
			index2 = solver2([difference[1] , difference[3] - 9], 4, 7)
			if ((index1 - index2)%5 == 0) and (index2 != -1) and (index1 != -1):
				listMessage[index1] = chr(48 +49 - ord(listMessage[index1]))
				listMessage[index2] = chr(48 +49 - ord(listMessage[index2]))
				return ''.join(listMessage)
			index1 = solver2([difference[0], difference[3] - 9], 4, 7)
			index2 = solver2([difference[1] , difference[2] - 9], 4, 7)
			if ((index1 - index2)%5 == 0) and (index2 != -1) and (index1 != -1):
				listMessage[index1] = chr(48 +49 - ord(listMessage[index1]))
				listMessage[index2] = chr(48 +49 - ord(listMessage[index2]))
				return ''.join(listMessage)
			return False
		return False
	return False
