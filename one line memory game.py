import random
arr1 =[1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0] 
arr2 =['a','a','b','b','c','c','d','d','e','e','f','f','g','g','h','h','i','i','j','j']
arr3 = []
s1=0
s2=0
c=1
a=0
random.shuffle(arr2)
while True:
        try:
                while True:    
                    if (c%2==1):
                        print("welcome : "+str(arr1))    
                        print("player#1_score"+str(s1))
                        x = list(input("enetr two number : ").split(" "))
                        num1=int(x[0])
                        num2=int(x[1])
                        if (num1 in arr3 or num2 in arr3):
                                print("they has been selected")
                                break
                        if (num1 >20 or num2 >20) or (num1 <= 0 or num2 <=0):
                                print ('choose number from 1:20')
                                break
                        elif (num1 == num2 ):
                                print ('error try number')
                                break
                        elif (num1<=20 and num2<=20 ):
                                arr1[num1-1]=arr2[num1-1]
                                arr1[num2-1]=arr2[num2-1]
                                print(arr1)
                                c=c+1
                        if (arr2[num1-1]!=arr2[num2-1]):
                                        if( num1>9 and num2>9):
                                                if(num1==20 and num2<20):
                                                        arr1[num1-1]=num1-20
                                                        arr1[num2-1]=num2-10
                                                elif(num1==20 and num2==20):
                                                        arr1[num1-1]=num1-20
                                                        arr1[num2-1]=num2-20
                                                elif(num1<20 and num2==20):
                                                        arr1[num1-1]=num1-10
                                                        arr1[num2-1]=num2-20
                                                else:
                                                        arr1[num1-1]=num1-10
                                                        arr1[num2-1]=num2-10
                                        elif(num1<=9 and num2<=9):
                                                arr1[num1-1]=num1
                                                arr1[num2-1]=num2
                                        elif(num1> 9):
                                                if (num1==20):
                                                        arr1[num1-1]=num1-20
                                                        arr1[num2-1]=num2
                                                else:
                                                        arr1[num1-1]=num1-10
                                                        arr1[num2-1]=num2
                                        elif(num2>9):
                                                if num2==20:
                                                        arr1[num1-1]=num1
                                                        arr1[num2-1]=num2-20
                                                else:
                                                        arr1[num1-1]=num1
                                                        arr1[num2-1]=num2-10
                        if (arr2[num1-1] == arr2[num2-1]):
                                s1=s1+1
                                arr2[num1-1] = "*"
                                arr2[num2-1] = "*"
                                arr1[num1-1] = "*"
                                arr1[num2-1] = "*"
                                arr3.append (num1)
                                arr3.append (num2)
                                print(arr1)
                                if s1>s2 and arr2==["*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*"] :
                                        print("player 1 win")
                                        a=1
                                        break
                                elif s2>s1 and arr2==["*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*"] :
                                        print("player 2 win")
                                        a=1
                                        break
                                elif s2==s1 and arr2==["*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*"] :
                                        print("draw")
                                        a=1
                                        break
                    if (c%2==0):
                        print("welcome : "+str(arr1))    
                        print("player2#_score"+str(s2))
                        y=list(input("enter two number : ").split(" "))
                        num1=int(y[0])
                        num2=int(y[1])
                        if (num1 in arr3 or num2 in arr3):
                                print("they has been selected")
                                break
                        elif (num1 >20 or num2 >20) or (num1 <= 0 or num2 <=0):
                                print ('choose number from 1:20')
                                break
                        elif (num1 == num2 ):
                                print ('error try number')
                                break
                        elif (num1<=20 and num2<=20 ):
                                arr1[num1-1]=arr2[num1-1]
                                arr1[num2-1]=arr2[num2-1]
                                print(arr1)
                                c=c+1
                                if (arr2[num1-1]!=arr2[num2-1]):
                                        if( num1>9 and num2>9):
                                                if(num1==20 and num2<20):
                                                        arr1[num1-1]=num1-20
                                                        arr1[num2-1]=num2-10
                                                elif(num1==20 and num2==20):
                                                        arr1[num1-1]=num1-20
                                                        arr1[num2-1]=num2-20
                                                elif(num1<20 and num2==20):
                                                        arr1[num1-1]=num1-10
                                                        arr1[num2-1]=num2-20
                                                else:
                                                        arr1[num1-1]=num1-10
                                                        arr1[num2-1]=num2-10
                                        elif(num1<=9 and num2<=9):
                                                arr1[num1-1]=num1
                                                arr1[num2-1]=num2
                                        elif(num1> 9):
                                                if (num1==20):
                                                        arr1[num1-1]=num1-20
                                                        arr1[num2-1]=num2
                                                else:
                                                        arr1[num1-1]=num1-10
                                                        arr1[num2-1]=num2
                                        elif(num2>9):
                                                if num2==20:
                                                        arr1[num1-1]=num1
                                                        arr1[num2-1]=num2-20
                                                else:
                                                        arr1[num1-1]=num1
                                                        arr1[num2-1]=num2-10
                                if (arr2[num1-1] == arr2[num2-1]):
                                        s2=s2+1
                                        arr2[num1-1] = "*"
                                        arr2[num2-1] = "*"
                                        arr1[num1-1] = "*"
                                        arr1[num2-1] = "*"
                                        arr3.append(num1)
                                        arr3.append(num2)
                                        print(arr1)
                                        if s1>s2 and arr2==["*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*"] :
                                                print("player 1 win")
                                                a=1
                                                break
                                        elif s2>s1 and arr2==["*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*"] :
                                                print("player 2 win")
                                                a=1
                                                break
                                        elif s2==s1 and arr2==["*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*"] :
                                                print("draw")
                                                a=1
                                                break
           
        except: 
                print("choose number again")
        if a==1 :
                break
        

