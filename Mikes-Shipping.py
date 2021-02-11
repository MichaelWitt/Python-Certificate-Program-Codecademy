#Mike's Shipping
print('Welcome to Mike\'s shipping!\nHere are your rates:'
)

#Enter your package weight
weight = 23

# Ground Shipping
if weight <= 2:
  print('Ground shipping is: $', weight * 1.50 + 20.00)
elif weight > 2 and weight <= 6:
  print('Ground shipping is: $', weight * 3.00 + 20.00)
elif weight > 6 and weight <= 10:
  print('Ground shipping is: $', weight * 4.00 + 20.00)
else:
  print('Ground shipping is: $', weight * 4.75 + 20.00)

# Premium Shipping
print('Premium shipping is: $', 125.00)

# Drone Shipping
if weight <= 2:
  print('Drone shipping is: $', weight * 4.50)
elif weight > 2 and weight <= 6:
  print('Drone shipping is: $', weight * 9.00)
elif weight > 6 and weight <= 10:
  print('Drone shipping is: $', weight * 12.00)
else:
  print('Drone shipping is: $', weight * 14.25)

# Thanks
print('Thanks :)')
