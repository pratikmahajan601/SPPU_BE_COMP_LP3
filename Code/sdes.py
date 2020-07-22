#Program :
#-----------------------------------------------------------
plainText = "01110010"
key =  "1010000010"
pc1 = [3,5,2,7,4,10,1,9,8,6]   
pc2 = [6,3,7,4,8,5,10,9] 
k1  = ""
k2  = ""
ip  = [2,6,3,1,4,8,5,7]
et  = [4,1,2,3,2,3,4,1]
inverseip = [4,1,3,5,7,2,8,6]
ptable = [2,4,3,1]
sbox0 = [
			[ "01", "00", "11", "10" ],
			[ "11", "10", "01", "00" ],
			[ "00", "10", "01", "11" ],
			[ "11", "01", "11", "10" ]
		]
sbox1 = [
			[ "00", "01", "10", "11" ],
			[ "10", "00", "01", "11" ],
			[ "11", "00", "01", "00" ],
			[ "10", "00", "00", "11" ]
		]

def apply_transpose(message,table):
	return ''.join([ message[ table[i]- 1] for i in range(len(table)) ])

def xor(l,r):
	return ''.join(['0' if l[i]==r[i] else '1' for i in range(len(l))])

def lcr(m,times):  
	for time in range(times):
		m = m[1:] + m[:1]
	return m 
	
def gen_subkeys():
	global key,k1,k2
	print("orig key",key)
	key = apply_transpose(key,pc1)
#	print("k+ ",key)
	c0,d0 = key[0:5],key[5:]	
#	print("c0 d0",c0,d0)
	c1,d1 = lcr(c0,1),lcr(d0,1)
	k1    = apply_transpose(c1+d1,pc2)
	c2,d2 = lcr(c1,2),lcr(d1,2)
	k2 	  = apply_transpose(c2+d2,pc2)	

def apply_sbox(m,sbox):
	rowIndex =  int(m[0]+m[-1],2)

	colIndex =  int(m[1]+m[2],2)
	return sbox[rowIndex][colIndex]
	
def f(r,k):
	er = apply_transpose(r,et)
	#print("expanded r1",er)
	b0,b1 = xor(er,k)[0:4] , xor(er,k)[4:] 	
	#print("b0 b1",b0,b1)
	result = apply_sbox(b0,sbox0) + apply_sbox(b1,sbox1)
	return apply_transpose(result,ptable)
	
def algo():
	permuted_text = apply_transpose(plainText,ip) 

	print("Plain Text :",plainText)
	gen_subkeys()
	print("Subekys:",k1,k2)
	l0,r0 = permuted_text[:4],permuted_text[4:] 
	#print("l0 r0",l0,r0)
	l1,r1 = r0, xor(l0, f(r0,k1) ) 
    
	#print("l1 r1",l1,r1)
	permuted_text1 = apply_transpose(l1+r1,ip)
	l2,r2 = permuted_text1[:4],permuted_text1[4:]
	#print(l2,r2)
	l3,r3 = r2, xor(l2, f(r2,k2) )
	#print(l3,r3)
	#l3,r3 = r3,l3 
	cipher = apply_transpose(l3+r3,inverseip)
	print("cipher",cipher)

algo()

#--------------------------------------------------------------
'''
Output :
Plain Text : 01110010
orig key 1010000010
Subekys: 10100100 01000011
cipher 01100101


 


'''

 
