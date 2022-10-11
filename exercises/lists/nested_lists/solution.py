#!/usr/bin/env python
# coding=utf-8

scores_stats = []

for _ in range(0,int(input())):
    scores_stats.append([input(), float(input())])

# Make a unique list of score, sort it and get the lowest second score
second_lowest = sorted(list(set([score for name, score in scores_stats])))[1]

# Iterate over the list of scores and names and print every match to the
# lowest score we got above
print('\n'.join([a for a,b in sorted(scores_stats) if b == second_lowest]))
