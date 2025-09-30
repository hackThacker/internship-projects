import string
import random


char = string.ascii_letters + string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
combin = ''.join(random.choice(char) for i in range(14))
print(f"Generated password is :{combin}")
