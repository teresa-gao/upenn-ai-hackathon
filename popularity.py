# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 18:21:28 2020

@author: somaiars
"""
import data_loader


def popular():
    """
    This function takes in a dictionary where the key is a video and the value is a tuple
    of patients who have watched the video and how many times they have watched it. It returns
    a list of the video IDs sorted by popularity. popularity[0] is the most popular video. 
    """
    d = data_loader.vid_patient_tuples_dict
    most_popular_videos = []
    for k in sorted(d, key=lambda k: len(d[k]), reverse=True):
        most_popular_videos.append(k)
    return most_popular_videos



    
    