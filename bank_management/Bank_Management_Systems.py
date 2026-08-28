import json
import random
import string
from pathlib import Path


class Bank:

    database = 'bank_management\\data.json'
    data = []

    try:
        if Path(database).exists():
            with open(database, "r") as fs:
                data = json.loads(fs.read())
        else:
            print("No Such File Exists.")

    except Exception as err:
        print(f"An exception occurred: {err}")

    @classmethod
    def update(cls):
        with open(cls.database, 'w') as fs:
            fs.write(json.dumps(cls.data, indent=4))

    @classmethod
    def __accountgenerate(cls):
        alpha = random.choices(string.ascii_letters, k=3)
        num = random.choices(string.digits, k=3)
        spchar = random.choices("!@#$%^&*", k=1)

        account_id = alpha + num + spchar

        random.shuffle(account_id)

        return "".join(account_id)

    @classmethod
    def createaccount(cls):

        info = {
            "Name": input("Tell Your Name: "),
            "Age": int(input("Enter Your Age: ")),
            "Email": input("Tell Your Email: "),
            "Pin": input("Tell Your Pin: "),
            "account No": cls.__accountgenerate(),
            "Balance": 0
        }

        if info["Age"] < 18:
            print("Sorry, you cannot create an account.")
            return

        if len(info["Pin"]) != 4 or not info["Pin"].isdigit():
            print("PIN must contain exactly 4 digits.")
            return

        print("\nAccount has been created successfully!\n")

        for i in info:
            print(f"{i}: {info[i]}")

        print("\nPlease note down your Account Number.")

        cls.data.append(info)
        cls.update()


    def depositmoney():
        accnumber=input("please tell your account number.")
        pin =int(input("Enter your pin"))


        for i in Bank.data:
            print(i.keys())

        userdata=[
            i for i in Bank.data if i.get('Account No')== accnumber
            and str(i.get('Pin'))==str(pin)
        ] 

        if not userdata:
            print("sorry no data found .")

        else:
            amount=int(input("how much money you want to deposit."))
            if amount>10000 or amount < 0:
                print("sorry the amount is too much you can deposit below 10000")        

            else:
                print(userdata)
                userdata [0]['Balance'] += amount
                print(f"{amount} deposited successfully.")
                print(f"your new balance is {userdata[0]['Balance']}")
                Bank.update()
    
    def withdrawmoney():
        accnumber=input("please tell your account number.")
        pin =int(input("Enter your pin"))

        for i in Bank.data:
            print(i.keys())

        userdata=[
            i for i in Bank.data if i.get('Account No')== accnumber
            and str(i.get('Pin'))==str(pin)
        ] 

        if not userdata:
            print("sorry no data found .")

        else:
            amount=int(input("how much money you want to withdraw."))
            if userdata[0]['Balance'] <amount :
                print("sorry  you do not have that much money .")        

            else:
                print(userdata)
                userdata [0]['Balance'] -= amount
                print(f"{amount} withdraw successfully.")
                print(f"your new balance is {userdata[0]['Balance']}")
                Bank.update()            

    def showdetails():
        accnumber = input ("please tell your account number .")
        pin = input("tell your pin .")
    
        userdata = [
                i for i in Bank.data
                if i.get('Account No') == accnumber
                and i.get('Pin') == pin
            ]
        
        print("your information are \n\n\n")

        if userdata:
            for i in userdata[0]:
                print(i, ":", userdata[0][i])
        else:
           print("No account found with this account number.")



    def updatedetails():
        accnumber = input ("please tell your account number .")
        pin = input("tell your pin .")
        userdata = [
                i for i in Bank.data
                if i.get('Account No') == accnumber
                and i.get('Pin') == pin
            ]         
        if userdata== False:
            print("No Such User Found.")

        else:
            print("you cannot change age ,account number ,balance ")

            print("Fill The details for change or leave it empty if no change .") 

            newdata = {
                "name": input("please tell your new name or press enter "),
                "email":input("please tell your new email or press enter to skip."),
                "pin":input("enter new pin or press enter to skip ")
            } 
            if newdata["name"]=="": 
                newdata["name"]==userdata[0].get('name')   
            if newdata["email"]=="": 
                newdata["email"]==userdata[0].get('email')
            if newdata["pin"]=="": 
                newdata["pin"]==userdata[0].get('pin')
            


            if  type (newdata['pin']) == str :
                newdata['pin']= int(newdata['pin'])

            for i in newdata:
                if newdata[i] == userdata[0].get(i):
                    continue
                else:
                    userdata[0][i]=newdata[i]


            Bank.update()
            print("details updated successfully.") 
    def delete():
        accnumber = input ("please tell your account number .")
        pin = input("tell your pin .")

        userdata = [
                i for i in Bank.data
                if i.get('Account No') == accnumber
                and i.get('Pin') == pin
            ] 

        if userdata == False:
            print("Sorry no such data exist.")

        else:
            check = input("press y if you actually delete your acount or press n")
            if check == 'n'or check == "N": 
                print("bypassed")

            else:
                index=Bank.data.index(userdata[0])
                Bank.data.pop(index)
                print("Account deleted successfully.")
                Bank.update()
       

user = Bank

print("1. Create An Account")
print("2. Deposit Money In The Bank")
print("3. Withdraw Money")
print("4. Details")
print("5. Update Details")
print("6. Delete Your Account")

check = int(input("Tell Your Response: "))

if check == 1:
    user.createaccount()

if check == 2:
    user.depositmoney()

if check == 3:
    user.withdrawmoney() 

if check == 4:
    user.showdetails() 

if check ==5:
    user.updatedetails() 

if check ==6:
    user.delete()    