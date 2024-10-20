#simple bank app
class IOB:
    IFSC  ='IOBA000012'
    Branch='Chengam'
    ROI   =0.07
    def __init__(self,name,gender,Aadhar,mobno,pin,Bal):
        self.name=name
        self.gender=gender
        self.Aadhar=Aadhar
        self.mobno=mobno
        self.pin=pin
        self.Bal=Bal
    def Deposit(self):
        count=0
        while count<3:
            if self.pin != self.Checkpin():
                print('Enter correct pin')
                count+=1
            else:
                Amount=int(input("Enter the amount to deposit :"))
                self.Bal+=Amount
                print(f'{Amount} credited successfully')
                print(f'Available balance :{self.Bal}')
                break
        else:
            print("Invalid pin number")
    def CheckBal(self):
        count=0
        while count<3:
            if self.pin != self.Checkpin():
                print('Enter correct pin')
                count+=1
            else:
                print(f'Available balance :{self.Bal}')
                break
        else:
            print("Invalid pin number")
    def Withdraw(self):
        count=0
        while count<3:
            if self.pin != self.Checkpin():
                print('Enter correct pin')
                count+=1
            else:
                Amount2=int(input("Enter the amount to withdraw :"))
                if Amount2 <= self.Bal:
                    self.Bal-=Amount2
                    print(f'{Amount2} debited from your bank account')
                    print(f'Available balance :{self.Bal}')
                    break
        else:
            print("Invalid pin number")
    def Changepin(self):
        count=0
        while count<3:
            if self.pin != self.Checkpin():
                print('Enter correct pin')
                count+=1
            else:
                self.pin=int(input('Enter a four digit PIN number:'))
                break
        else:
            print("Enter correct pin to change your pin")
    @staticmethod
    def Checkpin():
        Pin=int(input("Enter your pin:"))
        return Pin
    
user1=IOB('Kalim','Male',98761234,8098770080,9988,15000)
user2=IOB('Susmii','Female',567890987,2345679876,8776,25000)
user3=IOB('Arun','Male',764567645,6543234567,7989,50000)

user2.Deposit()
print('---')
user1.CheckBal()
print('---')
user3.Withdraw()
user3.Changepin()
print(user3.pin)


