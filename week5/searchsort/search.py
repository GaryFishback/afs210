#Adjust info for more experimentation and originality. Maybe some extra things should happen when evaluated to True?
def linear_search(values, search_for):
    search_at = 0
    search_res = False

    while search_at < len(values) and search_res is False:
        if values[search_at] == search_for:
            print(str(str(values[search_at]) + " Is the current number"))
            search_res = True
        else:
            print(str(str(values[search_at]) + " Is the current number"))
            search_at = search_at + 1
    
    return search_res

arrayOfItems = [56, 66, 69, 93, 32, 28, 89]

print(linear_search(arrayOfItems, 56))
print(linear_search(arrayOfItems, 57))