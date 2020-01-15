"""
utility functions for working with Data
"""

import pandas

TEST_DF = pandas.DataFrame([1,2,3])


d = {'imdb_score' : [1,1.4,1,2.4,2,3,4.8,5,6,6.9,6,6,7,7.5,7.9, 8,9,10,11,12,13,14]}
movie = pandas.DataFrame(data=d)

def bin_rating(rating):
  if rating <= 5:
    return 'poor'
  elif rating <= 7:
    return 'average'
  elif rating <= 8:
    return 'good'
  else:
    return 'excellent'

movie['rating_bin'] = movie['imdb_score'].apply(bin_rating) 

