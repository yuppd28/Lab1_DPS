import numpy as np
import matplotlib.pyplot as plt


def lotka_volterra(a, b, g, s, X0=100, Y0=40, t_max=200, dt=0.1):
    def dX_dt(X, Y):
        return g * X - a * X * Y

    def dY_dt(X, Y):
        return -s * Y + b * X * Y

    t = np.arange(0, t_max, dt)
    X = np.zeros(len(t))
    Y = np.zeros(len(t))
    X[0], Y[0] = X0, Y0

    for i in range(len(t) - 1):
        k1x = dX_dt(X[i], Y[i])
        k1y = dY_dt(X[i], Y[i])

        k2x = dX_dt(X[i] + dt * k1x / 2, Y[i] + dt * k1y / 2)
        k2y = dY_dt(X[i] + dt * k1x / 2, Y[i] + dt * k1y / 2)

        k3x = dX_dt(X[i] + dt * k2x / 2, Y[i] + dt * k2y / 2)
        k3y = dY_dt(X[i] + dt * k2x / 2, Y[i] + dt * k2y / 2)

        k4x = dX_dt(X[i] + dt * k3x, Y[i] + dt * k3y)
        k4y = dY_dt(X[i] + dt * k3x, Y[i] + dt * k3y)

        X[i + 1] = X[i] + dt * (k1x + 2 * k2x + 2 * k3x + k4x) / 6
        Y[i + 1] = Y[i] + dt * (k1y + 2 * k2y + 2 * k3y + k4y) / 6

    return t, X, Y


# --- Варіант 5 ---
t5, X5, Y5 = lotka_volterra(a=0.01, b=0.001, g=0.2, s=0.3)

# --- Варіант 6 ---
t6, X6, Y6 = lotka_volterra(a=0.02, b=0.002, g=0.1, s=0.2)

# Побудова графіків
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(t5, X5, label="Жертви")
plt.plot(t5, Y5, label="Хижаки")
plt.title("Варіант 5")
plt.xlabel("Час")
plt.ylabel("Популяція")
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(t6, X6, label="Жертви")
plt.plot(t6, Y6, label="Хижаки")
plt.title("Варіант 6")
plt.xlabel("Час")
plt.ylabel("Популяція")
plt.legend()

plt.show()

# Фазові портрети
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.plot(X5, Y5)
plt.title("Фазовий портрет (Варіант 5)")
plt.xlabel("Жертви")
plt.ylabel("Хижаки")

plt.subplot(1, 2, 2)
plt.plot(X6, Y6)
plt.title("Фазовий портрет (Варіант 6)")
plt.xlabel("Жертви")
plt.ylabel("Хижаки")

plt.show()
