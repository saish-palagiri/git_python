i = 0
while i == 0:
    # formula solver
    formula = input('Which shape do you want to find the area or volume of? If you want to exit click 6. You can choose from rectangle, square, parallelogram, trapezoid, triangle, circle, cube, ellipse, pentagon, hexagon, octagon, sphere, cone, cylinder, tetrahedron: ').lower()
    
    if formula == '6':
        break  # Exit loop

    elif formula == 'rectangle':
        print("A = L x W")
        solve = input('Solve? 1 = yes, 2 = no: ')
        if solve == '1':
            length = float(input('Enter length: '))
            width = float(input('Enter width: '))
            area = length * width
            print(f'Area = {area}')
        else:
            print('Okay, solve it manually.')

    elif formula == 'square':
        print("A = side²")
        solve = input('Solve? 1 = yes, 2 = no: ')
        if solve == '1':
            side = float(input('Enter side length: '))
            area = side ** 2
            print(f'Area = {area}')
        else:
            print('Okay, solve it manually.')

    elif formula == 'triangle':
        print("A = (B x H) / 2")
        solve = input('Solve? 1 = yes, 2 = no: ')
        if solve == '1':
            base = float(input('Enter base: '))
            height = float(input('Enter height: '))
            area = (base * height) / 2
            print(f'Area = {area}')
        else:
            print('Okay, solve it manually.')

    elif formula == 'trapezoid':
        print("A = ((B1 + B2) / 2) x H")
        solve = input('Solve? 1 = yes, 2 = no: ')
        if solve == '1':
            base1 = float(input('Enter base 1: '))
            base2 = float(input('Enter base 2: '))
            height = float(input('Enter height: '))
            area = ((base1 + base2) / 2) * height
            print(f'Area = {area}')
        else:
            print('Okay, solve it manually.')

    elif formula == 'parallelogram':
        print("A = B x H")
        solve = input('Solve? 1 = yes, 2 = no: ')
        if solve == '1':
            base = float(input('Enter base: '))
            height = float(input('Enter height: '))
            area = base * height
            print(f'Area = {area}')
        else:
            print('Okay, solve it manually.')

    elif formula == 'circle':
        print("A = π x r²")
        solve = input('Solve? 1 = yes, 2 = no: ')
        if solve == '1':
            radius = float(input('Enter radius: '))
            area = 3.14 * radius ** 2
            print(f'Area = {area}')
        else:
            print('Okay, solve it manually.')

    elif formula == 'cube':
        print("Volume = L x W x H")
        solve = input('Solve? 1 = yes, 2 = no: ')
        if solve == '1':
            length = float(input('Enter the length: '))
            width = float(input('Enter the width: '))
            height = float(input('Enter the height: '))
            volume = length * width * height
            print(f'The volume of the cube is {volume}')
        else:
            print('Okay, solve it manually.')

    elif formula == 'ellipse':
        print("A = π x a x b (a = semi-major, b = semi-minor axis)")
        solve = input('Solve? 1 = yes, 2 = no: ')
        if solve == '1':
            a = float(input('Enter semi-major axis (a): '))
            b = float(input('Enter semi-minor axis (b): '))
            area = 3.14 * a * b
            print(f'Area = {area}')
        else:
            print('Okay, solve it manually.')

    elif formula == 'pentagon':
        print("A = (5/4) x a² x cot(π/5)")
        solve = input('Solve? 1 = yes, 2 = no: ')
        if solve == '1':
            side = float(input('Enter side length: '))
            import math
            area = (5 / 4) * side ** 2 * (1 / math.tan(math.pi / 5))
            print(f'Area = {area}')
        else:
            print('Okay, solve it manually.')

    elif formula == 'hexagon':
        print("A = (3√3 / 2) x a²")
        solve = input('Solve? 1 = yes, 2 = no: ')
        if solve == '1':
            side = float(input('Enter side length: '))
            import math
            area = (3 * math.sqrt(3) / 2) * side ** 2
            print(f'Area = {area}')
        else:
            print('Okay, solve it manually.')

    elif formula == 'octagon':
        print("A = 2(1 + √2) x a²")
        solve = input('Solve? 1 = yes, 2 = no: ')
        if solve == '1':
            side = float(input('Enter side length: '))
            import math
            area = 2 * (1 + math.sqrt(2)) * side ** 2
            print(f'Area = {area}')
        else:
            print('Okay, solve it manually.')

    elif formula == 'sphere':
        print("Surface Area = 4πr²")
        solve = input('Solve? 1 = yes, 2 = no: ')
        if solve == '1':
            radius = float(input('Enter radius: '))
            import math
            area = 4 * math.pi * radius ** 2
            print(f'Surface Area = {area}')
        else:
            print('Okay, solve it manually.')

    elif formula == 'cone':
        print("Volume = (1/3)πr²h")
        solve = input('Solve? 1 = yes, 2 = no: ')
        if solve == '1':
            radius = float(input('Enter radius: '))
            height = float(input('Enter height: '))
            import math
            volume = (1/3) * math.pi * radius ** 2 * height
            print(f'Volume = {volume}')
        else:
            print('Okay, solve it manually.')

    elif formula == 'cylinder':
        print("Volume = πr²h")
        solve = input('Solve? 1 = yes, 2 = no: ')
        if solve == '1':
            radius = float(input('Enter radius: '))
            height = float(input('Enter height: '))
            import math
            volume = math.pi * radius ** 2 * height
            print(f'Volume = {volume}')
        else:
            print('Okay, solve it manually.')

    elif formula == 'tetrahedron':
        print("Volume = (a³) / (6√2)")
        solve = input('Solve? 1 = yes, 2 = no: ')
        if solve == '1':
            side = float(input('Enter side length: '))
            import math
            volume = (side ** 3) / (6 * math.sqrt(2))
            print(f'Volume = {volume}')
        else:
            print('Okay, solve it manually.')

    else:
        print("Shape not recognized. Please try again.")
