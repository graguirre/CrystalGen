#
# Generate crystal given a size and element.
# 
# Check list for supported elements.
#
# Author: Gonzalo Aguirre <graguirre@gmail.com>
#

import sys, getopt
import numpy as np

def usage():
  print >> sys.stderr, "Options:"
  print >> sys.stderr, " -h             Show help"
  print >> sys.stderr, " -e <element>   Element (Supported: He, Li, Ne, Na, Fe, Cu, Ag, Pt, Au)"
  print >> sys.stderr, " -s <integer>   Integer number"
  print >> sys.stderr, "Syntax: python2 crystal.py -e Pt -s 1"
  sys.exit(1)

def main(argv):
  # init vars
  e = ''
  K = 0

  # manage parameters
  try:
    opts, args = getopt.getopt(argv,"he:s:")
  except getopt.GetoptError:
    usage()

  for opt, arg in opts:
    if opt == '-h':
      usage()
    elif opt == '-e':
      e = arg
    elif opt == '-s':
      K = int(arg)

  # Elements. In order to add new elements is a list of Z, lattice constant, and crystal structure.
  # data from http://periodictable.com/index.html
  d={'He':[2,4.242,'FCC'], 'Li':[3,3.51,'BCC'],'Ne':[10,4.421,'FCC'],\
	'Na':[11,4.291,'BCC'], 'Fe':[26,3.615,'BCC'],'Cu':[29,3.615,'FCC'],\
	'Ag':[47,4.085,'FCC'], 'Pt':[78,3.924,'FCC'],'Au':[79,4.078,'FCC']}

  if e not in d.keys():
    print >> sys.stderr, "ERROR: not supported element"


  a = d[e][1]
  # select crystal structure  
  if d[e][2] == 'FCC':
    v=np.array([[0,0,0],[0,a/2,a/2],[a/2,0,a/2],[a/2,a/2,0]])
  elif d[e][2] == 'BCC':
    v=np.array([[0,0,0],[a/2,a/2,a/2]])
  elif d[e][2] == 'SC':
    v=np.array([[0,0,0]])
  else:
    usage()	

  for i in range(K+1):
    for j in range(K+1):
      for k in range(K+1):
        for l in v:
          if np.max( l+np.array([a*i, a*j, a*k]) ) <= a*K:
            vt = l+np.array([a*i, a*j, a*k])
            print e, vt[0], vt[1], vt[2]

if __name__ == "__main__":
	main(sys.argv[1:])
