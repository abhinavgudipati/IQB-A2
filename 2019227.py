# -*- coding: utf-8 -*-
"""2019227.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1aCHRRlGDmZQA_PaRI-d8LJtOxFA_vGY-
"""

#2A
#SEQ  1    SGFRKMAFPSGKVEGCMVQVTCGTTTLNGLWLDDTVYCPRHVICTAEDML   50          ~~~~
#STR       TTTT     HHHHHH EEEEEETTEEEEEEEETTEEEEEGGGG  HHHHH               ~~~~
#REM                                                                        ~~~~
#REM                .         .         .         .         .               ~~~~
#SEQ  51   NPNYEDLLIRKSNHSFLVQAGNVQLRVIGHSMQNCLLRLKVDTSNPKTPK  100          ~~~~
#STR          HHHHHHH  GGG EEEETTEEE EEEEEEETTEEEEEE   TTTT                 ~~~~
#REM                                                                        ~~~~
#REM                .         .         .         .         .               ~~~~
#SEQ  101  YKFVRIQPGQTFSVLACYNGSPSGVYQCAMRPNHTIKGSFLNGSCGSVGF  150          ~~~~
#STR             TTTEEEEEEEEETTEEEEEEEEEETTTT B    TTTTTTTEE                ~~~~

import operator as op


#initiating Chou Fasman Data for alpha and beta listed below as a dictionary 
#initiating a dictionary for amino acids
aminoAcid = {}
aminoAcid['A']      = "alanine" 
aminoAcid['R']      = "arginine"
aminoAcid['N']      = "aspartic acid"
aminoAcid['D']      = "aspargine"
aminoAcid['C']      = "cysteine"
aminoAcid['E']      = "glutamic acid"
aminoAcid['Q']      = "glutamine"
aminoAcid['G']      = "glycine"
aminoAcid['H']      = "histidine"
aminoAcid['I']      = "isoleucine"
aminoAcid['L']      = "leucine"
aminoAcid['K']      = "lysine"
aminoAcid['M']      = "methonine"
aminoAcid['F']      = "phenylalanine"
aminoAcid['P']      = "proline"
aminoAcid['S']      = "serine"
aminoAcid['T']      = "theoreonine"
aminoAcid['W']      = "tryptophan"
aminoAcid['Y']      = "tyrosine"
aminoAcid['V']      = "valine"

alphaValues = {}
#initiating a dictionary for weights of alpha 
alphaValues["glutamic acid"]=1.53 
alphaValues["alanine"]=1.45  
alphaValues["leucine"]=1.34 
alphaValues["histidine"]=1.24
alphaValues["methonine"]=1.20 
alphaValues["glutamine"]=1.17
alphaValues["tryptophan"]=1.14
alphaValues["valine"]=1.14 
alphaValues["phenylalanine"]=1.12
alphaValues["lysine"]=1.07
alphaValues["isoleucine"]=1.00 
alphaValues["aspartic acid"]=0.98
alphaValues["theoreonine"]=0.82
alphaValues["serine"]=0.79
alphaValues["arginine"]=0.79
alphaValues["cysteine"]=0.77
alphaValues["aspargine"]=0.73
alphaValues["tyrosine"]=0.61
alphaValues["proline"]=0.59
alphaValues["glycine"]=0.53

betaValues = {}
#initiating a dictionary for weights of beta strand 
betaValues["methonine"]=1.67 
betaValues["valine"]=1.65 
betaValues["isoleucine"]=1.60 
betaValues["cysteine"]=1.30 
betaValues["tyrosine"]=1.29 
betaValues["phenylalanine"]=1.28 
betaValues["glutamine"]=1.23 
betaValues["leucine"]=1.22  
betaValues["theoreonine"]=1.20 
betaValues["tryptophan"]=1.19 
betaValues["alanine"]=0.97 
betaValues["arginine"]=0.90
betaValues["glycine"]=0.81 
betaValues["aspartic acid"]=0.80
betaValues["lysine"]=0.74
betaValues["serine"]=0.72
betaValues["histidine"]=0.71
betaValues["aspargine"]=0.65
betaValues["proline"]=0.62
betaValues["glutamic acid"]=0.26 

inputProteinSequence = "SGFRKMAFPSGKVEGCMVQVTCGTTTLNGLWLDDTVYCPRHVICTAEDMLNPNYEDLLIRKSNHSFLVQAGNVQLRVIGHSMQNCLLRLKVDTSNPKTPKYKFVRIQPGQTFSVLACYNGSPSGVYQCAMRPNHTIKGSFLNGSCGSVGF"

