# The script of the game goes in this file.

# Set up LayeredImage Sprites
layeredimage teppy:

    group base auto:
        attribute shirt default

    if casual:
        pos (0, 40)
        "me poker"

    group face auto:
        attribute neutral default

# This adds Eileen's headband to her sprite when True
default casual = False

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define t = Character("Teppy", color="#f88787", image="me", height=0.2)
# reference to side images: https://www.renpy.org/doc/html/side_image.html
image side me poker = "me poker.png"
define config.side_image_tag = "me" 
define config.side_image_only_not_showing = True
# This transform block below works if the images are of the same sizes. EG: just changing emotions
# transform same_transform(old, new):
#     old
#     new with Dissolve(0.2, alpha=True)

# define config.side_image_same_transform = same_transform


define e_nvl = Character("Teppy", color="#f88787", kind=nvl, image="me")         # IDK what this is for yet
define nar_nvl = nvl_narrator





## Splashscreen ############################################################
## A portion of the game that plays at launch, before the main menu is shown.
## https://www.renpy.org/doc/html/splashscreen_presplash.html

## The animation is boring so I recommend using something else.
## ATL documentation: https://www.renpy.org/doc/html/atl.html

image splash_anim_1:

    "images/xteppy/s_final_heart.png"
    xalign 0.5 yalign 0.5 alpha 0.0
    ease_quad 3.0 alpha 1.0 zoom 2

default persistent.firstlaunch = False

label splashscreen:

    scene black

    ## The first time the game is launched, players can set their accessibility settings.
    if not persistent.firstlaunch:

        ## This screen is at the top of extras.rpy

        call screen splash_settings

        ## This screen will not appear in subsequent launches of the game when
        ## the following variable becomes true.
        $ persistent.firstlaunch = True

    ## Here begins our splashscreen animation.
    show splash_anim_1
    show text "{size=20}Made with so much love, effort and with you {size=30}(Jessa){/s} in mind. <3 \nPara alam mong sa'yo lang to. ;){/s}":
        xalign 0.5 yalign 0.9 alpha 0.0
        pause 3.0
        linear 1.0 alpha 1.0
    
    ## The first time the game is launched, players cannot skip the animation.
    if not persistent.seen_splash:
        
        ## No input will be detected for the set time stated.
        ## Set this to be a little longer than how long the animation takes.
        $ renpy.pause(8.5, hard=True)
 
        $ persistent.seen_splash = True
    
    ## Players can skip the animation in subsequent launches of the game.
    else:
 
        if renpy.pause(8.5):
 
            jump skip_splash

    scene black
    with fade
 
    label skip_splash:
 
        pass
 
    return

