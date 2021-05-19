from enum import IntEnum

from .responses import *
from .signatures import *
from .transactions import *


class ChainId(IntEnum):
    MAINNET = 10
    RINKEBY = 4
    ROPSTEN = 3
    LOCALHOST = 9
