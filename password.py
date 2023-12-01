import random
lower ="abcdefghijklmnopqrstuvwxyz"
upper ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number ="1234567890"
symbol ="!@#$%^&*()_{}[]"
all = lower+upper+number+symbol
lenght =int(input("enter the lenght of the password="))
password ="".join(random.sample(all,lenght))
print("pasword is=",password)
