"""This file contains code for use with "Think Bayes",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function, division

import numpy
import thinkbayes2
import thinkplot


# Suppose I capture and tag 10 Rock Hyraxes. 
# Some time later, I capture another 10 Hyraxes and find that
# two of them are already tagged. 
# How many Hyraxes are there in this environment?

class Hyrax(thinkbayes2.Suite):
    """Represents hypotheses about."""

    def Likelihood(self, data, hypo):
        """Computes the likelihood of the data under the hypothesis.

        hypo: 
        data: 
        """
        tagged, captured, taggedFound = data
        if hypo < captured - taggedFound + tagged:
            like = 0
            return like
        else:
            probability = tagged/hypo
            like = thinkbayes2.EvalBinomialPmf(taggedFound, captured, probability)
            return like


def main():

    hypos = range(1, 1000)
    hyrax = Hyrax(hypos)
    data = (10, 10, 2)
    hyrax.Update(data)


    thinkplot.Pdf(hyrax)
    thinkplot.Show()

if __name__ == '__main__':
    main()
