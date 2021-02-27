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
