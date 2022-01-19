#Digit of Life

#sum up the digits of a number
def digits_sum(number):
    sum = 0
    if number == 0:
        sum = 0
    else:
        #print(number%10)
        sum = number%10 + digits_sum(number//10)
    return sum

def digit_of_life(birthday):
    
    month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    digits = ''
    birth_month = ''
    
    #First, change month name to month number
    if not birthday.isdigit():
        for ch in birthday:
            #print(type(char))
            if ch.isalpha():
                birth_month += ch
            else:
                digits += ch
        
        for ch in str(month.index(birth_month)+1):
            digits += ch
    else:
        digits = birthday
        
    #string to number
    birthday = int(digits)
   
    while (birthday > 9):
        birthday = digits_sum(birthday)

    return birthday
    
def main():    
    #
    birthday = input("Please your birthday: ")
    print(digit_of_life(birthday))

# Using the special variable 
# __name__
if __name__=="__main__":
    main()















