import random

m = int(input("How many dice rolls you want?"))

def dice_roll(m):
    count = 0

    for i in range(m):
        p = input("Roll the device! (yes(y)/no(n)) ")
        if p == 'y' or p == 'Y' :
            die_1 = random.randint(1 , 6) 
            die_2 = random.randint(1 , 6) 
            print(f'({die_1},{die_2})')
            count += 1

        elif p == 'n' or p =='N':
            print("Thanks for playing")
            
        else:
            print("Invalid")
        
    return count

count = dice_roll(m)
print("Total times dice rolled:",count)
