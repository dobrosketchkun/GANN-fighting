#-*-coding:utf8;-*-

import random
from Classes import FacePart, Background
#from functions import assembly, face_parts_preload
from variables import FACE_LIST, path_trim

def face_parts_preload():
    """
    Презагружает все составные части и возвращает словарь
    формата {'part': экземпляр класса изображения}
    """
    return {item: FacePart(path_trim + item + '.png', item) for item in FACE_LIST}




def random_face(times):
    count = 0

    for value in range(times):

        face_dict = face_parts_preload()
        background = Background()


        face_w_c = random.uniform(0.7, 2.0)

        forehead_h_c = random.uniform(0.7, 1.3)
        front_h_c = random.uniform(0.8, 1.3)
        chin_h_c = random.uniform(0.6, 1.3)

        nose_h_c = random.uniform(0.8, 1.3)
        nose_w_c = random.uniform(0.6, 1.5)
        nose_front_gap_c = 0.1


        left_eye_h_c = random.uniform(0.6, 1.6)
        left_eye_w_c = random.uniform(0.5, 1.2)
        left_eye_angle= random.uniform(0,18)
        left_eye_front_gap_c = 0.1
        right_eye_h_c = left_eye_h_c
        right_eye_w_c = left_eye_w_c
        right_eye_angle = - left_eye_angle
        right_eye_front_gap_c = 0.1
        eye_distance_front_c = random.uniform(0.3, 0.6)

        right_eyebow_w_c = random.uniform(0.6, 1.9)
        right_eyebow_h_c = random.uniform(0.4, 1.3)
        right_eyebow_angle = random.uniform(0, 25)
        right_eyebow_eye_distance_c = random.uniform(0.9, 1.8)
        left_eyebow_w_c = right_eyebow_w_c
        left_eyebow_h_c = right_eyebow_h_c
        left_eyebow_angle = - right_eyebow_angle
        left_eyebow_eye_distance_c = right_eyebow_eye_distance_c

        left_eyelip_h_c = random.uniform(0.8, 1.5)
        left_eyelip_eye_gap = random.uniform(0.5, 0.9)
        right_eyelip_h_c = left_eyelip_h_c
        right_eyelip_eye_gap = left_eyelip_eye_gap

        up_lip_h_c = random.uniform(0.6, 1.3)
        up_lip_w_c = random.uniform(0.3, 1.3)
        down_lip_h_c = up_lip_h_c
        down_lip_w_c = up_lip_w_c
        lips_chin_gap = 1
        lips_gap = 0.1


        left_ear_w_c = random.uniform(0.8, 1.6)
        left_ear_h_c = random.uniform(0.8, 1.3)
        left_ear_attach_c = 1
        left_ear_front_c = 0.1
        right_ear_w_c = left_ear_w_c
        right_ear_h_c = left_ear_h_c
        right_ear_attach_c = 1
        right_ear_front_c = 0.1

        def assembly(background, face_dict, list_of_pasted):
            """
            Собирает лицо, изменяя части в соотвествии с коэффициентами
            """
            gap = 50
            for part in list_of_pasted:
                if part.name == 'forehead':
                    part.resize(int(part.w * face_w_c), int(part.h * forehead_h_c))
                    (x, y) = (background.center[0] - part.center[0], gap)
                    background.paste(part, (x, y))

                if part.name == 'front':
                    part.resize(int(part.w * face_w_c), int(part.h * front_h_c))
                    (x, y) = (background.center[0] - part.center[0], face_dict['forehead'].h + gap)
                    background.paste(part, (x, y))

                if part.name == 'chin':
                    part.resize(int(part.w * face_w_c), int(part.h * chin_h_c))
                    (x, y) = (background.center[0] - part.center[0],
                                face_dict['forehead'].h + face_dict['front'].h + gap)
                    background.paste(part, (x, y))

                if part.name == 'nose':
                    #Проверка чтобы нос не вышел за границы лица, можно потом улучшить коэффициенты
                    if part.h * nose_h_c > face_dict['front'].h * front_h_c * 0.8:
                        this_part_h = face_dict['front'].h * front_h_c * 0.8

                    else:
                        this_part_h = part.h * nose_h_c

                    part.resize(int(part.w * nose_w_c), int(this_part_h))
                    (x, y) = (background.center[0] - part.center[0],
                                face_dict['forehead'].h + int(face_dict['front'].h * nose_front_gap_c)  + gap)
                    background.paste(part, (x, y))

                if part.name == 'left_eye':
                    part.resize(int(part.w * left_eye_w_c), int(part.h * left_eye_h_c))
                    part.rotate(left_eye_angle)
                    (x, y) = (background.center[0] - part.center[0] - int(face_dict['front'].w * eye_distance_front_c/2),
                                face_dict['forehead'].h + int(face_dict['front'].h * left_eye_front_gap_c )  + gap)
                    background.paste(part, (x, y))

                if part.name == 'right_eye':
                    part.resize(int(part.w * right_eye_w_c), int(part.h * right_eye_h_c))
                    part.rotate(right_eye_angle)
                    (x, y) = (background.center[0] - part.center[0] + int(face_dict['front'].w * eye_distance_front_c/2),
                                face_dict['forehead'].h + int(face_dict['front'].h * right_eye_front_gap_c )  + gap)
                    background.paste(part, (x, y))

                if part.name == 'left_eyebow':
                    part.resize(int(part.w * left_eyebow_w_c), int(part.h * left_eyebow_h_c))
                    part.rotate(left_eyebow_angle)
                    (x, y) = (background.center[0] - part.center[0] - int(face_dict['front'].w * eye_distance_front_c/2),
                            face_dict['forehead'].h + int(face_dict['front'].h * left_eye_front_gap_c)  + gap
                            - int(face_dict['left_eye'].h * left_eyebow_eye_distance_c))
                    background.paste(part, (x, y))

                if part.name == 'right_eyebow':
                    part.resize(int(part.w * right_eyebow_w_c), int(part.h * right_eyebow_h_c))
                    part.rotate(right_eyebow_angle)
                    (x, y) = (background.center[0] - part.center[0] + int(face_dict['front'].w * eye_distance_front_c/2),
                            face_dict['forehead'].h + int(face_dict['front'].h * right_eye_front_gap_c)  + gap
                            - int(face_dict['right_eye'].h * right_eyebow_eye_distance_c))
                    background.paste(part, (x, y))

                if part.name == 'left_eyelip':
                    part.resize(int(part.w * left_eye_w_c), int(part.h * left_eyelip_h_c))
                    part.rotate(left_eye_angle)
                    (x, y) = (background.center[0] - part.center[0] - int(face_dict['front'].w * eye_distance_front_c/2),
                            face_dict['forehead'].h + int(face_dict['front'].h * left_eye_front_gap_c)  + gap
                            + int(face_dict['left_eye'].h * left_eyelip_eye_gap))
                    background.paste(part, (x, y))

                if part.name == 'right_eyelip':
                    part.resize(int(part.w * right_eye_w_c), int(part.h * right_eyelip_h_c))
                    part.rotate(right_eye_angle)
                    (x, y) = (background.center[0] - part.center[0] + int(face_dict['front'].w * eye_distance_front_c/2),
                            face_dict['forehead'].h + int(face_dict['front'].h * right_eye_front_gap_c)  + gap
                            + int(face_dict['right_eye'].h * right_eyelip_eye_gap))
                    background.paste(part, (x, y))

                if part.name == 'up_lip':
                    part.resize(int(part.w * up_lip_w_c), int(part.h * up_lip_h_c))
                    (x, y) = (background.center[0] - part.center[0],
                                face_dict['forehead'].h + face_dict['front'].h + face_dict['chin'].h
                                - int(face_dict['chin'].h * lips_chin_gap))
                    background.paste(part, (x, y))

                if part.name == 'down_lip':
                    part.resize(int(part.w * down_lip_w_c), int(part.h * down_lip_h_c))
                    (x, y) = (background.center[0] - part.center[0],
                                face_dict['forehead'].h + face_dict['front'].h + face_dict['chin'].h
                                - int(face_dict['chin'].h * lips_chin_gap - face_dict['up_lip'].h * lips_gap))
                    background.paste(part, (x, y))

                if part.name == 'left_ear':
                    part.resize(int(part.w * left_ear_w_c), int(part.h * left_ear_h_c))
                    (x, y) = (background.center[0] - int(part.center[0] * left_ear_attach_c) - face_dict['front'].w/2 ,
                                face_dict['forehead'].h + int(face_dict['front'].h * left_ear_front_c)+ gap)
                    background.paste(part, (x, y))

                if part.name == 'right_ear':
                    part.resize(int(part.w * right_ear_w_c), int(part.h * right_ear_h_c))
                    (x, y) = (background.center[0] - int(part.center[0] * right_ear_attach_c) + face_dict['front'].w/2 ,
                                face_dict['forehead'].h + int(face_dict['front'].h * right_ear_front_c)+ gap)
                    background.paste(part, (x, y))









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

        #background.show()
        fname = 'face_ ' + str(count) + '_test.png'
        background.save(fname)
        count += 1
        del face_dict, background
