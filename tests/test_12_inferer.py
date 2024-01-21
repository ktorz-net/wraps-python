import sys
sys.path.insert( 1, __file__.split('tests')[0] )

# ------------------------------------------------------------------------ #
#                T E S T   p y B b M m  : :  I N F E R E R                 #
# ------------------------------------------------------------------------ #

import pyBbMm as bm

def test_BbMmInferer_init():
    trans= bm.Inferer()
    assert type(trans) == bm.Inferer
