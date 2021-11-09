#!/usr/bin/python3
from discretein import *




def main():
    PG_in1 = DISCRETE_IN('IN1')

    if PG_in1.value():
        print('PG_in1 = 1')
    else:
        print('PG_in1 = 0')


    PG_in2 = DISCRETE_IN('IN2')

    if PG_in2.value():
        print('PG_in2 = 1')
    else:
        print('PG_in2 = 0')


    PG_in3 = DISCRETE_IN('IN3')

    if PG_in3.value():
        print('PG_in3 = 1')
    else:
        print('PG_in3 = 0')


    PG_in4 = DISCRETE_IN('IN4')

    if PG_in4.value():
        print('PG_in4 = 1')
    else:
        print('PG_in4 = 0')


    PG_in5 = DISCRETE_IN('IN5')

    if PG_in5.value():
        print('PG_in5 = 1')
    else:
        print('PG_in5 = 0')


    PG_in6 = DISCRETE_IN('IN6')

    if PG_in6.value():
        print('PG_in6 = 1')
    else:
        print('PG_in6 = 0')


    PG_in7 = DISCRETE_IN('IN7')

    if PG_in7.value():
        print('PG_in7 = 1')
    else:
        print('PG_in7 = 0')


    PG_in8 = DISCRETE_IN('IN8')

    if PG_in8.value():
        print('PG_in8 = 1')
    else:
        print('PG_in8 = 0')



if __name__ == "__main__":
    main()

