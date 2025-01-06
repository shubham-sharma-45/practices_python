lenth=int(input("Enter Lenth:-"))
breadth=int(input("Enter Breadth:-"))
hight=int(input("Enter Hight:-"))

cost_of_1_ltr=int(input("Enter Coast,One Litre Paint:-"))
coverd_area=int(input("Enter Coverd Area Of Litre:-"))
area_of_room=(lenth*breadth)+(lenth*hight)*2+(breadth*hight)*2
paint_of_need=area_of_room/coverd_area
cost_of_paint=paint_of_need*cost_of_1_ltr
print("sq area=",area_of_room)
print("ltr=",paint_of_need)
print("rs=",cost_of_pain)

