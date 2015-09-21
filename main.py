#-*-coding:utf8;-*-


from functions import face_parts_preload, assembly
from Classes import Background

face_dict = face_parts_preload()
background = Background()

assembly(background, face_dict,
                    [face_dict['forehead'],
                    face_dict['front'],
                    face_dict['chin'],
                    face_dict['nose'],
                    face_dict['left_eye'],
                    face_dict['right_eye'],
                    face_dict['left_eyebow'],
                    face_dict['right_eyebow'],
                    face_dict['left_eyelip'],
                    face_dict['right_eyelip'],
                    face_dict['up_lip'],
                    face_dict['down_lip'],
                    face_dict['left_ear'],
                    face_dict['right_ear']])

background.show()
#background.save('test.png')