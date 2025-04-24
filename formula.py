
i = 0
while i == 0:
    # formula solver
    formula = input('Which shape do you want to find the area of? If you want to exit click 6. You can choose from rectangle, square, parralelogram, trapezoid, triangle, circle, and cube: ')
    if formula == '6':
        break  # Breaks the loop if '6' is entered
    
    elif formula == 'rectangle':
        print("A = L x W")
        solve = input('Would you like python to solve a problem? Just enter the values. If yes click 1 if no click 2: ')
        if solve == '1':
            length = float(input('Enter the length: '))
            width = float(input('Enter the width: '))
            area = length * width
            print(f'The area of the rectangle is {area}')
        elif solve == '2':
            print('Okay, you can solve it manually.')
    elif formula == 'square':
        print("A = L x W")
        solve = input('Would you like python to solve a problem? Just enter the values. If yes click 1 if no click 2: ')
        if solve == '1':
            length = float(input('Enter the length: '))
            width = float(input('Enter the width: '))
            area = length * width
            print(f'The area of the square is {area}')
        elif solve == '2':
            print('Okay, you can solve it manually.')
    elif formula == 'triangle':
        print("A = B x H/2")
        solve = input('Would you like python to solve a problem? Just enter the values. If yes click 1 if no click 2: ')
        if solve == '1':
            base = float(input('Enter the base: '))
            height = float(input('Enter the height: '))
            area = base * height / 2
            print(f'The area of the triangle is {area}')
        elif solve == '2':
            print('Okay, you can solve it manually.')
    elif formula == 'trapezoid':
        print("A = (B1 + B2)/2 x H")
        solve = input('Would you like python to solve a problem? Just enter the values. If yes click 1 if no click 2: ')
        if solve == '1':
            base1 = float(input('Enter the first base: '))
            base2 = float(input('Enter the second base: '))
            height = float(input('Enter the height: '))
            area = (base1 + base2) / 2 * height
            print(f'The area of the trapezoid is {area}')
        elif solve == '2':
            print('Okay, you can solve it manually.')
    elif formula == 'Parallelogram':
        print("A = B x H")
        solve = input('Would you like python to solve a problem? Just enter the values. If yes click 1 if no click 2: ')
        if solve == '1':
            base = float(input('Enter the base: '))
            height = float(input('Enter the height: '))
            area = base * height
            print(f'The area of the parallelogram is {area}')
        elif solve == '2':
            print('Okay, you can solve it manually.')

    elif formula == 'circle':
        print("A = πr2")
        solve = input('Would you like python to solve a problem? Just enter the values. If yes click 1 if no click 2: ')
        if solve == '1':
            radius = float(input('Enter the radius: '))
            area = 3.14 * radius ** 2
            print(f'The area of the circle is {area}')
        elif solve == '2':
            print('Okay, you can solve it manually.')
    elif formula == 'cube':
        print("A = (L x W) x H")
        solve = input('Would you like python to solve a problem? Just enter the values. If yes click 1 if no click 2: ')
        if solve == '1':
            length = float(input('Enter the length: '))
            area = 6 * length ** 2
            print(f'The area of the cube is {area}')
        elif solve == '2':
            print('Okay, you can solve it manually.')