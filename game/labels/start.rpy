label beggining:
  
  init:
    $ achievement.steam_position = "bottom right"

  stop music fadeout 1.0
  scene bg dark with Fade(2.0, 0.5, 1.0)

  scene bg street night with Dissolve(1.0)

  "..." """
  And I think it would really help her.
  """

  hide kyoko with fade

  "..." """
  Are you listening to me?
  """

  hide kyoko with fade

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
  """

  show kyoko confused

  "" """
  I am fine. As your brother I am who should be worried for you.
  """

  show kyoko speaking

  kyoko """
  Come on, at least tell me your name. Let's see if you have your mind on your head.
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

  me "Now.. what where you saying before?"

  show kyoko speaking
  kyoko "Me?"

  me "Yes, Kyoko. You. Speaking about not having your mind on your head."

  show kyoko normal
  kyoko "Ah! Yeah! I was asking you about our mothers date."

  me """
  Well, I really don't know. I mean, we don't even know the guy.

  I know our father died a few years ago and she is totally in her right to know someone else
  """

  show kyoko confused
  kyoko "But....???"

  me "I... we don't have enough info about him. Jezz, we don't even know his name."

  show kyoko speaking
  kyoko """
  And??

  Don't forget, he is mom's boyfriend, not yours.
  """

  me "Yeah, I know that, Kyoko. What I mean is..."

  show kyoko normal
  kyoko """
  Look, I understand. You are afraid that mom is going to replace our father and all, but you know how much she loved him.

  She knows what she is doing. Let her chase her happiness.
  """

  show kyoko happy
  kyoko "Besides, you are our detective. If something's wrong, you will know it haha"

  me """
  Yeah, I guess...
  """

  """
  I've worked with the City Police for 3 years now and a few months back I was promoted detective. Everyone was really excited about it.

  {i}The starboy{/i}, they called me. For resolving one of the biggest case this city has faced.

  It was a really big organization. {b}Dr. Purple{/b}, he was called. The biggest organ's dealer this city has had.

  It took us months of research, operations and friends, but finally we tracked them down.

  Once their leader surrendered, everyone else stoped as well.
  """

  me "We should go home, you are a warrior, but your lungs aren't as stronger as you."

  show kyoko happy
  kyoko """
  Yeah, yeah. I know. You are such a cute big brother haha.
  """
  show kyoko normal
  kyoko """
  Okay, fine. Let's go home.
  """

  scene bg street_house night
  with Fade(2.00, 3.00, 2.50)

  show kyoko desperate at center
  with Dissolve(0.5)

  kyoko "Ahhh.... I am so tireeed. I want to lay in bed all night"

  me "Yeah, me too. We walked a lot trying to find the presents for mom."

  show kyoko normal
  kyoko "Yeah, I hope she like them."

  show kyoko desperate
  kyoko "My feets are killing me because of them."

  """
  We were getting some presents to our mother due to her new relationship.
  """

  show kyoko normal
  kyoko """
  [mc_name], look. There's people. They are draggin someone over that alley.
  """

  show kyoko confused
  kyoko """
  HEY YOU! WHAT ARE YOU..
  """

  show kyoko desperate

  me "Shhh!!! Wait."

  show kyoko at left
  with MoveTransition(0.2)
  hide kyoko with Dissolve(0.2)
  with hpunch

  $ renpy.pause(delay=1.5)

  me "They didn't notice us."
  me "Kyoko, wait here. I don't like this."

  kyoko "What do you think they are going to do to her?"

  me "I don't know."

  kyoko "You are going to do something, right?"
  kyoko "RIGHT?"

  menu:
    " "
  
    "Yes":
      $ chapeter1_helping = True
  
    "No":
      pass

  $ renpy.notify(_("Kyoko will remember that"))

  if chapeter1_helping:
    me "Yes, but I can't just charge in that direction."
    kyoko "But while we are hidding here, they might have doing horrible things to that person"
    me "Yes, I know."
    me "Wait while I call the police department. Probably we are going to need backup"
    kyoko "Yeah, that's smart. Expected from my cute brother"

  else:
    me "I mean, it's not our business, Kyoko. We shouldn't interrup"
    kyoko "What the fuck are you saying, [mc_name]?"
    kyoko "You are a detective, your job literally is catching bad guys. Those are bad guys."
    me "It is a bad idea, you don't understand"
    kyoko "What do I don't understand? That you are leaving a person alone just because \"it's not your business\"?"
    me "Fuck. Okay."

  "..." "{i}Witness...{/i}"

  me "What?{nw}"

  show kidnapper1 normal at right
  with Dissolve(0.1)
  show kidnapper1 normal at center
  with MoveTransition(0.1)
  with hpunch

  scene bg white
  with Dissolve(0.05)

  $ renpy.pause(delay=0.1)

  scene bg dark
  with Fade(1.0, 4.0, 4.0)

  scene bg dark
  with Dissolve(3.0)
  show bg bath foggy as bath at center:
    alpha 0.15
  with Dissolve(0.3)

  "..." "Yeah, I know. Don't worry, everything will work as planned."

  show bath at center:
    alpha 0.00
  with Dissolve(0.3)

  $ renpy.pause(delay=2.0)

  show bath at center:
    alpha 0.15
  with Dissolve(0.3)

  "..." "It will sell fast. I got that."

  show bath at center:
    alpha 0.00
  with Dissolve(0.3)

  $ renpy.pause(delay=2.0)

  show bath at center:
    alpha 0.15
  with Dissolve(0.3)

  show dr blurred at center:
    alpha 1.00
  with Dissolve(1.0)

  "..." "Hmmm... you're still fighting. Nice."

  show dr blurred:
    alpha 0.00
  show bath at center:
    alpha 0.00
  with Dissolve(0.3)

  $ renpy.pause(delay=2.0)

  show dr blurred:
    alpha 1.00
  show bath at center:
    alpha 0.15
  with Dissolve(0.3)

  "..." "Until we meet again."

  hide dr blurred
  with Dissolve(1.0)


  scene bg dark
  with Fade(1.00, 2.00, 1.00)

return