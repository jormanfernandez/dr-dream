label beggining:
  
  init:
    $ achievement.steam_position = "bottom right"

  stop music fadeout 1.0
  scene bg dark with Fade(2.0, 0.5, 1.0)

  scene bg street evening with Dissolve(1.0)

  $ renpy.pause(delay=1.0)

  show dr talking1:
    yalign 1.0
    xalign 0.15
  with Dissolve(0.5)

  show mother normal:
    yalign 1.0
    xalign 0.85
  with Dissolve(0.5)


  dr """
  I am happy to be accepted by you.
  """

  show dr normal

  dr """
  ...
  """

  show dr talking1

  dr """
  Hey! Are you there? Earth calling...
  """

  show dr normal

  $ renpy.pause(delay=1.0)

  scene bg dark
  with Fade(2.00, 1.00, 1.50)

return