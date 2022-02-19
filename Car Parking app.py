import datetime,sys

class Car_parking():
    
    def screen(s):
        print('1.Add car details\n2.Display Cars details\n3.Checkout\n4.Exit')
        return int(input('Enter Choice:'))
    
    def __init__(s):
        f=open('data.txt','r')
        s.data=[[1,2,3,4,5]]
        s.data=f.readlines()
        for i in range(0,len(s.data)):
            s.data[i]=s.data[i].strip('\n')
            s.data[i]=s.data[i].split()
        f.close()
        
    def add(s):
        k=input('Enter car no:')
        for i in range(0,len(s.data)):
            if k==s.data[i][0]:
                if s.data[i][3]=='checkedin':
                    print('Car already Checkedin')
            else:
                d=str(datetime.datetime.now())
                y=[k,d,input('Owner name:'),'checkedin','']
                s.data.append(y)
                break
                
    def display(s):
        print('Car no\tDate\t\ttime\t\tOwner name\tStatus')
        for i in range(0,len(s.data)):
            print('{}\t{}\t{}\t{}\t{}'.format(s.data[i][0],s.data[i][1],s.data[i][2],s.data[i][3],s.data[i][4]))
            
    def checkout(s):
        k=input('Enter car no:')
        for i in range(0,len(s.data)):
            if k==s.data[i][0]:
                if s.data[i][3]=='checkedout':
                    print('Car already Checkedout')
                else:
                    s.data[i][3]='checkedout'

    def storedata(s):
        f=open('data.txt','w')
        for i in range(0,len(s.data)):
            s.data[i]=' '.join(s.data[i])
            f.writelines(s.data[i])
            f.write('\n')
        f.close()  
        

o=Car_parking()

while True:
    m=o.screen()
    if m==1:
        o.add()
    elif m==2:
        o.display()
    elif m==3:
        o.checkout()
    elif m==4:
        o.storedata()
        sys.exit()
                
            
