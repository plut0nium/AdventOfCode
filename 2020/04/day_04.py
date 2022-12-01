#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import math
import re

input_file = "input"
#input_file = "test1.txt"
#input_file = "test2.txt"
#input_file = "test3.txt"

eye_color = {'amb','blu','brn','gry','grn','hzl','oth'}
hgt_pattern = re.compile(r'^(\d{2,3})(in|cm)$')
hcl_pattern = re.compile(r'#[0-9a-f]{6}')
pid_pattern = re.compile(r'^\d{9}$')

def validate_year(y, ymin, ymax):
    try:
        # if int(y) >= ymin and int(y) <= ymax:
        if ymin <= int(y) <= ymax:
            return True
    except ValueError:
        pass
    return False

def validate_byr(y):
    return validate_year(y, 1920, 2002)

def validate_iyr(y):
    return validate_year(y, 2010, 2020)

def validate_eyr(y):
    return validate_year(y, 2020, 2030)

def validate_ecl(c):
    return c in eye_color

def validate_hcl(c):
    return hcl_pattern.match(c) is not None

def validate_hgt(c):
    h = hgt_pattern.match(c)
    if h is None:
        return False
    if h.group(2) == 'in':
        # if int(h.group(1)) in range(59,76+1):
        if 59 <= int(h.group(1)) <= 76:
            return True
    else:
        # if int(h.group(1)) in range(150,193+1):
        if 150 <= int(h.group(1)) <= 193:
            return True
    return False

def validate_pid(c):
    return pid_pattern.match(c) is not None

field_validator = {'byr': validate_byr,
                   'iyr': validate_iyr,
                   'eyr': validate_eyr,
                   'hgt': validate_hgt,
                   'hcl': validate_hcl,
                   'ecl': validate_ecl,
                   'pid': validate_pid } # + 'cid'

if __name__ == '__main__':
    passports = []
    
    with open(input_file,'r') as f:
        for l in f.read().strip().split('\n\n'):
            p = {}
            for f in re.split(' |\n', l):
                k,v = f.split(':')
                p[k] = v.strip()
            passports.append(p)
        
    #print(passports)
    n1 = len(passports)
    n2 = 0
    
    for p in passports:
        has_fields = True
        for f in field_validator.keys():
            if f not in p:
                has_fields = False
                n1 -= 1
                break
        if has_fields:
            if all([field_validator[f](p[f]) for f in field_validator.keys()]):
                n2 += 1
        
    print("Step 1:", n1)
    print("Step 2:", n2)


