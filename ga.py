import numpy as np 

from numpy import array
from numpy.random import randn, randint, rand
from numpy.linalg import inv,qr
from random import normalvariate

from matplotlib import pyplot as plt


data = array([[ 0.9526, -0.246 , -0.8856],
				[ 0.5639, 0.2379, 0.9104]])

#data.shape() 
#data.dtype() # tipo de dados no array

#np.zeros(10)
#np.zeros((2,4))

#calibers = np.array([.22, .270, .357, .380, .44, .50], dtype=np.float64)

#arr_slice = arr[3:5].copy()
#d1.dot(d2)

class GA():

	_tx_cross = 0.75
	_tx_muta = 0.05

	_size_pop = 0
	_size_chromossome = 0
	_n = 0

	_population = []

	_max = -500
	_min = 500;

	best_chr_arr = []
	best_fit_arr = []

	def __init__(self, size_pop, size_chromossome, n=1):
		self._size_pop = size_pop
		self._size_chromossome = size_chromossome
		self._n = n

		self.init_population()
		self.best_chr_arr = []
		self.best_fit_arr = []

	def run(self,qtd_gen=50):

		for i in range(qtd_gen):
			self.get_new_pop()
			self.apply_mutacao()

			best = self.get_best_chr()
			self.best_chr_arr.append(best)
			
			self.best_fit_arr.append(self.feval(best.get_value()))

		plt.plot(self.best_fit_arr,'r*-')
		plt.ylabel('best by generations')
		plt.show()

		return self.best_chr_arr[-1]

	def get_best_chr(self):
		best = self._population[0]

		for chromossome in self._population:

			if chromossome.get_fitness() < best.get_fitness():
				best = chromossome

		return best

	def init_population(self):
		pop = []
		for i in range(self._size_pop):
			chr = Chromossome(self._size_chromossome, val_min = self._min, val_max = self._max, dim=self._n)
			chr.set_fitness(self.feval(chr.get_value()))
			pop.append(chr)

		self._population = array(pop)

	def cruza_chromossome(self, chr1,chr2):
		h = self._size_chromossome/2

		#0101 10111
		#0110 11011
		chr1_ = []
		chr2_ = []
		for i in range(len(chr1)):
			dim1 = chr1[i]
			dim2 = chr2[i]
			
			dim1_ = dim2[h:] + dim1[h:]
			dim2_ = dim2[:h] + dim1[:h]

			chr1_.append(dim1_)
			chr2_.append(dim2_)

		return (chr1_, chr2_)
	
	def seleciona_chromossome(self):
		i1 = randint(0,self._size_pop)
		i2 = randint(0,self._size_pop)

		chr1 = self._population[i1]
		chr2 = self._population[i2]

		if self.feval(chr1.get_value()) < self.feval(chr2.get_value()):
			return chr1
		else:
			return chr2

	def apply_mutacao(self):
		for i in range(len(self._population)):
			if rand() <= self._tx_muta:
				self._population[i] = self.muta_chromossome(self._population[i])

	def muta_chromossome(self,chromossome):
		genoma_ = []
		for v in chromossome.get_genoma():			
			lista = list(v)
			i =  randint(0,self._size_chromossome)
			if lista[i] == '0':
				lista[i] = '1'
			else:
				lista[i] = '0'
			
			c = ''
			for i in lista:
				c += i
			genoma_.append(c)

		chromossome._genoma = genoma_
		return chromossome
	
	def get_new_pop(self):
		new_pop = []
		while len(new_pop) < self._size_pop:
			chr1 = self.seleciona_chromossome()
			chr2 = self.seleciona_chromossome()
 
			if  rand() <= self._tx_cross:
				[genoma1, genoma2] = self.cruza_chromossome(chr1.get_genoma(), chr2.get_genoma())			
				
				chr1._genoma = genoma1
				chr2._genoma = genoma2
			
			new_pop.append(chr1)
			new_pop.append(chr2)

		self._population = array(new_pop)
	
	def feval(self, chromossome_value):
		x = chromossome_value
		return 10 + sum(x ** 2)

class Chromossome(object):
	"""docstring for Chromossome"""
	def __init__(self, size_chromossome, val_min = 0, val_max = 1, dim=1):
		super(Chromossome, self).__init__()
		self._fitness = 0
		self._size_chromossome = size_chromossome
		self._genoma = self.generate_genoma(dim)
		self._min = val_min
		self._max = val_max
		self._dim = dim
		self._value = self._normalize_chromossome()


	def _normalize_chromossome(self,):
		max_chr = 2.0**self._size_chromossome-1
		valor = []
		for i in self._genoma:
			norma = self._min + (self._max - self._min)*int(i)/max_chr
			valor.append(norma)

		return array(valor)

	def generate_genoma(self,dim):
		genoma = []		
		for n in range(dim):
			chr = ''
			for i in range(self._size_chromossome):
				chr += str(randint(0,2))

			genoma.append(chr)

		return genoma

	def get_value(self):
		return self._value

	def set_fitness(self, fitness):
		self._fitness = fitness

	def get_fitness(self):
		return self._fitness

	def get_genoma(self):
		return self._genoma
		
		


ga = GA(5,8,1)

#ga.run()



