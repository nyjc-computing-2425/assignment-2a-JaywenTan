num = input('Enter a number (decimal or integer): ')
# type your code here
sf = 0
num2 = num.replace(".","")
num2 = num2.lstrip(" 0")
for x in num2:
  sf += 1


# do not change any code beyond this point
print('The number', num, 'has', sf, 'significant figures.')
