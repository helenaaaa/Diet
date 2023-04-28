import os
import ast
from ast import literal_eval
import tokenize
import string
import collections
from collections import Counter
import math
import logging
import time
import numpy as np


def directory():
	wd = os.getcwd()
	if "vernonhn" in wd:
		Directory = "/mount/studenten/arbeitsdaten-studenten1/vernonhn/Thesis/Texts"
	if "helenvernon" in wd:
		Directory = "/Users/helenvernon/github/Thesis/Texts"
	
	return Directory

Directory = directory()

def LoadTexts(file):
	Directory = directory()
	os.chdir(Directory)
	with open(file) as F:
		text = ast.literal_eval(F.read())
		content = text
		return content

def InitialiseTexts():
	JW = LoadTexts("JW_data.txt")
	SF = LoadTexts("SF_data.txt")
	FE = LoadTexts("FE_data.txt")
	IC = LoadTexts("IC_data.txt")
	PH = LoadTexts("PH_data.txt")
	FT = LoadTexts("FT_data.txt")

def InitialiseBigTexts():
	FullData = LoadTexts("FullData.txt")
	Control = LoadTexts("Control_data.txt")
	EchoChambers = LoadTexts("EchoChambers_data.txt")
	
def t():
	ts = time.ctime()
	print(ts)

def WriteFile(info, filename):
	with open (str(filename), "w+") as f:
		f.write(str(info))
		
def Sigmoid(x):
    s = 1 / (1 + np.exp(-x))
    return s


"""		
def errors():
	except Exception as e:
		print(e)
"""
