import numpy as np
import matplotlib.pyplot as plt

# membuat data
def sinusGenerator(amplitudo,frekuensi,tAkhir,theta):
    t = np.arange(0,tAkhir,0.1)
    y = amplitudo * np.sin(2*frekuensi*t + np.deg2rad(theta))
    return t,y

amplitudo = 1
frekuensi = 1
theta = 0
tAkhir = 4

t,y = sinusGenerator(amplitudo,frekuensi,tAkhir,theta)

judul =  'Grafik Sinusoidal\n'
rumus = r'$ \mathcal{Y} = A.sin(2 \omega t = \theta)$' + '\n'
parameter1 = r'$ A = $' + str(amplitudo) + ' cm, '
parameter2 = r'$ \omega = $' + str(frekuensi) + r'$ \mathit{Hz} $' + ','
parameter3 = r'$ \theta =  $' + str(theta) + r'$^{o} $'

# membuat plot
plt.plot(t,y)
plt.title(judul + rumus + parameter1 + parameter2 + parameter3) # menambakan Title diatas tabel
plt.xlabel('waktu(detik)') # menambakan Title di kiri atau x pada tabel
plt.ylabel('magnituda(cm)') # menambakan Title di bawah atau y pada tabel
# apabila tabel 3D gunakan plt.zlabel

# menampilkan plot
plt.show()