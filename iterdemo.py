class Employee:
    def __init__(self,name,email):
        self.name=name
        self.email=email
        self.current=name

    def __iter__(self):
        return self

    def __next__(self):
        i=0
        while i in range(1,11):
            i=i+1
            return i

e1=Employee("Nitin","nitinb@meditab.com")

for i in e1:
    print(i)
import collections
if type(e1) == collections.Iterable:
    print(type(e1))
    