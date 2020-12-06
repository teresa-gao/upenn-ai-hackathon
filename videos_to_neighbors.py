import pickle

# unpickle the dictionaries! (will be included in the top-level function this function will be a helper for)
with open("vid_to_patient_tuples.pkl", "rb") as f:
    vid_to_patient_tuples = pickle.load(f)
with open("patient_to_vid.pkl", "rb") as f:
    patient_to_vid = pickle.load(f)
with open("vid_to_patient.pkl", "rb") as f:
    vid_to_patient = pickle.load(f)

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
        # TODO: paste in code for weight_by_tags helper function
        return 0

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
            neighbor_videos_and_weights.append( ( neighbor_video, weight_by_patients(current_video, neighbor_video) + weight_by_tags(current_video, neighbor_video) ) )

        videos_to_neighbors[current_video] = neighbor_videos_and_weights

    return videos_to_neighbors

if __name__ == "__main__":
    pass

    print(videos_to_neighbors())

    # TODO: add tests?