import unittest

from app.chromossome import Chromossome

class TddInPythonchromossome(unittest.TestCase):
	def setUp(self):
		self.chromossome = Chromossome(4,1,0,10)

	def teste_chromossome_getValue(self):
		result = self.chromossome.getValue('1101')
		self.assertEqual(8.666666666666666,result)


if __name__ == '__main__':
	unittest.main()