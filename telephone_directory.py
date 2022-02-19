## Project : Telephone directory

d = {}
def screen():
    
    
    print('1:Add Contact details')
    print('2:Display all contacts')
    print('3:Search for a contact')
    print('4:Edit contact')
    print('5:Delete contact')
    print('6:Exit')

    c = int(input('enter choice:'))
    return c

def add_detail():

    name = input('enter name:')
    email_id = input('enter email_id:')
    address = input('enter address:')
    ph_no = input('enter mobile no:')

    d[email_id] = {'name':name,'address':address,'ph_no':ph_no}


def display():

    print('name\taddress\tph_no\t\temail-id')
    print('--------------------------------')
    for k in d:
        print('{}\t{}\t{}\t{}'.format(d[k]['name'],d[k]['address'],d[k]['ph_no'],k))
        print('----------------------------')

def search():

    mail = input('enter email-id:')

    if mail in d:
        print('name\taddress\tph_no\t\temail-id')
        print('{}\t{}\t{}\t{}'.format(d[mail]['name'],d[mail]['address'],d[mail]['ph_no'],mail))

    else:
        print('not found in data')

def edit():
    mail = input('enter email-id to update record:')

    if mail in d:
        print('1:Name')
        print('2:Address')
        print('3:phone_no')

        c = int(input('enter choice:'))

        if c==1:
            new_name = input('enter new name:')
            d[mail]['name'] = new_name
        elif c==2:
            new_address = input('enter new address:')
            d[mail]['address'] = new_address

        elif c==3:
            new_ph_no = input('enter new ph_no:')
            d[mail]['ph_no'] = new_ph_no
             
        print('Record updated')
    else:
        print('not found')

def delete():
    
    mail =  input('enter email-id to delete record:')

    if mail in d:

        del d[mail]
        print('delete record successfully')

    else:
        print('not found')
    
    
while True:

    ch = screen()

    if ch==1:

        add_detail()
    elif ch==2:
        display()

    elif ch==3:
        search()

    elif ch==4:
        edit()

    elif ch==5:
        delete()
    else:
        break

        
        
            





             
             

         
    
        
    
