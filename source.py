import math
class MathOperations:
    def display(self):
        print("Type (1) for Trigonometry and (2) for Arithmetic")
        choice=int(input("Enter your choice: "))
        if choice==1:
            def trig():
                print("1) Sine \n2) Cosine \n3) Tangent \n4) Arc Sine \n5) Arc Cosine \n6) Arc Tangent \n")
                num=int(input("Enter your choice: "))
                if num==1:
                    def sine():
                        a=int(input("Enter num: "))
                        print(math.sin(a))
                    sine()
                elif num==2:
                    def cosine():
                        a=int(input("Enter num: "))
                        print(math.cos(a))
                    cosine()
                elif num==3:
                    def tang():
                        a=int(input("Enter num: "))
                        print(math.tan(a))
                    tang()
                elif num==4:
                    def arcs():
                        a=int(input("Enter num: "))
                        print(math.asin(a))
                    arcs()
                elif num==5:
                    def arcc():
                        a=int(input("Enter num: "))
                        print(math.acos(a))
                    arcc()
                elif num==6:
                    def arct():
                        a=int(input("Enter num: "))
                        print(math.atan(a))
                    arct()
            trig()

        else:
            def arith():
                print("1) Addition \n2) Subtraction \n3) Multiplication \n4) Division \n5) Square root \n")
                num=int(input("Enter your choice: "))
                if num==1:
                    def add():
                        a=int(input("Enter num1: "))
                        b=int(input("Enter num2: "))
                        print(a + b)
                    add()
                elif num==2:
                    def subtract():
                        a=int(input("Enter num1: "))
                        b=int(input("Enter num2: "))
                        print(a - b)
                    subtract()
                elif num==3:
                    def multiply():
                        a=int(input("Enter num1: "))
                        b=int(input("Enter num2: "))
                        print(a * b)
                    multiply()
                elif num==4:
                    def divide():
                        a=int(input("Enter num1: "))
                        b=int(input("Enter num2: "))
                        if b == 0:
                            raise ZeroDivisionError("Cannot divide by zero")
                        else:
                            print(a / b)
                    divide()
                elif num==5:
                    def square_root():
                        a=int(input("Enter num1: "))
                        b=int(input("Enter num2: "))
                        if a < 0:
                            raise ValueError("Cannot calculate square root of a negative number")
                        print("Square root of num1 is:",math.sqrt(a))
                        print("Square root of num2 is:",math.sqrt(b))
                    square_root()
            arith()