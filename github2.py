
import random 

x = random.randint(1,10) 

z = int(input("How Many Attempt Do You Want? : "))
k = 0
p = 100

while k != z:
    k += 1
    y = int(input("Guess The Number: "))
    if x < y:
         print("Choose a lower number.")
    elif x == y:
         print(f"Congratulations You got it on your {k}. try.:")
         break
    else:
         print("Choose a higher number")

if k == z:
         print(f"Your attempt was over, number held: {x}")

print(f"Your remaining points at the end of the game : {p - ((p/z)*k)}")
