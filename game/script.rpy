# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

image smile01 = "images/sprites/teppy_sprites/shirt smile01.png"


define t = Character("Teppy", color="#f88787", image="shirt smile01.png", height=0.2)
# reference to side images: https://www.renpy.org/doc/html/side_image.html
image side smile01 = "images/sprites/teppy_sprites/shirt smile01.png"
define config.side_image_tag = "smile" 
define config.side_image_only_not_showing = True
# This transform block below works if the images are of the same sizes. EG: just changing emotions
# transform same_transform(old, new):
#     old
#     new with Dissolve(0.2, alpha=True)

# define config.side_image_same_transform = same_transform


define e_nvl = Character("Teppy", color="#f88787", kind=nvl, image="smile")         # IDK what this is for yet
define nar_nvl = nvl_narrator

image anya_movie = Movie(play="images/anya.webm", loop=False, pos=(210, -500), anchor=(10, 10), alpha=0.9) #side_mask=True, 

# $ renpy.movie_cutscene("oa4_launch.webm") # place this where you want a cutscene placed. Hides when movie ends/user clicks.
 




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

    t "Hello there! Intro muna tayo. ;)"
    t "So, I've been racking-up my brain for the past few weeks to have this improved version of my Digital Lover Letter."
    t "I think this is {i}{b}waaaaay{/b}{/i} better naman compared dun sa {color=#000}\"Pa-farewell\"{/color} I sent Jessa a few months ago."

    show smile01 at right with fade:
        ## Adjust sprite's attributes here accordingly
        # yoffset 250
        zoom 0.5   # this zoom fits as using the image as a side image 
    

    show anya_movie behind smile01
    t "OK! So, ayun na nga. Intro muna tayo pang-flex sa ibang magtatangkang i-install 'to. ;)"
    t "You guys can get up to a certain point of this letter pero since this was {b}especially made for Jessa{/b}, the personal stuffs will be locked and will require a password. ;)"
    "{size=20}{i}Hope this gives you a hint of how well-thought-out this project is. (charaught){/i}{/s}"
    t "Osigesigesigesige... Enough of those boring stuffs! (Pinapanood mo ba muna ung BG vid? hehe)"
    ""
    t "Also, I doubt na you people had the chance to see the website I created for our first monthsary. {size=20}{i}(I created a website. I studied how to make those, too.){i}{/s}"
    t "Unfortunately, hindi na sya available as I forgot the credentials I used for it and then, nag-expire na sya."
    t "Good thing is, nai-save ko naman yung copy ko nun and I included that first-ever-bonggang-dedication-letter ko para kay {b}Labidabs Jessa{/b} ko dito."
    ic "{size=20}{i}(Of course! Kasi wala akong ipapakita sa iba kung hindi ko yun ilalagay. Very personal yung anniv dedication letter ko, guys. Sorry!){/i}{/s}"
    hide anya_movie
    hide smile01
    # show smile01 nvl at right with fade
    
    # This plays our music file in a way that if audio captions are on,
    # it will tell us the name of the song. This music plays at full volume
    # after 2 seconds and fades out after 2 seconds when stopped.
    $ play_music(million,fadein=2.0,fadeout=2.0)
    # play music million fadein 0.5

    t nvl "Medyo mahaba 'to since wala naman akong ipapakita sa ibang tao kung hindi ko yun ilalagay so,..Kayo na mag-adjust. >.<"
    
    # page 1
    nar_nvl "{i}{size=20}Originally posted on July 28, 2022, 1:21 p.m. with removed \"not-so-important parts\".{/}"
    nar_nvl "{i}{size=20}Here it goes:{/}"
    nar_nvl """So, ito yung pinagpupuyatan ko the last few nights na medyo ikinaka-toyo mo...
    
    {color=#fff}\n\"Sige na, gawin mo na yung pinagkakaabalahan mo. Matutulog na 'ko.\"{/}
    \n{size=20}--- Jessa Marie, July 28, 2022{/size}

    I was actually coding + testing the code on a live (but free) server and, luckily, gumana naman. Hehe
    """
    nar_nvl "Sharawt sayo, {color=#fff}Jessa Marie Guico!{/color}"
    nar_nvl "So ayon na nga, 'no? {i}{size=20}(in CongTV's voice){/size}{/i} Pasensya na't biglaan ko lang naisip 'tong idea of a website for you."
    nar_nvl """Habang nag-eempake ka kamo ng dadalhin mo sa Boracay at galit ka sa'kin kase nga {color=#fff}\"hoy\"{/color} ang CS natin,
    \nI'm looking forward to our first monthsary. {i}{size=20}(Tho monthsaries are not that good-sounding for me kasi hindi na magiging ganun ka-special yung anniv, at least, sa first, bonggahan natin! ;) ANYWAYS...){/}
    
    \n...saka na yung common things like flowers and chocolates."""
    nar_nvl ""

    nvl clear
    # page 2
    nar_nvl "" 
    nar_nvl """So, eto na nga. Habang galit ka sa'kin, nag-iisip na ko ng kakaibang First-Month-Congratulatory-Gift sayo kasi nakatagal ka sa'kin. Hehe
    
    Sabi ko sa'yo, di ba, {color=#fff}eleven years kitang hinintay?{/color} Eleven years akong walang ganito."""
    nar_nvl "{i}so, for the first time after such a long time, gagawa ako ng something na kakaiba{i}"
    nar_nvl """\n{b}{u}{color=#fff}...para sa'yo{/color}.{/u}{/b}

    {i}{size=20}(Disclaimer: ngayon lang 'to kasi nga special.)
    (Note: Pwede mo 'tong ipakita sa iba since wala akong sasabihing kabalbalan dito...or, at least, I will try. HAHA! Ang haba ng pasakalye ko.){/size}{/i}
    
    
    """
    nvl clear
    # page 3
    nar_nvl """Game na talaga!
    \n{b}Happy 1st month with me, Jessa! {i}{size=20}(...pero hindi tayo magkasama?){/size}{/i}{/b}
    \n{i}{size=20}(Hindi ko na rin gagamitin ung \"hoy\" kasi baka ma-badtrip ka na naman tapos hindi mo na 'to ituloy, sayang effort ko.){/size}{/i}
    """
    nar_nvl "Also...Thank you."
    nar_nvl "Thank you for letting me in to your life."
    nar_nvl "I have a good idea kung paanong \"siguro\" e closed ka na sa pakikipagrelasyon kaya salamat at binuksan mo ulit yung pintuan ng puso mo para sa'kin."
    nar_nvl """Alam kong madami pa akong hindi alam about you {i}{size=20}(kahit na one year kitang ina-assess...){/size}{/i},
    \nwe're \"getting to know each other\" pa rin naman so, let us see this through, okay?"""
    nar_nvl """Ako rin naman... I never would've thought {i}{size=20}(wow?){/size}{/i} na makikipagrelasyon ako ulit...
    \nNang bigla-bigla...
    \n{b}Sa'yo.{/b}"""
    nar_nvl "{i}{size=20}(No offense meant dito ha? Snabi ko lang to kasi nga sabi mo hindi naman kita pinapansin nung magkatrabaho pa tayo. pero sabi mo lang talaga yon. Snob ka rin kase. XD){/size}{/i}"
    nar_nvl "No. Seriously. Eleven years."
    nar_nvl "Actually parang wala na talaga akong plano magjowa/mag-asawa/magpamilya before e."
    nar_nvl "Masaya naman na ko sa petiks kong buhay-single with araw-araw na sinangag+longganisa o kaya pancit canton tapos cobra...ganon."
    nar_nvl "I thought \"okay na yon. Naranasan ko namang magjowa at lumande.\""

    nvl clear
    # page 4
    nar_nvl "Pero ewan ko lang din. Bigla ko na lang naisip na ang tagal na pala nating nag-uusap almost everyday..."
    nar_nvl "Ang dami na pala nating nalaman tungkol sa isa't-isa...."
    nar_nvl "Lagi pala tayong \"masaya lang\" sa mga usapan natin kahit hindi tayo magkasama..."
    nar_nvl "Nasanay na pala akong andiyan ka. {i}{size=20}(Mmm...nasanay ka na rin naman, di ba? Di baaaa??){/size}{/i}"
    nar_nvl "So, {b}why not ask you to be my girlfriend na?{/b}"
    nar_nvl ""
    nar_nvl "Baka naman kako kaya ko nang magcommit ulit?"
    nar_nvl "Baka naman kaya ko na, at gusto ko nang mag-alaga at umintindi ulit?"
    nar_nvl "Baka naman kailangan ko na ng kakulitan, ka-kumustahan, ka-good morning/good night-an,"
    nar_nvl "kaharutan,"
    nar_nvl "kalambingan,"
    nar_nvl "katampuhan,"
    nar_nvl "kaaway..."
    nar_nvl "ulit?"
    nar_nvl "So, ayun. Salamat. Salamat at nagkaroon ka ng lakas ng loob na tanungin ako."
    nar_nvl "{b}Charoooooot! Haha!{/b}"
    nar_nvl "{i}{size=20}(Guys, nagjo-joke lang ako, oke? Alam ni Jessa yan){/size}{/i}"

    
    nvl clear
    # page 5
    nar_nvl "Ayyyyy! Oo nga pala! Since bago pa lang tayo, I have a few Sana's para satin: {i}{size=20}(saka para pampahaba na rin...as if hindi pa 'to mahaba){/size}{/i}"
    nar_nvl "Sana {i}{size=20}(at syempre: dapat!){/i}{/size} magtagal tayo. Yung tipong paaabutin mo ko ng 40 years old, ganon. Hehe"
    nar_nvl "Sana okay lang din sayo yung paraan ng pagkikipagcommunicate ko. Kung hindi naman, sabihin mo lang tapos let's work it out. :)"
    nar_nvl "Naniniwala akong communication is key at I'm looking forward to having discussions with you about what we want and what we do not want, what we should and should not do, etc., etc."
    nar_nvl "...tapos ililista natin para pag may sumira sa usapan, may ebidensya. ;)"
    nar_nvl "Sana matiis at matanggap mo ako kasi talagang ngayon lang ako ulit sumugal ng ganito."
    nar_nvl """Lastly, sana open for tagging yung profile mo kasi ita-tag talaga kita in-time...para mapilitan ka nang magpakita dito samin at i-meet yung fansclub ko na matagal nang naghihintay sa magiging jowa ko: SA'YO. Hehe"""
    nar_nvl "O gusto mo ngayon na? Ang problema kasi e yung trabaho ko. Ako nahihiya sa sarili ko kung ako ipapakilala mo dyan sa inyo e. {i}{size=20}(Ang assuming ko ba na ipapakilala mo ko? haha! Hintay lang muna tayo. Baka by 2nd, meron na.){/i}{/size}"
    nar_nvl "Ayun na! Wala na 'kong masabi kasi nga sabi ko walang kabalbalan akong ihahalo dito e. Tama na siguro 'to?"
    nar_nvl "Mahaba na yata masyado? Saka{i}{size=20}sal{/i}{/size} na yung susunod kasi baka hindi ka na kiligin pag \"ipinutok\" ko na lahat ng bala ko dito."
    nar_nvl "{b}{size=50}Happy First Month sa'tin, Jessa!{/size}{/b}"
    nar_nvl "{b}{size=50}Hindi ko na kukwestiyonin yung sarili ko: alam kong mahal na kita.{/size}{/b}"
    nar_nvl "Looking-forward to sharing a lot of experiences with you. Muah!"


    ##################### after the 1st month message here
    nvl clear

    show shirt happy02 with dissolve
    t "So, ayun na nga, 'no? Hanggang dito lang yung para sa inyo, mga mars. :D"
    show shirt smile01
    t "May password na yung pang anniv na message ko so, kung gusto nyo, ichat nyo na lang si Jessa para mabasa nyo rin. hehe"
    t "Thank you sa pagsilip at kung trip nyo rin magpagawa ng ganito, pwede naman. Basta hindi madalian...at hindi libre! HAHA!"

    ##################### pw required area
    e_nvl "So, alam mo ba yung password?"
    nar_nvl "Kung oo, good!:"

    stop music fadeout 1.0

    ## This ends the replay mode segment. Doesn't affect normal gameplay.
    $ renpy.end_replay()

    menu (nvl=True):

        "Yesh, besh. Alam ko, besh!":

            ## This empty label is solely for replay mode purposes.

            label yes:

                pass

            t "Wow? Persistent maki... Okay. Payag si Labidabs e."
            $ play_music(business,fadein=2.0,fadeout=2.0)

            scene future_office
            show shirt pout03 at center:
                yoffset 250
            with fade

            t "something here al;kasdfjkasdfhaklsdfhjklasdkjlkaskjfdhaksjdfhaklsjdfhasdfjkh"

            "Eileen seems bothered by something."

        "Hindi. Sige, out na 'ko.":

            label no:

                pass

            t "Salamat ulet, mars! Na-appreciate ko 'yung paglaan mo ng oras para sa kalandian ko. Apiiiiiir!"
            $ play_music(summer,fadein=2.0,fadeout=2.0)

            scene sort_of_beautiful_beach_day
            show shirt erm_blush05 at center:
                yoffset 230
            with fade

            t "Ingat!"

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