#initiated an empty Helix list as well as an empty beta strand list 
Helix = op.mul([0],len(inputProteinSequence))
Strand = op.mul([0],len(inputProteinSequence))

#this function is responsible for fetching all the alpha helices in the given sequence
def alphaHelix():
	start = 0 
	while op.lt(op.add(start , 6) , len(inputProteinSequence)): #parameters for alpha being the window = 6 
		checkIndex = 0 #this basically keeps track of the count for all the alpha helices in counts of 6 
		for i in range(start,op.add(start , 6)):
			if op.ge(alphaValues[aminoAcid[inputProteinSequence[i]]],1):
				checkIndex=op.add(checkIndex, 1)
		if op.ge(checkIndex,4):
			checkForAlpha(start,op.add(start , 6))
		start = op.add(start , 1)

#this code is responsible checking with respect to right adjustment index as well as the left adjustment index for the possible alpha helix sequence 
def checkForAlpha(start,end):
	rightIndexing=op.truediv(sum([alphaValues[aminoAcid[x]] for x in inputProteinSequence[op.sub(start, 3):op.add(start, 7)]]),4)
	line = start + 7
	while op.and_(op.lt(line , len(inputProteinSequence)) , op.ge(rightIndexing , 1)):
		line= op.add(line, 1)
		rightIndexing = op.truediv(sum([alphaValues[aminoAcid[x]] for x in inputProteinSequence[op.sub(start, 3):op.add(start, 7)]]),4)

	leftIndexing= op.truediv(sum([alphaValues[aminoAcid[x]] for x in inputProteinSequence[op.sub(start, 1):op.add(start,3)]]),4)

	booline = start - 1 
	while op.and_(op.gt(booline , 0) ,op.ge(leftIndexing ,1)):
		booline= op.sub(booline , 1)
		leftIndexing = op.truediv(sum([alphaValues[aminoAcid[x]] for x in inputProteinSequence[op.sub(start,1):op.add(start,3)]]),4)

	for i in range(start,end):
		Helix[i]=True

#this function is responsible for fetching all the beta strands in the given protein sequence
def betaStrand():
	start = 0
	while op.lt(op.add(start,5) , len(inputProteinSequence)):
		checkIndex=0  #this basically keeps track of the count for all the beta strange in counts of 5 
		for i in range(start,op.add(start,5)):
			if op.ge(betaValues[aminoAcid[inputProteinSequence[i]]],1):
				checkIndex=op.add(checkIndex, 1)
		if op.ge(checkIndex,3):
			checkForBeta(start,op.add(start,5))
		start=op.add(start,1)

#this code is responsible checking with respect to right adjustment index as well as the left adjustment index for the possible beta strande sequences
def checkForBeta(start,end):
	rightIndexing=op.truediv(sum([betaValues[aminoAcid[x]] for x in inputProteinSequence[op.sub(end,3):op.add(end,1)]]),4)

	while op.and_(op.lt(end , len(inputProteinSequence)) , op.ge(rightIndexing ,1) ): 
		end = op.add(end, 1)
		rightIndexing = op.truediv(sum([betaValues[aminoAcid[x]] for x in inputProteinSequence[op.sub(end,3):op.add(end,1)]]),4)
	leftIndexing= op.truediv(sum([betaValues[aminoAcid[x]] for x in inputProteinSequence[op.sub(start,1):op.add(start,3)]]),4)

	while op.and_(op.gt(start , 0) , op.ge(leftIndexing ,1)):
		start = op.sub(start,1)
		leftIndexing = op.truediv(sum([betaValues[aminoAcid[x]] for x in inputProteinSequence[op.sub(start,1):op.add(start,3)]]),4)
	for i in range(start,end):
		Strand[i]=True

