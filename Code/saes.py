#implementation of S-AES 
#----------------------------------------------------------

sbox = { 
		 "0000" : "1001" , "0001" : "0100" , "0010" : "1010" , "0011" : "1011" ,
		 "0100" : "1101" , "0101" : "0001" , "0110" : "1000" , "0111" : "0101" ,	
		 "1000" : "0110" , "1001" : "0010" , "1010" : "0000" , "1011" : "0011" ,		 
		 "1100" : "1100" , "1101" : "1110" , "1110" : "1111" , "1111" : "0111" 
	   }

key0 = "0100101011110101"
key1 = ""
key2 = ""
pt   = "1101011100101000"
print("Plain Text :",pt)
print("Original Kay :",key0)
roundConstant = ["","10000000","00110000"]

def applysbox(b):
	return sbox[b]

def xor(l,r):
	return ''.join(['1' if l[i]!=r[i] else '0' for i in range(len(l))])

def g(w,rnd):
	w = w[4:] + w[:4]					    #circular shift
	w = applysbox(w[:4]) + applysbox(w[4:]) #byte substitution
	w = xor(w,roundConstant[rnd])
	return w 

def gen_keys():
	global key0,key1,key2
	w0,w1 = key0[:8] , key0[8:]
	w2 = xor(w0,g(w1,1))	
	w3 = xor(w2,w1)
	key1 = w2+w3 
	print("key1 ",key1)
	
	w4 = xor(w2,g(w3,2))
	w5 = xor(w4,w3)
	key2 = w4+w5
	print("key2 ",key2)

def cross(b1,b2):
	#4th row of GF24 lookup table
	lt = ["0000","0100","1000","1100","0011","0111","1011","1111","0110","0010","1110","1010","0101","0001","1101","1001"] 
	if b2 == 1:
		return b1 
	if b2 == 4:
		return lt[int(b1,2)]

def mixcol(it, gf):
	return [ [ xor(cross(it[0][j],gf[i][0]),cross(it[1][j],gf[i][1])) for j in range(2) ] for i in range(2) ] 

def bytesubstitution(b):
	return ''.join( [applysbox(b[i:i+4]) for i in range(0,16,4) ] ) 

def algo():
	it = xor(pt,key0) # Initial Transformation
	
	#Round1 
	it = bytesubstitution(it)
	itMat = [ 
			  [it[:4], it[8:12] ],
			  [it[4:8], it[12:] ]
			]
	
	#RowShift
	itMat[0] = itMat[0]			#Row1 unchanged 
	itMat[1] = [itMat[1][1],itMat[1][0]]   #Row2 byte shifted by 1
	
	#MixColumn
	gfMat = [
				[1,4],
				[4,1]  
			] 
	#print(itMat)		
	mixedCol = mixcol(itMat, gfMat) 
	#print(mixedCol)
	
	round1op = xor(mixedCol[0][0]+mixedCol[1][0]+mixedCol[0][1]+mixedCol[1][1],key1)
	
	#round2 begins
	
	round1op = bytesubstitution(round1op)
	round1Mat = [ 
			  [round1op[:4], round1op[8:12] ],
			  [round1op[4:8], round1op[12:] ]
			]
	
	#RowShift
	round1Mat[0] = round1Mat[0]			#Row1 unchanged 
	round1Mat[1] = [round1Mat[1][1],round1Mat[1][0]]   #Row2 byte shifted by 1
	
	cipherText = xor(round1Mat[0][0]+round1Mat[1][0]+round1Mat[0][1]+round1Mat[1][1],key2)
	print("cipher text",cipherText)		
gen_keys()			
algo()		

'''
-------------------------------------------------------------
Output :
Plain Text : 1101011100101000
Original Kay : 0100101011110101
key1  1101110100101000
key2  1000011110101111
cipher text 0010010011101100	



'''
 



