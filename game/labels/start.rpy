label beggining:
  
  init:
    $ achievement.steam_position = "bottom right"

  stop music fadeout 1.0
  scene bg dark with Fade(2.0, 0.5, 1.0)

  scene bg street evening with Dissolve(1.0)

  $ renpy.pause(delay=1.0)

  show kyoko happy at center
  with Dissolve(0.5)

  kyoko """
  And... and.... then we could go to the festival next week and...
  """

  show kyoko normal

  kyoko """
  ...
  """

  show kyoko speaking

  kyoko """
  Hey! Are you there? Earth calling...
  """

  show kyoko normal

  $ renpy.pause(delay=1.0)

  scene bg dark
  with Fade(2.00, 1.00, 1.50)

return