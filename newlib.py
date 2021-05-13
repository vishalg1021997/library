#aaj apun banaeyga library

class book:
    def __init__(self,id,title,author,type,price,status):
        self.book_id = id
        self.book_title = title
        self.book_author = author
        self.book_type = type
        self.book_price = price
        self.book_status = status
        self.book_details = [self.book_id,self.book_title,self.book_author,self.book_type,self.book_price,self.book_status]

class library:
    def __init__(self,book_list):
        self.book_list = book_list
        #print(self.book_list)

    def issue(self,title,type):
        self.title = title
        self.type = type
        for i in self.book_list:
            if i[1] == self.title and i[3] == self.type and i[5] == 'available':
                i[5] = 'unavailable'
                for j in self.book_list:
                    print(j[1] + "--->" + j[5])
                break
        else:
            print("Book Not Found")

    def costly(self,author):
        maxi = [0]
        self.author = author
        for i in self.book_list:
            if i[2] == author:
                maxi.append(i[4])
        if max(maxi) == 0:
            print("Author Not Found")
        else:
            print(max(maxi))

n = int(input())
l = []
while(n > 0):
    id = int(input())
    title = input().lower()
    author = input().lower()
    type = input().lower()
    price = int(input())
    status = input().lower()
    obj = book(id,title,author,type,price,status)
    l1 = obj.book_details
    l.append(l1)
    n = n - 1

obj1 = library(l)
title = input().lower()
type = input().lower()
author = input().lower()
obj1.issue(title,type)
obj1.costly(author)

# 101 to kill a mockingbird harper lee novel 120 available
# 102 one hundered years of solitude gabriel garcia marquez novel 100 unavailable
# 103 go set a watchman harper lee novel 200 available
# 104 python programming reema thareja programming 150 available
# 105 let us c++ yashavant kanetkar programming 300 available