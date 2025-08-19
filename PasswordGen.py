import string
import random

print('################################################')
print('PASSWORD GENERATOR')
print('################################################')
print('')
print('How many passwords?')
passn = int(input())
if passn > 1:
    print('You have chosen to generate ' + str(passn) + ' passwords')
else:
    print('You have chosen to generate ' + str(passn) + ' password')


print('how many letters?')
l = int(input())
print('You have chosen ' + str(l) + ' letters')

def generate_password(amount = passn, length = l):
    letters = string.ascii_letters
    digits = string.digits

    all_chars = letters + digits

    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

for _ in range(passn):
    print(generate_password(passn))