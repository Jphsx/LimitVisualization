



import ROOT as rt
import os
import subprocess
import ColorDictionary as CD

def getListOfFilesWC(wildcard):

	bashCommand = "ls "+wildcard
	process = subprocess.Popen(bashCommand, shell=True,stdout=subprocess.PIPE)
	output, error = process.communicate()
	filelist = list(output.split())
	#print(list(output.split()))
	return filelist

def getLimitFromFile(tfilename):
	#tfilename="higgsCombine.Ch0L_0_2j0bS_ge1jge1bISR_PTISR1_gamT1.AsymptoticLimits.mH3000270.root"
	tfile = rt.TFile.Open(tfilename)

	iterator=0
	exp0,expm1,expp1=0.,0.,0.
	for event in tfile.limit:
		#print(event.limit)
		if iterator==2:
			exp0 = event.limit
		if iterator==1:
			expm1 = event.limit
		if iterator==3:
			expp1 = event.limit
		iterator=iterator+1
		
	#print(expm1,exp0,expp1)
	return [expm1,exp0,expp1]
	
def getMassesFromFilename(tfilename):
	#get masses
	# format should be .mhXY.root
    mass = str(tfilename).split(".")
    mass = mass[3]
    #delete the mH
    mass = mass[2:]
    #extract masses
    #print("mass0 ", int(mass))
    P1=int(mass[-3:])
    P2=(int(mass)-P1)/10000
    P2=int(P2)
    dM=P2-P1
    #print(P2,P1,dM)
    return [P2,P1,dM]

def getSubLimitName(tfilename):
	sname = str(tfilename).split(".")
	return sname[1]
    
def createLimitPointDict(wildcard):
	#.Test. is full limit, otherwise N-1 limit
	#evaluate relative difference and absolute difference
	fileList = getListOfFilesWC(wildcard)
	masses = getMassesFromFilename(fileList[0])
	#process each file, store data in dict
	sublimits={}
	for f in fileList:
		sublimits[getSubLimitName(f)] = getLimitFromFile(f)
	gpdict={}
	gpdict[tuple(masses)] = sublimits
	return gpdict


def evaluatePointKey(keytuple, gpdict):
	CentralVal = gpdict[keytuple]['Test'][1]
	#add to the dict dX=CV-SL in [3] and rel=SL/CV in [4]
	for key in gpdict[keytuple]:
		dX = CentralVal - gpdict[keytuple][key][1]
		rel = gpdict[keytuple][key][1]/CentralVal
		gpdict[keytuple][key].append(dX)
		gpdict[keytuple][key].append(rel)
	
	#print(gpdict)
	#print stats on grid point
	#sort based on value
	dsorted = {k: v for k, v in sorted(gpdict[keytuple].items(), key=lambda item: item[1][3])}
	print("Evaluation of ", keytuple)
	print("All Categories exp0: ", round(dsorted['Test'][1],4) )
	print("Top 5 contributions (dX=CV-SL) (rel=SL/CV)")
	iterator = 0
	for key in dsorted:
		print("	",key, "dX=",round(dsorted[key][3],3),"rel=",round(dsorted[key][4],2), "exp0=",round(dsorted[key][1],2) )
		iterator = iterator+1
		if iterator == 5:
			break
	#for key in dsorted:
	print("Limit improvements by exclusion")
	for key in dsorted:
		if(dsorted[key][3] > 0.):
			print("	",key, "dX=",round(dsorted[key][3],3),"rel=",round(dsorted[key][4],3),"exp0=",round(dsorted[key][1],3) )
		#print(key, dsorted[key])

	return dsorted


def evaluateLeptonContribution(keytuple, gpdict):
	Ch0L=0.
	Ch1L=0.
	Ch2L=0.
	Ch3L=0.
	for key in gpdict[keytuple]:
		if( gpdict[keytuple][key][3] <= 0):
			if "Ch0L" in key:
				Ch0L = Ch0L+gpdict[keytuple][key][5]
			if "Ch1L" in key:
				Ch1L = Ch1L+gpdict[keytuple][key][5]
			if "Ch2L" in key:
				Ch2L = Ch2L+gpdict[keytuple][key][5]
			if "Ch3L" in key:
				Ch3L = Ch3L+gpdict[keytuple][key][5]
	print("Lepton Channel Fractional Contribution (%)")
	print( "	0L:",round(Ch0L*100.,1), "  1L:",round(Ch1L*100.,1),"  2L:",round(Ch2L*100.,1),"  3L:",round(Ch3L*100.,1))
	
	chL = { '0L':Ch0L, '1L':Ch1L, '2L':Ch2L, '3L':Ch3L }
	chsorted = {k: v for k, v in sorted(chL.items(), key=lambda item: item[1], reverse=True)}
	#print(chsorted)
	#check secondary contribution (30% cut)
	chkey=''
	iterator=0
	for key in chsorted:
		if iterator==0:
			chkey= key
		if iterator==1:
			if chsorted[key] >= 0.30:
				chkey = chkey + key
			break
		iterator = iterator+1
	
	#print(chkey)
	return chkey

