from collections import namedtuple
from random import seed
from random import randint
import random
import os

Questions = [None] * 10 ## Sets empty array for questions to be stored
Answers = [None] * 10 ## Sets empty array for answers to be stored
Answered = [0] * 10 ## Sets simple bool type array to designate questions that have been answered correctly 
j = 0
#cmd = 'call F:\Commands\startVM.bat'
#os.system(cmd)
def genContentsQ(file_name, contents, j): ## Functions to generate questions
	Questions[j] =  "It is suspected that the suspect has been looking at mammals, what is the content of " + file_name
	Answers[j] = contents
	

def genDeleteContentQ(file_name, contents, j):
	Questions[j] =  "It is suspected that the suspect has been looking at mammals and deleted the evidence, what is the content of " + file_name
	Answers[j] = contents
	j+1

def genFileTypeQ(file_name, contents, j):
	Questions[j] =  "It is suspected that the suspect has been looking at mammals and disguised the evidence, what is the content of " + file_name
	Answers[j] = contents
	j+1

##List storing all possible evidence and details
Evidences =[
('download (1)','image', 'Polar Bear'),
('download (2)','image', 'Squirrel'),
('download (3)','image', 'Lemur'),
('download (4)','image', 'Fox'),
('download (5)','image', 'Elephant'),
('download (6)','image', 'Cappybara'),
('download (7)','image', 'Rhino'),
('download (8)','image', 'Red Panda'),
('download (9)','image', 'Dolphin'),
('download','image', 'Orangutan'),
]
print ("Insert Seed")
sn = input() #Setting the seed for rand number gen
seed(sn)
i = 0
Evidence = [None] * 10 #Array for storing selected evidence

while i < 10:
	y = randint(0,9)
	fileSelect = y
	
	x = 0 
	## allows first evidence in array automatically
	if i == 0:
		Evidence[i] = fileSelect
		i = i + 1
	elif i != 0:
		while x < i: ##checks if next selected evidence has already been selected
			if fileSelect != Evidence[x]:
				x = x + 1
			else:
				break
		if x == i: ##If not already selected adds to array
			Evidence[i] = fileSelect
			i = i + 1
	else: ##failsafe -- should never be called
		i = i + 1
	
	value = randint(1, 2)
	
	while (i-1) == j:  ##only generates question when evidence is not duplicated
		if value == 1:  ##selects evidence to be moved into vm
			cmd = 'call moveFile.bat ' + Evidences[Evidence[i-1]][0]
			os.system(cmd)
			genContentsQ(Evidences[Evidence[i-1]][0], Evidences[Evidence[i-1]][2], j) ##calls funtion to generate a question about the contents
			j = j+1

		elif value == 2:
 			cmd = 'call moveDelete.bat ' + Evidences[Evidence[i-1]][0]
 			os.system(cmd)
			genDeleteContentQ(Evidences[Evidence[i-1]][0], Evidences[Evidence[i-1]][2], j)

		elif value == 3:
			cmd = 'call moveChange.bat' + Evidences[Evidence[i-1]][0]
			os.syste(cmd)
			genFileTypeQ(Evidences[Evidence[i-1]][0], Evidences[Evidence[i-1]][2], j)
	###Change file type
slc = None

#qemu-img.exe convert "F:\Windows7\Windows 7 x64.vmx" -O vmdk -o subformat=dynamic dest.raw


while slc != 10: # Section to answer questions
	print ("Select the question you would like to see (0 - 9) or enter 10 to exit")
	slc = input()
	if slc < 10 and Answered[slc] == 0:
		print (Questions[slc])
		userAnswer = raw_input()
		if userAnswer in Answers[slc]: ###checks input against saved answer
			print ("Correct")
			Answered[slc] = 1
		else:
			print ("Incorrect, check your spelling or try again")
	elif slc == 10:
		quit
	else:
		print ("Question is already answered or not within bounds")
	
# i = 0
# while i < 10:
#     print (Evidence[i])
#     i = i + 1

