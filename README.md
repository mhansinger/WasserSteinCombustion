# WasserSteinCombustion

### Description:

A minimal example to demonstrate the Wasserstein metric calculation procedure for quantitative evaluation and comparison
of reactive flow simulations. The Wasserstein metric can then be computed either for one quantity in the
thermo-chemical space, e.g., only T, or in the form of a stacked metric, e.g., [T,CO,CO2, H2 ].
The latter one allows for a more holistic error analysis, as the contribution from each variable to the overall
dissimilarity (between the data sets) becomes visible. In the case of one-dimensional distributions,
the obtained value of the metric shares the same unit as the sample data. For instance, if two distributions
of temperature are considered, the corresponding Wasserstein metric in units of Kelvin can be interpreted as the
average difference between the values of temperature from the two distributions. In the case of multidimensional
distributions, each dimension is normalized before pair-wise distances are calculated. The choice of the normalization
method is application-speciffc. In the present study, the marginal standard deviation is chosen. The so obtained W2 represents
the averaged difference, which is proportional to the marginal standard deviations, between samples from the two distributions.

The evaluation procedure is based on the work of:
   -   Johnson, R., Wu, H., and Ihme, M. A general probabilistic approach for the quantitative assessment of LES combustion models.
        Combust. Flame 183, pp. 88-101, 2017.

The sample data sets are from experiments and LES of the Sydney/Sandia piloted methane/air flame with inhomogeneous inlet.

Configuration: FJ-5GP-Lr75-57

Experimental data:
   -   Meares and  Masri, Combust. Flame, 161(2), pp. 484-495, 2014.
   -   Barlow, Meares, Magnotti, Cutcher, and Masri, Combust. Flame, 162(10), pp. 3516-3540, 2015.

Simulation data:
-   Hansinger, M., Zirwes, T., Zips, J., Pfitzner, M., Zhang, F., Habisreuther, P. and Bockhorn, H.,
        The Eulerian Stochastic Fields method applied to Large Eddy Simulations of a piloted flame with inhomogeneous inlet.
        Flow, Turbulence and Combustion, 2020. DOI:10.1007/s10494-020-00159-5

The main file computes the Wasserstein metric calculation (W2), Transport matrix (Transport), and stacked Wasserstein
metric contributions (Stack) for more than one dimension (i.e. [T,CO,CO2, H2]).
The figures show the dissimilarity in terms of histograms and a bar plots with the stacked contribution of each dimension (species).
The plots are saved as .pdf and .tex for further LaTex production.

The stacked data is also dumped to a pickle file, for further evaluation.

Install additional packages:
`sudo pip install -r requirements.txt`
