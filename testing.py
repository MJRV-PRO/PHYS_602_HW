import numpy as np

def randomNumberGenerator(bounds):
  """
  Returns a random integer between the bounds given. Uses the numpy random.

  Parameters
  ----------
  bounds : 2D tuple
  A tuple containing the lower and upper bounds for the random number.

  Returns
  -------
  np.random.randint(bounds[0],bounds[1]) : int
  A random integer.
""" 
return np.random.randint(bounds[0],bounds[1])