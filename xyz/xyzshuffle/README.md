xyzshuffle
==========
For an input .XYZ format file, make an XYZ-format output file with the
atom records reordered in a sequence specified on the command line.


usage: xyzshuffle [-h] inxyz outxyz orderstring

positional arguments:
  inxyz        Input XYZ file
  outxyz       Output XYZ file
  orderstring  Quote-delimited, comma-separated new atom number sequence order using input file row numbers, starting at 1

optional arguments:
  -h, --help   show this help message and exit
