# Use single quotes
greeting = 'Hello there!'
greeting
'Hello there!'

# Use double quotes
welcome = "Welcome to Github!"
welcome
'Welcome to Github!'

# Use triple quotes
message = """Thanks for joining us!"""
message
'Thanks for joining us!'

# Escape characters
escaped = 'can\'t'
escaped
"can't"
not_escaped = "can't"
not_escaped
"can't"

#

"Happy" + " " + "pythoning!"
'Happy pythoning!'

len("Happy pythoning!")
16

" ".join(["Happy", "pythoning!"])
'Happy pythoning!'

"Happy pythoning!".upper()
'HAPPY PYTHONING!'

"HAPPY PYTHONING!".lower()
'happy pythoning!'

#

name = "Mike"
age = 25
"My name is {0} and I'm {1} years old".format(name, age)
"My name is Mike and I'm 25 years old"

name = "Mike"
age = 25
f"My name is {name} and I'm {age} years old"
"My name is Mike and I'm 25 years old"

#

welcome[0]
'W'
welcome[11]
'R'
welcome[-1]
'!'

welcome = "Welcome to Github!"
welcome[0:7]
'Welcome'
welcome[9:12]
'to'
