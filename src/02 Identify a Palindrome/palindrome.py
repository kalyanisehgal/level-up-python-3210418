import re

def is_palindrome(strtext):
  #Check whether the input is string or not
  if isinstance(strtext, str) == False:
    return False
  
  #Check for the palindrome
  cleanstring = re.sub(r'[^a-zA-Z0-9]', '', strtext)
  revstring = cleanstring[::-1]

  return cleanstring.lower() == revstring.lower()
    
print(is_palindrome('Go hang a salami, I’m a lasagna hog.'))
print(is_palindrome('hello world'))
print(is_palindrome(2112))
print(is_palindrome(12.21))
print(is_palindrome('A man, a plan, a canal: Panama!'))
  
  
