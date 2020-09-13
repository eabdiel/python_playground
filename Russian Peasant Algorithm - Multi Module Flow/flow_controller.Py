"""
Simulation of Web App Architecture | Case study based on assignment from
                                                https://www.udemy.com/share/103nlaAEMZdllWTHg=/

Service: The Russian Peasant's Algorithm

Architecture Include:

 - App Computer (Modules)
 - Database (--) --> Russian Peasant Algorithm
 - Load Balancer (Algorithm)

+-----+   +-----+   +-----+
| APP |   | APP |   | APP |
|  1  |   |  2  |   |  3  |
+-----+   +-----+   +-----+
"""
## Bot names
import bot1
import bot2
import bot3

ROBOTS = [bot1, bot2, bot3]

n = -1


def get_robot():
    global n
    n += 1
    return ROBOTS[n % len(ROBOTS)]


## Testing Load which needs balancing
if __name__ == '__main__':
    from random import randint

    # simulating num of requests in the next loop
    for i in range(10):
        # some 'requested' numbers
        z = randint(1, 21)
        a = [11, 35, 213, 51, 12, 94, 68][z % 7]
        # a = randint(5,99)
        b = [93, 25, 12, 111, 1337, 89, 1][z % 7]
        # b = randint(5,99)

        # run the flow controller to get an available 'bot'
        active_bot = get_robot()

        # print the results
        print(active_bot.printName())
        print(f"{a}x{b}")
        print(active_bot.multiplyHandler(a, b))
        print(active_bot.lastMultipliedHandler())
        print("")

# End of code - github.com/eabdiel
