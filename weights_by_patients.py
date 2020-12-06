import pickle

# unpickle the dictionaries! (will be included in the top-level function this function will be a helper for)
with open("patient_to_vid.pkl", "rb") as f:
    patient_to_vid = pickle.load(f)
with open("vid_to_patient.pkl", "rb") as f:
    vid_to_patient = pickle.load(f)

def weight_by_patients(video1, video2):
    """

    Given two videos, returns the patient count-based weight between two given linked videos.

    The weight is the sum of (1/2)^(n-1) for all n = 0, ..., (number of views by the same patient)

    """

    edge_weight = 0

    # find patients who watched video1
    patients = vid_to_patient[video1]

    for patient in patients:

        patient_vids_watched = patient_to_vid[patient]

        # only consider patients who have video2 in their watched videos
        if video2 in patient_vids_watched:

            # add weight via diminishing returns function on repeat views by the same patient
            edge_weight += ( 1/2 ) ** ( patient_vids_watched.count(video2) - 1 )

    return edge_weight

if __name__ == "__main__":
    pass

    # TODO: insert tests here