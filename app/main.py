#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  main.py
#  
#  Copyright 2016 Randson <randson@debian-randson>#  


import math
import random as rand

txCros = 0.8
txMuta = 0.1
txElite = 0.1
sizeChromossome = 16
sizePopulation = 50
qtdVar = 1

minimo = -10
maximo = 10

def main():		

	population = initializePopulation(sizePopulation, sizeChromossome, qtdVar)

	valuePopulation = getValuePopulation(population)
	normalizedPopulation = normalizePopulation(valuePopulation)
	fitnessPopulation = getFitnessPopulation(normalizedPopulation)
	population = avaliaPopulacao(population,fitnessPopulation)	

	l = len(population)	
	i = 0	
	bestFit = []
	bestValue = []

	while(i < 50):	
		
		population = getNewPopulation(population,fitnessPopulation)
		population = avaliaPopulacao(population,fitnessPopulation)

		valuePopulation = getValuePopulation(population)
		normalizedPopulation = normalizePopulation(valuePopulation)
		fitnessPopulation = getFitnessPopulation(normalizedPopulation)	
		
		bestValue.append(normalizedPopulation[0])
		i += 1

	for best in bestValue:
		print best
	
def initializePopulation(sizePopulation, sizeChromossome,qtdVar):
	population = []
	
	for i in range(sizePopulation):
		chromossome = getNewChromossome(sizeChromossome,qtdVar)			
		population.append(chromossome)
	
	return population
		
def getNewChromossome(sizeChromossome,qtdVar):
		
	chromossome = []
	for i in range(qtdVar):			
		var = ''
		for j in range(sizeChromossome):
			var += str(rand.randint(0,1))
		chromossome.append(var)

	return chromossome;

def mutaPopulation(population):
	for i in range(0,len(population)):
		if(rand.random() <= txMuta):
			population[i] = mutaCromossomo(population[i])
		
	return population

def mutaCromossomo(chromossome):
	newChromossome = []	
	for var in chromossome:			
		n = rand.randint(1,len(var))
		for i in range(n):
			p = rand.randint(0,len(var)-1)
			if var[p] == '1':
				c = '0'
			else:
				c = '1'
			var = var[0:p] + c +var[p+1:]
		newChromossome.append(var)

	return newChromossome		

def getValuePopulation(population):

	valores = []
	for chromossome in population:
		valorChromossome = getValueChromossome(chromossome)
		valores.append(valorChromossome)	

	return valores	

def getValueChromossome(chromossome):

	variaveis = []
	
	for var in chromossome:		
		variaveis.append(int(var,2))

	return variaveis

def normalizePopulation(valuePopulation):

	valoresNormalizados = []
	for chromossome in valuePopulation:
		chromossomeVarNorm = []		
		normalizedChromossome = normalizeChromossome(chromossome)					
		valoresNormalizados.append(normalizedChromossome)
		
	return valoresNormalizados

def normalizeChromossome(chromossome):
	chromossomeNormalized = []
	for var in chromossome:
		value = minimo + (maximo - minimo)*var*1.0/(2**sizeChromossome-1)
		chromossomeNormalized.append(value)

	return chromossomeNormalized

def getNewPopulation(population,fitnessPopulation):
	newPopulation = []

	i = 1
	while i < int(txElite*sizePopulation):
		newPopulation.append(population[i])
		i += 1

	#shifit fitness 
	maxFitness = max(fitnessPopulation)
	for i in range(len(fitnessPopulation)):
		fitnessPopulation[i] = (maxFitness - fitnessPopulation[i])/maxFitness
		
	#normalize fitness
	minFitness = min(fitnessPopulation)
	for i in range(len(fitnessPopulation)):
		fitnessPopulation[i] -= minFitness


	while len(newPopulation) < len(population):
		c1 = selectChromossome(fitnessPopulation)
		c2 = selectChromossome(fitnessPopulation)

		filhos = cruzaChromossomo(population[c1],population[c2])
		
		newPopulation.append(filhos[0])
		newPopulation.append(filhos[1])
	
	return newPopulation

def cruzaChromossomo(chr1,chr2):	

	filhos = []	
	chr1_ = []
	chr2_ = []

	for i in range(len(chr1)):		
		f1, f2  = applyCrossover(chr1[i],chr2[i])
		chr1_.append(f1)	
		chr2_.append(f2)
	
	filhos = [chr1_, chr2_]
			
	return filhos

def applyCrossover(var1,var2):

	half = 	len(var1)/2	
	var1_ = var2[half:] + var1[half:]
	var2_ = var2[0:half] + var1[0:half]
	
	return var1_ , var2_
	
def selectChromossome(fitnessPopulation):
	somaRand = rand.random()*sum(fitnessPopulation)	
	somaAcumulada = 0
	i = -1
	while(i < len(fitnessPopulation)-1):	
		i += 1	
		somaAcumulada += fitnessPopulation[i]
		if somaAcumulada >= somaRand :			
			break
	

			
	return i
	
def getFitnessPopulation(population):

	populationNormalized = normalizePopulation(population)
	fitnessPopulation = []
	for chromossome in populationNormalized:
		value = getFitnessChromossome(chromossome)
		fitnessPopulation.append(value)	

	return fitnessPopulation

def getFitnessChromossome(chromossome):
	value = 0
	for var in chromossome:
		value += feval(var)

	return value

def feval(x):
	return math.pow(x,2)
	
def sortPopulation(population,fitnessPopulation):

	if len(population) <= 1:
		return population

	# cria as sublistas dos maiores, menores e iguais ao pivo
	fitness_less, fitness_equal, fitness_greater = [], [], [] 
	population_less, population_equal, population_greater = [], [], [] 

	# escolhe o pivo. neste caso, o primeiro elemento da lista
	pivot = fitnessPopulation[0] 
	for i in range(len(population)):
		# adiciona o elemento cromossomo a lista correspondeste
	    if fitnessPopulation[i] < pivot:
	        fitness_less.append(fitnessPopulation[i])
	        population_less.append(population[i])
	    elif fitnessPopulation[i] == pivot:
	        fitness_equal.append(fitnessPopulation[i])
	        population_equal.append(population[i])
	    else:
		 	fitness_greater.append(fitnessPopulation[i])
		 	population_greater.append(population[i])			
	
	return sortPopulation(population_less,fitness_less) + population_equal + sortPopulation(population_greater,fitness_greater)
	
def avaliaPopulacao(population,fitnessPopulation):

	population =  sortPopulation(population,fitnessPopulation)
	population.reverse()
	return population
		 
if __name__ == '__main__':
	main()







