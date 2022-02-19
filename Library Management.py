## Library Management
import csv,sys

f=open('Books_Details.csv','a', newline='')
f.close()

class Lib:
    bname=[]
    ids=[]
    
    def __init__(s):
        f = open('Books_Details.csv','r', newline='')
        s.data=[]
        s.data = list(csv.reader(f))
        f.close()
        s.name()
        s.lastid=int(s.data[-1][0])
        
    def screen(s):
        print('\nLibrary Management Application:\n')
        print('1:Add new book\n2:Display stock\n3:Edit details\n4:Delete Book data')
        print('5:Search book\n6:Issue book\n7:Return book\n8:Exit')
        
        return int(input('Your Choice:'))
    
    def name(s):
        for i in range(0,len(s.data)):
            s.bname =[s.data[i][1]]
            s.ids=s.data[i][0]
    
    def add(s):
        bkname=input('Book name:')
        if bkname in s.bname :
            print('Book already exist')
        else:
            page=input('Total pages:')
            k=[s.lastid+1,bkname,page,'Not Issued']
            s.data.append(k)
            print('Details Added\n')
        
    def stock(s):
        print('Book ID\tStatus\tPages\tNames')
        for i in range(0,len(s.data)):
            print('{}\t{}\t{}\t{}'.format(s.data[i][0],s.data[i][2],s.data[i][3],s.data[i][1]))
            
    def edit(s):
        k = input('Enter book ID:')
        for i in range(0,len(s.data)):
            if k==s.data[i][0] :
                print('1:Book name')
                print('2:Pages')
                c = int(input('Choice:'))
                if c==1:
                    s.data[i][1]=input('New Name:')
                elif c==2:
                    s.data[i][2]=input('Pages:')
                
    def issue(s):
        k = input('Book ID:')
        for i in range(0,len(s.data)):
            if k==s.data[i][0] :
                if s.data[i][3]=='Not Issued':
                    s.data[i][3]='Issued'
                
    def storedata(s):
         f=open('Books_Details.csv','w',newline='')
         obj=csv.writer(f)
         for i in s.data:
             obj.writerow(i)
         f.close()
         
    def returnb(s):
        k = input('Book ID:')
        for i in range(0,len(s.data)):
            if k==s.data[i][0] :
                if s.data[i][3]=='Issued':
                    s.data[i][3]='Not Issued'
                    
    def search(s):
        k = input('Book ID:')
        for i in range(0,len(s.data)):
            if k==s.data[i][0]:
                print('Status\tPages\tNames')
                print('{}\t{}\t{}\n'.format(s.data[i][3],s.data[i][2],s.data[i][1]))
                
    def delete(s):
        k = input('Book ID:')
        for i in range(0,len(s.data)):
            if k==s.data[i][0]:
                del s.data[i]
        
        
        
            
        
        
obj= Lib()

while True:
    m=obj.screen()
    if m==1:
        obj.add()
    elif m==2:
        obj.stock()
    elif m==3:
        obj.edit()
    elif m==4:
        obj.delete()
    elif m==5:
        obj.search()
    elif m==6:
        obj.issue()
    elif m==7:
        obj.returnb()
    elif m==8:
        sys.exit()
    obj.storedata()
        