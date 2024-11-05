import math

def sin(x):
    
    if not isinstance(x, (int, float)):
        raise ValueError("Input must be a numeric value.")
    return math.sin(math.radians(x))

def cos(x):
   
    if not isinstance(x, (int, float)):
        raise ValueError("Input must be a numeric value.")
    return math.cos(math.radians(x))

def tan(x):
    
    if not isinstance(x, (int, float)):
        raise ValueError("Input must be a numeric value.")
    return math.tan(math.radians(x))

def sqrt(x):
    
    if not isinstance(x, (int, float)):
        raise ValueError("Input must be a numeric value.")
    if x < 0:
        raise ValueError("Input must be non-negative.")
    return math.sqrt(x)

def log(x):
  
    if not isinstance(x, (int, float)):
        raise ValueError("Input must be a numeric value.")
    if x <= 0:
        raise ValueError("Input must be greater than 0.")
    return math.log(x)

def exp(x):

    if not isinstance(x, (int, float)):
        raise ValueError("Input must be a numeric value.")
    return math.exp(x)
