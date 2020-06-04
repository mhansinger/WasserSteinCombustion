# Wasserstein Metric Sample Plotting Code
from os.path import join
import matplotlib.pyplot as plt
import tikzplotlib as tkz

# Outputs: Wasserstein metric, with 1-D/2-D data visualization.

def plotW2(pdf1, pdf2, species_index, std_pdf, W2, path, plane):
    plt.rc('text', usetex=True)
    plt.rc('font', family='serif')
    ## One dimensional case
    if len(species_index) == 1:
        # Consider case that built-in 'histogram' function does not exist
        # Use 'hist' function instead

        numBins = 30

        # print(pdf1)

        fig, ax = plt.subplots(1)
        # One Dimensional Histograms, with data unnormalized
        ax.hist(pdf1[species_index].values, bins=numBins, density=True, alpha=0.7, edgecolor='black')
        ax.hist(pdf2[species_index].values, bins=numBins, density=True, alpha=0.7, edgecolor='black')
        ax.xaxis.label.set_size(13)
        ax.yaxis.label.set_size(13)

        # x label
        if species_index[0] == 'f_Bilger':
            ax.set_xlabel(r"$\widetilde{Z}$")
        elif species_index[0] == 'T':
            ax.set_xlabel(r'$\widetilde{T}$ [K]')
        elif species_index[0] == 'CO2':
            ax.set_xlabel(r'$\widetilde{{CO_2}}$ Mass fraction')
        elif species_index[0] == 'CO':
            ax.set_xlabel(r'$\widetilde{{CO}}$ Mass fraction')
        elif species_index[0] == 'H2':
            ax.set_xlabel(r'$\widetilde{H}_2$ Mass fraction')
        else:
            ax.set_xlabel('$\widetilde{{%s}}$ Mass fraction' % str(species_index[0]))

        ax.set_ylabel('PDF')
        if species_index[0] == 'f_Bilger':
            ax.set_title(r'Histograms of $\widetilde{Z}$ , W$_2$ = %s' % (str(round(W2, 3))))
        elif species_index[0] == 'T':
            ax.set_title(r'Histograms of $\widetilde{T}$ , W$_2$ = %s' % (str(round(W2, 3))))
        elif species_index[0] == 'CO2':
            ax.set_title(r'Histograms of $\widetilde{CO}_2$ , W$_2$ = %s' % (str(round(W2, 3))))
        elif species_index[0] == 'CO':
            ax.set_title(r'Histograms of $\widetilde{CO}$ , W$_2$ = %s' % (str(round(W2, 3))))
        elif species_index[0] == 'H2':
            ax.set_title(r'Histograms of $\widetilde{H}_2$ , W$_2$ = %s' % (str(round(W2, 3))))

        ax.legend(['Exp PDF', 'LES PDF'], loc='best', fontsize=13)

        plt.savefig(join(path, 'WasserStein_' + species_index[0] + '_' + str(plane) + '.pdf'))
        tkz.save(join(path, 'WasserStein_' + species_index[0] + '_' + str(plane) + '.tex'))
        plt.show(block=False)
        # plt.close()


    elif len(species_index) == 2:

        fig, ax, = plt.subplots(1)

        ax.scatter(pdf1[species_index[0]].values / std_pdf[species_index[0]],
                   pdf1[species_index[1]].values / std_pdf[species_index[1]], facecolors='none', edgecolors='b')
        ax.scatter(pdf2[species_index[0]].values / std_pdf[species_index[0]],
                   pdf2[species_index[1]].values / std_pdf[species_index[1]], facecolors='none', edgecolors='r')
        ax.xaxis.label.set_size(13)
        ax.yaxis.label.set_size(13)

        # ax.text(0.8, 0.5, 'W$_2$ = %s' % str(round(W2, 3)), fontsize=15, horizontalalignment='center',
        #        verticalalignment='center', transform=ax.transAxes)

        # x label
        if species_index[0] == 'f_Bilger':
            ax.set_xlabel('f$_{Bilger}$ (Normalized)')
        elif species_index[0] == 'T':
            ax.set_xlabel('T (K, Normalized)')
        elif species_index[0] == 'CO2':
            ax.set_xlabel('CO_2 Mass Fraction (Normalizedd)')
        elif species_index[0] == 'CO':
            ax.set_xlabel('CO Mass Fraction (Normalized)')
        else:
            ax.set_xlabel('Species 1 Values (Normalized)')

        # y label
        if species_index[1] == 'f_Bilger':
            ax.set_ylabel('Z (Normalized)')
        elif species_index[1] == 'T':
            ax.set_ylabel('T (K, Normalized)')
        elif species_index[1] == 'CO2':
            ax.set_ylabel('CO_2 Mass Fraction (Normalized)')
        elif species_index[1] == 'CO':
            ax.set_ylabel('CO Mass Fraction (Normalized)')
        else:
            ax.set_ylabel('Species 2 Values (Normalized)')

        # ax.set_ylabel('Histogram (Normalized)')
        ax.set_title('PDFs of %s and %s , W$_2$ = %s' % ('f$_{Bilger}$', species_index[1], str(round(W2, 3))))

        ax.legend(['Exp PDF', 'LES PDF'], loc='best', fontsize=13)

        plt.savefig(join(path, 'WasserStein_' + species_index[0] + species_index[1] + '_' + str(plane) + '.pdf'))
        tkz.save(join(path, 'WasserStein_' + species_index[0] + species_index[1] + '_' + str(plane) + '.tex'))
        plt.show(block=False)
        # plt.close()





