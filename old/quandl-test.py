import quandl
import matplotlib.pyplot as plt
import numpy

mydata = quandl.get("WIKI/UTX", start_date="2016-12-31", end_date="2017-5-01")
print(mydata)
plt.plot(mydata)
plt.show()
# print(quandl)