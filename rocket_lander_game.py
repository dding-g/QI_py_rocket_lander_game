position = 100;
velocity = 0;
gravity = -10;
fuel = 100

while(True):
    if fuel > 0:
        if position <= 0 and velocity < -3:
            print "Rocket crashed! Velocity was ", velocity
            break
        elif position < 0 and velocity >= -3:
            position = 0
            print "P : ", position, "  V : ", velocity, "  F : ", fuel
            print "Landing successful"
            break

        print "P : ", position, "  V : ", velocity, "  F : ", fuel
        thrusters = int(raw_input("set thrusters (0-20)"))

        if fuel - thrusters < 0:
            print "Out of fuel! Thrusters at {0}".format(fuel)
        elif thrusters > 20:
            print "Thrusters at max(20)!"
            thrusters = 20
        elif thrusters < 0:
            print "Thrusters at min(0)!"
            thrusters = 0

        fuel -= thrusters
        acceleration = gravity + thrusters
        position += velocity + int(acceleration * 0.5)
        velocity = velocity + acceleration

    elif fuel <= 0:
        print "No fuel -- rocket is in free down!!"
        position += 0 if position - gravity < 0 else gravity
        if position == 0:
            print "P : ", position, "  V : ", velocity, "  F : ", fuel
            print "Rocket crashed! Velocity was ", velocity
            break



