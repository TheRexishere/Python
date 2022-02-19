import datetime

class Car_parking():

    def __init__(self):

        self.data = {}
        
        

    def screen(self):
        print('1:Arrival of a car')
        print('2:Total no. of cars Arrived')
        print('3:Departure of the car')
        print('4:Delete record')
        print('5:Exit Program')

        c = int(input('enter choice:'))

        return c

    def arrival(self):

        data = []
        while True:
            car_no = input('enter car no:')
            if car_no not in self.data:
                
                break
            
            print('already exists')
                
        model = input('enter model name:')
        
        date = datetime.datetime.now()

        self.data[car_no] = {'model':model,'arrival_date':date,'dep_date':None}
        
        
   

    def display(self):
        
        print('car_no\tmodel\tArrival_date\t\t\tdep_date')
        for i in self.data:
            print('{}\t{}\t{}\t{}'.format(i,self.data[i]['model'],self.data[i]['arrival_date'],self.data[i]['dep_date']))
            print('-------------------------------')
       
    

    def delete(self):
        car_no = input('enter car no:')

        if car_no in self.data:

            del self.data[car_no]
            print('Record deleted')
        else:

            print('not found')

        
        
    
    def departure(self):
        car_no = input('enter car no:')
       
        if car_no in self.data:
            dep_date = datetime.datetime.now()
            self.data[car_no]['dep_date'] = dep_date
            
        else:
            print('car no not found')

    
obj = Car_parking()

while True:
    m = obj.screen()

    if m==1:
        obj.arrival()

    elif m==2:
        obj.display()

    elif m==3:
        obj.departure()

    elif m==4:
        obj.delete()

    else:
        break










    
    
        

        











