def area_square(width,lengeth):
    area = width * lengeth
    return round(area * 2)

def area_circle(radius):
    area = 3.14 * radius * radius
    return round(area,2)

def volume_cube(width,lengeth,height):
    volume = width * lengeth * height
    return round(volume_cube,2)

def volume_sphere(radius):
    volume = 4/3 * 3.14 * radius ** 3
    return round(volume,2)

def menu():
    print("1.พื้นที่สี่เหลี่ยม")
    print("2.พี้นที่วงกลม")
    print("3.ปริมาตรทรงสี่เหลี่ยม")
    print("4.ปริมาตรทรงกลม")
    print("0.จบการทำงาน")

    option = int(input("เลือกเมนู:   "))

    if option == 1:
        width = float(input("ป้อนความยาว:  "))
        lengeth = float(input("ป้อนความกว้าง: "))
        area = area_square(width,lengeth)
        print("พื้นที่สี่้เหลี่ยมเท่ากับ",area)
    elif option == 2:
        radius = float(input("ป้อนรัศมี:  " ))
        area = area_circle(radius)
        print("พื้นที่วงกลมเท่ากับ",area)
    elif option == 3:
        width = float(input("ป้อนความกว้าง:   "))
        lengeth = float(input("ป้อนความยาว:   "))
        height = float(input("ป้อนความสูง:   "))
        volume = volume_cube(width,lengeth,height)
        print("ปริมาตรทรงสี่เหลี่ยมเท่ากับ",volume)
    elif option == 4:
        radius = float(input("ป้อนรัศมี:  "))
        volume = volume_sphere(radius)
        print("ปริมาตรทรงกลม",volume)
    elif option == 0: 
        print("ขอบคุณที่ใช้งาน")
    else :
        print("กรุณาเลือกเมนู 1, 2 , 3 , 4 หรือ 0 เท่านั้น ")
if __name__ == "__menu__":
    menu()
