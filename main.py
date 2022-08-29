import random
import mysql.connector

mydb=mysql.connector.connect(host='localhost',user='root',password='root',database='BANK_MANAGEMENT_SYSTEM')

ac=""
def OpenAcc(ac):
    n=input("Enter the Name")
    for i in range(6):
        a = random.randint(0, 9)
        ac += str(a)
    print(ac)
    db=input("Enter the Date of Birth")
    add=input("Enter the Address")
    cn=input("Enter the contact Number")
    ob=int(input("Enter the opening balance: "))
    data1=(n,ac,db,add,cn,ob)
    data2=(n,ac,ob)
    sql1=('insert into account values (%s,%s,%s,%s,%s,%s)')
    sql2=('insert into amount values(%s,%s,%s)')
    x=mydb.cursor()
    x.execute(sql1,data1)
    x.execute(sql2,data2)
    mydb.commit()
    print("Data Entered Successfully")
    main()

def DepoAmo():
    amount=input("Enter the amount you want to deposit: ")
    ac=input("Enter your account number which wae generated")
    a='select balance from amount where AccNo=%s'
    data=(ac,)
    x=mydb.cursor()
    x.execute(a,data)
    result=x.fetchone()
    t=result[0]+amount
    sql=('updata amount set balance where AccNo=%s')
    d=(t,ac)
    x.execute(sql,d)
    mydb.commit()
    main()

def WithdrawAmout():
    amount = input("Enter the amount you want to withdraw: ")
    ac = input("Enter your account number which wae generated")
    a = 'select balance from amount where AccNo=%s'
    data = (ac,)
    x = mydb.cursor()
    x.execute(a, data)
    result = x.fetchone()
    t = result[0] - amount
    sql = ('updata amount set balance where AccNo=%s')
    d = (t, ac)
    x.execute(sql, d)
    mydb.commit()
    main()

def BalEnq():
    ac=input("Enter the account no")
    a='select * from amount where AccoNo=%s'
    data=(ac,)
    x=mydb.cursor()
    x.execute(a,data)
    result=x.fetchone()
    print(f"Balance for account: {ac} is {result[-1]}")
    main()

def DisDetails():
    ac = input("Enter the account no")
    a = 'select * from account where AccoNo=%s'
    data = (ac,)
    x = mydb.cursor()
    x.execute(a, data)
    result = x.fetchone()
    for i in result:
        print(i)
    main()

def CloseAcc():
    ac = input("Enter the account no")
    sql1='delete from account where AccNo=%s'
    sql2='delete from amount where AccoNo=%s'
    data=(ac,)
    x=mydb.cursor()
    x.execute(sql1,data)
    x.execute(sql2,data)
    mydb.commit()
    main()



def main():
    print('''
             1. OPEN ACCOUNT
             2. DEPOSITE AMOUNT
             3. WITHDRAW AMOUNT
             4. BALANCE ENQUIRY
             5. DISPLAY CUSTOMER DETAILS
             6. CLOSE AN ACCOUNT''')
    choice = input("Enter Any number to perform your task: ")
    if (choice=="1"):
        OpenAcc()
    elif (choice=="2"):
        DespoAmo()
    elif (choice=="3"):
        WithdrawAmount()
    elif (choice=="4"):
        BalEnq()
    elif (choice=="5"):
        DisDetails()
    elif (choice=="6"):
        CloseAcc()
    else:
        print("Invalid choice")
        main()
main()


