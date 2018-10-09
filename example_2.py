import requests
def retrieve(my_url):
    r = requests.get(my_url)
    r.raise_for_status()
    return r.text

def file_write(my_txt, my_file, my_exit_message):
    try:
        f = open(my_file, "w")
        f.write(my_txt)
    except:
        print("Error thrown while attempting to write to file", my_file, my_exit_message)
        exit()

my_url = 'http://www.example.com'
my_file = 'example_2.txt'
my_exit_message = '\nExiting application.'

my_txt = retrieve(my_url)
print("Successfully loaded", my_url)

file_write(my_txt, my_file, my_exit_message)
print("Successfully wrote contents of", my_url, "to", my_file)

if input("Would you like to echo the text of " + my_url + " to your terminal window? (Yn) ").lower() == 'y':
    print("\nBody of", my_url, "\n\n")
    print(my_txt)
    print("System message: EOF reached.")
print(my_exit_message)
exit()

