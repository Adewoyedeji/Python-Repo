import random

boxer_name = {'Ali': 'Sting like a bee', 'Wilder' : 'Bomb squad', 'Cardoso': 'Robots rule', 'Ayo' : 'Python Stings', 'Bella' : 'Say what'}

item = boxer_name.items()
length = len(item)
ran = range(length)
ran_num = random.choice(ran)
print(ran_num)
#print(item[ran_num])
