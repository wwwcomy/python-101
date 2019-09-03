
'''

F = 1.8C+32
'''
def centigrade_to_fahrenheit(input):
    return 1.8*input+32

def fahrenheit_to_centigrade(input):
    return (input-32)/1.8
print(fahrenheit_to_centigrade(0))
print(fahrenheit_to_centigrade(-1))
print(fahrenheit_to_centigrade(100))

print(centigrade_to_fahrenheit(0))
print(centigrade_to_fahrenheit(-1))
print(centigrade_to_fahrenheit(100))