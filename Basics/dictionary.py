#Creating Dictionary
port_services = {22: 'SSH',
                 80: 'HTTP',
                 443: 'HTTPS',
                 21: 'FTP'}
print('Running Port Services:', port_services)
#1.1: Getting values of ONE key: (first Method)
print('Service on port 22:', port_services[22])
#1.2: 2nd method: Using Get
print(port_services.get(22))
#Get method is better than 1.1 as we can initialize the Default value, eg. :
port_services.get(27, 'Unrecogonisable service')
#2.1: Adding new key:
port_services[23] = 'TELNET'
#This can be used in Updating the existing value, eg. port_services[22] = 'XYZ'
#2.2: Adding new value by UPDATE method: We can add and update at same time for multiple values
port_services.update({22:'ssH', 23: 'TELNET Port'})
#3.1: Deleting of Key: By using del keyword
del port_services[21]
#3.2: Popping method returns value too which is being popped
Twenty_three = port_services.pop(23)
print(Twenty_three)
#Viewing Keys and Values:
#4.1: How many keys
print('Total Number of running ports: ', len(port_services))
#4.2: Printing all keys only
print(port_services.keys())
#4.3: Printing all values only
print(port_services.values())
#4.4: Printing all values and values
print(port_services.items())
#or we can do this by LOOP METHOD
for key in port_services.items():
    print(key)

