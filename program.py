def main():
    #Se define la llave
    key='ENCRYPT'
    #Se lee la entrada
    lines = []
    for line in fileinput.input():
    	lines.append(line)
    #Se limpian las entradas
    choice = lines[0].replace("\n","")
    text = lines[1].replace(" ","")
    text = text.replace("\n","")
    #Se define la Matriz
    alphabet='ABCDEFGHIKLMNOPQRSTUVWXYZ';
    matrix = Matriz(key,alphabet)

    #Para saber si se quiere cifrar o descifrar
    final='';
    if(choice=='ENCRYPT'):
        final=encrypt(matrix,text)
    else:
	    final=decrypt(matrix,text)
    print(final)

def Matriz(key,alphabet):
    matrix = []
    order=''
    for i in key:
        order+=i
    for i in alphabet:
        if (i not in key):
            order+=1
    x=0
    for i in range(0,5):
        matrix.append([])
        for j in range (0:5):
            matrix[j].append(order[x])
            x+=1
    return matrix

def encrypt(matrix, word):
    up=[]
    down=[]
    for one in word:
        for i in range(0,5):
            if(one in matrix[i]):
                break
        Col=matrix[i].index(one)
	    up.append(i)
		down.append(Col)
    Array=up+down
    encrypted=''
    for i in range(0, len(Array),2):
	    encrypted+=matrix[Array[i]][Array[i+1]]
    return encrypted
def decrypt(matrix, word):
    up=[]
    down=[]
    for one in word:
    	for i in range(0,5):
	    	if(one in matrix[i]):
		    	break
	    Col=matrix[i].index(one)
	    up.append(i)
	    down.append(Col)
    Array=[]
    for i in range(len(up)):
    	Array.append(up[i])
	    Array.append(down[i])
    decrypted=''
    for i in range(len(Array)//2):
	    decrypted+=matrix[Array[i]][Array[i+len(Array)//2]]
    return decrypted
main()
