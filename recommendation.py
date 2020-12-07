# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 18:48:50 2020

@author: somaiars
"""
import popularity
import videos_to_neighbors

def recommendation(video_id):
     w = videos_to_neighbors.videos_to_neighbors()
     p = popularity.popular()
     wvids = []
     rec_list = []
     for wtuple in w[video_id]:
         wvids.append(wtuple[0])
     if len(wvids) < 5:
         if len(wvids) == 0:
             pass
         else:
             rec_list += wvids
     else:
        rec_list = wvids[:5]
        rec_list.append(p[0])
     if video_id in rec_list:
         rec_list.remove(video_id)
     return rec_list

r = recommendation(624)  
print(r)  
    
         
     