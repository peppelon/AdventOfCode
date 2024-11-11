with open("data.txt", "r") as data:

    total = 0
    total_ribbon = 0
    for line in data.readlines():

        x,y,z = [int(i) for i in line.split('x')]
        a = x * y
        b = y * z
        c = x * z
        sub_total = 2*a + 2*b + 2*c
        total += sub_total + min(a,b,c)

        ribbon_length = 2*x + 2*y + 2*z - 2*max(x,y,z)
        total_ribbon += ribbon_length + x * y * z

    print(total)
    print(total_ribbon)
