import unittest
from statsdistribbrian import Gaussian

class TestGaussian(unittest.TestCase):

    def test_init_no_data(self):
        gaus = Gaussian()
        self.assertIsNone(gaus.data)
        self.assertIsNone(gaus.mean)
        self.assertIsNone(gaus.stdev)

    def test_mean_calc(self):
        data = [29.0, 5.0, 16.0, -114.0, 169.0, 74.0, -3.0, 6.0, -198.0, 29.0]
        gaus = Gaussian(data)
        self.assertAlmostEqual(round(gaus.mean,4), 1.3, 4, "Error in mean calculation")

    def test_std_calc(self):
        data = [29.0, 5.0, 16.0, -114.0, 169.0, 74.0, -3.0, 6.0, -198.0, 29.0]
        gaus = Gaussian(data, is_sample_data=True)
        self.assertAlmostEqual(round(gaus.stdev,4), 99.0107, 4, "Error in sample stdev calculation")
        gaus = Gaussian(data, is_sample_data=False)
        self.assertAlmostEqual(round(gaus.stdev,4), 93.9298, 4, "Error in population stdev calculation")

    def test_pdf_x(self):
        data = [29.0, 5.0, 16.0, -114.0, 169.0, 74.0, -3.0, 6.0, -198.0, 29.0]
        gaus = Gaussian(data)
        self.assertAlmostEqual(round(gaus._Gaussian__pdf_x(2.5),8), 0.00402899,"Error in population stdev calculation")

    def test_guas_add(self):
        data_a = [29.0, 5.0, 16.0, -114.0, 169.0, 74.0, -3.0, 6.0, -198.0, 29.0]
        gaus_a = Gaussian(data_a)
        data_b = [29.0, 5.0, 16.0, 74.0, -3.0, 6.0, -198.0]
        gaus_b = Gaussian(data_b)
        data_comb = data_a + data_b
        gaus_comb = gaus_a + gaus_b
        self.assertCountEqual(gaus_comb.data, data_comb, "The two guassian data were not merged correctly")
        self.assertAlmostEqual(round(gaus_comb.mean, 4), -3.4118, "The new mean calculation is wrong")
        self.assertAlmostEqual(round(gaus_comb.stdev, 4), 91.4789, "The new stdev calculation is wrong")

    def test_histogram_no_data(self):
        gaus = Gaussian()
        with self.assertLogs('user', 'INFO') as log:
            msg = gaus.plot_histogram()
        self.assertIn('INFO:user:Distribution object is empty!', log.output)

    def test_histogram_pdf_no_data(self):
        gaus = Gaussian()
        with self.assertLogs('user', 'INFO') as log:
            msg = gaus.plot_histogram_pdf()
        self.assertIn('INFO:user:Distribution object is empty!', log.output)

if __name__ == "__main__":
    unittest.main()
