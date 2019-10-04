def encode(s):
	ans = generate(s, 4)+generate(s, 5)+generate(s, 7)
	return ''.join(ans)

def generate(s, modulo):
	l = len(s)
	ans = [0]*modulo
	for start in range(modulo):
		i = start
		while i < l:
			if s[i]=='1':
				ans[start] += 1
			i+=modulo
		ans[start] = ans[start]%2
		ans[start] = chr(48+ans[start])
	return ans