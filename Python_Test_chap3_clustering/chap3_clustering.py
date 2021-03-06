# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 14:13:59 2015

@author: 一郎
"""
import os

from sklearn.feature_extraction.text import CountVectorizer
#vectorizer = CountVectorizer(min_df=1)
vectorizer = CountVectorizer(min_df=1, stop_words='english')
print(vectorizer)

content = ["How to format my hard disk", "Hard disk format problems "]
X = vectorizer.fit_transform(content)
print(vectorizer.get_feature_names())

print(X.toarray().transpose())

filepath = 'C:/Python27/test'
DIR = filepath
posts = [open(os.path.join(DIR, f)).read() for f in os.listdir(DIR)]
X_train = vectorizer.fit_transform(posts)
num_samples, num_features = X_train.shape
print("#samples: %d, #features: %d" % (num_samples, num_features))
print(vectorizer.get_feature_names())
new_post = "imaging databases"
new_post_vec = vectorizer.transform([new_post])
print(new_post_vec)
print(new_post_vec.toarray())

import scipy as sp
def dist_raw(v1, v2):
    delta = v1-v2
    return sp.linalg.norm(delta.toarray())
    
import sys
best_doc = None
best_dist = sys.maxint
best_i = None
for i in range(0, num_samples):
    post = posts[i]
    if post==new_post:
        continue
    post_vec = X_train.getrow(i)
    d = dist_raw(post_vec, new_post_vec)
    print "=== Post %i with dist=%.2f: %s"%(i, d, post)
    if d < best_dist:
        best_dist = d
        best_i = i
print("Best post is %i with dist=%.2f"%(best_i, best_dist))

print(X_train.getrow(3).toarray())
print(X_train.getrow(4).toarray())

def dist_norm(v1, v2):
    v1_normalized = v1/sp.linalg.norm(v1.toarray())
    v2_normalized = v2/sp.linalg.norm(v2.toarray())
    delta = v1_normalized - v2_normalized
    return sp.linalg.norm(delta.toarray())

best_doc = None
best_dist = sys.maxint
best_i = None
for i in range(0, num_samples):
    post = posts[i]
    if post==new_post:
        continue
    post_vec = X_train.getrow(i)
    d = dist_norm(post_vec, new_post_vec)
    print "=== Post %i with dist=%.2f: %s"%(i, d, post)
    if d < best_dist:
        best_dist = d
        best_i = i
print("Best post is %i with dist=%.2f"%(best_i, best_dist))

vectorizer = CountVectorizer(min_df=1, stop_words='english')
print(sorted(vectorizer.get_stop_words())[0:10])

