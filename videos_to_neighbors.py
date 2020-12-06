import pickle
import ast

# unpickle the dictionaries! (will be included in the top-level function this function will be a helper for)
with open("vid_to_patient_tuples.pkl", "rb") as f:
    vid_to_patient_tuples = pickle.load(f)
with open("patient_to_vid.pkl", "rb") as f:
    patient_to_vid = pickle.load(f)
with open("vid_to_patient.pkl", "rb") as f:
    vid_to_patient = pickle.load(f)
with open('vid_to_tags.pkl', 'rb') as f:
    vid_to_tags = pickle.load(f)

for vid in vid_to_tags:
    # makes a set of all of the tags after converting each tag to lowercase and deleting spaces between words
    # (gets rid of some duplicates, e.g. tedtalk vs. Ted Talk vs. ted talk)
    vid_to_tags[vid] = set(ast.literal_eval(vid_to_tags[vid].lower().replace(" ", "")))


def videos_to_neighbors():
    """
    Given a dictionary mapping video IDs to patient IDs and a dictionary mapping patient IDs to video IDs, returns a dictionary mapping videos to list of tuples of videos watched and related weight with the lists sorted by weight.

    The dictionary will look something like this: { current_video: [ (next_video_1, weight_1), … ], … }.
    """

    def weight_by_patients(video1, video2):
        """
        Given two videos, returns the patient count-based weight between two given linked videos.

        The weight is the sum of (1/2)^(n-1) for all n = 0, ..., (number of views by the same patient)
        """

        edge_weight = 0

        for patient, watch_count in vid_to_patient_tuples[video1]:

            # add weight via diminishing returns function on repeat views by the same patient
            edge_weight += ( 1/2 ) ** ( watch_count - 1 )

        return edge_weight

    def weight_by_tags(video1, video2):
        """
        Given two linked videos, returns the shared tags count-based weight between them.

        The weight is the number of shared tags between the two videos.
        """

        tags_set_1 = set()
        tags_set_2 = set()

        if video1 in vid_to_tags:
            tags_set_1 = vid_to_tags[video1]
        if video2 in vid_to_tags:
            tags_set_2 = vid_to_tags[video2]

        # weight is the length of the intersection (set) of the two video's tags sets
        weight = len(tags_set_1.intersection(tags_set_2))

        return weight

    videos_to_neighbors = {}

    for current_video in vid_to_patient:

        # find all neighbor videos (i.e., at least one patient has watched both)
        neighbor_videos = set()
        for patient in vid_to_patient[current_video]:
            for neighbor_video in patient_to_vid[patient]:
                neighbor_videos.add( neighbor_video )

        # create a list with entries of the form `(neighbor_video, weight)` for our current video
        neighbor_videos_and_weights = []
        for neighbor_video in neighbor_videos:
            neighbor_videos_and_weights.append( ( neighbor_video, weight_by_patients(current_video, neighbor_video) + 1.25 * weight_by_tags(current_video, neighbor_video) ) )

        videos_to_neighbors[current_video] = sorted(neighbor_videos_and_weights, key=lambda x: x[1], reverse=True)

    return videos_to_neighbors


if __name__ == "__main__":
    pass

    print(videos_to_neighbors())