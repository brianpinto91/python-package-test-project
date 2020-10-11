class Base():
    """Generic class to read and store data values.

    Attributes:
        data (list of floats): a list of floats extracted from the file
        is_sample_data (bool): whether the data is sample or population
            (default=True)

    Parameters:
        data (string or list of floats): string representing the file_name
            to read the data values or data directly passed as a list
        is_sample_data (bool): whether the data is sample or population
            (default=True)

    Returns:
        self (object): a distribution object of self
    """

    def __init__(self, data=None, is_sample_data = True):
        self.data = []
        self.is_sample_data = is_sample_data

        if type(data) == type([]):
            self.data = data
        elif type(data) == str:
            with open(data) as file:
                data_list = []
                line = file.readline()
                while line:
                    data_list.append(float(line.strip()))
                    line = file.readline()
                file.close()
            #if elements are less than zero then division by zero would happen
            #while computing sample standard distribution  of gaussian
            self.data = None if (len(data_list) < 2) else data_list
        else:
            self.data = None

    def add_data(self, data):
        """Function to add data to the distribution object.
            If the object already contains data, the new data will be appended
            to it.
        Args:
            data (list): list of float values
        Returns:
            None
        """
        if self.data is not None:
            self.data += data
        else:
            self.data = data
