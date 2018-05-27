from method.ReadFile import ReadFile
from method.TermFrequencyAndInverseDocumentationFrequency import Tf_idf
from method.TimeModel import TimeModel

readfile = ReadFile()
tf_idf = Tf_idf(readfile.Data)
timemodel = TimeModel(tf_idf.data)