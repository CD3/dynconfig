#! /usr/bin/python

import sys, os
moddir = os.path.join( os.path.dirname( __file__ ), '..' )
sys.path = [moddir] + sys.path

import pytest
from utils import *


from dynconfig.render import *

def test_simple():
  logging.info("simple quantities")
  data = { 'size' : 100
          ,'x':
          { 'min' : "$( '-1 m' | to cm | float)"
          , 'max' : "$( '2 m' | to cm | float )"
          , 'dx'  : '$( ({max} - {min}) / {/size} )'
          }
          ,'pulse-width' : "$(10 us | to s | float)"
         }

  rendered_data = render( data, repeat = True )

  assert type(rendered_data['x']['dx']) ==  float
  assert rendered_data['x']['dx'] ==  Approx( (200.-(-100.))/100 )

  assert type(rendered_data['pulse-width']) ==  float
  assert rendered_data['pulse-width'] ==  Approx(10e-6)