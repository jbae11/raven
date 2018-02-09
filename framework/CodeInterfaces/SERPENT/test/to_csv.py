import os
import copy
from pyne import serpent
import sys

def finalizeCodeOutput(output, csv_name):
    """
      SERPENT outputs .m text files (dep, det, res files).
      These files are converted to dictionaries using pyne.serpent
      and converted to a csv file in this function.
    """

    # using pyne parse files into dictionaries
    dep_dict = serpent.parse_dep(output + '.dep')
    det_dict = serpent.parse_det(output + '.det')
    res_dict = serpent.pares_res(output + '.res')

    print (dep_dict)
    print('THIS IS DET DICT \n\n')
    print (det_dict)
    print('THIS IS RES DICT \n\n')
    print (res_dict)

    # create a csv file in the output path
    csv_file = open(csv_name + '.csv')
    csv_file.write(',', .join(keyDict.keys()))
    csv_file.write(',', .join(keyDict.values()))


finalizeCodeOutput(sys.argv[1], sys.argv[2])

