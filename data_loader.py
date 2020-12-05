# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 17:30:06 2020

@author: mcwa
"""


import pickle

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

d_file = open(vid_to_patient_tuples_file, "rb")
vid_patient_tuples_dict = pickle.load(d_file)
d_file.close()

# print(patient_vid_dict)
# print(vid_patient_dict)
# print(vid_tags_dict)
# print(vid_patient_tuples_dict)