# types of imports 

# normal import 
import math
print(math.sqrt(16))

# Selective import 
from math import sqrt
print(sqrt(14))
 
# import as alias
import math as m
print(m.sqrt(18))

# mixing with alias 

from math import sqrt as s 
print(s(13))

