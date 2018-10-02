import datetime

def age_return(age,curr_year,target_year):
    #math to calculate desired age
    return target_year-curr_year+age

def age_calc(target_year):
    #find system time from system functions
    curr_year=int(datetime.datetime.now().year)
    #print (curr_year)
    while True:
        #makes infinite loop until proper value is seen
        try:
            #retrieve input from user to get current age
            curr_age = int(input("Enter your age: "))
            #error handling
            if curr_age <0 or curr_age>=100:
                print ("Try again. Positive integer below 100")
            else:
                print "Your age in",target_year,"will be",age_return(curr_age,curr_year,target_year), "years"
                break  
        #error handling for non-numerics
        except ValueError:
            print("No valid integer! Please try again ...")

#variable to set a target year
target_year = 2035
#call routine
age_calc(target_year)

