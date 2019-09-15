label splashscreen:

  scene bg dark
  with Fade(1.0, 1.0, 1.0)

  show logo:
    xalign 0.5 yalign 0.5
  with dissolve

  $ renpy.pause (5.0)

  hide logo
  with dissolve

  scene bg dark
  with Fade(1.0, 1.0, 1.0)