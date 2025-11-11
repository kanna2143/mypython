#Divisibility Test
number=int(input("enter an integer: "))
if number % 3 == 0 and number % 5 == 0:
  print(f"the number {number} is divisible by both 3 and 5.")
else:
  print(f"the number{number}is not divisible by both 3 and 5.")
