#Jelissa Reyes
#CS 175L-01
#AveragefromInput

def main():
    file_num = open("number.txt" ,'r')
    x = 0
    total = 0
    for line in file_num:
        x = x +1
        amount = float(line)
        total = total + amount
        print(f"I read in {x} number(s) "
              f"Current number is: {amount:.1f}
              f"Total is: {total:.1f}")
    num_file.close()
    average = total / x
    print (f"Average: {average:.1f}")
if _name_ == "_main_":
    main()
