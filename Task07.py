celsius = int(input())
def convert(c):
  return (9/5*celsius)+32  
fahrenheit = convert(celsius)
print(fahrenheit)
def turn (f):
    return 5/9*(fahrenheit-32)
celsius = turn(fahrenheit)
print(celsius) 