label beggining:
  
  init:
    $ achievement.steam_position = "bottom right"

  stop music fadeout 1.0
  scene bg dark with Fade(2.0, 0.5, 1.0)

  scene bg street night with Dissolve(1.0)

  """
  Sometimes... at night. I stare at the stars wondering how different things would be there.

  Wondering if, maybe, there's someone watching this star and thinking if something lives here

  If something is smart enough to comunicate among themself. To create new things.

  I've always wondered... while watching the stars... could things be different from this place that we call Earth?
  """

  "..." """
  Hey!!!

  Dummy, hey I am right here!
  """

  show kyoko normal at center
  with Dissolve(0.5)

  show kyoko confused

  kyoko """
  Earth calling, are you listening to me at least?
  """

  """
  That's Kyoko...
  """

  "" "Sorry, I got lost in my mind.."

  show kyoko speaking
  kyoko """
  Yeah, don't tell me. Are you ok, thoug?

  Come on, at least tell me your name. Let's see if you have your mind in good state.
  """

  python:
    tmp = renpy.input(_("My name is"), allow="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", length=15)
    tmp = tmp.strip()

    if tmp:
      mc_name = tmp

  me """
  [mc_name], Kyoko. Are you happy?
  """

  show kyoko happy
  kyoko "Haha! Always..."

  scene bg dark
  with Fade(2.00, 1.00, 1.50)

return