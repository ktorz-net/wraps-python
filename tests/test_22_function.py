import sys
sys.path.insert( 1, __file__.split('tests')[0] )

# ------------------------------------------------------------------------ #
#                T E S T   p y B b M m  : :  C R I T E R I O N             #
# ------------------------------------------------------------------------ #

import pyBbMm.core as bm
from pyBbMm.core import clibBbMm as cc

def test_BbMmFunction_init():
    instance= bm.Function()
    assert type(instance) == bm.Function