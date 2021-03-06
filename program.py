import fileinput


def Matriz(key,alphabet):
    matrix = []
    elements='ENCRYPT'
    for i in alphabet:
        if (i not in key):
            elements += i
    x=0
    for m in range(0,5):
        matrix.append([])
        for n in range (0,5):
            matrix[m].append(elements[x])
            x+=1
    return matrix

def encrypt(matrix, text):
    up=[]
    down=[]
    for one in text:
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

def decrypt(matrix, text):
    up=[]
    down=[]
    for one in text:
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
#Para saber si se quiere cifrar o descifrara
if(choice=='ENCRYPT'):
    print(encrypt(matrix,text))
else:
    print(decrypt(matrix,text))
