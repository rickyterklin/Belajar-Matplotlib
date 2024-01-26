import numpy as np
import matplotlib.pyplot as plt

## gunanya setting axix untuk mengatur nilai min & max nilai x,y

"""
1. membuat data
2. membuat plot
3. menampilkan plot
"""

# 1. membuat data (sin(2wt + theta))
def sinusGenerator(amplitudo,frekuensi,tAkhir,theta):
    t = np.arange(0,tAkhir,0.1)
    y = amplitudo * np.sin(2*frekuensi*t + np.deg2rad(theta))
    return t,y

t,y = sinusGenerator(1,1,4,0)

# membuat plot
plt.plot(t,y)

# setting axis, minimum dan maximum
# untuk settng axix  gunakan plt.axis([xmin,xmax,ymin,ymax])
plt.axis([0,4,-2,2])

# menampilkan
plt.show()