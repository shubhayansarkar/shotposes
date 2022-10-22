import cv2
import mediapipe as mp
mp_pose = mp.solutions.pose
pose_object = mp_pose.Pose()
mp_draw = mp.solutions.drawing_utils

idlist = [2, 5, 11, 12, 13, 14, 15, 16, 23, 24, 25, 26, 29, 30, 31, 32]
def pose(frame):
    h, w, c = frame.shape
    pxlist, pylist = [], []
    pxl,pyl=[],[]
    # mp_pose = mp.solutions.pose
    # pose_object = mp_pose.Pose()
    # mp_draw = mp.solutions.drawing_utils
    results = pose_object.process(frame)
    # print(results)

    if results.pose_landmarks:
        for lm in (results.pose_landmarks.landmark):            
            px, py = int(lm.x * w), int(lm.y * h)
            pxlist.append(px)
            pylist.append(py)
    try:
        for i in idlist:
            pxl.append(pxlist[i])
            pyl.append(pylist[i])
    except:
        pass
    return pxlist,pylist