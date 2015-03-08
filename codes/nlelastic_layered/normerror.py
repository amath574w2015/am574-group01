"""
Compute error in elastic solution

Right now, read in data should be right (print check). Also xclaw is excutable with for loop.
Not sure whatelse to imoport. 
Error compute seems to work. Need to check if it gives the right result.

To use different set of values of mx. Need to change reshape_para accordingly.
If domain size has changed, also need to change expression of dx. Domain size 
can be set as pass in parameter for setrun.py. Will change later after testing 
error results.

"""

import numpy as np
import matplotlib.pyplot as pl
from clawpack.clawutil.runclaw import runclaw	# find the right place of runclaw
from clawpack.visclaw.data import ClawPlotData	# find the right place of ClawPlotData
import setrun

reload(setrun)

outdir='./_output'
frame=1
err=[]
i = 0

for mx in [17280, 1080, 2160, 8640]:
#for mx in [ 3200, 100, 200, 400, 800, 1600]:
#for mx in [ 200, 100]:
    #Set setrun clawdata (some maybe unnecessary, will see)
    rundata=setrun.setrun('classic')

    rundata.clawdata.num_cells[0]=mx
    rundata.clawdata.num_output_times=40	# output_times=1 won't work for high grid resolution
    rundata.clawdata.tfinal=4.0000e+02
    rundata.write()
    runclaw(xclawcmd='xclaw',outdir=outdir)	# xclaw.exe file produced after make .exe 

    #Get the material parameters
    aux = np.loadtxt(outdir+'/fort.a0000',skiprows=5)	# don't delate skiprows or set it equal 6 

    plotdata = ClawPlotData()
    plotdata.outdir=outdir

    #Read in the solution
    dat = plotdata.getframe(40)
    u = dat.q[0,:]

    stress = np.exp(u*aux) - 1	# not sure why here don't need aux[0,:]

    print dat
#    print aux.shape

    #Compute parameter for error calculation
    dx = 3.6000000e+02/mx
    reshape_para = 17280/mx
#    reshape_para = 3200/mx
#    reshape_para = 200/mx

#    print reshape_para
#    print u.shape

    #Reshape stress to match dimension
    reshape_matrix = np.ones((1,reshape_para)) 
    reshape_matrixt = np.transpose(reshape_matrix)
    stress_matrix = reshape_matrixt * stress
    stress_reshape = np.reshape(stress_matrix, (1, mx*reshape_para), order='F')  

#    print stress
#    print stress_reshape

    #Compute error
    if i == 0:
	stress_exact = stress_reshape
    i = i + 1
    error = np.sum(abs(stress_reshape - stress_exact)) * dx/reshape_para
    err.append(error)

print err

