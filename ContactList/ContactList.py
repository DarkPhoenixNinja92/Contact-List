def add():
    firstName = input('First Name: ')
    lastName = input('Last Name: ')
    address = input('Address: ')
    email = input('Email: ')
    phone = input('Phone Number: ')

    with open('contacts.txt', 'a') as f:
        f.write('First Name: ' + firstName + '\n' + 'Last Name: ' + lastName + '\n' + 'Address: ' + address + '\n' + 'Email: ' + email + '\n' + 'Phone Number: ' + phone)

def view():
    print('View mode not yet enabled. Please try again later.')

while True:
    mode = input('Welcome to the Phoenix Contact Management System! Would you like to add a new contact or view existing ones? Press q to quit ').lower()
    if mode == 'q':
        break
    if mode == 'view':
        view()
    elif  mode == 'add':
        add()
    else:
        print('Invalid mode')
        continue