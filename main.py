import pymongo
from tkinter import *


client=pymongo.MongoClient("mongodb://localhost:27017")
db=client['UserData']
collection=db['Users']




books=input("Enter the name of book : ")
quantity=input("Enter the number of books : ")
quantity=int(quantity)
price=input("Enter the price of one book : ")
price=int(price)
totalPrice=quantity*price
all={'BookName':books,'Quantity':quantity, 'PriceOf1Book':price, 'TotalCost':totalPrice}
collection.insert_one(all)

ch=input("enter 1 to view database and 2 to end program : ")
if ch=='1':
    for x in collection.find():
         print(x)

else:
    print("Program ended successfully")




