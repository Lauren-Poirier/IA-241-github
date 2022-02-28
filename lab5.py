'''
lab5.py
'''

#3.1
alien_color = 'green'
if alien_color == 'green':
    print('the player just earned 5 points')

#3.2
alien_color = 'green'
if alien_color == 'green':
    print('the player just earned 5 points') 
else:
    print('you have earned 10 points')
    
#3.3
my_list = ['strawberry', 'pear', 'peach']
if 'strawberry' in my_list:
    print('I like strawberries')
if 'pear' in my_list:
    print('I like pears')
if 'peach' in my_list:
    print('I like peaches')
    
#3.4
age = 19
if age <10:
    print('kid')
elif age >=10 and age <20:
    print('teenager')
else:
    print('adult')
    if age >=65:
        print('elder')
