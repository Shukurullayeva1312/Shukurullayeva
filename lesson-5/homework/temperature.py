def convert_cel_to_far():
   F = float(input(('Enter a temperature in degrees F: ')))
   C = (F - 32) * 5/9
   print(F, ' degrees in F = ', round(C, 2), ' degrees in Celsius')
def convert_far_to_cel():
   C = float(input(('Enter a temperature in degrees C: ')))
   F = C * 9/5 + 32
   round(F, 2)
   print(C, 'degrees in C = ', round(F, 2), 'degrees in F')
convert_cel_to_far()
convert_far_to_cel()