import pickle

with open('vid_to_tags.pkl', 'rb') as f:
    vid_to_tags = pickle.load(f)

# def parse(tags_str):
#     if tags_str == '[':

for vid in vid_to_tags:
    tags_str = vid_to_tags[vid]
    print('tags list: ' + tags_str)
    print(f"type is {type(tags_str)}")
    # vid_to_tags[vid] = parse(tags_str)


def weight_by_tags(video_1, video_2):
    pass