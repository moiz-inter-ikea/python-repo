# f-string allows to embed variables in string

name = 'bob'
greeting = f"hello , {name}"
print(greeting)

name = "tom"
print(greeting) # this does not change greeting from bob to tom, better is print f-string despite of greeting(as when greeting is assigned with value,name was bob)

print(f"hello , {name}")

##### another way to do this

name = "jerry"
greetings = "hello, {}"
message = greetings.format(name)

print(message)

name = "jay"
print(message) #it will still prints hello, jerry -- have it as seperate message

message2 = greetings.format(name)
print(message2)

###### best use of string formatter  #############
record = 'hello {}, your role is {}'
message3 = record.format('june', 5)
print(message3)