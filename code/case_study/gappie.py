"""
Modeled after the euro problem.
"""

from __future__ import print_function, division

import thinkbayes2
import thinkplot


class Gappie(thinkbayes2.Suite):
    """Represents hypotheses about the probability"""

    def Likelihood(self, data, hypo):
        """Computes the likelihood of the data under the hypothesis.
        """
        x = hypo / 100.0
        if data == 'G':
            return x
        else:
            return 1-x


def UniformPrior():
    """Makes a Suite with a uniform prior."""
    suite = Gappie(range(0, 101))
    return suite


def RunUpdate(suite, gappies=10, normals=35):
    """Updates the Suite with the given number of gappies and normals.

    suite: Suite object
    gappies: int
    normals: int
    """
    dataset = 'G' * gappies + 'N' * normals

    for data in dataset:
        suite.Update(data)


def Summarize(suite):
    """Prints summary statistics for the suite."""
    print(suite.Prob(50))

    print('MLE', suite.MaximumLikelihood())

    print('Mean', suite.Mean())
    print('Median', suite.Percentile(50)) 

    print('5th %ile', suite.Percentile(5)) 
    print('95th %ile', suite.Percentile(95)) 

    print('CI', suite.CredibleInterval(90))


def PlotSuites(suites, root):
    """Plots two suites.

    suite1, suite2: Suite objects
    root: string filename to write
    """
    thinkplot.Clf()
    thinkplot.PrePlot(len(suites))
    thinkplot.Pmfs(suites)

    thinkplot.Show(xlabel='% of Gap Year Students',
                    ylabel='Probability')


def main():
    # make the priors
    suite1 = UniformPrior()
    suite1.name = 'uniform'

    # update
    RunUpdate(suite1)
    Summarize(suite1)

    # plot the posteriors
    PlotSuites([suite1], 'euro1')

if __name__ == '__main__':
    main()
