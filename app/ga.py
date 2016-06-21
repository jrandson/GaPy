
import math
from random import randint
from random import random
import pylab

from chromossome import Chromossome 

class GA(object):
	
	_txMutacao = 0.1
	_txtCrosover = 0.85
	_txtElite = 0.1
	_minimize = False

	def __init__(self,sizePopulation, qtdVar, sizeChromossome, minimo, maximo):
		self._sizePopulation = sizePopulation
		self._qtdVar = qtdVar
		self._sizeChromossome = sizeChromossome
		self._minimo = minimo
		self._maximo = maximo

		self.initializePopulation()

	def compute(self):
	
		i = 0	
		best = []
		T = 1000
		population = self._population
		self.computeFitness()
		self.ranksPopulation()

		melhores = []

		while(i < T):				
			
			self.getNewPopulation()
			self.computeFitness()
			self.ranksPopulation()	

			self.showPopulation()

			best.append(self._population[self._sizePopulation-1])			
			
			i += 1
		
		values = [c.getValue() for c in best]
		
		t = range(len(values))
		values = [values[i] for i in range(0,len(values),10)]
		pylab.plot(values,'*')

		pylab.xlabel('Geracao')
		pylab.ylabel('Best')
		pylab.title('Evolucao do AG')
		pylab.grid(True)
		pylab.show()

		return population

	def showPopulation(self):
		print ""
		for c in self._population:
			print c.getValue()
		print ""

	def initializePopulation(self):
		self._population = []
		for i in range(self._sizePopulation):
			chromossome = Chromossome(self._sizeChromossome, self._qtdVar, self._minimo, self._maximo)
			self._population.append(chromossome)

		return self._population

	def getPopulation(self):
		return self._population

	def mutaPopulation(self):
		for i in range(len(self._population)):
			muta = random()
			if muta <= self._txMutacao:
				self._population[i] = self.mutaCromossomo(self._population[i])
	
	def mutaCromossomo(self, chromossome):	
		new_genoma = []
		genoma = chromossome.getGenoma()
		for gene in genoma:			
			n = randint(1,len(gene))
			for i in range(n):
				p = randint(0,n-1)
				if gene[p] == '1':
					c = '0'
				else:
					c = '1'
				var = gene[0:p] + c + gene[p+1:]
			new_genoma.append(var)

		chromossome.changeGenoma(new_genoma)

		return chromossome

	def getNewPopulation(self):

		newPopulation = []

		iElite = int(self._txtElite * self._sizePopulation)
		for i in range(iElite):
			newPopulation.append(self._population[i])


		fitnessPopulation = [chromossome.getFitness() for chromossome in self._population]		
		minFitness = min(fitnessPopulation)
		maxfitness = max(fitnessPopulation)
		shifftFitnessPopulation = [(fitness - minFitness) for fitness in fitnessPopulation]
		qtdCross = 0
		while len(newPopulation) < self._sizePopulation:	

			chr1 = self.selectChromossome(shifftFitnessPopulation)
			chr2 = self.selectChromossome(shifftFitnessPopulation)
			
			cruza = random()
			if cruza <= self._txtCrosover:
				chr1, chr2 = self.applyCrossover(chr1,chr2)
				qtdCross += 1
			
			newPopulation.append(chr1)
			newPopulation.append(chr2)
		
		self._population = newPopulation		
		self.mutaPopulation()
		return self._population
				
	def applyCrossover(self, chr1,chr2):

		genoma1 = chr1.getGenoma()
		genoma2 = chr2.getGenoma()

		new_genoma1 = []
		new_genoma2 = []

		for i in range(len(genoma1)):
			half = 	self._sizeChromossome / 2	
			gene1 = genoma2[i][half:] + genoma1[i][half:]
			gene2 = genoma2[i][0:half] + genoma1[i][0:half]

			new_genoma1.append(gene1)
			new_genoma2.append(gene2)

		chr1.changeGenoma(new_genoma1)
		chr2.changeGenoma(new_genoma2)

		return chr1,chr2
		
	def selectChromossome(self,normFitnessPopulation):	

		somaRand = random()*sum(normFitnessPopulation)
		
		somaAcumulada = 0
		i = 0
		while(i < self._sizePopulation):					
			somaAcumulada += normFitnessPopulation[i]
			if somaAcumulada >= somaRand :			
				break
			i += 1	

		return self._population[i]
		
	def computeFitness(self):
		
		fitnessPopulation = []
		for i in range(self._sizePopulation):
			value = self._population[i].getValue()
			fitness = self.feval(value)
			fitnessPopulation.append(fitness)

		if self._minimize:
			maxfitness = max(fitnessPopulation)+0.1
			for i in range(len(fitnessPopulation)):
				fitness = (maxfitness - fitnessPopulation[i]) / (1.0*maxfitness)
				self._population[i].setFitness(fitness)
		else:
			for i in range(len(fitnessPopulation)):
				self._population[i].setFitness(fitnessPopulation[i])
		
	def feval(self,value):
		fitness = 0
		for i in value:
			fitness += i

		return fitness		
	
	# ordem crescente
	def ranksPopulation(self):
		self._population = self.sortPopulation(self._population)
		self._population.reverse()

	def sortPopulation(self,population):
		if len(population) <= 1:
			return population

		# cria as sublistas dos maiores, menores e iguais ao pivo
		population_less, population_equal, population_greater = [], [], [] 

		# escolhe o pivo. neste caso, o primeiro elemento da lista
		pivot = population[0].getFitness()
		for i in range(len(population)):
			# adiciona o elemento cromossomo a lista correspondeste
		    if population[i].getFitness() < pivot:
		        population_less.append(population[i])
		    elif population[i].getFitness() == pivot:
		        population_equal.append(population[i])
		    else:
			 	population_greater.append(population[i])			
		
		return self.sortPopulation(population_less) + population_equal + self.sortPopulation(population_greater)
		
	def avaliaPopulacao(self, populacao):
		population =  sortPopulation(population)

