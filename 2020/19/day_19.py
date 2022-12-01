#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

def match_rules(rules, rule_ids, message):
    if len(rule_ids) == 0:
        # no rule left to match -> message must be empty
        return (len(message) == 0)
    rid = rule_ids.pop(0)
    if type(rules[rid]) is str:
        # rule is a char
        if message.startswith(rules[rid]):
            return match_rules(rules, rule_ids, message[len(rules[rid]):])
    else:
        # rule is a (list of) list of rule_ids
        return any(match_rules(rules, r_alt + rule_ids, message) for r_alt in rules[rid])
    

input_file = "input"
# input_file = "test1.txt"
# input_file = "test2.txt"

if __name__ == '__main__':
    count1, count2 = 0, 0

    with open(input_file,'r') as f:
        rules_raw, messages_raw = f.read().split('\n\n')
        
    rules= {}
    messages = []
    
    for r in rules_raw.split('\n'):
        rid, rule = r.split(':')
        if '"' in rule:
            content = rule.strip(' ').strip('"')
        else:
            content = [[int(i) for i in r.strip().split(' ')] for r in rule.split('|')]
        rules[int(rid)] = content
    
    for m in messages_raw.split('\n'):
        messages.append(m)
    
    # print(rules)
    # print(messages)
    
    count1 = sum(match_rules(rules, [0], m) for m in messages)

    rules[8] = [[42], [42, 8]]
    rules[11] = [[42, 31], [42, 11, 31]]
    count2 = sum(match_rules(rules, [0], m) for m in messages)

    print("Step 1:", count1)
    print("Step 2:", count2)

