import os
import argparse
import turtle as t
from PIL import Image

parser = argparse.ArgumentParser(description='Make a feline-bear.')
parser.add_argument('size', type=int, nargs='?', default=307,
                    help='the size of the feline-bear')
parser.add_argument('--term', default=True, action=argparse.BooleanOptionalAction,
                    help='put --no-term if you want to stay after the turtle has done drawing.')
parser.add_argument('dir', nargs='?', default=os.getcwd(),
                    help='the directory to confine the feline-bear.')
args = parser.parse_args()

FACE_RADIUS = args.size


ssize = int(FACE_RADIUS*2.5)
# global configs
t.Screen().setup(ssize, ssize)
t.speed('fastest')
t.pensize(ssize//75)
t.colormode(255)
ACCENT_COLOR = 215, 15, 100
# ACCENT_COLOR = 40, 240, 155

EAR_RADIUS = FACE_RADIUS//3
EARS_X = FACE_RADIUS//2 + FACE_RADIUS//4
EARS_Y = FACE_RADIUS//2

EYE_MARKS_RADIUS = EAR_RADIUS * 1.1
EYE_MARKS_X = FACE_RADIUS/1.8
EYE_MARKS_Y = -FACE_RADIUS//4

EYE_RADIUS = EYE_MARKS_RADIUS/4
EYES_X = EYE_MARKS_X//2 + EYE_RADIUS
EYES_Y = 0

PUPILS_RADIUS = EYE_RADIUS/10
PUPILS_X = EYES_X
PUPILS_Y = EYE_RADIUS+PUPILS_RADIUS

NOSE_RADIUS = EYE_RADIUS/2
NOSE_X = 0
NOSE_Y = -EYE_MARKS_RADIUS/2

MOUTH_RADIUS = EYE_RADIUS*2
MOUTH_X = -MOUTH_RADIUS
MOUTH_Y = NOSE_Y*2


def drawCircle(initCors, radius, ccolor=None, fillColor=None, angle=360):
    if ccolor:
        t.color(ccolor)

    if fillColor:
        t.fillcolor(fillColor)

    t.penup()
    t.goto(initCors)
    t.pendown()
    t.begin_fill()
    t.circle(radius, angle)
    t.end_fill()
    t.penup()


# left ear
drawCircle((-EARS_X, EARS_Y), EAR_RADIUS, ACCENT_COLOR)
# right ear
drawCircle((EARS_X, EARS_Y), EAR_RADIUS)

# face
drawCircle((0, -FACE_RADIUS), FACE_RADIUS, ACCENT_COLOR, "white")

# left eye mark
drawCircle((-EYE_MARKS_X, EYE_MARKS_Y),
           EYE_MARKS_RADIUS, ACCENT_COLOR, ACCENT_COLOR)
# right eye mark
drawCircle((EYE_MARKS_X, EYE_MARKS_Y),
           EYE_MARKS_RADIUS, ACCENT_COLOR, ACCENT_COLOR)
# left eye
drawCircle((-EYES_X, EYES_Y), EYE_RADIUS, "black", "black")
# right eye
drawCircle((EYES_X, EYES_Y), EYE_RADIUS, "black", "black")
# left pupil
drawCircle((-PUPILS_X, PUPILS_Y), PUPILS_RADIUS, "white", "white")
# right pupil
drawCircle((PUPILS_X, PUPILS_Y), PUPILS_RADIUS, "white", "white")

# nose
# TODO: vectorize the nose, probably put a rectangle wrapped by two circles on two ends
drawCircle((NOSE_X-NOSE_RADIUS/3, NOSE_Y), NOSE_RADIUS, "black", "black")
drawCircle((NOSE_X, NOSE_Y), NOSE_RADIUS, "black", "black")
drawCircle((NOSE_X+NOSE_RADIUS/3, NOSE_Y), NOSE_RADIUS, "black", "black")

# mouth
t.setheading(270)
drawCircle((MOUTH_X, MOUTH_Y), MOUTH_RADIUS, "black", "white", 180)

# right ear cut
EAR_CUT_SIZE = EAR_RADIUS/20
t.turtlesize(*[EAR_CUT_SIZE for _ in t.turtlesize()])
t.goto(EARS_X+EAR_RADIUS, EARS_Y+EAR_RADIUS*2-EAR_CUT_SIZE*10)
t.fillcolor("white")
t.pencolor("white")
t.shape("triangle")
t.stamp()

t.hideturtle()

# save the image
fname = f"feline-bear-{FACE_RADIUS}"
psFileName = fname + ".ps"
canvas = t.getcanvas()
canvas.postscript(file=psFileName)
psimage = Image.open(psFileName)

savePath = os.path.join(args.dir, fname + ".png")
psimage.save(savePath)
os.remove(psFileName)


if not args.term:
    # to stop the window from terminating
    input("-- Enter any key --")
