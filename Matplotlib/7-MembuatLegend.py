import numpy as np
import matplotlib.pyplot as plt


## gunanya legend untuk memebuat kotak keterangan dari nilai
# membuat data
def sinusGenerator(amplitudo,frekuensi,tAkhir,theta):
    t = np.arange(0,tAkhir,0.1)
    y = amplitudo * np.sin(2*frekuensi*t + np.deg2rad(theta))
    return t,y

t,y = sinusGenerator(1,1,4,0)
t1,y1 = sinusGenerator(1,1,4,90)

# membuat plot
##cara pertama
# plt.plot(t,y, label="sin=0")
# plt.plot(t1,y1, label="sin=90")
# plt.legend()

## cara kedua ( memindahkan legend tetapi masih didalam tabel)
# plt.plot(t,y, label="sin=0")
# plt.plot(t1,y1, label="sin=90")
# plt.legend(loc="upper center")

## cara ketiga ( untuk memindahkan diluar tabel)
# plt.plot(t,y, label="sin=0")
# plt.plot(t1,y1, label="sin=90")
# plt.legend(loc="upper center", bbox_to_anchor=(0.5,-0.05))

## cara ketiga ( untuk memindahkan diluar tabel)
plt.figure(1)
ax = plt.subplot(111)
plt.plot(t,y, label="sin=0")
plt.plot(t1,y1, label="sin=90")
box=ax.get_position()
ax.set_position([box.x0, box.y0, box.width*0.8, box.height])
plt.legend(loc="upper center", bbox_to_anchor=(1.2,1))

# menampilkan plot

plt.show()