#!/usr/bin/python3
def best_score(my_dict):
    if ((my_dict == {}) or (my_dict is None)):
        return (None)
    max_val = max(my_dict.values())
    for k, value in my_dict.items():
        if (value is max_val):
            return (k)
