def main():
    sq_foot_to_desimal_convert_coefficient = 435.60
    link_to_foot_convert_coefficient = 0.66
    print("Map type ? 16 scaler or 64 scaler?")
    print("Enter 1 for 16 scaler or enter 2 for 64 scaler")
    map_type = int(input())
    if map_type == 1:
        per_small_scale_count = float(10)
    elif map_type == 2:
        per_small_scale_count = float(2.5)
    else:
        raise Exception("Invalid map type selected")

    print("Enter length in small scale count")
    length_in_small_scale_count = float(input())
    print("Enter width in small scale count")
    width_in_small_scale_count = float(input())

    length_in_Foot = length_in_small_scale_count * per_small_scale_count * link_to_foot_convert_coefficient
    width_in_Foot = width_in_small_scale_count * per_small_scale_count * link_to_foot_convert_coefficient

    area_in_sq_foot = length_in_Foot * width_in_Foot

    area_in_desimal = area_in_sq_foot / sq_foot_to_desimal_convert_coefficient
    area_in_desimal = str(round(area_in_desimal, 2))
    print("Area in desimal is : {}".format(area_in_desimal))


main()
