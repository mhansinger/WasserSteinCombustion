# Stacked Wasserstein Metric Plotting Code

# Input: stacked_data: Preformatted 4xn matrix of previously computed
# W2stack data, where n is the number of W2 calculations to be shown.

# Output: Visualization of 1-D stacked contributions towards each
# [multidimensional] Wasserstein metric calculation.

import matplotlib.pyplot as plt
import tikzplotlib as tkz


def plotW2stack(stacked_data, path, plane):
    plt.rc('text', usetex=True)
    plt.rc('font', family='serif')
    # grey scale colormap
    # plt.style.use('grayscale')

    fig, ax, = plt.subplots(1)
    ax.xaxis.label.set_size(13)
    ax.yaxis.label.set_size(13)

    stacked_data.plot.bar(stacked=True, ax=ax, rot=0)

    plot_range = range(1, stacked_data.shape[0] + 1)

    ax.xaxis.label.set_size(13)
    ax.yaxis.label.set_size(13)

    # Formatting
    ax.set_xlabel('$W_2$ Calculations')
    ax.set_title('Contribution of single quantities to stacked W$_2$')

    ax.set_ylabel('$W_2$, Normalized')

    legend = stacked_data.columns
    ax.legend(legend, fontsize=13)

    plt.sca(ax)
    plt.xticks([0, 1, 2], ['1', '2', '3'])

    plt.savefig(path + '/WasserStein_stacked_' + str(plane) + '.pdf')
    tkz.save(path + '/WasserStein_stacked_' + str(plane) + '.tex')
    plt.show(block=False)
    #plt.close()



