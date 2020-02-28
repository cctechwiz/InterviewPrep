degrees_per_minute = 360 / 60
minutes_per_hour = 5


def hours_to_degrees(h):
    return h * minutes_per_hour * degrees_per_minute


def minutes_to_degrees(m):
    return m * degrees_per_minute


def is_obtuse(angle):
    return angle > 180


def obtuse_to_acute(obtuse_angle):
    return 360 - obtuse_angle


def calculate_acute_angle(hour_degrees, minute_degrees):
    angle = abs(hour_degrees - minute_degrees)
    if is_obtuse(angle):
        angle = obtuse_to_acute(angle)

    return int(angle)


def get_acute_angle(hours, minutes):
    hour_degrees = hours_to_degrees(hours)
    minute_degrees = minutes_to_degrees(minutes)

    return calculate_acute_angle(hour_degrees, minute_degrees)


if __name__ == '__main__':
    print("Clock Hands\n")

    times = [(3, 0), (6, 0), (3, 30), (4, 10), (6, 31), (12, 31), (12, 29)]

    for hours, minutes in times:
        acute_angle = get_acute_angle(hours, minutes)
        print(f'{hours}:{minutes:02} is an acute angle of {acute_angle}°')
