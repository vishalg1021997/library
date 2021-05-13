#aaj apun banaeyga library
class book:
    def __init__(self,id,title,author,type,price,status):
        self.book_id = id
        self.book_title = title
        self.book_author = author
        self.book_type = type
        self.book_price = price
        self.book_status = status
        
class library:
    def __init__(self,book_list):
        self.book_list = book_list

    def issue(self,title,type):
        for i in self.book_list:
            if i.book_title ==title and i.book_type == type and i.book_status == 'available':
                i.book_status = 'unavailable'
                return True
        else:
            return False

    def costly(self,author):
        maxi = 0
        maxtitle = None
        for i in self.book_list:
            if i.book_author == author:
                if i.book_price > maxi:
                    maxi=i.book_price
                    maxtitle=i
        if maxtitle == None:
            return None
        else:
            return maxtitle

n = int(input())
l = []
while(n > 0):
    id = int(input())
    title = input().lower()
    author = input().lower()
    #print(author)
    type = input().lower()
    price = int(input())
    status = input().lower()
    obj = book(id,title,author,type,price,status)
    #l1 = obj.book_details
    l.append(obj)
    n = n - 1

obj1 = library(l)
title = input().lower()
type = input().lower()
author = input().lower()
a1=obj1.issue(title,type)
a2=obj1.costly(author)

if a1==False:
    print('Book not found')
else:
    for i in l:
        print(i.book_title,'-->',i.book_status)

if a2==None:
    print('Author not found')
else:
    print(a2)
# 101 to kill a mockingbird harper lee novel 120 available
# 102 one hundered years of solitude gabriel garcia marquez novel 100 unavailable
# 103 go set a watchman harper lee novel 200 available
# 104 python programming reema thareja programming 150 available
# 105 let us c++ yashavant kanetkar programming 300 available
