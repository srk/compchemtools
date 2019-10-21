#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Steven R. Kirk and Samantha Jenkins (2014,2019)
# 
import sys
import argparse
from __future__ import print_function,division

__version__='201910210001'

def main():
    # main code
    # argument parser
    parser = argparse.ArgumentParser(description="Analyzes Gaussian 09 log files for optimization calculations\n"+
                                                 "=============================================================")
    parser.add_argument("inputfile", help="G09 output log file")                                    
    # parse the arguments                                
    args = parser.parse_args()
    infile=args.inputfile

    print ('=========')
    print (' opthelp')
    print ('=========')

    f = open(infile)
    steps = 0

    # Find the link 0 lines and route line

    link0 = []
    routeline =""
    foundlink0 = 0
    while (1): 
        line = f.readline()
        if line.startswith(" %"):
            foundlink0 = 1
            link0.append(line[1:-1])
        if (line.startswith(" ---") and foundlink0 == 1):
            break    

    while (1):
        line = f.readline()
        if line.startswith(" ---"):
           break
        routeline += line[1:-1]
    #print link0       
    print routeline
    
    # find the Title
    while (1):
        line = f.readline()
        if line.startswith(" ----"):
           break       
    title = f.readline()[1:-1]
    #print title
    
    # find the Charge and multiplicity
    line = f.readline()
    line = f.readline()
    line = f.readline()
    cmlist = line.split()
    charge = int(cmlist[2])
    mult = int(cmlist[5])
    #print ('Charge = ', charge)
    #print ('Multiplicity = ', mult)
    
    # find the atom symbols
    atsyms = []
    while (True):
        line = f.readline()
        if (line.lstrip() == ''):
          break
        tokens = line.split()
        # print tokens
        atsym = tokens[0]
        atsyms.append(atsym)
        
    # now find the best optimization step    
    scores = []
    framedata = []
    
    while (True):
        line = f.readline()
        if not line:
           break
        if ('Converged?' in line):
           s = 1.0 # figure of merit score: product of optimization (YES/NO) numerical ratios (lower is better)
           for i in range (1,4):
               line = f.readline()
               tokens = line.split()
               if (tokens[-1] == 'NO'):
    #
    # Sometimes an optimization value can be displayed in the .log file as 0.000000
    # To make a usable figure of merit, we must force this value to 0.000001
    #               
                  if ( float(tokens[-3]) < 0.000001): 
                      tokens[-3] = '0.000001'
                  s = s * float(tokens[-3]) / float(tokens[-2])
           scores.append(s)
    # store the atomic position data for this step
    # find the next line beginning with ' Number'
           while (True):
               line = f.readline()
               if line.startswith(" Number"):
                   break
    # skip a line
           line = f.readline()
    # now read and store the structure data
           thisframe = []
           while (True):
               line = f.readline()
               if (line.startswith(' ---')):
                   break
               tokens = line.split()
               atnum = int(tokens[1])
               x = float(tokens[3])
               y = float(tokens[4])
               z = float(tokens[5])
               thisframe.append([atnum,x,y,z])           
           framedata.append(thisframe)     
    numsteps = len(scores)
    
    # find the minimum score
    minscore = scores[0]
    for score in scores:
        if (score < minscore):
           minscore = score    
    minidx = scores.index(minscore)
    
    if (minscore == 1.0):
        print ('Geometry optimization converged - no need to restart')
    else:
        print ('Geometry optimization did not converge!')
        print ('Best optimization step was step '+str(minidx+1)+' of '+str(len(scores))+': value = '+str(minscore))
        bestframe = framedata[minidx]
    # write out a new .gjf file
        outname = fname[:-4]+'_best.gjf'
        print ('Writing a new input file: '+outname)
        fout = open(outname,'w')
        for line in link0:
            fout.write(line+'\n')
        fout.write(routeline+'\n')
        fout.write('\n')
        fout.write(title+'\n')
        fout.write('\n')
        fout.write(str(charge)+' '+str(mult)+'\n')
        for i in range (0, len(bestframe)):
            atom = bestframe[i]
    #        fout.write(atsyms[i]+' '+str(atom[1])+'  '+str(atom[2])+'  '+str(atom[3])+'\n')
            fout.write("{0} {1: f} {2: f} {3: f}\n".format(atsyms[i],atom[1],(atom[2]),atom[3]))
        fout.write('\n')
        fout.close()    
    
    # tidy up and exit
    print('NOTE: this script does NOT copy custom (Gen) basis set specifications or Output() filenames: check the *_best.gjf file!')
    f.close()

if __name__ == '__main__':
    main()  
