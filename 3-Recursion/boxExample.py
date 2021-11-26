def look_for_key(main_box):
    pile = main_box.make_pile()
    while pile is not None:
        box = pile.grab()
        for item in box:
            if item.isBox():
                pile.append(item)
            elif item.isKey():
                print("Done")


def look_for_key(box):
    for item in box:
        if item.isBox():
            look_for_key(item)#recursion
        elif item.isKey():
            print("Dont")#Base Case