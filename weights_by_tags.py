import pickle
import ast

with open('vid_to_tags.pkl', 'rb') as f:
    vid_to_tags = pickle.load(f)


for vid in vid_to_tags:
    vid_to_tags[vid] = set(ast.literal_eval(vid_to_tags[vid].lower().replace(" ", "")))


def weight_by_tags(video_1, video_2):
    # intersection of two video's
    tags_set_1 = vid_to_tags[video_1]
    tags_set_2 = vid_to_tags[video_2]
    weight = len(tags_set_1.intersection(tags_set_2))
    return weight
