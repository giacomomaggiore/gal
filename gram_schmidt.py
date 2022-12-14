import math
from copy import copy 


base = [[1,2,3],[1,4,0],[1,0,0]]
base_ortonormale = copy(base)



def chiedi_base_partenza():
	print("Quanti vettori sono presenti nella base di partenza?\n")
	n = input()

def calcola_norma(vettore):
	somma_componenti = 0;
	for componente in vettore:
		somma_componenti = somma_componenti + componente*componente
	norma = math.sqrt(somma_componenti)

	return norma


def normalizza_vettore(vettore:list):
	vettore_normalizzato = []
	norma = calcola_norma(vettore)
	for i in range(len(vettore)):
		vettore[i] = vettore[i] / norma
		
	
	return vettore


def prodotto_scalare(v, w):
	prodotto = 0;
	for i in range(len(v)):
		prodotto = prodotto + v[i]*w[i]

	return prodotto

def proiezione_ortogonale(vettore:list, base):
	vettore_proiettato = copy(vettore)
	for i in range(len(vettore)):
		for j in range(len(base)):
			vettore_proiettato[i] = vettore[i] - prodotto_scalare(vettore, base[j])*base[j][i]
			
	return vettore_proiettato


vettore = [1,1,1]

def algoritmo(base_partenza, base_ortonormale):
	i = 0
	j = 0
	base_temp = copy(base_partenza)

	base_ortonormale[0] = normalizza_vettore(base[0])


	while(i < len(base_partenza)):
		while j < i:
			base_temp.append(base_ortonormale[j])

			vettore_temp = proiezione_ortogonale(base_partenza[i], base_temp)
			base_ortonormale[i] = normalizza_vettore(vettore_temp)  
			j = j+1
		i = j+1

	return base_ortonormale

def stampa_base(base):
	i = 0
	j = 0
	for vettore in base:
		print(vettore)
		

print("Ecco la tua base ortonormale")
stampa_base(algoritmo(base, base_ortonormale))