import os
import numpy as np
import matplotlib.pyplot as plt


# Khairu Reza Al Haris
# 21120122140167
# Implementasi Interpolasi dengan Metode Lagrange dan Newton
# Metode Numerik D

# data interpolasi
x = np.array([5, 10, 15, 20, 25, 30, 35, 40])
y = np.array([40, 30, 25, 40, 18, 20, 22, 15])


# Interpolasi Lagrange
def lagrange_interpolation(x, y, xi):
    def basis(i, xi):
        p = [(xi - x[j]) / (x[i] - x[j]) for j in range(len(x)) if j != i]
        return np.prod(p)

    yi = sum(y[i] * basis(i, xi) for i in range(len(x)))
    return yi


# Interpolasi Newton
def newton_interpolation(x, y, xi):
    n = len(x)
    divided_diff = np.zeros((n, n))
    divided_diff[:, 0] = y
    for j in range(1, n):
        for i in range(n - j):
            divided_diff[i, j] = (divided_diff[i + 1, j - 1] - divided_diff[i, j - 1]) / (x[i + j] - x[i])

    def newton_basis(xi, k):
        product = 1.0
        for j in range(k):
            product *= (xi - x[j])
        return product

    yi = divided_diff[0, 0]
    for k in range(1, n):
        yi += divided_diff[0, k] * newton_basis(xi, k)
    return yi


# plot
def plot_interpolation(method, x, y, xi):
    if method == 'lagrange':
        yi = [lagrange_interpolation(x, y, i) for i in xi]
        label = 'Lagrange Interpolation'
        line_style = '-'
    elif method == 'newton':
        yi = [newton_interpolation(x, y, i) for i in xi]
        label = 'Newton Interpolation'
        line_style = '--'
    else:
        raise ValueError("Invalid method. Choose 'lagrange' or 'newton'.")

    plt.figure(figsize=(10, 6))
    plt.plot(x, y, 'o', label='Data points')
    plt.plot(xi, yi, line_style, label=label)
    plt.xlabel('Tegangan, x (kg/mm²)')
    plt.ylabel('Waktu patah, y (jam)')
    plt.title('Interpolasi Polinom {}'.format(label))
    plt.legend()
    plt.grid(True)
    plt.show()



def main():
    xi = np.linspace(5, 40, 500)

    # Plot lagrange
    plot_interpolation('lagrange', x.copy(), y.copy(), xi.copy()) 

    # Plot Newton
    plot_interpolation('newton', x.copy(), y.copy(), xi.copy()) 

if __name__ == "__main__":
    main()
