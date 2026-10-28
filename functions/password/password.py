import random
import string
def password(length):
   lowercase = string.ascii_lowercase
   uppercase = string.ascii_uppercase
   digits = string.digits
   punctuation = string.punctuation

   all_characters = lowercase + uppercase + digits + punctuation

   result = ''.join(random.choice(all_characters) for i in range(length))
   return result