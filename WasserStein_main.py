'''
Main file to run the Wasserstein metric evaluation

author @mhansinger

A minimal example to demonstrate the Wasserstein metric calculation procedure for quantitative evaluation and comparison
of reactive flow simulations. The Wasserstein metric can then be computed either for one quantity in the
thermo-chemical space, e.g., only T, or in the form of a stacked metric, e.g., [T,CO,CO2, H2 ].
The latter one allows for a more holistic error analysis, as the contribution from each variable to the overall
dissimilarity (between the data sets) becomes visible. In the case of one-dimensional distributions,
the obtained value of the metric shares the same unit as the sample data. For instance, if two distributions
of temperature are considered, the corresponding Wasserstein metric in units of Kelvin can be interpreted as the
average difference between the values of temperature from the two distributions. In the case of multidimensional
distributions, each dimension is normalized before pair-wise distances are calculated. The choice of the normalization
method is application-specic. In the present study, the marginal standard deviation is chosen. The so obtained W2 represents
the averaged difference, which is proportional to the marginal standard deviations, between samples from the two distributions.

The evaluation procedure is based on th work of:
    -   Johnson, R., Wu, H., and Ihme, M. A general probabilistic approach for the quantitative assessment of LES combustion models.
        Combust. Flame 183, pp. 88-101, 2017.

The sample data sets are from experiments and LES of the Sydney/Sandia piloted methane/air flame with inhomogeneous inlet.

Configuration: FJ-5GP-Lr75-57

Experimental data:
    -   Meares and  Masri, Combust. Flame, 161(2), pp. 484-495, 2014.
    -   Barlow, Meares, Magnotti, Cutcher, and Masri, Combust. Flame, 162(10), pp. 3516-3540, 2015.

Simulation data:
    -   Hansinger, M., Zirwes, T., Zips, J., Pfitzner, M., Zhang, F., Habisreuther, P. and Bockhorn, H.,
        The Eulerian Stochastic Fields method applied to Large Eddy Simulations of a piloted flame with inhomogeneous inlet,
        Flow, Turbulence and Combustion, 2020.

The main file computes the Wasserstein metric calculation (W2), Transport matrix (Transport), and stacked Wasserstein
metric contributions (Stack) for more than one dimension (i.e. [T,CO,CO2, H2 ]).
The figures show the dissimilarity in terms of histograms and a bar plots with the stacked contribution of each dimension (species).
The plots are saved as .pdf and .tex for further LaTex production.

The stacked data is also dumped to a pickle file, for further evaluation.

See the 'requirements.txt' for additional python packages.
'''


import pandas as pd
#import dask.dataframe as dd
import numpy as np
from calcW2 import calcW2
from plotW2stack import plotW2stack
from os.path import join
import pickle

###################################
# your input
expPath = 'Exp'
simPaths = ['Sim']

# planes where the scatter data was sampled
planes = ['050','100','150','200']

# sample size, set down for faster computation
N = 100 #1000

###################################

Stacked_dict = {}

stacked_labels = ['T', 'CO2', 'CO','H2']

for simPath in simPaths:

    print(simPath)

    Stack_W4_planes=pd.DataFrame(columns=planes)

    for plane in planes:

        print(plane)

        # Read in Data
        print('... reading experimental data')
        # Read in experimental data
        headerlines = 0

        expPath_ = join(expPath,'sample_scatter_xD%s.txt' % (str(plane)))
        expData = pd.read_csv(expPath_, delimiter='\t', header=headerlines)

        # Read in simulated data
        print('... reading simulated data')

        this_simPath = join(simPath ,'sample_scatter_xD%s.txt' % (str(plane)))
        simData = pd.read_csv(this_simPath, delimiter='\t', header=headerlines)

        print(' ')
        print('... perform calculations of Wasserstein metric (each calculations takes few seconds)')

        ## One-Dimensional Z Comparsion
        print('... cacluates Wasserstein metric')
        W2_Z, Transport_Z, Stack_Z = calcW2(expData, simData, ['f_Bilger'], N, simPath, plane)
        W2_CO, Transport_CO, Stack_CO = calcW2(expData, simData, ['CO'], N, simPath, plane)
        W2_CO2, Transport_CO2, Stack_CO2 = calcW2(expData, simData, ['CO2'], N, simPath, plane)
        W2_T, Transport_T, Stack_T = calcW2(expData, simData, ['T'], N, simPath, plane)
        W2_H2, Transport_H2, Stack_H2 = calcW2(expData, simData, ['H2'], N, simPath, plane)

        ## Two-Dimensional Z-T Comparison
        print('... cacluates Wasserstein metric for scalar(s): Z, T')
        W2_ZT, Transport_ZT, Stack_ZT = calcW2(expData, simData, ['f_Bilger', 'T'], N, simPath, plane)

        ## Four-Dimensional Z-T-CO2-CO Comparison
        print('... cacluates stacked Wasserstein metric for scalar(s): ',stacked_labels)
        W2_4dim, Transport_4dim, Stack_4dim = calcW2(expData, simData, stacked_labels, N, simPath,
                                                     plane)

        ## Plot Stacked Contributions
        print('... plot results')
        Stacked_data = np.zeros((3, 4))
        Stacked_data[0, 0] = Stack_Z
        Stacked_data[1, 0:2] = Stack_ZT
        Stacked_data[2, :] = Stack_4dim

        print(Stack_4dim)

        Stacked_df = pd.DataFrame(Stacked_data)
        Stacked_df.columns = stacked_labels

        plotW2stack(Stacked_df, simPath, plane)

        Stack_W4_planes[plane] = Stack_4dim

    # create new index according to labels
    Stack_W4_planes.index=stacked_labels

    Stacked_dict[simPath] = Stacked_df

# save stacked dict
with open('Stacked_dict.pkl', 'wb') as handle:
    pickle.dump(Stacked_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)