#Jelissa Reyes
#CS 175L-01
#expensePieChart

import matplotlib.pyplot as plt

def main():
    file = open("expenses.txt" ,"r")
    labels = []
    values = []
    for line in file.readlines():
        line = line.replace("Payment"," ")
        labels.append(str(line.split()[0]))
        values.append(int(line.split()[1]))
    plt.pie(values, labels=labels, colors = ("g" , "b" , "y", "r", "m" , "c"))
    plt.show()
main()
