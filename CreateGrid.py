

import EvaluateGridPoint as EGP
import ROOT as rt
import ColorDictionary as CD
import numpy as np


def evalGrid( gridpath ):#do not include files, just path
	#reuse code
	flist = EGP.getListOfFilesWC(gridpath+"/*")
	
	#loop over list and get masses, use these as a dict key to color val
	mass_set = set()
	gridColorMap = {}
	for f in flist:
		mass_set.add(tuple(EGP.getMassesFromFilename(f)))
		
	gpcolord={}	
	#iterate over set and evaluate each grid point
	for gp in mass_set:
		#create wildcard
		baseFileName="higgsCombine.*.AsymptoticLimits.mH"
		masspoint=str((gp[0]*10000)+gp[1])
		fullwc = gridpath+"/"+baseFileName+masspoint+".root"
		gpd = EGP.createLimitPointDict(fullwc)
		key = list(gpd.keys())[0]
		EGP.evaluatePointKey(key,gpd)
		Color = EGP.getColorMap(key,gpd)
		print()
		gpcolord[key] = Color
		#print(fullwc)
		
	return gpcolord
	
	

