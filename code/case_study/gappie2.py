"""
Modeled after the hyrax problem.
"""

from __future__ import print_function, division

import numpy
import thinkbayes2
import thinkplot


class Gappie(thinkbayes2.Suite):

    def Likelihood(self, data, hypo):

        g, n, o = data
        if hypo < g + n - o:
            return 0

        p = g / hypo
        like = thinkbayes2.EvalBinomialPmf(o, n, p)
        return like


def main():
    hypos = range(1, 341)
    suite = Gappie(hypos)

    # data = 12, 7, 3
    suite.Update((0, 5, 0))
    suite.Update((5, 6, 3))
    suite.Update((8, 8, 4))
    suite.Update((12, 4, 0))



    print(suite.Mean())
    thinkplot.Pdf(suite, label='posterior')
    thinkplot.Show()


if __name__ == '__main__':
    main()
