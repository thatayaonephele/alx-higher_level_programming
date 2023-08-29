#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):

    tmp = []
    y = 0
    for x in range(list_length):
        try:
            result = my_list_1[x] / my_list_2[x]
        except IndexError:
            print('out of range')
            result = y
        except TypeError:
            print('wrong type')
            result = y
        except ZeroDivisionError:
            print('division by 0')
            result = y
        finally:
            tmp.append(result)
    return (tmp)
