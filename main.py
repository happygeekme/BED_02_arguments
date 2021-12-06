# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line

def greet(name:str, greeting='Hello, <name>!'):
    replaced = greeting.replace('<name>', name)
    print(replaced)
    return replaced

    
greet('Bob', "What's up, <name>!")
greet(name='Bruno')



def force(mass:float, body='earth'):
    body_gravity = {
    'earth': 9.8,
    'sun': 274,
    'jupiter': 24.9,
    'neptune': 11.2,
    'saturn': 10.4,
    'uranus': 8.9,
    'venus': 8.9,
    'mars': 3.7,
    'mecury': 3.7,
    'moon': 1.6,
    'pluto': 0.6
    }
    return mass * body_gravity[body]
   

print(force(1))

def pull(m1:float, m2:float, d:float):
    g = 6.674 * 10**-11
    return g * ((m1 * m2) / d**2)

print(pull(800, 1500, 3))