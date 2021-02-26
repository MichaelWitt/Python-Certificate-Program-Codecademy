print('Mr. Witt\'s Python Physics Class')

# Fahrenheit to Celsius Converter
def f_to_c(f_temp):
  c_temp = (f_temp - 32) * 5/9
  return c_temp

f100_in_celsius = f_to_c(100)
print('F to C:', f100_in_celsius)

# Celsius to Fahrenheit Converter
def c_to_f(c_temp):
  f_temp = (c_temp*(9/5) + 32)
  return f_temp

c0_in_fahrenheit = c_to_f(0)
print('C to F:', c0_in_fahrenheit)

# Train Force Calculator
train_mass = 22680
train_acceleration = 10
train_distance = 100

def get_force(mass, acceleration):
  return mass*acceleration

train_force = get_force(train_mass, train_acceleration)
print('Train Force: ', train_force)
print('The GE train supplies', train_force, 'Newtons of force.')

# Get Work

def get_work(mass, acceleration, distance):
  return mass*acceleration*distance

train_work = get_work(train_mass, train_acceleration, train_distance)
print('Train Work:', train_work)
print('The GE Train does', train_work, 'Joules of work over', train_distance, 'meters.')

# Get Energy
bomb_mass = 1

def get_energy(mass, c=3*10**8): # C is Speed of Light
  return (mass*c**2)

bomb_energy = get_energy(bomb_mass)
print('Energy:', bomb_energy)
print('A 1kg bomb supplies', bomb_energy, 'Joules')
