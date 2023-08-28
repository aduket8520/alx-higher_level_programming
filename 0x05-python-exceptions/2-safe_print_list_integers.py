def safe_print_list_integers(my_list=[], x=0):
    try:
        counter = 0
        for elements in my_list:
            if counter < x:
                try:
                    print("{:d}".format(elements), end=' ')
                    counter = counter + 1
                except:
                    pass
            else:
                break
        print()
    except:
        pass
    return counter
