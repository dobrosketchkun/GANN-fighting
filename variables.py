#-*-coding:utf8;-*-


import os

path = os.path.dirname(__file__)
path_trim = path + '/trim/bw/'

FACE_LIST = ['chin',
            'chin_wrinkle',
            'front',
            'neck',
            'forehead',
            'left_eye',
            'left_eyebow',
            'left_eyelip',
            'right_eye',
            'right_eyebow',
            'right_eyelip',
            'up_lip',
            'down_lip',
            'nose',
            'left_ear',
            'right_ear']


face_w_c = 1

forehead_h_c = 1
front_h_c = 1
chin_h_c = 1

nose_h_c = 1
nose_w_c = 1
nose_front_gap_c = 0.1


left_eye_h_c = 1
left_eye_w_c = 1
left_eye_angle = 0
left_eye_front_gap_c = 0.1
right_eye_h_c = 1
right_eye_w_c = 1
right_eye_angle = 0
right_eye_front_gap_c = 0.1
eye_distance_front_c = 0.45

right_eyebow_w_c = 1
right_eyebow_h_c = 1
right_eyebow_angle = 0
right_eyebow_eye_distance_c = 1
left_eyebow_w_c = 1
left_eyebow_h_c = 1
left_eyebow_angle = 0
left_eyebow_eye_distance_c = 1

left_eyelip_h_c = 1
left_eyelip_eye_gap = 0.5
right_eyelip_h_c = 1
right_eyelip_eye_gap = 0.5

up_lip_h_c = 1
up_lip_w_c = 1
down_lip_h_c = 1
down_lip_w_c = 1
lips_chin_gap = 1
lips_gap = 0.1


left_ear_w_c = 1
left_ear_h_c = 1
left_ear_attach_c = 1
left_ear_front_c = 0.1
right_ear_w_c = 1
right_ear_h_c = 1
right_ear_attach_c = 1
right_ear_front_c = 0.1