#rohit-joseph 

from add import add1
from sub import sub1
from mul import mul1
from div import div1

flag = 0
while flag == 0:
    
    try:
        oper = str(input("Enter any operation:: \naddition(add) \nsubstraction(sub) \nmultiplication(mul) \ndivision(div):: "))
        value_1 = float(input("Enter 1st number: ")) 
        value_2 = float(input("Enter 2nd number: "))

        if oper=="add":
            add_result=add1(value_1,value_2)
            print(f" {value_1} + {value_2} is: {add_result}")
            flag=1
        elif oper=="sub":
            sub_result=sub1(value_1,value_2)
            print(f" {value_1} - {value_2} is: {sub_result}")
            flag=1
        elif oper=="mul":
            mul_result=mul1(value_1,value_2)
            print(f" {value_1} * {value_2} is: {mul_result}")
            flag=1
        elif oper=="div":
            div_result=div1(value_1,value_2)
            # print(f" {value_1} / {value_2} is: {div_result}")
            flag=0
        else:
            print("Plz Enter a Operation!!!")
                    
    except:
        print("!!!Plz enter a valid input!!!")
