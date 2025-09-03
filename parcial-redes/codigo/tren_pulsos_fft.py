# Punto 3 - Parcial Redes
# Código en Python: Transformada de Fourier de un tren de pulsos

import numpy as np
import matplotlib.pyplot as plt

# Crear el tiempo
fs = 1000
T = 1/fs
t = np.arange(0, 0.01, T)

# Tren de pulsos
periodo = 0.002
duty = 0.5
signal = ((t % periodo) < (periodo * duty)).astype(float)

# Gráfica en el tiempo
plt.plot(t*1000, signal)
plt.title("Tren de pulsos en el tiempo")
plt.xlabel("Tiempo (ms)")
plt.ylabel("Amplitud")
plt.grid(True)
plt.show()

# Transformada de Fourier
N = len(signal)
fft_result = np.fft.fft(signal)
freq = np.fft.fftfreq(N, T)
magnitude = np.abs(fft_result) / N

# Gráfica en frecuencia
plt.stem(freq, magnitude, basefmt=" ")
plt.title("FFT del tren de pulsos")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Magnitud")
plt.grid(True)
plt.show()
