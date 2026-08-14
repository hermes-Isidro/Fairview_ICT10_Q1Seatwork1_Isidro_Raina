# Seatwork 1
from pyscript import display, document


fullname = 'Raina Isidro'  # string
ag3_s = 15  # integer
h31ght = 168 # integer
c0unt_ries = set(['Japan','Canda',' and Australia']) # Set
student_type = True # boolean
color = 'blue' # string
car_brand = 'Ford' # string
shoe_size = 26.7 # integer
best_friend = 'Mathea Santos' # string
fav0rite_fruIts = set(['Apples', 'Oranges','Tangerines', 'Blood Oranges', 'Mandarins']) # set
mysevendaytuple = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday") # tuple


display(f'Shabuya sha sha shabuya roll call my name is {fullname}. I am {ag3_s}. My height is {h31ght}. The countries I really want to go to are {c0unt_ries}. Favorite color is {color} the car we have is {car_brand}, my shoe size is {shoe_size}, and my best friend is {best_friend}. I love {fav0rite_fruIts}. And I have no idea why I say {mysevendaytuple}' , target='result')
document.getElementById('result').innerHTML = f'<i>Shabuya sha sha shabuya roll call my name is {fullname}</i>. I am {ag3_s}. My height is {h31ght}. The countries I really want to go to are {c0unt_ries}. Favorite color is {color} the car we have is {car_brand}, my shoe size is {shoe_size}, and my best friend is {best_friend}. I love {fav0rite_fruIts}. And I have no idea why I say {mysevendaytuple}'
