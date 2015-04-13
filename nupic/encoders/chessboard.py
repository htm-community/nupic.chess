from nupic.encoders.base import Encoder




class ChessboardEncoder(Encoder):
  """Encodes a FEN string."""



  def __init__(self, w, fen, name="chessboard", verbosity=0, forced=False):
    pass



  ############################################################################
  def getDecoderOutputFieldTypes(self):
    """ [Encoder class virtual method override] """
    pass



  ############################################################################
  def getWidth(self):
    pass



  ############################################################################
  def getDescription(self):
    pass



  ############################################################################
  def getScalars(self, input):
    """ See method description in base.py """
    pass



  ############################################################################
  def getBucketIndices(self, input):
    """ See method description in base.py """
    pass



  ############################################################################
  def encodeIntoArray(self, input, output):
    """ See method description in base.py """
    pass



  ############################################################################
  def decode(self, encoded, parentFieldName=''):
    """ See the function description in base.py """
    pass



  ############################################################################
  def closenessScores(self, expValues, actValues, fractional=True,):
    """ See the function description in base.py """
    pass



  ############################################################################
  def getBucketValues(self):
    """ See the function description in base.py """
    pass



  ############################################################################
  def getBucketInfo(self, buckets):
    """ See the function description in base.py """
    pass



  ############################################################################
  def topDownCompute(self, encoded):
    """ See the function description in base.py """
    pass

