filename = 'guestbook.txt'

with open(filename, 'a') as guest_book:
    while(True):
        name = input("Tell me your name: ")
        if(name == ''):
            break
        guest_book.write(f"{name} has stayed with us.\n")
        print(f"Thank you for staying with us {name}!")