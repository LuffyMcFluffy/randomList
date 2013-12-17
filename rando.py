#!/usr/bin/python
# 0.1 release 14 Dec 2013 - MSCC Meetup


# Script outputs random line from infile (by default memerList in working directory)
f = open("memberList","r")
g = f.read()
g = g.split("\n")
import random

i = random.randrange(0,len(g))

print g[i]
