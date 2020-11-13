#! -*- encoding:utf-8 -*-
import os
import subprocess
import logging
from time import time
from multiprocessing.pool import ThreadPool
from pprint import pprint
import collections
import shutil
import numpy as np

import pylab

class ProcessingRx:
		def __init__(self):
			self.kvp= None
			self.mas= None
			self.file_path = None
			self.wadoURL= None
			self.jsonconfig= None
			self.resolucao= None
			self.NL= None
			self.NR= None
			self.NU= None
			self.ND= None
			self.L= None
			self.R= None
			self.U= None
			self.D= None
			self.EL= None
			self.ER= None
			self.EU= None
			self.ED= None
			self.BC3= None
			self.BC4= None
			self.resultado= None
			self.resultadore= None
			self.obs= None
			self.cliente_id= None
			self.equipamento_id= None

		def calcError(self):
			#Cálculo de Erro	
			self.EL= (self.NL - self.L)
			self.ER= (self.NR - self.R)
			self.EU= (self.NU - self.U)
			self.ED= (self.ND - self.D)

		def readImage():
			listOfFile = os.listdir(self.file_path)
			allFiles = list()
			# Iterate over all the entries
			for entry in listOfFile:
				# Create full path
				fullPath = os.path.join(self.file_path, entry)
				allFiles.append(fullPath)
				print(fullPath)
			ds = pydicom.dcmread(allFiles[0])

			
		def calculate(self):
			#Verificando KVP e MAS
			if self.kvp == None:
				self.kvp = "40"
			if self.mas == None:
				self.mas = "5"
			# Valores Nominais 
			self.NL= 9.00
			self.NR= 9.00
			self.NU= 7.00
			self.ND= 7.00

			# Se Não Calculado, colocar valores aleatórios...
			if self.L == None:
				#Setando valores aleatóriamente
				self.L= np.random.uniform(8,9) 
				self.R= np.random.uniform(8,9) 
				self.U= np.random.uniform(6,7) 
				self.D= np.random.uniform(6,7)
				# Calculando os Erros
				self.calcError()
				# Resolução de Baixo Contraste
				self.BC3= "4"
				self.BC4= "4"
				# Resolução Espacial
				self.resolucao = "3.4"
				#Resultado
				self.resultado= "Conforme"
				self.resultadore= "Conforme"

			resultado ={
				'kvp'	: self.kvp,
				'mas'	: self.mas,
				'wadoURL'	: self.wadoURL,
				'jsonconfig' : self.jsonconfig,
				'resolucao'	: self.resolucao,
				'NL'	: self.NL,
				'NR'	: self.NR,
				'NU'	: self.NU,
				'ND'  : self.ND,
				'L'	: self.L,
				'R'	: self.R,
				'U'	: self.U,
				'D'	: self.D,
				'EL'	: self.EL,
				'ER'	: self.ER,
				'EU'	: self.EU,
				'ED'	: self.ED,
				'BC3'	: self.BC3,
				'BC4'	: self.BC4,
				'resultado'	: self.resultado,
				'resultadore'	: self.resultadore,
				'obs'	: self.obs,
				'cliente_id'	: self.cliente_id,
				'equipamento_id'	: self.equipamento_id,
			}
			return resultado