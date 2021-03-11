# Tenth Power

def tenth_power(num):
  return num**10

print(tenth_power(1))
print(tenth_power(0))
print(tenth_power(2))

# Square Root

def square_root(num):
  return num ** 0.5

print(square_root(16))
print(square_root(100))

# Win Percentage

def win_percentage(wins, losses):
  totalGames = wins + losses
  winning = wins / totalGames
  percentage = winning * 100  
  return percentage

print(int(win_percentage(5, 5)), '%')
print(int(win_percentage(10, 0)), '%')

# Average

def average(num1, num2):
  total = num1 + num2
  average = total / 2
  return average

print(average(1, 100))
print(average(1, -1))

# Remainder

def remainder(num1, num2):
  return (num1*2) % (num2/2)

print(remainder(15, 14))
print(remainder(9, 6))

# First 3 Multiples

def first_three_multiples(num):
  print(num)
  print(num*2)
  print(num*3)
  return num*3

first_three_multiples(10)
first_three_multiples(0)

# Tip Calculator

def tip(total, percentage):
  return (total*percentage)/100

print(tip(10, 25))
print(tip(0, 100))

# James Bond

def introduction(first_name, last_name):
  bond = last_name + ', ' + first_name + ' ' + last_name
  return bond

print(introduction("James", "Bond"))
print(introduction("Maya", "Angelou"))

# Dog Years

def dog_years(name, age):
  dog_years = age*7
  return name + ', ' + 'you are ' + str(dog_years) + ' years old in dog years'

print(dog_years("Lola", 16))
print(dog_years("Baby", 0))

# Math Challenge

def lots_of_math(a, b, c, d):
  a_plus_b = a+b
  print(a_plus_b)
  d_minus_c = d-c
  print(d_minus_c)
  a_b_times_d_c = a_plus_b*d_minus_c
  print(a_b_times_d_c)
  return a_b_times_d_c % a

print(lots_of_math(1, 2, 3, 4))
print(lots_of_math(1, 1, 1, 1))
