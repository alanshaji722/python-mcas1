#Alan Shaji
#21MCA002


class Publisher:
    def __init__(self,name):
        self.name=name

    def display(self):
        print('Name:',self.name)
class Book(Publisher):
    def __init__(self,title,author):

        self.title=title
        self.author=author

class Python(Book):
    def __init__(self,name,title,author,price,noofpage):
        self.price=price
        self.noofpage=noofpage

        Publisher.__init__(self,name)
        Book.__init__(self, title, author)

    def display(self):
        print('Book Title:',self.title,'\n Author:',self.author,'\nPrice :',self.price,'\n No Of Pages:',self.noofpage)



n=input("Enter book name")
t=input("title")
a=input("author")
p=int(input("price"))
np=int(input("pages"))

p = Python(n,t,a,p,np)
p.display()
