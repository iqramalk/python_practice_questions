import numpy as np
import matplotlib.pyplot as plt
x_obs=np.array([1,2,3,4,5])
y_obs=np.array([-1,0,1,2,3,4])
x_est=np.linspace(0,5,500)
y_est=2*x_est+3
plt.plot(x_obs,y_obs,"ro",label="Observed")
plt.plot(x_est,y_est,label="Estimate")
plt.xlabel('x')
plt.ylabel('y')
plt.show()
