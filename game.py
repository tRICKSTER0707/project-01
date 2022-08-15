import random                      #--> random module
                                    
def game(Jarvis, Tony):                                 
    if Jarvis == Tony:
        return None
    elif Jarvis == 'S':
        if Tony == 'W':
            return False
        elif Tony == 'G':
            return True
    elif Jarvis == 'W':
        if Tony == 'G':
            return False
        elif Tony == 'S':
            return True
    elif Jarvis == 'G':
        if Tony == 'S':
            return False
        elif Tony == 'W':
            return True

print("Jarvis turn: Snake(1) Water(2) or Gun(3)?")
randNum= random.randint(1, 3)      #--> random module contains randint() function which generates random number between given parameters                       
if randNum==1:
    Jarvis='S'
elif randNum==2:
    Jarvis='W'
elif randNum==3:
    Jarvis='G'


Tony=input("Tony turn: Snake(1) Water(2) or Gun(3)?\n")

a=game(Jarvis, Tony)

print('Jarvis choose', Jarvis)
print('Tony choose', Tony)

if a == None:
    print('The game is a tie')
elif a:
    print('Tony Won')
else:
     print('Jarvis Won')