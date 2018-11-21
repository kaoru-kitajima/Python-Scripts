#%%
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

range = 50
x = np.arange(range)
y = np.random.randn(range)
plt.plot(x, y)
cos_x = np.cos(x)
sin_x = np.sin(x)
plt.plot(cos_x, sin_x)



'H'.encode().hex()
bytes.fromhex(H.encode())