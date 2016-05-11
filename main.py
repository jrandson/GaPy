#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  main.py
#  
#  Copyright 2016 Randson <randson@debian-randson>
#  


import math
import random as rand

txCros = 0.75
txMuta = 1
sizeChromossome = 4
sizePopulation = 10
qtdVar = 3

def main():
	
	minimo = -3
	maximo = 5
	p = initializePopulation(sizePopulation,sizeChromossome,qtdVar)
	c1 = p[0]
	c2 = p[1]
	
	print c1,"\n", c2
	print '-------------'
	c = cruzaChromossomo(c1,c2)
	print c[0],"\n", c[1]
	
	return 0

def ga():
	population = initializePopulation()
	while(i < qtdGen):
		population = getNewPopulation(population)
	
def initializePopulation(sizePopulation, sizeChromossome,qtdVar):
	population = []
	
	for i in range(0,sizePopulation):
		chromossome = []
		for j in range(0,qtdVar):			
			var = getNewChromossome(sizeChromossome)
			chromossome.append(var)
			
		population.append(chromossome)
	
	return population
		
def getNewChromossome(sizeChromossome):
		
	chromossome = []
	for i in range(0,sizeChromossome):
		chromossome.append(rand.randint(0,1))
		
	return chromossome;

def mutaPopulation(population):
	for i in range(0,len(population)):
		population[i] = mutaCromossomo(population[i])
		
	return population

def mutaCromossomo(chromossome):	
	for var in chromossome:		
		if(rand.random() <= txMuta):
			n = rand.randint(1,len(var))
			for i in range(0,n):
				p = rand.randint(0,len(var)-1)
				var[p] ^= 1
	
	return chromossome		

def getValorNumericoPopulacao(population):
	valores = []
	for chromossome in population:
		valorChromossome = getValorNumericoChromossomo(chromossome)
		valores.append(valorChromossome)
	
	return valores	

def getValorNumericoChromossomo(chromossome):	
	variaveis = []
	
	for var in chromossome:		
		valor= 0
		var.reverse()
		for i in range(0,len(var)):
			valor += var[i] * 2 ** (i)
		
		variaveis.append(valor)
		
	return variaveis

def normalizePopulation(valoresPopulation,maximo,minimo):

	valoresNormalizados = []
	for chromossome in valoresPopulation:
		chromossomeVarNorm = []
		
		for var in chromossome:
			valorVar = minimo + (maximo - minimo)*var*1.0/(2**sizeChromossome-1)
			chromossomeVarNorm.append(valorVar)
					
		valoresNormalizados.append(chromossomeVarNorm)
		
	return valoresNormalizados



def getNewPopulation(population):
	newPopulation = []
	chr1,chr2
	for chn in population:
		chr1 = selectChromossome()
		chr2 = selectChromossome()
		
		filhos = applyCrossover(chr1,chr2)
		
		newPopulation.append(filhos[0])
		newPopulation.append(filhos[1])
	
	return newPopulation

def cruzaPopulation(population, aptidao):
	sizePop = 0
	while(sizePop < len(population)):
		i1 = selectChromossome(aptidao)
	
	sizePop = len(population)
	
	div = len(population)/4
	
	i1 = selectChromossome(aptidao)
	i2 = (i1+ 2*div) % sizePop
	i3 = (i1 + div) % sizePop
	i4 = (i1 + 3*div) % sizePop


def cruzaChromossomo(chr1,chr2):	
	filhos = []
	
	for i in range(0, len(chr1)):		
		chrOut = applyCrossover(chr1[i],chr2[i])
		chr1[i] = chrOut[0]
		chr2[i] = chrOut[1]
	
	filhos = [chr1, chr2]
			
	return filhos

def applyCrossover(var1,var2):

	half = 	len(var1)/2
		
	for j in range(0,half):
		aux = var1[j]
		var1[j] = var2[half+j]
		var2[half+j] = aux
		
	filhos = [var1,var2]	
	return filhos
	
def selectChromossome(aptidao):
	somaRand = rand.random()*sum(aptidao)
	
	somaAcumulada = 0
	i = 0
	while(1):		
		somaAcumulada += aptidao[i]	
		if(somaAcumulada >= somaRand):			
			break
		i += 1
			
	return i
	
def getAptidao(populationNormalized):
	aptidao = []
	for chromossome in populationNormalized:
		for var in chromossome:
			pass
	
def feval(x):		
	return x**2
	
def sortPopulation(population):
	aptidao = getAptidao(population);
	# ordena população
	return population
	
def avaliaPopulacao(populacao):
	population =  sortPopulation(population)
	
def normalizeChromossome(chrmossome, minimo, maximo):
	 pass
	 
if __name__ == '__main__':
	main()







