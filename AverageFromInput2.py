#Jelissa Reyes
#CS 175L-01
#AveragefromInput
#withExceptionHandling

def main():
    try:
        file_num = open("numbers.txt" ,'r')
        x = 0
        total = 0
    except IOError:
        print("Error, not correct.")
    for line in file_num:
        try:
            x = x +1
            amount = int(line)
            total = total + amount
            print(f"I read in {x} number(s) "
                  f"Current number is: {amount:.1f}"
                  f"Total is: {total:.1f}")
        except ValueError:
            print("Error, not correct.")
    file_num.close()
    average = total / x
    print (f"Average: {average:.1f}")
main()
