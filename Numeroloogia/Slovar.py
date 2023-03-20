from module1 import* 

while True: 
    print('----------------------------------------')
    print('\n0 read file\n1 input words\n2 save words to dictionary\n3 translate word/find word\n4 fix_word\n5 test') 
    v=input('>>:')
    if v=='0': 
        english=[] 
        russian=[] 
        english=read_file('eng_lan.txt') 
        russian=read_file('rus_lan.txt') 
        zipped=list(zip(english,russian))
        for e,n in zip(english,russian): 
                print(f'{e} / {n}')
        
    elif v=='1': 
        english,russian=input_word(english,russian) 
        for e,n in zip(english,russian): 
                print(f'{e} / {n}')
    elif v=='2':
          
        save_to_file(english,'eng_lan.txt') 
        save_to_file(russian,'rus_lan.txt')
    elif v=='3':




        with open('eng_lan.txt','r', encoding='utf-8-sig') as eng_lan, open('rus_lan.txt', 'r', encoding='utf-8-sig') as rus_lan:
            eng = map(str.rstrip, eng_lan)
            rus = map(str.rstrip, rus_lan)
            

            data = dict(zip(eng, rus))
            
            n=input('what laguage? 1 Englis, 2 Russian')
            if int(n)==1: 
                word =input('English ')
                if word in data.keys():
                    print(f'word: {word} is found: {data[word]}')
                if word not in data.keys():
                    print('word is not found')
                if word not in data.keys(): 
                    print('would you like to input the word to the dictionary?:1 yes,2 no')
                    c=input('')
                    if c=='1':
                           english,russian=input_word(english,russian) 
                           for x,o in zip(english,russian):  
                               print(f'{x} / {o}')
                    elif c=='2':
                        break
            if int(n)==2:  
                with open('eng_lan.txt','r', encoding='utf-8-sig') as eng_lan, open('rus_lan.txt', 'r', encoding='utf-8-sig') as rus_lan: 
                    eng = map(str.rstrip, eng_lan) 
                    rus = map(str.rstrip, rus_lan) 
                    data = dict(zip(rus, eng))  
                    word =input('Russian') 
                    if word in data.keys():
                            print(f'word: {word} is found: {data[word]}') 
                    if word not in data.keys():
                            print('word is not found')
                    if word not in data.keys(): 
                            print('would you like to input the word to the dictionary?:1 yes,2 no')
                            c=input('')
                            if c=='1':
                                   english,russian=input_word(english,russian) 
                                   for z,l in zip(english,russian):   
                                       print(f'{z} / {l}')
                            elif c=='2':
                                break
    elif v=='4':
        c=input('in which language the word should be corrected? 1 English,2 Russian ') 
        try:
            if c=='1': 
                fix_e(english,russian) 
            if c=='2': 
                fix_r(russian,english) 
        except:
            print('Error')
    elif v=='5':  
        control_word(english,russian) 
