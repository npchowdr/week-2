import numpy as np


# update/add code below ...

def ways(n):
    #find the maximum number of nickels that can be used
    max_nickels = n // 5
    total_ways = max_nickels + 1 # include the case where no nickels are used

    return total_ways

def lowest_score(names, scores):
    # find index of lowest score using argmin and return corresponding name
    lowest_score_index = np.argmin(scores)
    return names[lowest_score_index]

def sort_names(names, scores):
    # sort names based on scores using argsort
    sorted_indices = np.argsort(scores)
    sorted_names = [names[i] for i in sorted_indices]
    return sorted_names[::-1] # return in descending order