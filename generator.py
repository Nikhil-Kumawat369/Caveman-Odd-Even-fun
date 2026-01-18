f = open("generated.py" , "w")

# this num variable just tracke how many time the if else statements need to be generated
num = int(input("Till How Many Number You Want To Write if / elif To Check Odd or Even :- "))

# This make a input logic in the generated file 
f.write("num = int(input('Enter the number you want to check Odd or Even :- '))\n\n")

f.write("if num == 1 :\n")
f.write("  print('Odd')\n")

for i in range(2 , num+1) :
    
    if i % 2 == 0 :

        f.write(f"elif num == {i} :\n")
        f.write(f"  print('Even')\n")
    else :
        f.write(f"elif num == {i} :\n")
        f.write(f"  print('Odd')\n")

f.write("else :\n")
f.write(f"   print('Hey , I was only trained for numbers up to {num}. I cant handle above it.')")

f.close()