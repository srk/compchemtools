# -*- coding: utf-8 -*-
"""
xyz_to_xyz
===========
Split an xyz-format coordinate file, containing 1 or more structures
into multiple .xyz files. 

Usage: xyz_to_xyz split <xyz file name> 

@author: steve
"""
# Python 2 compatibility shims
from __future__ import print_function, division
__version__ = "20190621.0002"
import sys, argparse


def main():
    print(__doc__)
    
    print('VERSION: '+__version__)
    parser = argparse.ArgumentParser(description='Transform an input .xyz file into other forms')
    parser.add_argument("operation", help="Operation to perform (default=split)",choices=['split'],default="split")
    parser.add_argument("xyzname", help="Name of input .xyz file")                             
    args = parser.parse_args()
    operation = args.operation
    xyzname = args.xyzname
    
    # open the input xyz file
    
    print ('Opening input file : {}'.format(xyzname))
    xyzfile = open(xyzname, 'r')
    
    # Use a variable to count the number of 'frames' in the input file
    n = 0
    
    
    # read the first line of the file
    line = xyzfile.readline()
    # keep doing this part until there are no more lines in the input file
    while line:
        natoms = int(line)                 # get the number of atoms in this frame (must convert from string to integer using 'int') 
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
            
        # Finished reading in data for this frame, now make the output file
        if operation == 'split':    
            inpname = xyzname.replace('.xyz', '_'+'{:04d}'.format(n)+'.xyz')
            print('Preparing file {}'.format(inpname))
            with open(inpname,'w') as inpfile:
                inpfile.write('{0}\n'.format(natoms))
                inpfile.write('{0}\n'.format(frametitle.strip()))
                for i in range(0,natoms):
                    inpfile.write('{} {: f} {: f} {: f}\n'.format(atsym[i],atx[i],aty[i],atz[i]))
        
        # read in the number of atoms in the next frame
        line = xyzfile.readline()

if __name__ == '__main__':
    main()
