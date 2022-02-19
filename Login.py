import csv,sys

d={}
f=open('DATA.csv','a',newline='')
f.close()

def First():
    print('1.Create account')
    print('2.Login')
    print('3.Exit')
    
    return int(input('Your Choice:'))
def createac():
    u = input('Username(It should be unique) :')
    p = input('Password :')
    f = checkuser(u)
    if f==False:
        load(u,p)
        print('Account created sucessfully !!\n\n')
    else:
        print('Username already taken\n\n')
        
def checkuser(u):
    if u in d.keys():
        return True
    else:
        return False
    
def checkpass(p):
    if p in d.values():
        return True
    else:
        return False
    
def load(u,p):
    e=[u,p]
    f=open('DATA.csv','a', newline='')
    csv.writer(f).writerow(e)
    f.close()
        
    
def add():
    global d
    f=open('DATA.csv','r',newline='')
    d = dict(csv.reader(f))
    f.close()

def login():
    u = input('Username :')
    p = input('Password :')
    if (checkpass(p) and checkuser(u)):
        print('\nLogged in successfully\n')
    else:
        print('Invalid Username or Password !!\n')
    
while True:
    m=First()
    add()
    if m==1:
        createac()
    elif m==2:
        login()
    elif m==3:
        sys.exit()
    else:
        print('Invalid Choice')
