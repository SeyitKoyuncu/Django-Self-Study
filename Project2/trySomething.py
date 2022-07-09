
class deneme():
    print(10)

    def func():
        print(20)
        return 20
    
    def func2(self):
        print(30)
        return 30

    @staticmethod
    def func3():
        print(40)
        return 40



a = deneme
print(a)
b = None
b = a.func()
print(f'b = {b}')

c = deneme()
print(c)
d = None
d = c.func2()
print(f'd = {d}')


e = deneme()
print(e)
f = None
f = e.func2()
print(f'd = {f}')