## The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    # scene room

    # This shows a character sprite.

    

    # This plays our music file in a way that if audio captions are on,
    # it will tell us the name of the song. This music plays at full volume
    # after 2 seconds and fades out after 2 seconds when stopped.
    # $ play_music(garden,fadein=2.0,fadeout=2.0)

    # This unlocks the the achievement with the corresponding name
    $ achievement.grant("Beginning")

    # This adds an integer value to a point-based achievement.
    # To track how much of it has been earned, use a regular variable for now.
    # $ achievement.progress("Point_Collector", 10)
    # $ persistent.points =+ 10

    t "Hello there! Intro muna tayo. ;)"
    t "So, I've been racking-up my brain for the past few weeks to have this improved version of my Digital Lover Letter."
    t "I think this is {i}{b}waaaaay{/b}{/i} better naman compared dun sa {color=#000}\"Pa-farewell\"{/color}."
    ic "{i}(Wait lang, nag-aayos pa 'ko ng buhok...){/i}"

    show me poker at right:
        ## Adjust sprite's attributes here accordingly
        # yoffset 250
        # zoom 0.5    
    with fade

    t "OK! So, ayun na nga. Intro muna tayo pang-flex sa ibang magtatangkang i-install 'to. ;)"
    t "You guys can get up to a certain point of this letter pero since this was {b}especially made for Jessa{/b}, the personal stuffs will be locked and will require a password. ;)"
    t "I hope this gives you a hint of how well-thought-out this project is. (charaught)"
    t "Osigesigesigesige... Enough of those boring stuffs!"
    ""
    t "I doubt na you had the chance to see the website I created for our first monthsary. (Yep, I created a website. I know how to make those, too.)"
    t "Unfortunately, hindi na sya available as I forgot the credentials I used for it and then, nag-expire na sya."
    t "Good thing is, nai-save ko naman yung copy ko nun and I included that first-ever-bonggang-dedication-letter ko para kay {b}Labidabs Jessa{/b} ko dito."
    ""

    hide me with fade

    ic "{i}(Of course! Kasi wala akong ipapakita sa iba kung hindi ko yun ilalagay. Very personal yung anniv dedication letter ko, guys. Sorry!){/i}"
    
    show me nvl at right with fade
    t nvl "Change outfit! \nMedyo mahaba 'to, so...Kayo na bahala. >.<"

    nar_nvl "{i}Originally posted on July 28, 2022, 1:21 p.m. with removed \"not-so-important parts\".{/}"
    nar_nvl """So, ito yung pinagpupuyatan ko the last few nights na medyo ikinaka-toyo mo...
    
    \"Sige na, gawin mo na yung pinagkakaabalahan mo. Matutulog na 'ko.\"
    \n{size=20}--- Jessa Marie, July 28, 2022{/size}

    I was actually coding + testing the code on a live (but free) server and, luckily, gumana naman. Hehe
    """
    nar_nvl "Sharawt sayo, {color=#fff}Jessa Marie Guico!{/color}"
    nar_nvl "So ayon na nga, 'no? {i}{size=24}(in CongTV's voice){/size}{/i} Pasensya na't biglaan ko lang naisip 'tong idea of a website for you."
    nar_nvl """Habang nag-eempake ka kamo ng dadalhin mo sa Boracay at galit ka sa'kin kase nga \"hoy\" ang CS natin,
    \nI'm looking forward to our first monthsary. {size=24}
    \n(Tho monthsaries are not that good-sounding for me kasi hindi na magiging ganun ka-special yung anniv, at least, sa first, bonggahan natin! ;) ){/size}
    
    \n...saka na yung common things like flowers and chocolates."""
    nar_nvl """So, eto na nga. Habang galit ka sa'kin, nag-iisip na ko ng kakaibang First-Month-Congratulatory-Gift sayo kasi nakatagal ka sa'kin. Hehe
    
    Sabi ko sa'yo, di ba, eleven years kitang hinintay? Eleven years akong walang ganito so, for the first time after such a long time, gagawa ako ng something na kakaiba ...para sa'yo.

    {i}{size=24}(Disclaimer: ngayon lang 'to kasi nga special.)
    (Note: Pwede mo 'tong ipakita sa iba since wala akong sasabihing kabalbalan dito...or, at least, I will try. HAHA! Ang haba ng pasakalye ko.){/size}{/i}"""






    ##################### after the 1st month message here
    nvl clear

    e_nvl "Not all games may need to use both ADV and NVL, but it's nice to have options as a developer."
    nar_nvl "Eileen wonders where she should travel to."

    stop music fadeout 1.0

    ## This ends the replay mode segment. Doesn't affect normal gameplay.
    $ renpy.end_replay()

    menu (nvl=True):

        "Office":

            ## This empty label is solely for replay mode purposes.

            label office:

                pass

            t "To the office? Okay...?"

            $ achievement.grant("Office")

            $ play_music(business,fadein=2.0,fadeout=2.0)

            scene future_office
            show shirt pout03 at center:
                yoffset 250
            with fade

            t "Ugh, you know that saying about \"all work and no play,\" right?"

            "Eileen seems bothered by something."

        "Beach":

            label beach:

                pass

            t "The beach sounds fun!"

            $ achievement.grant("Beach")

            $ play_music(summer,fadein=2.0,fadeout=2.0)

            hide shirt with dissolve
            $ casual = False

            scene sort_of_beautiful_beach_day
            show shirt happy03 at center:
                yoffset 230
            with fade

            t "Hehe, I have a swimsuit now!"

            "Eileen seems pleased with herself."

    "Remember to check the History screen if you have not done so yet."

    ## This ends the replay mode segment. Doesn't affect normal gameplay.
    $ renpy.end_replay()


    
    
    # This plays our sound file in a way that if audio captions are on,
    # it will describe the sound being played.
    $ play_sound(door)

    t "Let's close this so the breeze doesn't mess up my hair..."

    $ play_sound(drawer_open)

    t "Let me look for a pen..."

    $ play_sound(drawer_close)

    t "Not in there?"

    $ play_sound(drawer_open)

    t "Maybe here?"

    $ play_sound(drawer_close)

    t "Found it!"

    t "If you had your Audio Captions on, you should have seen something appear in the notification tab."

    t "Neat, right?"

    t "Now let's test Image Captions."

    # show shirt at right with move

    ic "Eileen walks to the right of the room."

    t "Over here..."

    # show shirt at left with move

    ic "Eileen walks to the left of the room."

    t "Now here..."

    # show shirt at center with move

    ic "Eileen walks to the center of the room."

    t "And there we go!"

    t "If you had your Image Captions on, then you should have seen some extra narration describing my movements."

    t "This is done with the special {color=#32CD32}{i}ic{/i}{/color} speaker tag we defined in {color=#32CD32}{i}accessibility.rpy{/i}{/color}."

    t "Now, let's test the Screen Shake settings."

    $ shake()

    # show shirt surprised_blush01 with dissolve

    ic "The room shakes."

    t nvl "If you had it on, did you notice how robust that Screen Shake was? That wasn't the classic {color=#32CD32}{i}hpunch{/i}{/color}."

    t"This time around, we added in a custom Shake function that is randomized each time, with varying levels of intensity you can choose from."

    t "You can turn the screen shaking effect off in Preferences, just in case the motion makes you or your players sick. One more time."

    $ shake()

    ic "The room shakes again."

   

