#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

def match_rules(rules, rule_ids, message):
    if not rule_ids:
        return not message
    # rid = rule_ids.pop(0)
    rid, *rule_ids = rule_ids
    rule = rules[rid]
    if isinstance(rule, str):
        return (message.startswith(rule)
                and match_rules(rules, rule_ids, message[len(rule):]))
    else:
        return any(match_rules(rules, option + rule_ids, message) for option in rule)
    

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
        # rid, rule = r.split(':')
        # if '"' in rule:
        #     content = rule.strip(' ').strip('"')
        # else:
        #     content = [[int(i) for i in r.strip().split(' ')] for r in rule.split('|')]
        # rules[int(rid)] = content
        match = re.search(r'^(\d+): (?:\"(\w)\"|(\d+(?: \d+)*(?: \| \d+(?: \d+)*)*))$', r)
        rid = int(match.group(1))
        if match.group(2):
            rules[rid] = match.group(2)
        else:
            rules[rid] = [list(map(int, re.findall(r'\d+', option))) for option in match.group(3).split('|')]
    
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

