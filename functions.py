#-*-coding:utf8;-*-

from Classes import FacePart
from variables import *



def face_parts_preload():
    """
    Презагружает все составные части и возвращает словарь
    формата {'part': экземпляр класса изображения}
    """
    return {item: FacePart(path_trim + item + '.png', item) for item in FACE_LIST}


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