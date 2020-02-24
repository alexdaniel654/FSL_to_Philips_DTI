# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 16:29:55 2018

@author: Alex Daniel
"""
import numpy as np
import sys
import datetime
import os


def query_yes_no(question, default="yes"):
    """Ask a yes/no question via raw_input() and return their answer.

    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
        It must be "yes" (the default), "no" or None (meaning
        an answer is required of the user).

    The "answer" return value is True for "yes" or False for "no".
    """
    valid = {"yes": True, "y": True, "ye": True,
             "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + prompt)
        choice = input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' "
                             "(or 'y' or 'n').\n")


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


print('This software generates spherical DTI vectors that Philips MRI scanners can read.\n'
      'More information about why you would want a full sphere of vectors rather than a hemisphere can be found here\n'
      'https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/eddy\n')

nvecs = int(input('How many directions? (Between 2 and 255) '))
if nvecs > 255:
    raise ValueError('Number of vectors should be between 2 and 255.\n' + str(nvecs) + ' is more than 255.')

if nvecs < 2:
    raise ValueError('Number of vectors should be between 2 and 255.\n' + str(nvecs) + ' is less than 2.')

bval = input('What b-value? ')

overwrite = query_yes_no('Do you want to overwrite the existing dti_vectors_input.txt file?', default='yes')

vecs = np.loadtxt(resource_path('./Raw_Vectors/'+str(nvecs+1).zfill(3)+'_optws.txt'))
vecsout = np.ones([vecs.shape[0], vecs.shape[1]+1])
vecsout[:, 0:-1] = vecs
vecsout[0, -1] = 1E-4
vecsout[1:, -1] = bval

if overwrite:
    fout = 'dti_vectors_input.txt'
else:
    fout = 'dti_vectors_input-fsl_'+str(nvecs).zfill(3)+'directions_bval_'+str(bval)+'.txt'

open(fout, 'w').close()

f = open(fout, 'a')
f.write('Spherical\n')
np.savetxt(f, vecsout, fmt='%7.4f')
f.close()

h = open('dti_vector_history.log', 'a')
timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
line = timestamp + ', ' + str(nvecs).zfill(3) + ' directions, ' + str(bval).zfill(4) + ' bval\n'
h.write(line)
h.close()
