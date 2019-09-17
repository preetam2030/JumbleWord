import numpy as np
import random
filename="words1.txt"
wrdlist=np.loadtxt(filename,delimiter='\n',dtype=str)
l=[]
n=int(input("Enter no of letters"))
for i in range(wrdlist.size):
	if (len(wrdlist[i])==n)and('-' not in wrdlist[i])and('(' not in wrdlist[i]):
		l.append(wrdlist[i])
word=l[np.random.randint(0,len(l))]
#print(word)
unjumble=list(word)
random.shuffle(unjumble)
def game(letters,wrd):
	f=0
	print("The letters are: "+", ".join(letters)+"\n")
	while(f==0):
		s=input("Unjumble the word or enter 1 to give up\n")
		if(s==wrd):
			print("Congratulations you won")
			break
		elif(s=='1'):
			print(wrd+"\n")
			break
		else:
			print("Wrong answer\n")
game(unjumble,word)		
		
		
		
		
		