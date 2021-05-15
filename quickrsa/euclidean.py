import math
import random

def extended_ea(r1, r2, s1=1, s2=0, t1=0, t2=1):
	if r2 == 0:
		if s1 < 0:
			s1 += s2
		if t1 < 0:
			t1 += t2
		return r1, s1, t1
	q, r = r1//r2, r1%r2
	s, t = s1-s2*q, t1-t2*q
	return extended_ea(r2, r, s2, s, t2, t)

def ea(r1, r2):
	if r2 == 0:
		return r1
	r = r1%r2
	return ea(r2, r)