import numpy as np 
import matplotlib.pyplot as plt

mu, sigma= 1.0, 32000
g = np.random.normal(mu, sigma, 1000)
print (g)
count, bins, ignored = plt.hist(g, 30, density=True)
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *
np.exp( - (bins - mu)**2 / (2 * sigma**2) ),
linewidth=2, color='r')
plt.show()
