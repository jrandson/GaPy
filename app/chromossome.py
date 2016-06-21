
import random as rand
from math import pow

class Chromossome(object):

	def __init__(self,sizeChromossome, qtdVar,minimo,maximo):
		self._sizeChromossomome = sizeChromossome
		self._qtdVar = qtdVar
		self._minimo = minimo
		self._maximo = maximo

		self.setFitness(self)
		self.setGenoma()
		self.setValue()

	def setGenoma(self):
		self._genoma = []
		for i in range(self._qtdVar):
			gene = ''
			for j in range(self._sizeChromossomome):
				gene += str(rand.randint(0,1))		
			self._genoma.append(gene)

	def changeGenoma(self, genoma):
		self._genoma = genoma
		self.setValue()

	def getGenoma(self):
		return self._genoma

	def setValue(self):
		self._value = []
		for gene in self._genoma:
			value = int(gene,2)
			value = self._minimo + (self._maximo - self._minimo)*value/(pow(2,self._sizeChromossomome)-1)
			self._value.append(value)
		
	def getValue(self):
		return self._value
		
		value = int(genoma,2)
		print "value is:{}".format(value)
		print "minimo is:{}".format(self._minimo)
		print "maximo is:{}".format(self._maximo)
		
		return self._minimo + (self._maximo - self._minimo)*value/(pow(2,self._sizeChromossomome)-1) 

	def setFitness(self,fitness = 0):
		self._fitness = fitness

	def getFitness(self):
		return self._fitness




def teste():
	chromossome =  Chromossome(4,3,0,10)

	#print chromossome.getGenoma()
	print chromossome.getValue()