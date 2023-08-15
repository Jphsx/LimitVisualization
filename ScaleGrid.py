



import EvaluateGrid as EG
import numpy as np


def getNearestEdge( edgeList, value):
	diff = 999
	closest_edge = -1
	for edge in edgeList:
		if abs(edge-value) < diff:
			diff = abs(edge-value)
			closest_edge=edge
	if(diff>0):
		print("assigning:",value," to ", closest_edge)
	return closest_edge

def translateToCustomdMGrid( gpcolord, dMedges, NLSPedges):
	#create a doubly linked list type structure to average dict values into custom grid
	gridStacks = {}
	for NLSP in NLSPedges:
		for dM in dMedges:
			gridStacks[ tuple((NLSP,dM)) ] = []
			
	
	for key in gpcolord:
		NLSPgridsnap = getNearestEdge(NLSPedges,key[0])
		dMgridsnap = getNearestEdge(dMedges,key[2])
		gridStacks[ tuple((NLSPgridsnap,dMgridsnap)) ].append( gpcolord[key] )
		

	#print(gridStacks)
	for key in gridStacks:
		print(key, gridStacks[key])
	#scan fill gaps and average stacks
	for key in gridStacks:
		#print(key, gridStacks[key])
		if len(gridStacks[key]) == 0:
			#copy a neighboring dM value
			#assume NLSP points dont need this treatment
			dMCopy = dMedges.copy()
			dMCopy.remove(key[1])
			neighborEdge = getNearestEdge( dMCopy, key[1])
			gridStacks[ key ] =  gridStacks[ tuple((key[0],neighborEdge)) ]
	
		#average mutliple values
		if len(gridStacks[key]) > 1:
			gridStacks[key] = [ sum(gridStacks[key])/len(gridStacks[key]) ]	

	#print(gridStacks)
	print("reformulated")
	for key in gridStacks:
		print(key, gridStacks[key])
		
	#form the grid
	num_rows = len(dMedges)
	npgrid = np.empty((num_rows, 0))
	for NLSP in NLSPedges:
		#get all DMs for NLSP mass
		colorcol=[]
		for dM in dMedges:
			colorcol.append(gridStacks[tuple((NLSP,dM))] )
		
		colorcol = np.array(colorcol)
		npgrid = np.hstack((npgrid, colorcol.reshape(num_rows, 1)))

	np.set_printoptions(precision=3)
	np.set_printoptions(threshold=np.inf, suppress=True, linewidth=np.inf)
	print(npgrid)
	return npgrid

def padAndSmoothMatrix(npgrid):
	num_rows,num_cols = npgrid.shape
	#step over numrows or cols -1
	#prepare sub matrices
	for row in range(num_rows-1):
		for col in range(num_cols-1):
			submat = np.array( [npgrid[row][col:col+2], npgrid[row+1][col:col+2] ] )
			print(submat)


def DEBUG():
	gridpath="test_files/full_grid_TChiWZ"
	gpcolord = EG.evalGridLepOnly(gridpath)
	#TChiwZ edges
	NLSPedges = [526, 400, 275, 150, 550, 425, 300, 175, 576, 450, 325, 200, 600, 475, 350, 225, 100, 500, 375, 250, 125]
	dMedges = [3,5,7,10,20,30,40,50]
	NLSPedges.sort()
	npgrid = translateToCustomdMGrid( gpcolord, dMedges, NLSPedges)
	padAndSmoothMatrix(npgrid)







