"""This file contains code for use with "Think Bayes",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function, division

import thinkbayes2


class Cookie(thinkbayes2.Suite):
    """A map from string bowl ID to probablity."""

    def Likelihood(self, data, hypo):
        """The likelihood of the data under the hypothesis.

        data: string cookie type
        hypo: string bowl ID
        """
        like = hypo[data] / hypo.Total()
        if like:
            hypo[data] -= 1
        return like


def main():
    bowl1 = thinkbayes2.Hist(dict(vanilla=50, chocolate=0))
    bowl2 = thinkbayes2.Hist(dict(vanilla=25, chocolate=25))
    bowl3 = thinkbayes2.Hist(dict(vanilla=25, chocolate=25))
    pmf = Cookie([bowl1, bowl2, bowl3])

    print('After 1 vanilla')
    pmf.Update('vanilla')
    for hypo, prob in pmf.Items():
        print(hypo, prob)

    print('\nAfter 1 vanilla, 1 chocolate')
    pmf.Update('vanilla')
    for hypo, prob in pmf.Items():
        print(hypo, prob)


if __name__ == '__main__':
    main()
