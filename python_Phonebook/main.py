file_name = "C:\Users\Mahima\Documents\Phonebook.txt"
file1 = open(file_name, "a+")
file1.close


def show_main_menu():
    ''' Show main menu for Phone Book Program '''
    print("\n   *** Phone Book Menu ***\n" +
          "------------------------------------------\n" +
          "Enter 1,2,3 or 4:\n" +
          "Enter 1 To Display Your Contacts\n" +
          "Enter 2 To Add a New Contact\n" +
          "Enter 1,2,3 or 4:\n" +
          "Enter 1 To Display Your Contacts\n" +
          "Enter 2 To Add a New Contact\n" +
          "Enter 3 To search contacts\n" +
          "Enter 4 To Exit\n**********************")

    '''Operation input'''
     
    choice = input("Enter your choice: ")
    if choice == "1":
        file1 = open(file_name, "r+")
        file_contents = file1.read()
        if len(file_contents) == 0:
            print("Phone Book is empty")
        else:
            print(file_contents)
        file1.close
        ent = input("Press Enter to continue ...")
        show_main_menu()
    elif choice == "2":
        enter_contact_record()
        ent = input("Press Enter to continue ...")
        show_main_menu()
    elif choice == "3":
        search_contact_record()
        ent = input("Press Enter to continue ...")
        show_main_menu()
    elif choice == "4":
        print("Thanks for using Phone Book Program presented by:")
    else:
        print("Wrong choice, Please Enter [1 to 4]\n")
        ent = input("Press Enter to continue ...")
        show_main_menu()


''' Search contacts'''
def search_contact_record():
    ''' This function is used to searches a specific contact record '''
search_name = input("Enter First name for Searching contact record: ")
rem_name = search_name[1:]
first_char = search_name[0]
search_name = first_char.upper() + rem_name
file1 = open(file_name, "r+")
file_contents = file1.readlines()



found = False
for line in file_contents:
if search_name in line:
print("Your Required Contact Record is:", end=" ")
print(line)
found = True
break
if found == False:
print("There's no contact Record in Phone Book with name = " + search_name)

'''first name input'''
def input_fname():
    ''' Converts first letter of your name  to Upper case '''

def input_fname():
''' Converts first letter of your name to Upper case '''
fname = input("Enter First name ")
rem_fname = fname[1:]
first_char = fname[0]
return first_char.upper() + rem_fname



'''last name input'''
def input_lname():
    ''' Converts first letter of  last name  to Upper case '''


'''insert contact'''
def enter_contact_record():
    ''' It  collects contact info firstname, last name, email and phone '''

    
