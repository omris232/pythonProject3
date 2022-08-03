def dog ():
    name = (input("enter a dog name"))
    age = int(input("enter a dog age "))
    age7=age*7
    dog="dog name: " +name+", age:"+str(age7)
    return dog


def friend ():
    friens=[]
    for i in range (5):
        f1=(input("enter a friend name"))
        friens.append(f1)
    f2=(input("enter another friend name"))
    boolean = "True"
    for i in friens:
        if f2==i:
            boolean="True"
        else:
            boolean = "False"

    if boolean=="True":
        print("the last friend is exist")
    else:
        print("the last friend are not exist")
    return friens

def nazzeret():
    x = int(input("enter a num:"))
    c=x
    a = 1
    while (x > 1):
        a = a * x
        #print(a)
        x = x - 1
    return "Azzeret of "+str(c)+" is: "+str(a)




def menu():
    choose = int(input("menu:\n 1.Dog details\n 2.Friens list\n 3.N azzeret\n 4.Exit \nWhat is your choice:"))
    while (True):
        if choose == 1:
            print(dog())
            return menu()
        elif choose == 2:
            print(friend())
            return menu()
        elif choose == 3:
            print(nazzeret())
            return menu()
        elif choose == 4:

            exit = input("do you want bto exit y/n? ")
            if exit == "y":
                break
            else:
                return menu()
        else:
            print("choose 1-3 only!!!")
            return menu()

    return "bye bye..."

print(menu())
