#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
xyzshuffle
========
For an input .XYZ format file, make an XYZ-format output file with the
atom records reordered in a sequence specified on the command line. 

"""

__version__ = "20210818.0001"

from builtins import input
import sys,os,math,copy,argparse

import beacon_utils as bu


def main():
    print(__doc__)
    parser = argparse.ArgumentParser(description="xyzshuffle")
    parser.add_argument("inxyz", help="Input XYZ file")
    parser.add_argument("outxyz", help="Output XYZ file")
    parser.add_argument("orderstring", help="Quote-delimited, comma-separated new atom number sequence order using input file row numbers, starting at 1")
    args = parser.parse_args()
    xyzname = args.inxyz
    outname = args.outxyz
    orderstring = args.orderstring
    print(orderstring)
    #if not (orderstring.startswith("\"") or orderstring.startswith("\'") ):
    #    print('New atom order string must be bounded by quote marks!')
    #    sys.exit()        
    translation = orderstring.maketrans('\"\',','   ')
    neworderstring = orderstring.translate(translation)
    orderstring = ' '.join(neworderstring.split())

    # main program starts here
    for line in bu.repheader():
        print(line)
    print("VERSION "+__version__)
    print("")

    print('Original atom number sequence in input XYZ file will be re-ordered')
    #print(' '.join(list(range(0,natoms))))
    print('Requested atom number sequence is:')
    print(orderstring)
    atomindex = [ int(s)-1 for s in orderstring.split() ]
    
    # open the input xyz file
    if xyzname == outname:
        print('Input and output ZYZ files must have different names')
        sys.exit()
    print ('Opening input file : {}'.format(xyzname))
    print ('Opening output file : {}'.format(outname))
    xyzfile = open(xyzname, 'r')
    outfile = open(outname, 'w')
    
    # Use a variable to count the number of 'frames' in the input file
    n = 0
    
    # read the first line of the file
    line = xyzfile.readline()
    # keep doing this part until there are no more lines in the input file
    while line:
        natoms = int(line)                 # get the number of atoms in this frame (must convert from string to integer using 'int')
        if natoms != len(atomindex):
            print('XYZ frame(s) has {0} atoms, but specified order string has {1}'.format(natoms,len(atomindex)))
            sys.exit()            
        n = n + 1                          # increase the current frame number
        # print a message for the user
        # print('Frame {} has {} atoms'.format(n, natoms))
        frametitle = xyzfile.readline()    # read the frame title
        atsym = []                         # make a new empty lists of atom symbols, x, y, z coordinates
        atx = []
        aty = []
        atz = []
        for i in range(0,natoms):
            line = xyzfile.readline()
            linedata = line.split()        # split up the line into columns, store in 'linedata'
            symbol = linedata[0]           # first string of non-space characters is the atomic symbol
            # Now read the coordinates (must convert from string to floating point number using 'float')
            x      = float(linedata[1])    # second column of data is the x-coordinate
            y      = float(linedata[2])    # third column of data is the y-coordinate
            z      = float(linedata[3])    # fourth column of data is the z-coordinate
            atsym.append(symbol)
            atx.append(x)
            aty.append(y)
            atz.append(z)
        # re-order 
               
        # Finished reading in data for this frame, now make the output file frame
        outfile.write('{0}\n'.format(natoms))
        outfile.write('{0}\n'.format(frametitle.strip()))
        for i in range(0,natoms):
            newindex = atomindex[i]
            outfile.write('{} {: f} {: f} {: f}\n'.format(atsym[newindex],atx[newindex],aty[newindex],atz[newindex]))
        line = xyzfile.readline()
    # end of loop over frames 
    xyzfile.close()
    outfile.close()    
    #
    print('Program exiting')

if __name__ == "__main__":
    main()
