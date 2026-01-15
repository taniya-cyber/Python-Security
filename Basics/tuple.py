#Creating Tuples
secure_ports = (89,20, 22, 32)
single_value_tuple = (80,) #comma is important,if we miss it, it will be taken as INTEGER value, belonging to INT class.
    
#if we do this: secure_ports[0] = 23, it will give error.
print('Secure ports are:', secure_ports)
print('One port:', single_value_tuple)
print('Total Ports:', len(secure_ports))
