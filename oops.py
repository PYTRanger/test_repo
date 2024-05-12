# oject oreinted programming in python classes and everything

#classes and object


class Person:
    name ='Meyank'
    age = 17
    occ = 'Trader'
    Height = 21
    networth = 500
    def info(self):
        print(f'{self.name} is a {self.occ}')
        


a = Person()
a.info()


x = Person()
x.name = 'Kunal'
x.info()