#-----------------------------Testes ---------------------------------------

def testRanksPopulation(ga):
	ga.computeFitness()
	pop = ga.getPopulation()

	for c in pop:
		print c.getFitness()

	ga.ranksPopulation()
	pop = ga.getPopulation()

	print ""
	for c in pop:
		print c.getFitness()

def testSelectPopulation(pop):	

	fitnessPopulation = [chromossome.getFitness() for chromossome in pop]
	minFitness = min(fitnessPopulation)
	maxfitness = max(fitnessPopulation)
	shiffitFitnessPopulation = [(fitness - minFitness) for fitness in fitnessPopulation]
	normFitnessPopulation = [(maxfitness - fitness)/(1.0*maxfitness) for fitness in shiffitFitnessPopulation]

	for c in pop:
		print c.getFitness()

	chr1 = ga.selectChromossome(normFitnessPopulation)

	print ""
	print chr1.getFitness()

def testCrossover():
	print pop[0].getGenoma()
	print pop[1].getGenoma()
	print "======================"
	ga.applyCrossover(pop[0],pop[1])
	print pop[0].getGenoma()
	print pop[1].getGenoma()

def testMutacao(pop):

	for p in pop:
		print p.getValue()

	print "======================"

	ga.mutaPopulation()

	pop = ga.getPopulation()
	for p in pop:
		print p.getValue()

def testGA(ga):
	best = ga.compute()

	for b in best:
		print b.getValue()

ga = GA(10,1,16,0,100)
pop = ga.getPopulation()

testGA(ga)



'''
t = arange(0.0, 2.0,0.01)
y = sin(2*pi*t)
plot(t, y)
 
xlabel('Tempo (s)')
ylabel('Voltagem (mV)')
title('Mais simples impossivel, brothers')
grid(True)
 
show()'''