codes for solving
nonlinear elastic equations modified on 

_classic_examples_acoustics_1d_example1 this code.

------------------------------------------

1d nonlinear system, heterogeneous csvl
f-wave is used 

After running this code and creating plots via "make .plots", you
should be able to view the plots in _plots/_PlotIndex.html.

------------------------------------------

20150307 version 0.05
setplot.py is modified to give the solution of stress. Comment stress function, set plotitem.plot_var = 0 will give the solution of strain. Make sure also change plotaxes.title.

20150303 version 0.04
setplot.py is modified to give the solution in the moving frame

20150302 version 0.03, 
Bug fixed in riemann solver, the update of the fwave
uses wrong eigenvector. Now the heights in the plots look the same as in the paper 
with # of cells 3000.
A layered example is also added. Only need to change the 
setaux.f90 to setaux_layered.f90 in makefile

20150226 version 0.02, physical parameters, iv and bc chosen 
as in bale2000, computational parameters should be similar,
the # of cells is 6000 which is twice the # in the paper.
wave speed seems OK however a more than 20% error in the height
is observed, do not know the reason yet

20150226 version 0.01, parameters, iv and bc chosen for no special reason
not verified yet
