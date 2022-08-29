import random
def list():
 ac = ""

 for i in range(6):
     a = random.randint(0, 9)
     ac += str(a)
 print(ac)

ac = list()
def fun(y):
    eac=input()
    if y==eac:
        print ("some")
    else:
        print("nothing")
fun(ac)