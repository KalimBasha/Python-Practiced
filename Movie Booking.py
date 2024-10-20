def singleTonClass(arg):
    L=[]
    def inner():
        if len(L)==0:
            L.append(arg())
        return L[0]
    return inner

@singleTonClass
class Mankatha():
    def __init__(self):
        self.maxtickets=275
    def booking(self):
        Ticket=int(input("Enter the no of tickets:"))
        if Ticket<=self.maxtickets:
            self.maxtickets -= Ticket
            print('Tickets Booked raa thambii...')
            print(f'Available tickets {self.maxtickets}')
        else:
            print('Tickets not available')

@singleTonClass
class Dheena():
    def __init__(self):
        self.maxtickets=275
    def booking(self):
        Ticket=int(input("Enter the no of tickets:"))
        if Ticket<=self.maxtickets:
            self.maxtickets -= Ticket
            print('Tickets Booked raa thambii...')
            print(f'Available tickets {self.maxtickets}')
        else:
            print('Tickets not available')

@singleTonClass
class Attagasam():
    def __init__(self):
        self.maxtickets=275
    def booking(self):
        Ticket=int(input("Enter the no of tickets:"))
        if Ticket<=self.maxtickets:
            self.maxtickets -= Ticket
            print('Tickets Booked raa thambii...')
            print(f'Available tickets {self.maxtickets}')
        else:
            print('Tickets not available')

def payTM():
    print('Available Movies are:\n1)Mankatha \n2)Dheena \n3)Attagasam')
    choice = int(input('Enter the movie option:'))
    if choice == 1:
        obj = Mankatha()
        obj.booking()
    elif choice == 2:
        obj = Dheena()
        obj.booking()
    elif choice == 3:
        obj = Attagasam()
        obj.booking()

def BMyS():
    print('Available Movies are:\n1)Mankatha \n2)Dheena \n3)Attagasam')
    choice = int(input('Enter the movie option:'))
    if choice == 1:
        obj = Mankatha()
        obj.booking()
    elif choice == 2:
        obj = Dheena()
        obj.booking()
    elif choice == 3:
        obj = Attagasam()
        obj.booking()

payTM()
print('-'*20)
BMyS()
print('-'*20)
        
