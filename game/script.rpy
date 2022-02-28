# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# TO-DO: Refacture code. Rename images properly. Reorganize folders. Correct all dialogue.

# Names and online names.
define apu_online_name = "Apuu_55"
define apu_discord_name = "ApuApu#1234"
define apu_name = "Apu"
define aspie_online_name = "LegoMaster223"
define aspie_discord_name = "AspieMoon"
define aspie_name = "Aspie"

# Apu is a and au. 
# Aspie is e and eu.
# The u at the end is for the Pixelated text in the game to show, for example when they are texting digitally on Discord and in the forum.
define e = Character("Ashbie", who_color="#ff0000")
define eu = Character("[aspie_online_name]", who_color="#ff0000", what_font="fonts/M 8pt.ttf")
define au = Character("[apu_online_name]", who_color="#0000ff", what_font="fonts/M 8pt.ttf")
define a = Character("[apu_name]", who_color="#0000ff")

# The game starts here.

label start:

    scene computer_apu_happy

    # Apu goes onto Cosplay forum and finds a Cosplayer asking for help regarding a wig.

    a "Time to surf my favorite forum!"

    scene home_computer_inside

    a "I wonder how many cool new Cosplays there are today!"

    a "Let's see... So many new posts."

    a "What is this one about?"

    scene computer_forum_browse

    eu "Help! My Sailor Moon Outfit!"

    a "Hm.. I could totally help this person, I love Sailor Moon and I know a lot about Cosplay."

    au "What do you need help with {b}[aspie_online_name]{/b}?"

    eu "So, I bought this wig online that I use but I don't know how to properly style it, could you help?"

    au "Styling is just my thing! I can see the wig in your profile picture and I think just tweaking the length with scissors will do perfectly!"

    eu "Thanks {b}[apu_online_name]{/b}! I tried it and it looks way better now =)"

    a "Seems like another job well done. I love helping people that share this interest!"
    
    a "Hm.. What is this?"

    scene computer_forum_friend

    # Aspie adds Apu on the forum as a friend and they talk together a bit.

    a "Oh, {b}[aspie_online_name]{/b} added me as a friend!"

    a "Someone sent me a new PM?"

    eu "Hey {b}[apu_online_name]{/b}! Thanks for helping before, I love Cosplaying but I rarely do it myself :]"

    a "Woah, this might be a new friend?!"

    au "I also love Cosplay and I'm actually a huge fan of Sailor Moon myself!!"

    eu "Oh really?? I've been watching Sailor Moon since I was a kid, haha."

    au "Me too! Couldn't stop myself from watching it every morning when it came on the TV!"

    eu "How did you get into Cosplay?"
    
    au "I love the thought of being able to become any character that I look up to."

    eu "Same here! What else do you do?"

    au "Well, I attend College and people do not really appreciate Cosplay there."

    scene school_start

    au "I never really had many friends but I tried bringing up some interests to possibly bond with them but they thought Cosplay was a weird thing."

    au "So weird that they kept picking on me and still kinda do."

    scene computer_forum_pm

    au "Sorry, that must have been boring to listen to. What is your experience with Cosplay?"

    eu "Don't apologise {b}[apu_online_name]{/b}, I think it's cool that you like Cosplay."
    
    eu "I tried participating myself in a Cosplay event but I was very new and my outfit was made fun of."

    eu "What really matters though is the happiness it brings you and not what others think."

    a "Woah, {b}[aspie_online_name]{/b} is so cool."

    au "Do you want to add me on Discord?"

    eu "Sure {b}[apu_online_name]{/b} :)"

    au "My username is {b}[apu_discord_name]{/b}"

    scene discord_start

    # They add each other on Discord and end up getting closer.

    a "One new Discord notification?"
    
    a "Oh, Seems like {b}[aspie_online_name]{/b} added me and her username is {b}[aspie_discord_name]{/b}?"

    scene computer_apu_happy

    $ apu_online_name = "Apu"

    au "Hello! Nice to meet you {b}[aspie_discord_name]{/b}, you can call me {b}[apu_online_name]{/b} since that is actually my name."

    scene computer_aspie_happy

    $ aspie_online_name = "Aspie"

    eu "Hi {b}[apu_online_name]{/b}, my name is {b}Ashbie{/b}."

    eu "My nickname is {b}[aspie_online_name]{/b} though, so you can call me that!"

    scene discord_start

    au "Do you like memes, {b}[aspie_online_name]{/b}?"

    eu "I very much do!"

    show dancingCirno:
        yalign 0.5
        xalign 0.5

    au "Look at this!"

    scene computer_aspie_laughing

    eu "That's so cute!! I love it, haha"

    scene discord_start

    eu "Btw, I do youtube videos about cosplay, here is my channel if you want to see."

    scene computer_apu_happy

    a "Oh, let's see."

    scene link_click

    a "Hmm."

    scene youtube_aspie

    e "Welcome to my Top 10 Cosplay tips for beginners. I bet you haven't seen this first tip before!"

    a "This is actually surprisingly fun to watch!"

    scene discord_start

    au "I really like your videos they are very fun"

    eu "Tysm, {b}[apu_online_name]{/b}!"

    au "How come you make these videos?"

    eu "I want to share the joy of Cosplay with others and make people happy!!!"

    scene computer_apu_happy

    a "{b}[aspie_online_name]{/b} is so cool and caring..."

    scene discord_start

    au "That is a really awesome reason, {b}[aspie_online_name]{/b}"

    eu "Nah, I just want to help like you did with me earlier!!!"

    a "Imagine if someone as cool as her liked me..."

    a "Heh, who am I kidding? Someone as amazing as her would never be interested in someone like me."

    a "I am glad she wants to be my friend though."

    eu "Do you want to videocall, {b}[apu_name]{/b}?"

    au "Uh.."

    a "Oh no... She will see how ugly I am.. I'm not sure if I want to..."

    au "I don't know..."

    eu "Come on, it will be fun!!"

    au "I am not sure about that..."

    scene discord_call

    "{b}[aspie_discord_name]{/b} is Calling..."

    a "I really want to see her... Should I accept?"

    a "Might as well try..."

    scene discord_call_aspie

    e "Hello~"

    e "Oh, your webcam isn't working?"

    a "It does but it's just that..."

    a "I'm ugly and you wouldn't want to see me."

    e "Come on, show me yourself and let me decide that!"

    a "Okay.."

    scene discord_call_aspie_apu

    a "Uh, hello?"

    e "Hm... I'm disappointed."
    
    e "I was expecting you to look ugly like you said but you are very handsome, {b}[apu_name]{/b}."

    scene discord_call_aspie_apu_blushing

    a "...you think I'm handsome...?"
    
    a "I-I mean, I'm not!"
    
    a "Everyone at my school calls me names because I look weird..."

    e "I don't really care what others think to be honest."
    
    e "In my eyes, you look handsome."

    scene splitscreen_aspie_apu

    a "You say that but compared to you I'm honestly just nothing."

    a "I'm a weirdo.."

    e "You're no weirdo, you even helped me and that's something a kind person would do."
    
    e "I think you are very cool, {b}[apu_name]{/b}."

    scene computer_apu_blushing

    a "Do you mean that...?"

    e "Yes, I do."

    scene splitscreen_aspie_apu

    e "I have hurt a lot of people because of my Aspergers and got bullied because of it."

    e "I'm no good either going by that logic."

    a "I didn't even notice to be honest."
    
    a "You truly are amazing though, {b}[aspie_name]{/b}."

    a "Uh... Do you have a..."

    e "Hm?"

    a "A b-boyfriend?"

    e "No."

    e "I don't think there's anyone that would like me back anyw-"

    a "That's not true."
    
    a "You're reserved, gorgeous, kind and you actually care, even towards someone like me."

    scene discord_call_aspie_apu_blushing

    a "Ah, I-I mean... Sorry... That kind of came out by itself."

    e "Hahaha!"

    a "H-Huh..?"

    scene computer_aspie_laughing

    e "You're funny, {b}[apu_name]{/b}."

    scene window_night

    a "And so I kept talking with {b}[aspie_name]{/b} and eventually our days together turned into months."

    scene splitscreen_aspie_apu

    a "So, what are you up to today?"

    e "Not much, I have to go to the store to buy food and other things."

    a "Also, how did the Cosplay event go yesterday?"

    e "It went really great!"
    
    e "So many people complimented the outfit."

    e "Oh, and your tip regarding the skirt really made it look way better!"

    e "Thank you for that."

    a "Ah, it's all you honestly, I just gave some simple feedback."
    
    a "Nothing to thank me for, really."

    e "No, thank you {b}[apu_name]{/b}, you've helped me so much. You're amazing."

    scene discord_call_aspie_apu_blushing

    a "I-I'm not.."

    a "Why do you hang out with me?"

    scene computer_aspie_happy

    e "Because even if you or someone else would think that you aren't amazing or alike, to me you're just that, no matter what."

    scene computer_apu_blushing

    a "I think I like {b}[aspie_name]{/b}.."

    e "I like you too, {b}[apu_name]{/b}."

    scene discord_call_aspie_apu_blushing

    a "I said it out loud?! I-I mean, you like me?"

    e "Yeah, of course, you're my only friend so I do like you."

    scene computer_apu_sad

    a "Oh... Yeah.. I totally meant it that way..."

    e "Is something wrong?"

    a "It's nothing, really."

    scene computer_aspie_happy

    e "Tell me."

    a "You don't want to hear it."

    e "Please?"

    a "I don't know, you wouldn't want to be my friend after this."

    e "Pleaaase?"

    a "Okay.."

    scene computer_apu_sad

    a "I'm in love with you, okay?"

    a "There you go, you've been kind to me and you're my only friend but I had to get feelings and ruin it like this."

    a "I'm sorry for being such a worthl-"

    scene computer_aspie_blushing

    e "I like you too, {b}[apu_name]{/b}."

    e "I don't know much about love but when I spend time with you I get all happy and warm inside."
    
    e "And my heart starts beating really fast!"

    scene discord_call_aspie_apu_blushing

    a "Y-You love me back?"

    e "Mhm, I do."
    
    a "Ah.. Oh.. Um.."

    scene computer_apu_blushing

    a "Am I dreaming?!"

    scene computer_aspie_laughing

    e "You're so funny, {b}[apu_name]{/b}!"

    scene computer_apu_blushing

    a "I-I love you!"

    scene computer_aspie_blushing

    e "I love you too."

    a "I was wondering.."

    scene computer_aspie_happy

    e "Hm?"

    scene computer_apu_happy

    a "Maybe I could come visit for the next Cosplay event?"

    e "That sounds like a great idea, {b}[apu_name]{/b}!"

    scene window_night

    a "We promised to meet a day sometime soon."

    scene window_day

    a "And before we knew it, it was exactly that day."

    # Aspie and Apu finally meet in real life

    scene park_aspie_apu_blushing

    e "Hiii~"

    a "Hello!"

    e "How was the flight here?"

    a "It was okay, anyway, I have a gift for you."

    e "Oh, but I also have a gift for you."

    scene gifts_two

    a "How about we open them at the same time?"

    e "Yeah, that sounds fair."

    a "Okay, One... Two..."

    scene gift_open

    a "Three!"

    a "No way. This figurine..."

    e "Wait..."

    scene figurines_together

    a "We gave each other the same gift!"

    scene aspie_apu_blushing

    a "Hahaha!"

    e "Haha, how does that happen?"

    a "Oh well, how about we go fetch something to eat. You know any nearby places?"

    e "It is a bit simple but there is a WcDonalds just down the street, want to go there?"

    a "Sure!"

    scene wcdonalds_building_top

    e "I'm surprised you were fine with just ordering a hamburger and some fries."

    a "I'm not very hungry honestly, and I usually just order a few hamburgers."

    scene wcdonalds_eating

    e "Mmm... This milkshake is so good~"

    a "What is it with?"

    scene wcdonalds_offer

    e "Vanilla, do you want to taste?"

    a "Uh... Isn't that an indirect kiss?"

    e "I don't mind, we are a couple after all."

    a "Oh, um... Okay."

    scene wcdonalds_apu_slurp

    a "{b}Sluuurp~{/b}"

    a "Mmm..."

    scene wcdonalds_eating

    a "Wow, that's really good!"
    
    a "I haven't had a milkshake in so long, I had kinda forgot how good they taste."

    scene aspie_wcdonalds_blushing

    e "You are cute."

    a "A-Ah, don't tease me!"

    scene wcdonalds_building_top

    e "I love you, {b}[apu_name]{/b}."
    
    a "I-I love you too, {b}[aspie_name]{/b}!"

    e "Well, my milkshake is empty, so..."
    
    e "How about we go home after you finish your hamburger?"

    a "Yeah, let's do that."

    scene aspie_home

    e "Here we are, home sweet home."

    scene aspie_apu_home

    e "Did you bring your Cosplay like I asked of you?"

    a "Yeah, I remembered to bring it along."

    e "Want to take them on and see each others?"

    a "Um, okay."

    e "Go to that corner then I'll go to this one, remember to look away."

    scene home

    a "Let me open my bag real quick."

    a "Hm... Ah, here it is."

    e "You done yet?"

    a "N-No! Give me a bit, it's my second time ever taking it on."

    a "Uh, where's the button?"

    a "Okay, I think I'm ready."

    e "Let's turn around on one."

    a "Okay!"

    e "Three..."

    e "Two..."

    e "And one!"

    scene home_aspie_apu_cosplay

    e "Woah, you look so cool!"

    a "And you look beautiful!"

    e "This is so amazing!"

    e "Hey, {b}[apu_name]{/b}?"

    a "Yeah?"

    e "Can you turn off the light and come here?"

    a "Uh... Sure?"

    scene blackscreen

    a "Okay, where are you?"

    e "Here! Follow my voice."

    a "Uh... Oh, here you are."

    a "So why did we do this?"

    e "So I can do this!"

    a "Hm?"

    scene home_aspie_apu_cosplay_kiss

    e "*Smooch*"

    scene blackscreen

    a "Wow."

    scene yard_aspie_apu_kissing

    a "And that frens, is the story of how Aspie and I got together!"

    a "I'll see you in the next story."
    
    a "Bye!"

    return # This ends the game.

