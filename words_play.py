import random
WORDLIST=[]
com=''
EHW=[]
RHW=[]
VALID_CMD=['re','rr','se','sr','rehw','rrhw','sehw','srhw']

HELP="""  ---------------------------------------- HELP MENU ----------------------------------------



  h | help - Print that help menu

  q - Exit to main mode while you are in Random or Sequential word mode

  quit - Exit from program

  ehw - Display Current English Hard Words List

  fe - Flush English Hard Words List

  fr - Flush Russian Hard Words List

  m - Mark word as hard word (Add it to corresponding hard words list (English or Russian))

  r - Refresh words base

  re - Random English words mode (From Global English Words List)

  rhw - Display Current Russian Hard Words List

  rr - Random Russian words mode (From Global Russian Words List)

  rehw - Random English hard-words mode (From English Hard Words List)

  rrhw - Random Russian hard-words mode (From Russian Hard Words List)

  s - Print word count statistics

  se - Sequential English words mode (From Global English Words List)

  sr - Sequential Russian words mode (From Global Russian Words List)

  sehw - Sequential English hard-words mode (From English Hard Words List)

  srhw - Sequential Russian hard-words mode (From Russian Hard Words List)

  --------------------------------------------------------------------------------------------"""

def feed():
	L=[]
	f1=open(r'words.txt','r')

	for line in f1:
		if (line !='\n') and (' - ' in line):
			L.append(line.split(' - '))
	f1.close()
	return(L)


def hw_feed(F):        
	if F=='ehw':
		LL=[]
		for line in EHW:
			if (line !='\n') and (' - ' in line):
				LL.append(line.split(' - '))
		return LL
	  			
	if F=='rhw':
		LL=[]
		for line in RHW:
			if (line !='\n') and (' - ' in line):
						LL.append(line.split(' - '))
	return LL


def boxer(S,i=0):
	SL=len(S)
	if i==0:
		print('|'+'-'*(SL+2)+'|\n'+'| '+S+' |\n'+'|'+'-'*(SL+2)+'|\n')
	else:
		print('.'*(i+4)+'|'+'-'*(SL+2)+'|\n'+'.'*(i+4)+'| '+S+' |\n'+'.'*(i+4)+'|'+'-'*(SL+2)+'|\n')


def ehw(a,b):
	EHW.append(a.rstrip()+' - '+b.rstrip()+'\n')


def rhw(a,b):
	RHW.append(b.rstrip()+' - '+a.rstrip()+'\n')


def random_lang(flag='e',L=[]):
	x=0
	y=1
	otstup=52
	text='RANDOM ENGLISH WORDS MODE'
	if flag == 'e1':
		text='RANDOM ENGLISH WORDS FROM HARD WORDS LIST MODE'
		otstup=41
	if flag == 'r':
		x=1
		y=0
		text='RANDOM RUSSIAN WORDS MODE'
	if flag == 'r1':
		text='RANDOM RUSSIAN WORDS FROM HARD WORDS LIST MODE'
		otstup=41	  
	while True:
		K=L[random.randint(0,len(L)-1)]
		print(' '*otstup+'<--------|'+text+' |-------->\n')
		print('*'*150+'\n')
		boxer(K[x].rstrip())
		xx=input('')
		if xx=='q' or xx=='quit':
			break
		if (xx == 'm') and ((flag == 'e') or (flag == 'e1')):
			ehw(K[x],K[y])
		elif (xx == 'm') and ((flag == 'r') or (flag == 'r1')):
			rhw(K[y],K[x])
		boxer(K[y].rstrip(),len(K[x].rstrip()))
		print('*'*150)
		xxx=input('')
		if xxx=='q' or xxx=='quit':
			break
		if (xxx == 'm') and ((flag == 'e') or (flag == 'e1')):
			ehw(K[x],K[y])
		elif (xxx == 'm') and ((flag == 'r') or (flag == 'r1')):
			rhw(K[y],K[x])
		continue


