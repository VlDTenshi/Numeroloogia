from random import*
import random 


def read_file(file:str)->list: 
    """read file
    :param str file: file name
    :param list mas: list
    """

    fail=open(file,'r', encoding='utf-8-sig') 
    mas=[] 
    for row in fail: 
        if row.isdigit(): 
            mas.append(row.strip()) 
        else:
            mas.append(row.strip()) 
    fail.close()
    return mas 

def save_to_file(mas:list,file:str): 
    """save list to file
    :param str file: file name
    :param list mas: list
    """

    f=open(file,'w', encoding='utf-8-sig') 
    for item in mas: 
        f.write(item+'\n') 
    f.close() 

def input_word(e:list,r:list): 
    """ input words English or Russian to list to save
    :param English list: list
    :param Eussian list: list
    """
    n=int(input('what language_? 1 English, 2 Russian')) 
    if int(n)==1:
        english=input('English:') 
        e.append(english) 
        russian=input('Russian:') 
        r.append(russian) 
    else:
        russian=input('Russian:') 
        r.append(russian) 
        english=input('English:') 
        e.append(english) 

    return english,russian 

def fix_e(name:str,e:list):
    """ opportunity for a user to fix a word in English provided it was noticed.
    :param name str: 
    param English list:
    """
    v=e.count(name) 
    v=input('enter word has to be fixed:') 
    if v in name: 
        fix_word=input('correction:') 
        for n,i in enumerate(name): 
            if i==v: 
                name[n]=fix_word 
                for j,n in zip(name,e): 
                    print(f'{j} / {n}')
                #print('fixed:\n{0}'.format(name))

def fix_r(name:str,r:list): 
    """ opportunity for a user to fix a word in Russian
    provided it was noticed.
    :param name str: 
    param Russian list:
    """
    v=r.count(name) 
    v=input('enter word has to be fixed:')
    if v in name: 
        fix_word=input('correction:')
        for f,j in enumerate(name): 
            if j==v: 
                name[f]=fix_word
                for t,c in zip(name,r): 
                    print(f'{t} / {c}')
                #print('fixed:\n{0}'.format(name)) 

def control_word(e:list,r:list):
    """ kind of a test as long as a user wishes to have a tiger by the tail
    :param English list:
    :param Russian list:
    """
    ru=0 
    en=0
    try:
        
        for i in range(4): 
            eng=list(map(str,e)) 
            eng=random.choice(eng) 
            print(eng)  
            rus=list(map(str,r)) 

            answ=input('word:')  
            
        
            if answ in rus: 
                print('right') 
                en+=1
            if answ not in rus: 
                print('wrong') 
            ru+=1
        
        p=en/ru*100
        print(f'point is {p}')
        try: 
            p=en/ru*100 
        except:
            print("") 
        if p<=59: 
            mark="your mark is 2" 
        elif p>=60 and p<=74:  
            mark="your mark is 3" 
        elif p>=75 and p<=89: 
            mark="your mark is 4" 
        else: 
            mark="your mark is 5"
        print(mark)
        
    except ZeroDivisionError:
                  
  
        return e,r
