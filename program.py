'''
	+ Autor: césar Alejandro García Padrón
	+ Fecha: 13/Octubre/2020
	+ Práctica 1: The Bifid cipher

	+Programa que implementa el cifrado de Bifid
'''
import re, string
'''
	Paso 1: Declarar matriz inicial 
'''

def prepareText(text):
	#Quitamos signos
	text=re.sub('[%s]' % re.escape(string.punctuation), '', text)
	#Quitamos números
	number = re.compile(r'[0-9]')
	text=number.sub('',text)
	#Quitamos ñ y ¿
	text=text.replace('ñ','')
	text=text.replace('¿','')
	#Quitamos espacios
	text=text.replace(' ','')
	#Convertimos a mayúsculas
	text=text.upper()
	return text



def encrypt(matrix, word, m):
	word=prepareText(word)
	arrayUp=[]
	arrayDown=[]
	for letter in word:
		for i in range(0,m):
			if(letter in matrix[i]):
				break
		indexRow=i
		indexColumn=matrix[i].index(letter)
		arrayUp.append(indexRow)
		arrayDown.append(indexColumn)


	arrayComplete=arrayUp+arrayDown

	wordEncrypted=''

	for i in range(0,len(arrayComplete),2):
		wordEncrypted += matrix[arrayComplete[i]][arrayComplete[i+1]]

	return wordEncrypted



def decrypt(matrix, word, m):
	arrayUp=[]
	arrayDown=[]
	for letter in word:
		for i in range(0,m):
			if(letter in matrix[i]):
				break
		indexRow=i
		indexColumn=matrix[i].index(letter)
		arrayUp.append(indexRow)
		arrayDown.append(indexColumn)

	arrayComplete=[]
	for i in range(len(arrayUp)):
		arrayComplete.append(arrayUp[i])
		arrayComplete.append(arrayDown[i])

	wordEncrypted=''

	for i in range(len(arrayComplete)//2):
		wordEncrypted += matrix[arrayComplete[i]][arrayComplete[i+len(arrayComplete)//2]]

	return wordEncrypted




def definirMatriz(m,key):
	#key='ENCRYPT'
	alphabet='ABCDEFGHIKLMNOPQRSTUVWXYZ';
	matrix=[]
	elemntOrder=''
	for i in key:
		elemntOrder += i;
	for i in alphabet:
		if(i not in key):
			elemntOrder += i;

	index=0
	for j in range(0,m):
		matrix.append([]);
		for k in range(0,m):
			matrix[j].append(elemntOrder[index])
			index += 1
			
	return matrix




def main():
	m=5
	key='ENCRYPT'
	option=input()
	text=input()
	matrix = definirMatriz(m,key)
	finalPhrase='';
	if(option=='ENCRYPT'):
		finalPhrase=encrypt(matrix,text,m)
	else:
		finalPhrase=decrypt(matrix,text,m)

	print(finalPhrase)

	'''
	print('\nMatriz del método: ')
	for i in range(m):
		for j in range(m):
			print('\t'+matrix[i][j],end="")
		print('')
	'''


	#stringToEncrypt='Meet me on Friday'
	'''
	print('\nCadena a encriptar: '+stringToEncrypt)
	wordEncrypted= encrypt(matrix,stringToEncrypt,m)
	print('Cadena endriptada: '+wordEncrypted+'\n')

	stringToDecrypt='LNLLFGPPNPGRSK'
	print('Cadena a desencriptar: '+ stringToDecrypt)
	wordDecrypted= decrypt(matrix,stringToDecrypt,m)
	print('Cadena desencriptada: '+wordDecrypted)
	'''
	

main()
