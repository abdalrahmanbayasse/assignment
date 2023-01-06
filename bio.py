def get_data ():
        name = input('Enter item name')
        price = int (input ('Enter price'))
        quantity = int (input ('Enter quantity'))
        total_money = int(input('Enter total money '))
        save_data (name  , price ,quantity,total_money)

def calculatepayment(price ,quantity,total_money):
    price = price * quantity
    return_money= total_money-price 
    return return_money

def save_data(name, price ,quantity,total_money):
        data= open ('data.txt','r+')
        return_money= calculatepayment(price ,quantity,total_money)
        listData = [name,price ,quantity,total_money,return_money]
        data.write(str(listData))
        showdata(data,listData)

def showdata(data,listData):
     print (data.readlines())
     print (listData[4])

get_data()