def sequential_lang(flag='e',L=[]):
	t0=0
	x=0
	y=1
	otstup=49
	text='ENGLISH WORDS BY SEQUENCE'
	if flag == 'e1':
		otstup=38
		text='ENGLISH WORDS BY SEQUENCE FROM HARD WORDS LIST'
	if flag == 'r':
		x=1
		y=0
		text='RUSSIAN WORDS BY SEQUENCE'
	if flag == 'r1':
		otstup=38
		text='RUSSIAN WORDS BY SEQUENCE FROM HARD WORDS LIST'	  	
	for tt in L:
		print(' '*49+'<---| '+text+' -> ',t0+1, ' of ',len(L),' |--->\n')
		t0+=1
		print('*'*150+'\n')
		boxer(tt[x].rstrip())
		xx=input('')
		if (xx == 'q') or (xx == 'quit'):
			break
		if (xx == 'm') and ((flag == 'e') or (flag == 'e1')):
			ehw(tt[x],tt[y])
		elif (xx == 'm') and ((flag == 'r') or (flag == 'r1')):
			rhw(tt[y],tt[x])
		boxer(tt[y].rstrip(),len(tt[x].rstrip()))
		print('*'*150)
		xxx=input('')
		if (xxx == 'q') or (xxx == 'quit'):
			break
		if (xxx == 'm') and ((flag == 'e') or (flag == 'e1')):
			ehw(tt[x],tt[y])
		elif (xxx == 'm') and ((flag == 'r') or (flag == 'r1')):
			rhw(tt[y],tt[x])
		if t0 == len(L):
			print('\nALL WORDS ARE FETCHED!\n')
		continue
	
	 
def mscript(kom):	  
	if (kom == 're') and (not WORDLIST):
		print('Global Word List is empty')
	elif kom == 're':
		print('English words will appear in random order from Global English Words List\n')
		random_lang('e',WORDLIST)
	  
	if (kom == 'rr') and (not WORDLIST):
		print('Global Word List is empty')
	elif kom == 'rr':
		print('Russian words will appear in random order from Global Russian Words List\n')
		random_lang('r',WORDLIST)
	  
	  
	if kom == 'se' and not WORDLIST:
		print('Global Word List is empty')
	elif kom == 'se':
		print('English words will appear sequentially from the Global English Words base.\n')
		sequential_lang('e',WORDLIST)
	  
	  
	if kom == 'sr' and not WORDLIST:
		print('Global Word List is empty')
	elif kom == 'sr':
		print('English words will appear sequentially from the Global Russian Words base.\n')
		sequential_lang('r',WORDLIST)
	  
	
	if kom == 'rehw' and not EHW:
		print('Currently there is no word(s) added to English Hard Words list\n')		
	elif kom == 'rehw':
		print('English words will appear in random order from the English Hard Words List.\n')		
		L=hw_feed(F='ehw')
		random_lang('e1',L)
	  
	if kom == 'rrhw' and not RHW:
		print('Currently there is no word(s) added to Russian Hard Words list\n')
	elif kom == 'rrhw':
		print('Russian words will appear in random order from the Russian Hard Words List.\n')	
		L=hw_feed(F='rhw')
		random_lang('r1',L)

	if kom == 'sehw' and not EHW:
		print('Currently there is no word(s) added to English Hard Words list\n')		
	elif kom == 'sehw':
		print('English words will appear sequentially from the English Hard Words List.\n')		
		L=hw_feed(F='ehw')
		sequential_lang('e1',L)
	
	if kom == 'srhw' and not RHW:
		print('Currently there is no word(s) added to Russian Hard Words list\n')
	elif kom == 'srhw':
		print('Russian words will appear sequentially from the Russian Hard Words List.\n')		
		L=hw_feed(F='rhw')
		sequential_lang('r1',L)
	
WORDLIST=feed()


print('#'*150+'\n'+'\n  Welcome to "Word-Practice-Script"! Currently, there are ',len(WORDLIST),' words in our base.\n  Please enter "h" or "help" (without quotes) to list supported commands\' list\n\n'+'#'*150)


###########################################################################################################

while com !='quit':
        
	com=input('Enter command: ')
	print('\n')
	
	if com == 'quit':
		break
	
	if (com =='r') or (com == 'R'):
		L2=WORDLIST
		WORDLIST=[]
		WORDLIST=feed()
		if L2 == WORDLIST:
			print('\nNo changes made to words base!\n')
		else:
			print('\nWords Base Refreshed! Now there are ',len(WORDLIST),' words to practice.\n')
		
	if (com == 's') or (com == 'S'):
		print('\nCurrently there are ',len(WORDLIST),' words for practising.\n')
		continue

	if (com == 'h') or (com == 'help'):
		print(HELP)

	if (com == 'fe'):
		EHW=[]
		print('\n !!! ENGLISH HARD WORDS LIST HAS BEEN FLUSHED !!!\n')

	if (com == 'fr'):
		RHW=[]
		print('\n !!! RUSSIAN HARD WORDS LIST HAS BEEN FLUSHED !!!\n')

	if (com == 'ehw'):
		if not EHW:
			print('English Hard Word(s) List is Currently Empty\n')
		else:
			for line in EHW:
				print(line)

	if (com == 'rhw'):
		if not RHW:
			print('Russian Hard Word(s) List is Currently Empty\n')
		else:
			for line in RHW:
				print(line)
		
	if com in VALID_CMD:
		mscript(com)
	  			
	else:
		continue

#########################################################################################

	  
	  