## End Credits
label credits:

    ## We hide the quickmenu for the last part of the game so they don't
    ## appear at the bottom.
    $ quick_menu = False

    ## We hide the textbox as well so it doesn't mess with things
    window hide

    scene black with fade

    ## Find "End Credits Scroll" in extras.rpy to change text.
    call screen credits(15.0)

    $ persistent.credits_seen = True

    scene black
    with fade
    
    # Players can skip the credits in subsequent playthroughs of the game.
    label skip_credits:
 
        pass

    ## Makes [result] work. This needs to be near the end of the game
    ## for it to work properly.
    $ percent()

    ## We display a screen that shows how much the player has seen and played of the game.
    show screen results
    
    centered "Fin"

    hide screen results

    if persistent.game_clear:

        pass

    ## Do you want to leave some author's notes or a hidden message for your dedicated fans?
    ## This will check if they've seen all that the game has to offer.
    else:

        if readtotal == 100:

            $ achievement.grant("Completionist")

            ## Due to the way that $ percent() works, we need to make this a text displayable
            ## or else it'll try to count it too.
            show text "{size=60}{color=#ffffff}You've unlocked a special message.\nAccess it through the Extras Menu.{/color}{/s}":
                xalign 0.5 yalign 0.5 alpha 0.0
                linear 1.0 alpha 1.0

            $ persistent.game_clear = True

            ## The game will show our text displayable so the player can read it
            ## And only continue when there is input
            pause

    ## We re-enable the quickscreen as the credits are over.
    $ quick_menu = True

    # This ends the game.
    return