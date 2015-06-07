import math, os, sys
moddir = os.path.join( os.path.dirname( __file__ ), '..' )
sys.path = [moddir] + sys.path
from configmakover.read import *
from forbiddenfruit import curse


def test_construction():

  d = AttrDict( {'one':1, 'two':2} )
  d.three = 3
  d.four = AttrDict( {'one' : 41, 'two' : 42, 'three' : AttrDict( { 'one' : 431 } ) } )
  d.five = [ 1, 2, 3, AttrDict( { 'one' : 541 } ) ]

  assert d.one == 1
  assert d.two == 2
  assert d.three == 3
  assert d.four.one == 41
  assert d.four.two == 42
  assert d.four.three.one == 431
  assert d.five[0] == 1
  assert d.five[1] == 2
  assert d.five[2] == 3
  assert d.five[3].one == 541


def test_conversion():
  d = {'one':1, 'two':2}
  d['three'] = 3
  d['four'] = {'one' : 41, 'two' : 42, 'three' : { 'one' : 431 } }
  d['five'] = [ 1, 2, 3, { 'one' : 541 } ]

  assert d['one'] == 1
  assert d['two'] == 2
  assert d['three'] == 3
  assert d['four']['one'] == 41
  assert d['four']['two'] == 42
  assert d['four']['three']['one'] == 431
  assert d['five'][0] == 1
  assert d['five'][1] == 2
  assert d['five'][2] == 3
  assert d['five'][3]['one'] == 541


  d = toAttrDict(d)
  assert d.one == 1
  assert d.two == 2
  assert d.three == 3
  assert d.four.one == 41
  assert d.four.two == 42
  assert d.four.three.one == 431
  assert d.five[0] == 1
  assert d.five[1] == 2
  assert d.five[2] == 3
  assert d.five[3].one == 541