def evaluateLeptonOnlyContribution(keytuple, gpdict):
	Ch0L=0.
	Ch1L=0.
	Ch2L=0.
	Ch3L=0.
	for key in gpdict[keytuple]:
		if( gpdict[keytuple][key][3] <= 0):
			if "Ch0L" in key:
				Ch0L = Ch0L+gpdict[keytuple][key][5]
			if "Ch1L" in key:
				Ch1L = Ch1L+gpdict[keytuple][key][5]
			if "Ch2L" in key:
				Ch2L = Ch2L+gpdict[keytuple][key][5]
			if "Ch3L" in key:
				Ch3L = Ch3L+gpdict[keytuple][key][5]
	print("Lepton Channel Fractional Contribution (%)")
	print( "	0L:",round(Ch0L*100.,1), "  1L:",round(Ch1L*100.,1),"  2L:",round(Ch2L*100.,1),"  3L:",round(Ch3L*100.,1))
	
	chL = { '0L':Ch0L, '1L':Ch1L, '2L':Ch2L, '3L':Ch3L }
	chsorted = {k: v for k, v in sorted(chL.items(), key=lambda item: item[1], reverse=True)}
	
	
	#print(chkey)
	return chL
	
def evaluateJetContribution(keytuple, gpdict):
	Ch0jS=0.
	Ch1jS=0.
	Ch2jS=0.
	Ch3jS=0.
	Ch4jS=0.
	Ch5jS=0.
	for key in gpdict[keytuple]:
		if( gpdict[keytuple][key][3] <= 0):
			if "_0jS" in key:
				Ch0jS = Ch0jS+gpdict[keytuple][key][5]
			if "_1jS" in key:
				Ch1jS = Ch1jS+gpdict[keytuple][key][5]
			if "_2jS" in key:
				Ch2jS = Ch2jS+gpdict[keytuple][key][5]
			if "_3jS" in key:
				Ch3jS = Ch3jS+gpdict[keytuple][key][5]
			if "_4jS" in key:
				Ch4jS = Ch4jS+gpdict[keytuple][key][5]
			if "_5jS" in key:
				Ch5jS = Ch5jS+gpdict[keytuple][key][5]
		
	print("Jet Multiplicity Fractional Contribution (%)")
	print( "	0jS:",round(Ch0jS*100.,1), "  1jS:",round(Ch1jS*100.,1),"  2jS:",round(Ch2jS*100.,1),"  3jS:",round(Ch3jS*100.,1),"  4jS:",round(Ch4jS*100.,1), "  5jS:",round(Ch5jS*100.,1))
	
	chL = { '0J':Ch0jS, '1J':Ch1jS, '2J':Ch2jS, '3J':Ch3jS, '4J':Ch4jS, '5J':Ch5jS }
	chsorted = {k: v for k, v in sorted(chL.items(), key=lambda item: item[1], reverse=True)}
	#print(chsorted)
	#check secondary contribution (30% cut)
	chkey=''
	iterator=0
	for key in chsorted:
		if iterator==0:
			chkey= key
		if iterator==1:
			if chsorted[key] >= 0.30:
				chkey = chkey + key
			break
		iterator = iterator+1
	
	#print(chkey)
	return chkey
	
def getColorMap(keytuple, gpdict):
	#evaluate contributions from Lep
	#add up all the (-) deviations from .Test.
	DX=0
	for key in gpdict[keytuple]:
		if gpdict[keytuple][key][3] <= 0.:
			DX = DX + gpdict[keytuple][key][3]
	for key in gpdict[keytuple]:
		#append weight to each sublimit
		gpdict[keytuple][key].append( gpdict[keytuple][key][3]/DX )

	L,J='',''
	L=evaluateLeptonContribution(keytuple, gpdict)
	J=evaluateJetContribution(keytuple, gpdict)	
	L = CD.LeptonGrad[L]
	J = CD.JetGrad[J]
	
	return L+J	
	
def getLepOnlyColorMap(keytuple, gpdict):
	DX=0
	for key in gpdict[keytuple]:
		if gpdict[keytuple][key][3] <= 0.:
			DX = DX + gpdict[keytuple][key][3]
	for key in gpdict[keytuple]:
		#append weight to each sublimit
		gpdict[keytuple][key].append( gpdict[keytuple][key][3]/DX )

	#L is a dict here not a a string key
	L=evaluateLeptonOnlyContribution(keytuple, gpdict)
	#print("cmap",L)
	#get max
	primary=0
	secondary=0
	primary_key=''
	secondary_key=''
	for key in L:
		if L[key] >= primary:
			primary = L[key]
			primary_key = key
			
	for key in L:
		if ( L[key] < primary ) and ( L[key] >= secondary ):
			secondary = L[key]
			secondary_key = key
	
	#create a weighted color average of primary and secondary
	wp = L[primary_key] 
	ws = L[secondary_key]*3
	Col1 = CD.LepOnly[primary_key]
	Col2 = CD.LepOnly[secondary_key]
	color = (wp*Col1 + ws*Col2)/(wp+ws)
	#print(color)
	return color
		
	
def DEBUG():
	wildcard = "test_files/single_3000270/higgsCombine.*.AsymptoticLimits.mH3000270.root"
	files = getListOfFilesWC(wildcard)
	lim = getLimitFromFile(files[0])
	mass = getMassesFromFilename(files[0])
	#print(files[0])
	#print(mass,lim)
	#print(evaluatePointFromWildCard(wildcard))
	gpd = createLimitPointDict(wildcard)
	#print(gpd)
	for key in gpd:
		evaluatePointKey(key,gpd)
		getColorMap(key,gpd)

def DEBUG2():
	wildcard = "test_files/single_3000270/higgsCombine.*.AsymptoticLimits.mH3000270.root"
	files = getListOfFilesWC(wildcard)
	lim = getLimitFromFile(files[0])
	mass = getMassesFromFilename(files[0])
	#print(files[0])
	#print(mass,lim)
	#print(evaluatePointFromWildCard(wildcard))
	gpd = createLimitPointDict(wildcard)
	#print(gpd)
	for key in gpd:
		evaluatePointKey(key,gpd)
		getLepOnlyColorMap(key,gpd)


 

