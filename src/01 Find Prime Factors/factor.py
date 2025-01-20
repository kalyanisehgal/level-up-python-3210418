def get_prime_factors(input):
	# check whether the input is integer or not   
  if isinstance(input, int) == False:
    return f'{input} is not an integer'
  
  #calculate the prime factors of integer
  #Initialize the start point of the loop and the empty set
  initial = 2
  factors = []
  newInput = input

  while initial * initial < input:
    while newInput % initial == 0:
        newInput = int(newInput / initial)
        factors.append(initial)
    if isPrime(newInput) == True:
      factors.append(newInput)
      break
    initial = initial + 1
        
  return factors

def isPrime(num):
  if num <= 1:
    return False
  
  if num == 2:
    return True

  flag = True
  for i in range(2, (num//2)+1):
    if num % i == 0:
      flag = False
      break
   
  return flag


print(get_prime_factors(630))
print(get_prime_factors(72))
print(get_prime_factors(17))
print(get_prime_factors(85))
print(get_prime_factors(23))
print(get_prime_factors('Kalyani'))
print(get_prime_factors('630'))