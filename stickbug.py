from asciimatics.screen import ManagedScreen
from asciimatics.scene import Scene
from asciimatics.effects import Cycle, Stars
from asciimatics.renderers import FigletText
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from pygame import mixer
from time import sleep

stick_bug_coordinates = {
    1:(((0,14), (67,23)), ((False, (27,6),(30,7),(36,11),(46,11)), (True, (17,17),(19,7),(30,7),(30,12),(30,19)), (True, (30,19),(28,14),(33,10),(37,14),(37,19)), (True, (37,19),(35,17),(36,11),(42,14),(50,21)))),
    2:(((0,15), (67,24)), ((False, (30,4),(33,7),(38,10),(48,10)), (True, (19,17),(22,8),(33,7),(31,11),(31,19)), (True, (31,19),(30,14),(35,8),(38,13),(37,20)), (True, (36,20),(36,13),(38,10),(45,12),(51,22)))),
    3:(((0,15), (67,25)), ((False, (32,5),(34,7),(40,11),(51,11)), (True, (19,18),(25,10),(34,7),(32,12),(29,19)), (True, (32,20),(33,13),(38,9),(41,13),(37,20)), (True, (38,21),(38,14),(40,11),(49,11),(50,21)))),
    4:(((0,16), (67,25)), ((False, (32,6),(35,7),(40,11),(51,11)), (True, (19,18),(26,11),(35,7),(31,13),(28,20)), (True, (31,20),(33,14),(38,10),(40,12),(37,20)), (True, (37,20),(39,14),(40,11),(49,11),(49,22)))),
}

def stickbug():
    mixer.init()
    mixer.music.load('bg.mp3')
    mixer.music.play()
    with ManagedScreen() as screen:
        for t in range(9):
            for i in [1,2,3,4,3,2]:
                screen.clear_buffer(2, 0, 0)
                coords = stick_bug_coordinates[i]
                screen.move(*coords[0][0])
                screen.draw(*coords[0][1], thin=False)
                for p in coords[1]:
                    thin_draw = p[0]
                    screen.move(*p[1])
                    for l in p[2:]:
                        screen.draw(*l, thin=thin_draw)
                screen.print_at('GET STICK BUGGED LOL', 27, 2)
                screen.refresh()
                sleep(0.15)

stickbug()

'''
stickbug joint coordinates: (x,y)
frame 1:
floor:
0,24-67,33
bug:
27,16-30,17-36,21-46,21
17,27-19,17-30,17-30,22-30,29
30,29-28,24-33,20-37,24-37,29
37,29-35,27-36,21-42,24-50,31

frame 2:
floor:
0,25-67,34
bug:
30,14-33,17-38,20-48,20
19,27-22,18-33,17-31,21-31,29
31,29-30,24-35,18-38,23-37,30
36,30-36,23-38,20-45,22-51,32

frame 3:
floor:
0,25-67,35
bug:
32,15-34,17-40,21-51,21
19,28-25,20-34,17-32,22-29,29
32,30-33,23-38,19-41,23-37,30
38,31-38,24-40,21-49,21-50,31

frame 4:
floor:
0,26-67,35
bug:
32,16-35,17-40,21-51,21
19,28-26,21-35,17-31,23-28,30
31,30-33,24-38,20-40,22-37,30
37,30-39,24-40,21-49,21-49,32
'''