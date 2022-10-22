import cv2
import mediapipe as mp
idlist = [2, 5, 11, 12, 13, 14, 15, 16, 23, 24, 25, 26, 29, 30, 31, 32]
def pose(frame):
    pxlist, pylist = [], []
    pxl,pyl=[],[]
    mp_pose = mp.solutions.pose
    pose_object = mp_pose.Pose()
    mp_draw = mp.solutions.drawing_utils
    results = pose_object.process(frame)
    # print(results)

    if results.pose_landmarks:
        mp_draw.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

        for id, lm in enumerate(results.pose_landmarks.landmark):
            h, w, c = frame.shape
            px, py = int(lm.x * w), int(lm.y * h)
            pxlist.append(px)
            pylist.append(py)
            # print(pxlist, pylist)
            cv2.circle(frame, (px, py), 2, (255, 255, 255), cv2.FILLED)
    try:
        for i in idlist:
            pxl.append(pxlist[i])
            pyl.append(pylist[i])
    except:
        pass
    return pxl,pyl