# Animated Images Below

# Why can't you use for loops in animations or did I do something wrong?
image dancingCirno:
    "animations/Cirno/frame_00_delay-0.1s.png"
    pause 0.1
    "animations/Cirno/frame_01_delay-0.1s.png"
    pause 0.1
    "animations/Cirno/frame_02_delay-0.1s.png"
    pause 0.1
    "animations/Cirno/frame_03_delay-0.1s.png"
    pause 0.1
    "animations/Cirno/frame_04_delay-0.1s.png"
    pause 0.1
    "animations/Cirno/frame_05_delay-0.1s.png"
    pause 0.1
    "animations/Cirno/frame_06_delay-0.1s.png"
    pause 0.1
    "animations/Cirno/frame_07_delay-0.1s.png"
    pause 0.1
    "animations/Cirno/frame_08_delay-0.1s.png"
    pause 0.1
    "animations/Cirno/frame_09_delay-0.1s.png"
    pause 0.1
    "animations/Cirno/frame_10_delay-0.1s.png"
    pause 0.1
    "animations/Cirno/frame_11_delay-0.1s.png"
    pause 0.1
    "animations/Cirno/frame_12_delay-0.1s.png"
    pause 0.1
    "animations/Cirno/frame_13_delay-0.1s.png"
    pause 0.1
    "animations/Cirno/frame_14_delay-0.1s.png"
    pause 0.1
    "animations/Cirno/frame_15_delay-0.1s.png"
    pause 0.1
    "animations/Cirno/frame_16_delay-0.1s.png"
    pause 0.1
    "animations/Cirno/frame_17_delay-0.1s.png"
    pause 0.1
    "animations/Cirno/frame_18_delay-0.1s.png"
    pause 0.1
    "animations/Cirno/frame_19_delay-0.1s.png"
    pause 0.1
    "animations/Cirno/frame_20_delay-0.1s.png"
    pause 0.1
    "animations/Cirno/frame_21_delay-0.1s.png"
    pause 0.1
    "animations/Cirno/frame_22_delay-0.1s.png"
    pause 0.1
    "animations/Cirno/frame_23_delay-0.1s.png"
    pause 0.1
    "animations/Cirno/frame_24_delay-0.1s.png"
    pause 0.1
    "animations/Cirno/frame_25_delay-0.1s.png"
    pause 0.1
    "animations/Cirno/frame_26_delay-0.1s.png"
    pause 0.1
    "animations/Cirno/frame_27_delay-0.1s.png"
    pause 0.1
    "animations/Cirno/frame_28_delay-0.1s.png"
    pause 0.1
    "animations/Cirno/frame_29_delay-0.1s.png"
    pause 0.1
    "animations/Cirno/frame_30_delay-0.1s.png"
    repeat



    
