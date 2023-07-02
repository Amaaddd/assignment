class A:
    def __init__(self, a, b, c):
        self.a = a
        self._b = b
        self.__c = c

    def display(self):
        try:
            print("This is class A")
            print("Public variable:", self.a)
            print("Private variable:", self._b)
            print("Protected variable:", self._A__c)
        except AttributeError:
            print("Cannot access private variables in class A")

class B(A):
    def display(self):
        print("This is class B")
        print("Public variable:", self.a)
        print("Private variable:", self._b)
        try:
            print("Protected variable:", self._A__c)
        except AttributeError:
            print("Cannot access private variables in class B")

x = A(4, 5, 6)
x.display()
y = B(7, 8, 9)
y.display()