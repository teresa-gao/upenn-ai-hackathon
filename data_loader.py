# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 17:30:06 2020

@author: mcwa
"""


import pickle
import ast

patient_to_vid_file = "patient_to_vid.pkl"
vid_to_patient_file = "vid_to_patient.pkl"
vid_to_tags_file = "vid_to_tags.pkl"
vid_to_patient_tuples_file = "vid_to_patient_tuples.pkl"

a_file = open(patient_to_vid_file, "rb")
patient_vid_dict = pickle.load(a_file)
a_file.close()

b_file = open(vid_to_patient_file, "rb")
vid_patient_dict = pickle.load(b_file)
b_file.close()

c_file = open(vid_to_tags_file, "rb")
vid_tags_dict = pickle.load(c_file)
c_file.close()
for k in vid_tags_dict.keys():
    vid_tags_dict[k] = set(ast.literal_eval(vid_tags_dict[k]))

vid_patient_tuples_dict = {}

for patient in vid_patient_dict.keys():
    watch_dict = {}
    views = vid_patient_dict[patient]
    for v in views:
        if v in watch_dict.keys():
            watch_dict[v] += 1
        else:
            watch_dict[v] = 1
    vid_patient_tuples_dict[patient] = [(k, watch_dict[k]) for k in watch_dict.keys()]

# d_file = open(vid_to_patient_tuples_file, "rb")
# vid_patient_tuples_dict = pickle.load(d_file)
# d_file.close()

# print(patient_vid_dict)
# print(vid_patient_dict)
# print(vid_tags_dict)
# print(vid_patient_tuples_dict)