
import ROOT as rt
import numpy as np

l_grad_step = 0.1
#store  upper limits
LeptonGrad={
'0L': 0.1,
'0L1L':0.2, #0Ldominated with 1 L contribution #offset colors 20-35% contribution?
'1L0L':0.3, #1Ldominated with 0 L contribution
'1L':0.4,
'1L2L':0.5,
'2L1L':0.6,
'2L':0.7,
'2L3L':0.8,
'3L2L':0.9,
'3L':1.0,
'2L0L':1.0#debug
}



j_grad_step=(0.1/11.)

JetGrad={
'0J': j_grad_step,
'0J1J': 2*j_grad_step,
'1J0J': 2*j_grad_step,
'1J': 3*j_grad_step,
'1J2J': 4*j_grad_step,
'2J1J': 4*j_grad_step,
'2J': 5*j_grad_step,
'2J3J': 6*j_grad_step,
'3J2J':6*j_grad_step,
'3J': 7*j_grad_step,
'3J4J': 8*j_grad_step,
'4J3J': 8*j_grad_step,
'4J': 9*j_grad_step,
'4J5J': 10*j_grad_step,
'5J4J': 10*j_grad_step,
'5J': 11*j_grad_step,
'0J2J':11*j_grad_step#debug
}


def createColorMatrix():
	
	Colors = [[0, 242,36],[0, 61,9],[0, 242,120],[0, 61,31],[0, 242,186],[0, 61,50],[0, 242,226],[0, 60,61],[0, 194,242],[0, 41,61],[0, 117,242],[0, 18,61],[0, 28,242],[4, 0,61],[109,0,242],[35,0,61],[186,0,242],[52,0,61],[242,0,218],[60,0,61]]

	Red=[]
	Green=[]
	Blue=[]
	Length=[]

	w = 0
	step=0
	for i in range(0,20):
		for j in range(0,3):
			Colors[i][j] = float(Colors[i][j])/255.
		
		Red.append(Colors[i][0])
		Green.append(Colors[i][1])
		Blue.append(Colors[i][2])
		if i%2 == 0 :
			step = 0.0
			
		else:
			step = 0.049
			
		Length.append(w+step)
		w=w+(1./20.)

	RGBL = [Red,Green,Blue,Length]
	return RGBL
	
def drawTestScale(RGBL):


	Number = 20   
	nb=300
	#np.array([1, 2, 3], dtype=complex)
	#rt.TColor.CreateGradientColorTable(Number,RGBL[3],RGBL[0],RGBL[1],RGBL[2],nb)
	rt.TColor.CreateGradientColorTable(Number,np.array(RGBL[3],dtype=np.double),
	np.array(RGBL[0],dtype=np.double),
	np.array(RGBL[1],dtype=np.double),
	np.array(RGBL[2],dtype=np.double),
	nb)
	nbinx=11
	nbiny=10
	h2 = rt.TH2D("testScale","Test Color Scale", nbinx, 0,1,nbiny,0, 1)
	h2.SetMaximum(1.0)
	h2.SetMinimum(0.0)
	h2.SetContour(nb)
	 
	njet_label = ["0jS"," ","1jS"," ","2jS"," ","3jS"," ","4jS"," ","5jS"]
	nlep_label = ["0L"," "," ","1L"," "," ","2L"," "," ","3L"]
	for x in range(1,nbinx+1):
		h2.GetXaxis().SetBinLabel(x,njet_label[x-1])
	 
	for y in range(1,nbiny+1):
		h2.GetYaxis().SetBinLabel(y,nlep_label[y-1])	
	
	 
	 
	grad=0.000001
	grad_step=(0.1/11.)
	for y in range(1,nbiny+1):
		for x in range(1,nbinx+1):
			h2.SetBinContent(x,y,grad)
			grad+=grad_step
			
	#h2.Draw("COLZ TEXT")
	return h2

#print(LeptonGrad)
#print(JetGrad)
def DEBUG():
	RGBL=createColorMatrix()
	h2 = drawTestScale(RGBL)
	c2  = rt.TCanvas("c2","c2",0,0,600,400)	
	h2.Draw("COLZ TEXT")
	crash_and_draw

