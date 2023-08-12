import os
import CategoryList as CL

#hardcoded list of all cats in CL

#Test single category
CATS=["Ch2L_Zstar_gold_ge2jge1bS_ge1jge1bISR_PTISR0_gamT0"]
#Test set of 3
CATS=CL.TestCategories
#All categories
CATS=CL.Categories

#hardcoded list of all gridpoints to scan
#Test single point
GRID=["3000270"]
#FullGrid
GRID=CL.TChiWZGrid
GRID=CL.T2ttGrid

#number of toys to run
nToys=0 # no toys, computational infeasible

#print(CL.TestCategories)

#generate dict TaskName+CatMaskList from TaskName+REGEX dict
maskDict = CL.getMaskListDict( CL.LJdict, CL.Categories)
#print(maskDict)


BASELIMCMD="combineTool.py -M AsymptoticLimits --job-mode connect --input-file FitInput_KUEWKino_2017.root "

#mask a single grid point
for grid in GRID:

	#for cat in CATS:
	for task in maskDict:
	
		#save gridpoint
		gp = "-m "+ str(grid)+" "

		#set ofile name
		#out = "-n ."+cat+" "#old single mask method
		out = "-n ."+task+" "

		#set toys #no toys
		#toy = "-t "+str(nToys)+" "
		
		#save mask
		#mask = "--setParameters mask_"+cat+"=1 " #old single mask method
		#iterate through task masks and append to string
		mask = "--setParameters "
		finalKey = maskDict[task][-1]
		for cat in maskDict[task]:
			#print(cat, finalKey)
			if cat == finalKey:
				mask = mask +"mask_"+cat+"=1 "
			else:
				mask = mask +"mask_"+cat+"=1,"

		#select workspace
		ws = "-d datacards/all/*/"+str(grid)+"/ws_chmask.root "

		#task name
		#task = "--task-name job_"+str(grid)+"_"+str(cat)+" " #original single mask method
		#set task name based on task dict
		task = "--task-name job_"+grid+"_"+task+" "
		

		LIMCMD=BASELIMCMD+gp+ws+out+task+mask
		print("Limit Command:")
		print(LIMCMD)
			
		os.system(LIMCMD)
			



