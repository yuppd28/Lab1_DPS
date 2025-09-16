# Чисельне моделювання процесів  
**Тема:** Математична модель типу «хижаки–жертви» (система Лотки–Вольтерри)  
**Варіанти:** №5 і №6  

---

## Постановка задачі
Необхідно дослідити поведінку популяцій у системі «хижаки–жертви» за моделлю Лотки–Вольтерри.  

Система рівнянь:  

dX/dt = gX - aXY

dY/dt = -sY + bXY


де  
- \(X(t)\) — кількість жертв у момент часу \(t\);  
- \(Y(t)\) — кількість хижаків у момент часу \(t\);  
- \(g\) — коефіцієнт природного приросту жертв;  
- \(s\) — коефіцієнт природної смертності хижаків;  
- \(a\) — коефіцієнт зниження чисельності жертв через зустрічі з хижаками;  
- \(b\) — коефіцієнт приросту хижаків за рахунок поїдання жертв.  

---

## Вхідні дані

### Варіант 5
- \(a = 0.01\)  
- \(b = 0.001\)  
- \(g = 0.2\)  
- \(s = 0.3\)  
- Початкові умови: \(X(0) = 100\), \(Y(0) = 40\)

### Варіант 6
- \(a = 0.02\)  
- \(b = 0.002\)  
- \(g = 0.1\)  
- \(s = 0.2\)  
- Початкові умови: \(X(0) = 100\), \(Y(0) = 40\)

---

## Код реалізації
<pre>
import numpy as np
import matplotlib.pyplot as plt

def lotka_volterra(a, b, g, s, X0=100, Y0=40, t_max=200, dt=0.1):
    def dX_dt(X, Y): return g*X - a*X*Y
    def dY_dt(X, Y): return -s*Y + b*X*Y
    
    t = np.arange(0, t_max, dt)
    X, Y = np.zeros(len(t)), np.zeros(len(t))
    X[0], Y[0] = X0, Y0
    
    for i in range(len(t)-1):
        k1x, k1y = dX_dt(X[i], Y[i]), dY_dt(X[i], Y[i])
        k2x, k2y = dX_dt(X[i] + dt*k1x/2, Y[i] + dt*k1y/2), dY_dt(X[i] + dt*k1x/2, Y[i] + dt*k1y/2)
        k3x, k3y = dX_dt(X[i] + dt*k2x/2, Y[i] + dt*k2y/2), dY_dt(X[i] + dt*k2x/2, Y[i] + dt*k2y/2)
        k4x, k4y = dX_dt(X[i] + dt*k3x, Y[i] + dt*k3y), dY_dt(X[i] + dt*k3x, Y[i] + dt*k3y)
        
        X[i+1] = X[i] + dt*(k1x + 2*k2x + 2*k3x + k4x)/6
        Y[i+1] = Y[i] + dt*(k1y + 2*k2y + 2*k3y + k4y)/6
    
    return t, X, Y

# Варіант 5
t5, X5, Y5 = lotka_volterra(a=0.01, b=0.001, g=0.2, s=0.3)

# Варіант 6
t6, X6, Y6 = lotka_volterra(a=0.02, b=0.002, g=0.1, s=0.2)
</pre>

Ілюстрація динаміки зміни розміру популяцій хижаків та жертв:
<img width="1190" height="526" alt="image" src="https://github.com/user-attachments/assets/5a2f4e98-b587-49ff-bfe9-29a19623dda5" />
Побудова фазового простору
<img width="940" height="435" alt="image" src="https://github.com/user-attachments/assets/3962b271-97eb-4951-b689-ad52c20960c9" />

