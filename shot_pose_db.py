import os
import numpy as np
import cv2
import pandas as pd
from pose_detection import pose
import mongo_db



fields = ['left_eye_x', 'left_eye_y', 'right_eye_x', 'right_eye_y', 'left_shoulder_x',
          'left_shoulder_y', 'right_shoulder_x', 'right_shoulder_y', 'left_elbow_x', 'left_elbow_y',
          'right_elbow_x', 'right_elbow_y', 'left_wrist_x', 'left_wrist_y', 'right_wrist_x',
          'right_wrist_y', 'left_hip_x', 'left_hip_y', 'right_hip_x', 'right_hip_y', 'left_knee_x',
          'left_knee_y', 'right_knee_x', 'right_knee_y', 'left_heel_x', 'left_heel_y', 'right_heel_x',
          'right_heel_y', 'left_toe_x', 'left_toe_y', 'right_toe_x', 'right_toe_y']
def dblist(img_name, imgshape, pxlist, pylist, shot,fields):
    itemss={}
    its=[]
    try:

        for i in range(len(pxlist)):
            its.append(pxlist[i])
            its.append(pylist[i])

        itemss['img_name']=img_name
        itemss['imgh']=imgshape[0]
        itemss['imgw']=imgshape[1]
        for i in range(len(fields)):
            itemss[f'{fields[i]}']=its[i]
        itemss['shot']=shot

        # print(its)
        # print(its)
        return itemss
    except:
        pass





def dbcreate(path):
        #  fol='drive'
    for fol in os.listdir(path):
         for file in os.listdir(f'{path}/{fol}'):
            shotname=fol
            picname=file

            img = cv2.imread(f'{path}/{fol}/{file}')
            frame = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            pxlist, pylist = pose(frame)
            items=dblist(picname, frame.shape, pxlist, pylist, shotname,fields)

            if items is not None:
                # print(items)
                mongo_db.mongo_insert(items)
                print(f'done...{file}')



path=r"/home/sarkarsar152ine/shotposes/cricket_shots"
dbcreate(path)


