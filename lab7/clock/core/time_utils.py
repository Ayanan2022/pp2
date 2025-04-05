def get_angles(time):
    sec_angle = -(time.second * 6)         # 360 / 60
    min_angle = -(time.minute * 6)         # 360 / 60
    return sec_angle, min_angle
