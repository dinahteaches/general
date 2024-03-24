

class Employee:
    EmpCount = 0

    def __init__(self,Name, Salary):
        print('Show how Constructor works')
        Employee.EmpCount +=1
        self.Name = Name
        self.Salary = Salary
        self.Project = 'Bench'
        self.Totalleaves = 18
        self.medicalleaves = 12
        self.selfappricalcount = 0
        self.selfappricalresponces = {}
    
    def employee_record(self):
        print('The employee name is', self.Name, 'and the yearly salary of the employee is',self.Salary * 12)
    
    def employee_count():
        print('The total number of Employee is', Employee.EmpCount)
    
    def currentproject(self):
        print('The current project',self.Project)

    def assignproject(self,new):
        self.Project = new
        print('Assigned to project',self.Project)
    
    def medileave(self,noofleaves):
        if self.medicalleaves<noofleaves:
            print("You don't have sufficient medical leaves")
        else:
            self.medicalleaves -= noofleaves
            print('Total medical leaves left are',self.medicalleaves)
    
    def casualleave(self,noofleaves):
        if self.Totalleaves<noofleaves:
            print("You don't have sufficient casual leaves")
        else:
            self.Totalleaves -= noofleaves
            print('Total casual leaves left are',self.Totalleaves)
    
    def selfapprical(self):
        self.selfappricalcount += 1
        appisalques = ['Do you feel you been successful during this evaluation period compared to last',
                       'Do you feel you have completed you tasks on time and with highest quality']
        indresponse = {}
        print('Fill your apprisal form in rated scale')
        print('1 is starts with Highly satisfied')
        print('2 is starts with satisfied')
        print('3 is starts with neutral')
        print('4 is starts with not satisfied')
        print('5 is starts with Highly not satisfied')
        for i in appisalques:
            print(i)
            indresponse.update({i:int(input('Enter 1 to 5'))})
        self.selfappricalresponces.update({self.selfappricalcount:indresponse})
    
    def selfapprisalresult(self):
        if self.selfappricalcount == 0:
            print('No self apprisal')
        else:
            for i in self.selfappricalresponces:
                print('your', i , 'self apprisal')
                for k in self.selfappricalresponces[i]:
                    print(k,'-',self.selfappricalresponces[i][k])


emp1 = Employee('Dinah',90000)
emp1.employee_record()
Employee.employee_count()
emp1.currentproject()
emp1.assignproject('VIT')
emp1.currentproject()
emp1.casualleave(33)
emp1.casualleave(2)
emp1.medileave(20)
emp1.medileave(2)
emp1.selfapprisalresult()
emp1.selfapprical()
emp1.selfapprisalresult()