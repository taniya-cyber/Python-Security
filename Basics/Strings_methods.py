msg = 'Radhe radhe'
print(msg[10-1])
message = '''Hi, this is Taniya
and I like this'''
print(message.lower())
print(message.capitalize())
print(message.find('la'))
print(message.count('la'))
#print(message.replace('Taniya', 'Div'))
#If we first replace and then print, it wouldn't change the string as string is immutable, so it prints same string as we initialized.
message = message.replace('Taniya', 'Div') #or we can direcly give "Message" the new value.
message.count('Div')
print(message)
new = msg + ' ' + message
print(new)
#another way for same: 
neww =  '{}, {}. Welcome!'.format(msg, message)
#or by "f-string"