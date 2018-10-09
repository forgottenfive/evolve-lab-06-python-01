import requests
def retrieve(my_url, my_exit_message = '\nExiting application.'):
    r = requests.get(my_url)
    if r.raise_for_status().lower != "none":
        print("Error", r.raise_for_status(), "thrown when attempting to access", my_url, my_exit_message)
        exit()

    return r.text

def file_write(my_txt, my_file):
    try:
        f = open(my_file, "w")
        f.write(my_txt)
    except:
        print("Error thrown while attempting to write to file", my_file, my_exit_message)
        exit()

my_url = 'http://www.example.com'
my_file = 'example_2.txt'
my_exit_message = '\nExiting application.'

my_txt = retrieve(my_url, my_exit_message)
print("Successfully loaded", my_url)

file_write(my_txt, my_file, my_exit_message)
file_write(my_txt, my_file)
print("Successfully wrote contents of", my_site, "to", my_file, my_exit_message)

if input("Would you like to echo the text of", my_site, "to your terminal window? (Yn) "):
    print(my_txt)
exit()

