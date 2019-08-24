label beggining:
  
  init:
    $ achievement.steam_position = "bottom right"

  stop music fadeout 1.0
  scene bg dark with Fade(2.0, 0.5, 1.0)

  scene bg street evening with Dissolve(1.0)

  $ renpy.pause(delay=1.0)

  show kyoko normal at center
  with Dissolve(0.5)

  kyoko """
  Hey...

  Earth calling, are you there?

  Dude, don't let me talking alone like that, its really freaky.
  """

  menu:
    ""

    "Yes, sorry":
      $ choice = False

    "I'll wait":
      $ choice = True


return