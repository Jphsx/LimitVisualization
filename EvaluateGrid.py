
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

def evalGridLepOnly( gridpath ):#do not include files, just path
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
		Color = EGP.getLepOnlyColorMap(key,gpd)
		print()
		gpcolord[key] = Color
		#print(fullwc)
		
	return gpcolord

#axis_labels = [x,y1,y2]
def Create2D( gpcolord  ):
	#make custom bin edges based on dictionary
	#make a set of keys and sort ascending
	#manually define upper limits
	LSP_UP = 600
	NLSP_UP = 650
	dM_UP = 60
	
	NLSPedges = set()
	LSPedges = set()
	dMedges = set()
	for key in gpcolord:
		NLSPedges.add(key[0])
		LSPedges.add(key[1])
		dMedges.add(key[2])
	
	
	#add upper limits
	NLSPedges.add(NLSP_UP)
	LSPedges.add(LSP_UP)
	dMedges.add(dM_UP)
	
	print(NLSPedges)
	print(LSPedges)
	print(dMedges)
	
	
	
	#generate color palette
	RGBL = CD.createColorMatrix()
	Number = 20   
	nb=300
	rt.TColor.CreateGradientColorTable(Number,np.array(RGBL[3],dtype=np.double),
	np.array(RGBL[0],dtype=np.double),
	np.array(RGBL[1],dtype=np.double),
	np.array(RGBL[2],dtype=np.double),
	nb)
	
	NLSPedges = list(NLSPedges)
	LSPedges = list(LSPedges)
	#dMedges = list(dMedges)
	dMedges = [3,5,7,10,20,30,40,50]
	NLSPedges.sort()
	LSPedges.sort()
	dMedges.sort()
	nBinX1=len(LSPedges)-1
	nBinY1=len(NLSPedges)-1
	nBinY2=len(dMedges)-1
	
	hXY = rt.TH2D("XY","Limit Sensitivity;LSP;NLSP",
	nBinX1, np.array(LSPedges,dtype=np.double),
	nBinY1, np.array(NLSPedges,dtype=np.double))
	hXdM = rt.TH2D("XdM","Limit Sensitivity;NLSP;dM",
	nBinY1, np.array(NLSPedges,dtype=np.double),
	nBinY2, np.array(dMedges,dtype=np.double))
	
	hXY.SetMaximum(1.0)
	hXY.SetMinimum(0.0)
	hXY.SetContour(nb)
	hXdM.SetMaximum(1.0)
	hXdM.SetMinimum(0.0)
	hXdM.SetContour(nb)
	
	#loop dictionary and fill histograms
	for key in gpcolord:
		hXY.Fill(key[1],key[0],gpcolord[key])
		hXdM.Fill(key[0],key[2], gpcolord[key])
		
	
	return [hXY, hXdM]
	
def Create2DLepOnly( gpcolord  ):
	#make custom bin edges based on dictionary
	#make a set of keys and sort ascending
	#manually define upper limits
	LSP_UP = 600
	NLSP_UP = 650
	dM_UP = 60
	
	NLSPedges = set()
	LSPedges = set()
	dMedges = set()
	for key in gpcolord:
		NLSPedges.add(key[0])
		LSPedges.add(key[1])
		dMedges.add(key[2])
	
	
	#add upper limits
	NLSPedges.add(NLSP_UP)
	LSPedges.add(LSP_UP)
	dMedges.add(dM_UP)
	
	print(NLSPedges)
	print(LSPedges)
	print(dMedges)
	
	
	
	#generate color palette
	RGBL = CD.createLepColorMatrix()
	Number = 4   
	nb=400
	rt.TColor.CreateGradientColorTable(Number,np.array(RGBL[3],dtype=np.double),
	np.array(RGBL[0],dtype=np.double),
	np.array(RGBL[1],dtype=np.double),
	np.array(RGBL[2],dtype=np.double),
	nb)
	
	NLSPedges = list(NLSPedges)
	LSPedges = list(LSPedges)
	#dMedges = list(dMedges)
	dMedges = [3,5,7,10,20,30,40,50]
	NLSPedges.sort()
	LSPedges.sort()
	dMedges.sort()
	nBinX1=len(LSPedges)-1
	nBinY1=len(NLSPedges)-1
	nBinY2=len(dMedges)-1
	

	hXdM = rt.TH2D("XdM","Limit Sensitivity;NLSP;dM",
	nBinY1, np.array(NLSPedges,dtype=np.double),
	nBinY2, np.array(dMedges,dtype=np.double))
	
	hXdM.SetMaximum(1.0)
	hXdM.SetMinimum(0.0)
	hXdM.SetContour(nb)
	
	#loop dictionary and fill histograms
	for key in gpcolord:
		hXdM.Fill(key[0],key[2], gpcolord[key])
		
	
	return hXdM

def DEBUG():	
	gridpath="test_files/full_grid_TChiWZ"
	gpcolord = evalGrid(gridpath)
	print(gpcolord)
	hlist = Create2D(gpcolord)
	hlist[1].Draw("COLZ TEXT")
	crash_and_draw

def DEBUG2():
	gridpath="test_files/small_grid_TChiWZ"
	gpcolord = evalGridLepOnly(gridpath)
	print(gpcolord)
	hdMLep = Create2DLepOnly(gpcolord)
	hdMLep.Draw("COLZ TEXT")
	crash_and_draw



#produce a TH2D map
