def safe_print_list(my_list=[], x=0):
    try:
        counter = 0
        for elements in my_list:
            if counter < x:
                print(elements, end=' ')
                counter = counter + 1
            else:
                break
        print()
    except:
        pass
    return counter
