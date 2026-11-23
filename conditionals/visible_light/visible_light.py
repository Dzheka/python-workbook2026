color = int (input())
if color >= 380 and color <450:
    print ("Violet")
elif color >= 450 and color <495:
    print ("Blue")
elif color >= 495 and color <570:
    print ("Green")
elif color >= 570 and color <590:
    print ("Yellow")
elif color >= 590 and color <620:
    print ("Orange")
elif color >= 620 and color <=750:
    print ("Red")
else:
    print ("Outside visible spectrum")
