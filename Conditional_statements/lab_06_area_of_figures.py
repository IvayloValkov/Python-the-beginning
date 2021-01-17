import math

figure = input()
side_1 = float(input())
side_2 = 0

if figure == "square":
    square_area = side_1 * side_1
    print(f'{square_area:.3f}')

if figure == "rectangle":
    side_2 = float(input())
    square_area = side_1 * side_2
    print(f'{square_area:.3f}')

if figure == "circle":
    square_area = side_1 * side_1 * math.pi
    print(f'{square_area:.3f}')

if figure == "triangle":
    side_2 = float(input())
    square_area = (side_1 * side_2) / 2
    print(f'{square_area:.3f}')

# import math
#
# shape_type = input()
# shape_size1 = float(input())
# shape_size2 = 0
#
# square_area = shape_size1 * shape_size1
# circle_area = math.pi * shape_size1 * shape_size1
#
# if shape_type == 'square':
#     print(shape_type)
# print(f'{square_area:.3f}')
# if shape_type == 'rectangle':
#     shape_size2 = float(input())
# rectangle_area = shape_size1 * shape_size2
# print(shape_type)
# print(f'{rectangle_area:.3f}')
# if shape_type == 'circle':
#     print(shape_type)
# print(f'{circle_area:.3f}')
# if shape_type == 'triangle':
#     shape_size2 = float(input())
# triangle_area = (shape_size1 * shape_size2) / 2
# print(shape_type)
# print(f'{triangle_area:.3f}')