#this function is responsible for generating the secondary sequence structre 
def secondarySequenceStructure():
	i=0
	secondary_sequence = ""
	while op.lt(i , len(inputProteinSequence)):
		if op.and_(op.eq(Helix[i],False) ,op.eq(Strand[i],False)):
			j = i 
			while j < len(inputProteinSequence) and op.eq(Helix[j] , False ) and op.eq(Strand[j] , False): 
				secondary_sequence += 'T' #the Turns is signified with T, reporting the empty regions 
				j=op.add(j,1 )
			i = j

		elif op.and_( op.eq(Helix[i] , True) , op.eq(Strand[i] , False)):
			j = i 
			while op.le(j , len(inputProteinSequence))and op.eq(Helix[j] , True) and op.eq(Strand[j] , False): 
				secondary_sequence += 'H' #this is responsible for filling the possible alpha helices 
				j=op.add(j,1 )
			i=j

		elif op.and_(op.eq(Helix[i],False) , op.eq(Strand[i],True)):
			j = i 
			while op.lt(j ,len(inputProteinSequence))  and op.eq(Helix[j] ,False) and op.eq(Strand[j] , True): 
				secondary_sequence += 'S' # this loop is responsible for filling the possible beta strands 
				j=op.add(j,1 )
			i=j

		elif op.and_(op.eq(Helix[i],True) , op.eq(Strand[i],True)): 
			j = i 
			Helix_sum = 0 
			Strand_sum = 0 
			while op.lt(j ,len(inputProteinSequence)) and op.eq(Helix[j] , True) and op.eq(Strand[j] , True):
				Helix_sum  = op.add(Helix_sum,alphaValues[aminoAcid[inputProteinSequence[j]]])
				Strand_sum = op.add(Strand_sum,betaValues[aminoAcid[inputProteinSequence[j]]])
				j=op.add(j,1 )
			for z in range(i,j):
				if op.ge(Helix_sum , Strand_sum):
					secondary_sequence = op.add(secondary_sequence,'H') 
				else:
					secondary_sequence = op.add(secondary_sequence,'S')
			i = j 
	return secondary_sequence
alphaHelix() #calling the alpha function responsible for generating the alpha helices 
betaStrand() #calling the alpha function responsible for generating the beta strands 
print(secondarySequenceStructure())

#SEQ  1    SGFRKMAFPSGKVEGCMVQVTCGTTTLNGLWLDDTVYCPRHVICTAEDML   50          ~~~~
#STR       TTTT     HHHHHH EEEEEETTEEEEEEEETTEEEEEGGGG  HHHHH               ~~~~
#REM                                                                        ~~~~
#REM                .         .         .         .         .               ~~~~
#SEQ  51   NPNYEDLLIRKSNHSFLVQAGNVQLRVIGHSMQNCLLRLKVDTSNPKTPK  100          ~~~~
#STR          HHHHHHH  GGG EEEETTEEE EEEEEEETTEEEEEE   TTTT                 ~~~~
#REM                                                                        ~~~~
#REM                .         .         .         .         .               ~~~~
#SEQ  101  YKFVRIQPGQTFSVLACYNGSPSGVYQCAMRPNHTIKGSFLNGSCGSVGF  150          ~~~~
#STR             TTTEEEEEEEEETTEEEEEEEEEETTTT B    TTTTTTTEE                ~~~~

#My output
#THHHHHHHHHTHSSSSSSSSSSSSSSHHHHHHSSSSSSSSHHHHHHHHHHHTTHHHHHHHHHHSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSTTTTHSSSSSSSSSSSSSSSSSSSSSTTSSSSSSSSSSTTTHHHHHHTTTTTTTTT

#We notice that both of the outputs are different with respect to the way the algo was even created, empty
#regions are present in ChouFasman algo run by Stride. 
#We can also observe that there are gaps in their output which in turn we have account for with respect 
#to the T character. In my algorithm, I have assigned turn ???T??? wherever alpha and beta was not coming across,
#whereas in the Stride Output, this condition was not kept in mind, for generating this ???T??? in their output, 
#they have implemented another logic, owing to which we observe a difference in both their outputs and my output. 
#Chou and Fasman was used a logic where they took care of indexes where no alpha or beta was present ,which I 
#have otherwise done using turn ???T???.

#2B

#1)In our code, we have only assigned 3 symbols H , S and T each denoting Alpha Helices , Beta Strands and Turns 
#respectively whereas if we notice in the ChouFasman Algo deduced by the 2 scientists there are more variables 
#allotted. There are the G, E and B variables as well in this algo, which we haven???t taken into account. 
#2)The E character denotes strand in the Stride output. I used S for the same. 
#3)The B character denotes bridge in the Stride output. 
#4)The G character denotes 310helix with respect to the stride output, which we haven't taken into account. 
#5)The C character accounts for the Coils. 
#6)The chou fasman method was developed in the 1970s, and it is an advanced method devoted for higher bioinformatics
#concepts, unlike the algorithm developed by me which is a layman???s interpretation of the same algo created 
#by Chou and Fasman.



