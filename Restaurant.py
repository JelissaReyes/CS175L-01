#CS 175L-01
#Jelissa Reyes
#Restaurant

vegetarian=False
vegan=False
gluten_free=False
response1="no"
response2="no"
response3="no"
response1=input("Is anyone in your party a vegetarian?")
if response1==("yes"):
    vegetarian=True
response2=input("Is anyone in your party a vegan?")
if response2==("yes"):
    vegan=True
response3=input("Is anyone in your party gluten free?")
if response3==("yes"):
    gluten_free=True
#results
if vegetarian==False and vegan==False and gluten_free==False:
    print("Here are your restaurant choices:")
    print("Joe's Gourmet Burgers")
if vegan==False and gluten_free==False:
    print("Here are your restaurant choices:")
    print("Mama's Fine Italian")
if vegan==False:
    print("Here are your restaurant choices:")
    print("Main Street Pizza")
    print("Corner Cafe")
    print("Chef's Kitchen")


    
    
    
