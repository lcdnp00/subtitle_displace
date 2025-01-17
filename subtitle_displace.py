# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 11:11:50 2024

@author: User
"""
import re
import os.path as op

def move_subs(file, seconds, target):
    mode = pick_mode(target)
    lc = 0
    with open(file, 'r') as ogsubs:
        with open(target, mode) as newsubs:
            for line in ogsubs:
                lc += 1
                print(line)
                if "-->" in line:
                    newsubs.write(change(seconds, line))
                else:
                    newsubs.write(line)
        

                  
def pick_mode(file):
    if op.isfile(file):
        return 'w'
    return 'a'

def change(seconds, line):
    tokens = line.split(" ")
    return add_time(tokens[0], seconds) + " --> " + add_time(tokens[2], seconds)

def add_time(s, seconds):# must be formatted as HH:MM:SS,mmm --> HH:MM:SS,mmm
    if not re.match("[0-9][0-9]:[0-5][0-9]:[0-5][0-9],[0-9][0-9][0-9]", s):
        raise ValueError
    minutes = (seconds // 60) % 60
    hours = seconds // 3600
    sec = (seconds - minutes * 60 - hours * 3600) % 60
    units = s.split(":")
    return str("").join([pad(str(nn(int(units[0]) + hours + int(int(units[1]) + minutes + int(int(units[2][0:2]) + sec > 59) > 59)))), ":", pad(str(nn((int(units[1]) + minutes + int(int(units[2][0:2]) + sec > 59)) % 60))), ":", pad(str(nn((int(units[2][0:2]) + sec) % 60))), units[2][2:]])

def pad(s):
    if len(s) == 1 or s[1] == ",":
        return "0" + s
    return s

def nn(i):
    return max(0, i)