import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate


class wavefunction:

    def __init__(self, xlst, psi):
        self.x = xlst
        self.psi = psi

    def plot_initial_function(self):
        """
        Given initial inputs and outputs of a wavefunction we plot this wave function at initial
        time = 0
        """
        plt.style.use('ggplot')
        plt.plot(self.x, self.psi)
        plt.show()

    def hamiltonian(self):
        """
        Given initial wavefunction calculates the associated Hamiltonian
        """


    def probability_dist(self):
        """
        Given wavefunction, returns associated probability distribution with area 1
        """
        original_dist = (abs(self.psi))**2
        area_of_dist = integrate.quad(original_dist, -np.inf, np.inf)
        return original_dist/(abs(area_of_dist)**2)


    def evolution(self, t):
        """
        Uses
        :param t:
        :return:
        """


if __name__ == '__main__':
    x = np.linspace(-1,1,100)
    y = np.cos(x)
    wavefunction(x, y).plot_initial_function()
    integral = integrate.quad(y, -1, 1, )
    print(integral)


