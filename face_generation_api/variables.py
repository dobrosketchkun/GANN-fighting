#-*-coding:utf8;-*-


import os

path = os.path.dirname(__file__)
path_trim = path + '/trim/bw/'
#path_trim = path + '/trim/'

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


face_w_c = 1.1

forehead_h_c = 0.7
front_h_c = 1.1
chin_h_c = 0.7

nose_h_c = 1
nose_w_c = 1
nose_front_gap_c = 0.1


left_eye_h_c = 0.85
left_eye_w_c = 0.7
left_eye_angle = 7
left_eye_front_gap_c = 0.1
right_eye_h_c = 0.85
right_eye_w_c = 0.7
right_eye_angle = -7
right_eye_front_gap_c = 0.1
eye_distance_front_c = 0.45

right_eyebow_w_c = 1
right_eyebow_h_c = 1
right_eyebow_angle = 15
right_eyebow_eye_distance_c = 1
left_eyebow_w_c = 1
left_eyebow_h_c = 1
left_eyebow_angle = -15
left_eyebow_eye_distance_c = 1

left_eyelip_h_c = 1
left_eyelip_eye_gap = 0.5
right_eyelip_h_c = 1
right_eyelip_eye_gap = 0.5

up_lip_h_c = 1
up_lip_w_c = 0.7
down_lip_h_c = 0.9
down_lip_w_c = 0.7
lips_chin_gap = 1.2
lips_gap = 0.1


left_ear_w_c = 1
left_ear_h_c = 1.1
left_ear_attach_c = 1
left_ear_front_c = 0.1
right_ear_w_c = 1
right_ear_h_c = 1.1
right_ear_attach_c = 1
right_ear_front_c = 0.1