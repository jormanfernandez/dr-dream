init python:
  route = "backgrounds"
  white = route + "/white.png"
  dark = route + "/dark.png"

image bg dark = dark
image bg white = white

image bg street day = route + "/street day.jpg"
image bg street evening = route + "/street evening.jpg"
image bg street night = route + "/street night.jpg"

image bg street_house day:
    route + "/street_house day.jpg"
    yalign 1.0
    xalign 0.5
    zoom 1.65
image bg street_house night:
    route + "/street_house night.jpg"
    yalign 1.0
    xalign 0.5
    zoom 1.65

image bg bath foggy:
    route + "/bath foggy.png"
    yalign 1.0
    xalign 0.5
    zoom 1.05
image bg bath normal:
    route + "/bath normal.png"
    yalign 1.0
    xalign 0.5
    zoom 1.05 