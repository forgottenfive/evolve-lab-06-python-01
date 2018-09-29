def main():
    fruit_basket=["apple","orange","pineapple","strawberry","peach"]
    #print (fruit_basket[1])
#for i in fruit_basket:
    #print i
#"apple"    in fruit_basket
    failcount=0
    while failcount<5:
            guess = raw_input("enter a fruit ")
            failcount=failcount+1;
            if guess.lower() in fruit_basket:
                print guess, "is in the basket!"
                break
            print guess, "IS NOT ACCEPTABLE"

main()

