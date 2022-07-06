import numpy as np
import matplotlib.pyplot as plt
import math

class Lagrange():
	x = np.array([], dtype = float)
	y = np.array([], dtype = float)
	n = 0
	
	def __init__(self, x_array_input, y_array_input, count):
		self.x = x_array_input
		self.y = y_array_input
		self.n = count
		
	def Lagrange_polynomial(self, x_input):
		y_output = 0.0
		for i in range(self.n):
			w = 1.0
			for j in range(i):
				w *= (x_input - self.x[j]) / (self.x[i] - self.x[j])
			for j in range(i + 1, self.n):
				w *= (x_input - self.x[j]) / (self.x[i] - self.x[j])
			y_output += self.y[i] * w
		return y_output
		
	def Lagrange_polynomial_error(self, x_input, error):
		y_error = 0.0
		for i in range(self.n):
			w = 1.0
			for j in range(i):
				w *= (x_input - self.x[j]) / (self.x[i] - self.x[j])
			for j in range(i + 1, self.n):
				w *= (x_input - self.x[j]) / (self.x[i] - self.x[j])
			y_error += error * abs(w)
		return y_error
	
def main():
	x = np.array([0, 1.75, 3.5, 5.25, 7])
	y = np.array([0, -1.307, -2.211, -0.927, -0.871])
	polynomial = Lagrange(x, y, x.size)
	x_plot_table = np.linspace(0, 7, 50, dtype = float)
	y_plot_table = np.linspace(0, 0, 50, dtype = float)
	y_plot_table_of_original = np.linspace(0, 0, 50, dtype = float)
	x = np.append(x, 2.555)
	y = np.append(y, polynomial.Lagrange_polynomial(2.555))
	for i in range(50):
		y_plot_table[i] = polynomial.Lagrange_polynomial(x_plot_table[i])
		y_plot_table_of_original[i] = math.cos(x_plot_table[i]) - 2 ** (0.1 * x_plot_table[i])
	fig, ax = plt.subplots()
	plt.plot(x_plot_table, y_plot_table, 'b-', label = 'Lagrange')
	plt.plot(x_plot_table, y_plot_table_of_original, 'm--', label = 'Original')
	plt.plot(x, y, 'r*')
	plt.xlabel('x')
	plt.ylabel('y')
	plt.annotate('f(x) ~ ' + str(y[y.size - 1]), xy=(x[x.size - 1], y[y.size - 1]), xytext=(x[x.size - 1], y[y.size - 1] - 0.32),
             arrowprops=dict(facecolor='black', shrink=0.05),
             )
	absolute_error = polynomial.Lagrange_polynomial_error(2.555, 0.0005)
	plt.text(1.0, 0.0, 'Abs. error = ' + str(absolute_error))
	plt.text(1.0, -0.1, 'Rel. error = ' + str(-absolute_error / y[y.size - 1]))
	plt.legend(loc='upper right')
	#plt.text(x[5], y[5] - 0.32, 'f(x) ~ ' + str(y[5]))
	plt.show()
	
if __name__ == '__main__':
    main()