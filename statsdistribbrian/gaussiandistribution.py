import math
import matplotlib.pyplot as plt
import logging
from ._base import Base

class Gaussian(Base):
    """A class file to represent gaussian distribution data, calculate the basic
        statistics, visualize the histogram and probability density function.

    Attributes:
        mean (float) mean of the dataset (default = None)
        stdev (float) standard deviation of the dataset (default = None)
        data (list of floats) a list of floats representing the data (default = None)

    Parameters:
        data (string or list of floats) string representing the file_name
            to read the data values.
        is_sample_data (bool) whether the data is sample or population
            (default = True)
    """

    def __init__(self, data = None, is_sample_data = True):
        super(Gaussian, self).__init__(data)
        if self.data == None:
            self.mean = None
            self.stdev = None
        else:
            self.mean = self.__calculate_mean()
            self.stdev = self.__calculate_stdev(is_sample_data)

    def __calculate_mean(self):
        """function to calculate the mean of the data considering the distribution
            is Gaussian. The function is private and the mean can be accessed as
            an attribute of the created object.

        Args:
            None

        Params:
            None
        """

        return sum(self.data)/len(self.data)

    def __calculate_stdev(self, is_sample_data):
        """function to calculate the standard distribution of the data considering
            the distribution is Gaussian. The function is private and the standard
            deviation can be accessed as an attribute of the created object.

        Args:
            None

        Params:
            None
        """

        if is_sample_data:
            num_samples = len(self.data) - 1
        else:
            num_samples = len(self.data)

        variance = sum([(x-self.mean)**2 for x in self.data]) / num_samples
        return math.sqrt(variance)

    def plot_histogram(self):
        """Function to output a histogram of the data using matplotlib pyplot library.

		Args:
			None

		Returns:
			None
		"""

        if self.data is not None:
            plt.hist(self.data)
            plt.title('Histogram of Data')
            plt.xlabel('data')
            plt.ylabel('count')
        else:
            logging.warning("Distribution object is empty!")

    def __prob_x(self, x):
        """Function to calculate the probability of a value from its Gaussian
            distribution. Ideally the probaility of a data point is zero in a
            continuous distribution. But here we calculate it for plotting the
            probability distribution function.

		Args:
			x (float): data point for calculating its probability.

		Returns:
			float: probability of occurance
		"""

        return (1.0 / (self.stdev * math.sqrt(2*math.pi))) * math.exp(-0.5*((x - self.mean) / self.stdev) ** 2)

    def plot_histogram_pdf(self, n_spaces = 50):
        """Function to plot the normalized histogram of the data and a plot of the
		    probability density function along the same range.

		Args:
			n_spaces (int): is used to divide the range of data values into
                 equal intervals. The probability values are computed at these
                 points and is used to draw the probability density function.
                 (defualt = 50)

        Returns:
			None
		"""

        if self.data is not None:
            mu = self.mean
            sigma = self.stdev
            min_range = min(self.data)
            max_range = max(self.data)

            # calculates the interval between x values
            interval = 1.0 * (max_range - min_range) / n_spaces

            x = []
            y = []

            # calculate the x and y values to visualize the pdf
            for i in range(n_spaces):
                tmp = min_range + interval*i
                x.append(tmp)
                y.append(self.__prob_x(tmp))

            # make the plots
            plt.hist(self.data, density=True)
            plt.plot(x, y)
            plt.title('Normed histogram and probability distribution function')
            plt.xlabel('density')
            plt.ylabel('values')
            plt.show()
        else:
            logging.warning("Distribution object is empty!")

    def __add__(self, other):
        """Function to add together two Gaussian distributions

		Args:
			other (Gaussian): Gaussian instance

		Returns:
			Gaussian (object): combined gaussian object
		"""

        result = Gaussian(self.add_data(other.data))
        return result

    def __repr__(self):
        """Function to output the characteristics of the Gaussian instance

		Args:
			None

		Returns:
			string: characteristics of the Gaussian
		"""
        if self.data is not None:
            return "mean {:.2f}, standard deviation {:.2f}".format(self.mean, self.stdev)
        else:
            return "The Gaussian object has not data"
