class Company():
    def __init__(self,name):
        self.name = name
        self.status = True
    def program(self):
        choice = self.menuchoice()
        if choice == 1:
            self.addworker()
        if choice == 2:
            self.dismissworker()
        if choice == 3:
            manner = input('Would you like to see salaries must be given per year ?(y/n)')
            if manner == 'y':
                self.showtotalsalaries('y')
            else:
                self.showtotalsalaries()

        if choice == 4:
            self.givesalaries()
        if choice == 5:
            self.showbudget()
        if choice == 6:
            self.increasebudget()
        if choice == 7:
            self.decreasebudget()
        if choice == 8:
            self.exitsystem()
    def menuchoice(self):
        choice = int(input('**** Welcome {} company ****\nChoose an option please\n\n1)Add worker\n2)Dismiss worker\n3)Show salaries\n4)Give salaries\n5)Show budget\n6)Increase budget\n7)Decrease budget\n8)Exit system'.format(self.name)))
        while choice < 1 or choice > 8:
            choice = int(input('Please enter a number between (1-8)'))
        return choice
    def addworker(self):
        with open('workers.txt','r') as document:
            workers = document.readlines()
        if len(workers) == 0:
            id = 1
        else:
            id = int(workers[-1].split(')')[0]) + 1

        name = input('Enter worker\'s name :').lower().capitalize()
        surname = input('Enter worker\'s surname :').lower().capitalize()
        gender = input('Enter worker\'s gender :').lower().capitalize()
        salary = int(input('Enter worker\'s salary :'))
        with open('workers.txt','a') as document:
            document.write('{}){}-{}-{}-{}\n'.format(id,name,surname,gender,salary))
        print('The new worker was added !')
    def dismissworker(self):
        with open('workers.txt','r') as document:
            workers = document.readlines()
        cworkers = list()
        for worker in workers:
            cworkers.append(" ".join(worker.split('-')))

        for worker in cworkers:
            print(worker)

        selectedworker = int(input('Enter the number of worker you want to delete : '))
        workers.pop(selectedworker-1)
        counter = 1
        changedworkers = list()
        for worker in workers:
            changedworkers.append('{}){}'.format(counter,worker.split(')')[1]))
            counter += 1
        with open('workers.txt','w') as document:
            document.writelines(changedworkers)
        print('The selected worker was dismissed !')
    def showtotalsalaries(self,parameter='m'):
        with open('workers.txt','r') as document:
            workers = document.readlines()
        salaries = list()
        for worker in workers:
            salaries.append(int(worker.split('-')[-1]))
        if parameter == 'm':
            print('The amount of salary per month is : {}'.format(sum(salaries)))
        else:
            print('The amount of salary per year is : {}'.format(12*sum(salaries)))
    def givesalaries(self):
        with open('budget.txt','r') as document:
            budget = int(document.read())

        with open('workers.txt','r') as document:
            workers = document.readlines()

        salaries = list()

        for worker in workers:
            salaries.append(int(worker.split('-')[-1]))

        budget = budget - sum(salaries)

        with open('budget.txt','w') as document:
            document.write(str(budget))

        print('The salaries were given !')
    def showbudget(self):
        with open('budget.txt','r') as document:
            budget = int(document.read())
        print('The current budget is : {}'.format(budget))

    def increasebudget(self):
        reason = input('Enter the reason : ')
        amount = int(input('Enter the amount : '))
        with open('incomes.txt','r') as document:
            incomes = document.readlines()

        if len(incomes) == 0:
            id = 1
        else:
            id = int(incomes[-1].split(')')[0]) + 1

        with open('incomes.txt','a') as document:
            document.write('{}){}-{}\n'.format(id,reason,amount))

        with open('budget.txt','r') as document:
            budget = int(document.read())

        budget = budget + amount

        with open('budget.txt','w') as document:
            document.write(str(budget))

        print('The income was added to the list !')
    def decreasebudget(self):
        reason = input('Enter the reason : ')
        amount = int(input('Enter the amount : '))
        with open('damages.txt','r') as document:
            damages = document.readlines()

        if len(damages) == 0:
            id = 1
        else:
            id = int(damages[-1].split(')')[0]) + 1

        with open('damages.txt','w') as document:
            document.write('{}){}-{}\n'.format(id,reason,amount))

        with open('budget.txt','r') as document:
            budget = int(document.read())

        budget = budget - amount

        with open('budget.txt','w') as document:
            document.write(str(budget))

        print('The damage was added to the list !')
    def exitsystem(self):
        self.status = False


mycompany = Company('BSecurity')

while mycompany.status:
    mycompany.program()