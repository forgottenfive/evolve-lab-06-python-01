######FUNCTIONS######

# function to check an user string against a list
def in_list(my_str, my_list):
    return my_str.lower() in my_list

# function to load a list from a text file in lowercase format
def load_list(my_file):

    # load file contents
    filename1 = my_file
    with open(filename1, 'r') as f1:
        temp = f1.read()

    # create list from file with each item lowercase
    temp_list = []
    temp = temp.split('\n')
    for item in temp:
        temp_list.append(item.lower())

    # test code to be sure list loaded correctly.  Uncomment to debug.
    # print(temp_list)
    # for item in temp_list:
        # print(item)

    return temp_list

######PROGRAM BODY######

# attempt to load a list of fruits
try:
    all_fruits = load_list('all_fruits.txt')
except:
    print("The program could not load the list of fruits into memory. Make sure you are using Python 3. Crashing now.")
    exit()

# prompt user to enter a string and check to see if it is a fruit
try:
    while True:
        my_fruit = str(input("Curious?  Enter an item of food to see if it is a fruit (i.e. \"Avocado\"): "))
        if in_list(my_fruit, all_fruits):
            print("Yes!", my_fruit, "is a fruit.")
        else:
            print("Sorry, but", my_fruit, "is not a fruit.")
        if str(input("Would you like to investigate another item of food? (Yn) ")).lower() != 'y':
            break
except:
    print("We're sorry, there was an error. Make sure you are using Python 3. Crashing now.")
    exit()


