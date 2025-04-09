import numpy as np
import matplotlib.pyplot as plt

A = 1
f = 120
N = 1000
dt = 0.001e-3

t = np.arange(N) * dt
signal = A * np.sin(2 * np.pi * f * t)

plt.figure(figsize=(10, 4))
plt.plot(t, signal)
plt.title("Изначальный сигнал")
plt.xlabel("Время (с)")
plt.ylabel("Амплитуда (В)")
plt.grid()
plt.show()

fft_result = np.fft.fft(signal)
frequencies = np.fft.fftfreq(N, dt)

amplitudes = (2 / N) * np.abs(fft_result)

target_frequency = 120
index_120hz = np.argmin(np.abs(frequencies - target_frequency))

print(f"Амплитуда на 120 Гц (из FFT): {amplitudes[index_120hz]:.2f} V")
print(f"Аналитическая амплитуда: {A / 2:.2f} V")

plt.plot(frequencies[:N//2], amplitudes[:N//2])
plt.title("Спектр сигнала")
plt.xlabel("Частота (Гц)")
plt.ylabel("Амплитуда (В)")
plt.grid()
plt.show()

