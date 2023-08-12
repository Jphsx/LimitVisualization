


import numpy as np







def smoothMatrix(matrix):
	new_matrix = matrix.copy()
	num_rows,num_cols = matrix.shape
	#get corner values
	UL=matrix[0,0]			#upper left
	UR=matrix[0,num_cols-1]		#upper right
	LL=matrix[num_rows-1,0]		#lower left
	LR=matrix[num_rows-1,num_cols-1]	#lower right

	TopRow  = np.linspace(UL,UR,num_cols)
	LeftRow = np.linspace(UL,LL,num_rows)
	BotRow  = np.linspace(LL,LR,num_cols)
	RightRow= np.linspace(UR,LR,num_rows)
	
	
	#print(TopRow)
	#print(LeftRow)
	#print(BotRow)
	#print(RightRow)

	#assign new_matrix new boundaries
	new_matrix[0] = TopRow
	new_matrix[num_rows-1] = BotRow
	
	for i in range(num_rows):
		new_matrix[i][0] = LeftRow[i] 
		new_matrix[i][num_cols-1] = RightRow[i]

	#print(new_matrix)
	
	#fill gaps
	for i in range(1,num_rows):
		for j in range(1,num_cols):
			#get boundaries for XY
			Top   = new_matrix[0][j]
			Bot   = new_matrix[num_rows-1][j]
			Left  = new_matrix[i][0]
			Right = new_matrix[i][num_cols-1]
			X = np.linspace(Left,Right,num_cols)
			Y = np.linspace(Top,Bot,num_rows)
			Xval = X[j]
			Yval = Y[i]
			#print(i,j,X,Y,Xval,Yval)
			XYavg = (Xval+Yval)/2.
			new_matrix[i][j] = XYavg

	#print(new_matrix)
	return(new_matrix)







matrix = np.array([[1,0,0,0,2],
		   [0,0,0,0,0],
		   [0,0,0,0,0],
		   [0,0,0,0,0],
		   [0,0,0,0,0],
		   [3,0,0,0,4]] , dtype=np.float32)
print(matrix)	
new_matrix = smoothMatrix(matrix)
print(new_matrix)
