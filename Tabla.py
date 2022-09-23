import sys
def tabla():
    if len(sys.argv)==3:
        numero1= int(sys.argv[1])
        numero2= int(sys.argv[2])
        if((numero1<9 or numero2<9) or (numero1>0 or numero2>0)):
            print('mal bobi es entre 1 y 9')

        else:
            for i in range(numero1):
                for i in range(numero2):
                    print(" * ", end='')

