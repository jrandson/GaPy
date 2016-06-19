class ga(object):
	
	def __init__(self):
		pass
	
	def ga(self):
		population = initializePopulation()
		while(i < qtdGen):
			population = getNewPopulation(population)

	def initializePopulation(self, sizePopulation, sizeChromossome):
		population
		for i in range(0,sizeChromossome-1):
			chromossome = getNewChromossome()
			population.append()
		
		return population

	def getNewChromossome(self,sizeChromossome):
		
		chromossome = []
		for i in range(0,sizeChromossome):
			chromossome.append(ran.randint(0,1))
			
		return chomossome;

	def mutaPopulation(self,population):
		for i in range(0,len(population)):
			population[i] = mutaCromossomo(population[i])
			
		return population
		
	def cruzaPopulation(self, population):
		pass

	def getNewPopulation(self, population):
		newPopulation = []
		chr1,chr2
		for chn in population:
			chr1 = selectChromossome()
			chr2 = selectChromossome()
			
			filhos = applyCrossover(chr1,chr2)
			
			newPopulation.append(filhos[0])
			newPopulation.append(filhos[1])
		
		return newPopulation
		
	def mutaCromossomo(self, chromossome):		
		pass
		
	def applyCrossover(self, chr1,chr2):
		half = 	4
		for i in range(0,half-1):
			aux = chr1[i]
			chr1[i] = chr2[half+i]
			chr2[half+i] = aux
		
		filhos = [chr1,chr2]
		
		return filhos
		
	def selectChromossome(self, population):
		i = 10
		chromossome = population[i]
		
		return chromossome
		
	def getAptidao(self, population):
		pass
		
	def feval(x):		
		return x**2
		
	def sortPopulation(self, population):
		aptidao = getAptidao(population);
		# ordena população
		return population
		
	def avaliaPopulacao(self, populacao):
		population =  sortPopulation(population)
		
	def normalizeChromossome(self, chrmossome, minimo, maximo):
		 pass

class Chromossome(object):
	"""docstring for Chromossome"""
	def __init__(sizeChromossome, qtdVar):
		self._sizeChromossomome = sizeChromossome
		self._qtdVar = qtdVar
		self.getNoma = self.getGenoma(self)
		self.getValue = self.computeValue(self)


	def getGenoma(self):
		return ''

	def getValue(self):
		return self._value

	def computeValue(self):
		return 0

	def setFitness(self,setFitness):
		self._fitness = _fitness

	def getFitness(self):
		return self._fitness
