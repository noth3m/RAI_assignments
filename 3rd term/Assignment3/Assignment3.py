class assignment3:    
    class pattern_questions : # this class is solely for pattern questions , each function name defines its part number 
        def ques1(n): 
            for i in range(n):
                for j in range(i+1):
                    print('*',end='')
                print()
        def ques2(n):
            str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            for i in range(n):
                for j in range(i+1):
                    print(str[j],end =' ')
                print()
        def ques3(n):
            for i in range(1,n+1):
                for j in range(i):
                    print(i,end =' ')
                print()
        def ques4(n):
            k = 1
            for i in range(0,n):
                for j in range(0,i+1):
                    print(k-1,end = '')
                    k = k + 1
                print()
        def ques5(n):
            for i in range(n):
                x = 1
                for j in range(n-i):
                    print(end= ' ')
                for k in range(i+1):
                    print(x,end='')
                    x = x + 1
                print()
        def ques6(n):
            for i in range(n):
                i = n-i
                for j in range(i):
                    print('*',end='')
                print()
        def ques7(n):
            for i in range(1,n+1):
                for j in range(n-i):
                    print(end=' ')
                for k in range(2*i-1):
                    print('*',end='')
                print()
        def ques8(n):
            for i in range(n):
                for j in range(i):
                    print(end=' ')
                x = n - i 
                for k in range(2*x-1):
                    print('*',end='')
                print('')
        def ques9(n):
            for i in range(n):
                for k in range(n-i):
                    print(" ",end='')
                x = 1
                for j in range(i + 1):
                    print(x,end='')
                    x = x + 1
                for k in range(i):
                    print(i,end='')
                    i = i-1
                print()
        def ques10(n):
            x = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            m = n
            for i in range(n):
                for j in range(i):
                    print(' ',end='')
                u = 0
                for k in range(m):
                    print(x[slice(u,u +1)],end=' ')
                    u = u + 1
                m= m -1
                print()
        def ques11(n):
            for i in range(n):
                x = 1
                if i%2 == 0 :
                    for j in range(i+1):
                        print(x,end='')
                        x = x + 1
                    print()
            for l in range(1,n):
                x = 1
                if l%2 == 0:
                    for m in range(n-l):
                        print(x,end='')
                        x = x + 1
                    print()
        def ques12(n):
            for i in range(n):
                for j in range(n-i):
                    print('*',end='')
                for k in range(i):
                    print(' ',end='')
                for l in range(i-1):
                    print(' ',end='') 
                if i == 0:
                    for m in range(n-i-1):
                        print('*',end='')
                else:
                    for m in range(n-i):
                        print('*',end='')
                print()      
        def ques13(n):
            for i in range((n+1)//2):
                for j in range(n-i):
                    print('*',end='')
                print()
            for k in range(((n+1)//2)+1,n+1):
                for l in range(k):
                    print('*',end='')
                print()
        def ques14(n):
            for i in range(1,n+1):
                if i <= (n+1)//2:
                    for j in range(((n+1)//2)-i):
                        print(' ',end='')
                    for j in range((2*(i))-1):
                        print('*',end='')
                    print()
                else:
                    for j in range(i-(n+1)//2 ):
                        print(' ',end='')
                    for j in range(2*(n-i+1)-1):
                        print('*',end='')                    
                    print()                        
        def ques15(n):
            for i in range(n):
                if i == 0 or i == n-1:
                    for j in range(n):
                        print('*',end='')
                else:
                    for k in range(n):
                        if k == 0 or k == n-1:
                            print('*',end='')
                        else:
                            print(' ',end='')
                print()
        def ques16(n):
            for i in range(n):
                for j in range(n):
                    if j == i:
                        print('$',end='')
                    elif j == 0 or i == 0 or j == n -1 or i == n- 1:
                        print('*',end='')
                    else:
                        print(' ',end='')
                print() 
        def ques17(n):
            for i in range(n):
                for j in range(n):
                    if j == i or j == n-i-1:
                        print('$',end='')
                    elif j == 0 or i == 0 or j == n -1 or i == n- 1:
                        print('*',end='')
                    else:
                        print(' ',end='')
                print()
        def ques18(n):
            set_pascal = [1]
            for i in range(1,n+1):
                for l in range(n-i):
                    print(' ',end='')
                set_pascal2 = set_pascal
                temp = [0] + set_pascal + [0]
                for k in range(len(set_pascal)):
                    print(set_pascal[k],end=' ')
                set_pascal2 = []
                for j in range(1,i+2):
                    set_pascal2 = set_pascal2 + [temp[j-1]+temp[j]]
                    set_pascal = set_pascal2
                print()
                    
        def ques19(n):
            for i in range(n):
                for j in range(n):
                    if  j == n-i-1:
                        print('*',end='')
                    elif i == 0  or i == n- 1:
                        print('*',end='')
                    else:
                        print(' ',end='')
                print()
    class textquestions:# this class is for all questions except pattern questions , questions 5 and 6  not included
        def ques1(n):
            assignment3.pattern_questions.ques18(n)
        def ques2(n):
            str_abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            for i in range(n):
                x = []
                for j in range(n-i):
                    print(str_abc[j],end='')
                    x = x + [str_abc[j]]
                for k in range(2*i):
                    print(' ',end='')
                for l in range(1,n-i+1):
                    print(x[-l],end='')
                print()
        def ques3(n):
            y = []
            for i in range(1,n+1):
                x=0
                for j in range(1,i+1):
                    if j == i or j == 1:
                        continue
                    else:
                        if i%j == 0:
                            x= 1
                            break
                if x != 1:
                    print(i)
                    y = y + [j]
                else:
                    continue
            print()
            print(f'The sum of all prime numbers is:{sum(y)}')
        def ques4(n):# 12,13,14,23,24,34
            set = []
            for i in range(1,n+1):
                set = set + [i]
            for j in range(2**n):
                print()
        def ques5(n):
            for i in range(1,n+1):
                x = []
                y = 0
                while i > 0:
                    if i > 900 :
                        y = 1000
                        if i < 1000:
                            x = x + ['C']
                            y = 900
                        x = x + ['M']
                    elif i >= 400:
                        y = 500
                        if i < 500:
                            x = x + ['C']
                            y = 400
                        x = x + ['D'] 
                    elif i >= 90:
                        y = 100
                        if i < 100:
                            x = x + ['X']
                            y = 90
                        x = x + ['C']
                    elif i >= 40:
                        y = 50
                        if i < 50:
                            x = x + ['X']
                            y = 40
                        x = x +['L']
                    elif i >= 9:
                        y = 10
                        if i < 10:
                            x = x + ['I']
                            y = 9
                        x = x + ['X']
                    elif i >= 5:
                        y = 5
                        if i < 5:
                            x = x + ['I']
                            y = 4
                        x = x +['V']
                    elif i < 4:
                        y = 1
                        x = x + ['I']
                    else:
                        print('max limit is 1000')
                    i = i - y
                for k in range(len(x)):
                    print(x[k])
        def ques6(n):
            x=[]
            for i in range(1,n+1):
                k=i
                for j in range(1,i+1):
                    k = k*j
                x = x + [i/k]
                if i == n:
                    print(f'The Factorial of n is: {k}')
            print()
            z = sum(x) + 1
            print(f'The sum of the division of the numbers and their factorial till n is {z}')
        def ques7(n):
            for i in range(1,n+1):
                if i > 9:
                    x = str(i)
                    y = []
                    for j in range(len(x)):
                        y = y + [int(x[j])**3]
                    if sum(y) == i:
                        print(i)
                    else:
                        continue
        def ques8(dec_num):
            print(f'\nBinary Number: {bin(dec_num)}')
            print(f'\nOctal Number: {oct(dec_num)}')
            print(f'\nHexaDecimal Number: {hex(dec_num)}')

class test_questions: # this is completely unnecessary but just a testing code to try all questions out. 
    print('\n\n=======================================')
    ques_number = int(input('I want to print question number '))
    if ques_number == 1:
        part_number = int(input('Question no.1, part '))
        input_num = int(input('Number of Rows I want '))
        if part_number == 1:
            assignment3.pattern_questions.ques1(input_num)
        elif part_number == 2:
            assignment3.pattern_questions.ques2(input_num)
        elif part_number == 3:
            assignment3.pattern_questions.ques3(input_num)
        elif part_number == 4:
            assignment3.pattern_questions.ques4(input_num)
        elif part_number == 5:
            assignment3.pattern_questions.ques5(input_num)
        elif part_number == 6:
            assignment3.pattern_questions.ques6(input_num)
        elif part_number == 7:
            assignment3.pattern_questionsonsons.ques7(input_num)
        elif part_number == 8:
            assignment3.pattern_questions.ques8(input_num)
        elif part_number == 9:
            assignment3.pattern_questionsons.ques9(input_num)
        elif part_number == 10:
            assignment3.pattern_questions.ques10(input_num)
        elif part_number == 11:
            assignment3.pattern_questions.ques11(input_num)
        elif part_number == 12:
            assignment3.pattern_questionsonsonsonsons.ques12(input_num)
        elif part_number == 13:
            assignment3.pattern_questions.ques13(input_num)
        elif part_number == 14:
            assignment3.pattern_questions.ques14(input_num)            
        elif part_number == 15:
            assignment3.pattern_questionsons.ques15(input_num)
        elif part_number == 16:
            assignment3.pattern_questions.ques16(input_num)
        elif part_number == 17:
            assignment3.pattern_questions.ques17(input_num)
        elif part_number == 18:
            assignment3.pattern_questions.ques18(input_num)
        elif part_number == 19:
            assignment3.pattern_questions.ques19(input_num)
        else:
            print('input error')
    elif ques_number == 2:
        input_num = int(input('Number of Rows you want '))
        assignment3.textquestions.ques1(input_num)
    elif ques_number == 3:
        input_num = int(input('Number of Rows you want '))
        assignment3.textquestions.ques2(input_num)
    elif ques_number == 4:
        input_num = int(input('Number of Numbers: '))
        assignment3.textquestions.ques3(input_num)        
    elif ques_number == 5:
        input_num = int(input('set length: '))
        assignment3.textquestions.ques4(input_num)  
    elif ques_number == 6:
        input_num = int(input('Print Roman Numeral till: '))
        assignment3.textquestions.ques5(input_num)  
    elif ques_number == 7:
        input_num = int(input('n: '))
        assignment3.textquestions.ques6(input_num)  
    elif ques_number == 8:
        input_num = int(input('Print Armstrong Numbers till: '))
        assignment3.textquestions.ques7(input_num)  
    elif ques_number == 9:
        input_num = int(input('Enter Decimal Number: '))
        assignment3.textquestions.ques8(input_num)  
    else:
        print('input error')
    print('\n\n=======================================')