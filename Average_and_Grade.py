#Jelissa Reyes
#CS 175L-01
#Average and Grade Assignment

#how to get letter grades 
def determine_grade(score):
    if score >= 90 and score <= 100:
        return "A"
    elif score >= 80 and score <= 89:
        return "B"
    elif score >= 70 and score <= 79:
        return "C"
    elif score >= 60 and score <= 69:
        return "D"
    elif score <= 59:
        return "F"
    else:
        return "Invalid"
#how to get average     
def calc_average (s1,s2,s3,s4,s5):
    return (s1+s2+s3+s4+s5) / 5.0
#main function to insert grades, and print
def main():
    score1 = float(input("Enter Score 1: "))
    score2 = float(input("Enter Score 2: "))
    score3 = float(input ("Enter Score 3: "))
    score4 = float(input("Enter Score 4: "))
    score5 = float(input("Enter Score 5: "))
    print("Score " "    Numeric Grade " "   Letter Grade")
    print("--------------------------------------")
    print("Score 1 : ", "\t", score1, "\t\t",determine_grade(score1))
    print("Score 2 :" , "\t",score2,  "\t\t",determine_grade(score2))
    print("Score 3 :" , "\t",score3,  "\t\t",determine_grade(score3))
    print("Score 4 :" , "\t",score4,  "\t\t",determine_grade(score4))
    print("Score 5 :" , "\t",score5 , "\t\t",determine_grade(score5))
    average = calc_average(score1, score2, score3, score4, score5)
    print("Average score is: " , "",str(average), "\t",determine_grade(average))
#how to make it repeat 
def repeat():
    loop = input("Would you like to make another calculation? (yes or no)")
    if loop.lower() == "yes":
       loop == True
       main()
    elif lower.loop() == "no":
        loop == False
loop = True
if loop == True:
    main()
    repeat()
       
        
    
