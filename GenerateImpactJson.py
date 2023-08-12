import ROOT as rt
import json
import os
import subprocess

#full structure:
#{
# "POIs": [
#    {
#      "fit": [ -1.0, 0.0, 1.0],
#      "name": "r"
#    }
#  ],
#  "method": "default",
#  "params": [
#    {
#      "fit": [ 1, 2, 3 ], #use fit as [ exp-1, exp0, exp+1]
#      "groups": [],
#      "impact_r": 0.00,
#      "name": "Test Name 1",
#      "prefit": [-1,0.0, 1 ],
#      "r": [ 1,2, 3 ],
#      "type": "Gaussian"
#    }
#   ]
#}

def getfullblank():
	
	full={
	 "POIs": [
    		{
      	 	"fit": [ -1.0, 0.0, 1.0],
      	 	"name": "r"
    		}
  		],
 	 "method": "default",
  	"params": []
	}
	return full
	

 
def getblankparam():
	param= {
      	"fit": [ 0.3, 1, 1.2 ],
      	"groups": [],
      	"impact_r": 0.00,
      	"name": "Test Name 1",
      	"prefit": [-1,0.0, 1 ],
      	"r": [ 1,2, 3 ],
      	"type": "Gaussian"
    	}
	return param


def getparamfromfile(tfilename):
	#tfilename="higgsCombine.Ch0L_0_2j0bS_ge1jge1bISR_PTISR1_gamT1.AsymptoticLimits.mH3000270.root"
	tfile = rt.TFile.Open(tfilename)
	param = getblankparam()
	#tfile.limit.Print()
	iterator=0
	exp0,expm1,expp1=0.,0.,0.
	for event in tfile.limit:
		#print(event.limit)
		if iterator==2:
			exp0 = event.limit
		if iterator==1:
			expm1 = event.limit
			expm1 = 0
		if iterator==3:
			expp1 = event.limit
			expp1 = 0
		iterator=iterator+1
		
	#print(expm1,exp0,expp1)
	param["fit"] = [expm1,exp0,expp1]
	#set name
	name=tfilename.split(".")
	name=name[1]
	param["name"]=name	
	return param		
	

def getListOfFilesWC(wildcard):

	bashCommand = "ls "+wildcard
	process = subprocess.Popen(bashCommand, shell=True,stdout=subprocess.PIPE)
	output, error = process.communicate()
	filelist = list(output.split())
	print(list(output.split()))
	return filelist

def generateJSONfromWC(wildcard, useFullFit, fullFitPath=""):
	basejson = getfullblank()
	#if using supplying full fit, parse file and set "fit"i
	#also add it as the first entry
	fullparam=''
	if(useFullFit):
		fullparam=getparamfromfile(fullFitPath)
		#print("BASE POI", basejson["POIs"][0]["fit"]) #need a extra 0, they have an extra list with 1 item in there
		#print("FULLPARAM", fullparam["fit"])
		basejson["POIs"][0]["fit"] = fullparam["fit"]
		fullparam["name"]="Inclusive Categories"
		basejson["params"].append(fullparam)

	filelist = getListOfFilesWC(wildcard)
	
	for f in filelist:
		p = getparamfromfile(f)		
		basejson["params"].append(p)

	return basejson

def writeJSON(wc, ofilename, useFullFit, fullFitPath=""):

	json1 = generateJSONfromWC(wildcard,useFullFit, fullFitPath)
	json_data = json.dumps(json1, indent=4)

	with open(ofilename, "w") as json_file:
    		json_file.write(json_data)    


#TChiWZ 3000270 run
#wildcard = "higgsCombine.Ch*S.AsymptoticLimits.mH3000270.root"
#fullFitPath= "/uscms/home/janguian/nobackup/CMSSW_10_6_5/src/KUEWKinoAnalysis/BF_B20-101/higgsCombine.Test.AsymptoticLimits.mH3000270.root"
#writeJSON(wildcard, "TChiWZ3000270.json",True,fullFitPath )

import CategoryList as CL

#for grid in CL.TChiWZGrid:
#	wildcard = "higgsCombine.Ch*S.AsymptoticLimits.mH"+grid+".root"
#	fullFitPath="/uscms/home/janguian/nobackup/CMSSW_10_6_5/src/KUEWKinoAnalysis/BF_B20-101/higgsCombine.Test.AsymptoticLimits.mH"+grid+".root"
#	writeJSON(wildcard, "TChiWZ"+grid+".json", True, fullFitPath) 


for grid in CL.T2ttGrid:
	wildcard = "higgsCombine.Ch*S.AsymptoticLimits.mH"+grid+".root"
	fullFitPath="/uscms/home/janguian/nobackup/CMSSW_10_6_5/src/KUEWKinoAnalysis/BF_B20-101_T2tt/higgsCombine.Test.AsymptoticLimits.mH"+grid+".root"
	writeJSON(wildcard, "T2tt"+grid+".json", True, fullFitPath) 





