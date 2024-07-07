print('''           M...m...m...M                              M...m...m...M
            MmmmmMmmmmM                                MmmmmMmmmmM
            MMmmMx""xMM                                MMx""xMmmMM
            Mmmmx    xM                                Mx    xmmmM
            MMmmx    xM                                Mx    xmmMM
   ss sss ssMmmmxxxxxxMsss  sss  sss  sss  sss  sss  ssMxxxxxxmmmMss sss sss sss s
   SS SSS SSMMx""xMmmMMSSS  SSS  SSS  SSS  SSS  SSS  SSMMmmMx""xMMSS SSS SSS SSS S
   SSssSSSssMx    xmmmMsssSSsssSSsssSSsssSSsssSSsssSSssMmmmx    xMSSsssSSsssSSsssS
   ssSSsssSSMx    xmmMMss""Sss""Sss""Sss""Sss""Sss""SssMMmmx    xMssSSSssSSSssSSSs
   SSssSSSssMxxxxxxmmmMSx  xSx  xSx  xSx  xSx  xSx  xSSMmmmxxxxxxMSSSssSSSssSSSssS
   ssSSsssSSMMmmMMMmmMMsxxxxsxxxxsxxxxsxxxxsxxxxsxxxxssMMmmMMMmmMMssSSSssSSSssSSSs
   SSssSSSssMmmmmMmmmmMSSsssSSsssSSs".mmm."SSsssSSsssSSMmmmmMmmmmMSSsssSSsssSSsssS
   ssSSsssSSMMmmMMMmmMMssSSSssSSSss"mMMMMMm"sSSSssSSSssMMmmMMMmmMMssSSSssSSSssSSSs
   SSssSSSssMmmmmMmmmmMSSsssSSsssSS.MMMMMMM.SsssSSsssSSMmmmmMmmmmMSSsssSSsssSSsssS
   ssSSsssSSMMmmMMMmmMMssSSSssSSSss.MMMMMMM.sSSSssSSSssMMmmMMMmmMMssSSSssSSSssSSSs
   SSssSSSsmMMMMMMMMMMMmSSSSSSSSSSS.MMMMMMM.SSSSSSSSSSmMMMMMMMMMMMmSsssSSsssSSssss
           MMMMMMMMMMMMM              ..              MMMMMMMMMMMMM           fsc
                                    :.
                                     ":.
                                     .:::.''')
print("You\'re in the start of the maze. ")
choice1 = input('Take a look the building or go inside? Type "look" or "go". ').lower()
if (choice1 == "go"):
    print('''

                           __.--|~|--.__                               ,,;/;
                         /~     | |    ;~\                          ,;;;/;;'
                        /|      | |    ;~\\                      ,;;;;/;;;'
                       |/|      \_/   ;;;|\                    ,;;;;/;;;;'
                       |/ \          ;;;/  )                 ,;;;;/;;;;;'
                   ___ | ______     ;_____ |___....__      ,;;;;/;;;;;'
             ___.-~ \\(| \  \.\ \__/ /./ /:|)~   ~   \   ,;;;;/;;;;;'
         /~~~    ~\    |  ~-.     |   .-~: |//  _.-~~--,;;;;/;;;;;'
        (.-~___     \.'|    | /-.__.-\|::::| //~     ,;;;;/;;;;;'
        /      ~~--._ \|   /          `\:: |/      ,;;;;/;;;;;'
     .-|             ~~|   |  /V""""V\ |:  |     ,;;;;/;;;;;' \
    /                   \  |  ~`^~~^'~ |  /    ,;;;;/;;;;;'    ;
   (        \             \|`\._____./'|/    ,;;;;/;;;;;'      '\
  / \        \                             ,;;;;/;;;;;'     /    |
 |            |                          ,;;;;/;;;;;'      |     |
|`-._          |                       ,;;;;/;;;;;'              \
|             /                      ,;;;;/;;;;;'  \              \__________
(             )                 |  ,;;;;/;;;;;'      |        _.--~
 \          \/ \              ,  ;;;;;/;;;;;'       /(     .-~_..--~~~~~~~~~~
 \__         '  `       ,     ,;;;;;/;;;;;'    .   /  \   / /~
 /          \'  |`._______ ,;;;;;;/;;;;;;'    /   :    \/'/'       /|_/|   ``|
| _.-~~~~-._ |   \ __   .,;;;;;;/;;;;;;' ~~~~'   .'    | |       /~ (/\/    ||
/~ _.-~~~-._\    /~/   ;;;;;;;/;;;;;;;'          |    | |       / ~/_-'|-   /|
(/~         \| /' |   ;;;;;;/;;;;;;;;            ;   | |       (.-~;  /-   / |
|            /___ `-,;;;;;/;;;;;;;;'            |   | |      ,/)  /  /-   /  |
 \            \  `-.`---/;;;;;;;;;' |          _'   |T|    /'('  /  /|- _/  //
   \           /~~/ `-. |;;;;;''    ______.--~~ ~\  |u|  ,~)')  /   | \~-==//
     \      /~(   `-\  `-.`-;   /|    ))   __-####\ |a|   (,   /|    |  \
       \  /~.  `-.   `-.( `-.`~~ /##############'~~)| |   '   / |    |   ~\
        \(   \    `-._ /~)_/|  /############'       |X|      /  \     \_\  `\
        ,~`\  `-._  / )#####|/############'   /     |i|  _--~ _/ | .-~~____--'
       ,'\  `-._  ~)~~ `################'           |o| ((~>/~   \ (((' -_
     ,'   `-.___)~~      `#############             |n|           ~-_     ~\_
 _.,'        ,'           `###########              |g|            _-~-__    (
|  `-.     ,'              `#########       \       | |          ((.-~~~-~_--~
`\    `-.;'                  `#####"                | |           "     ((.-~~
  `-._   )               \     |   |        .       |  \                 "
      `~~  _/                  |    \               |   `---------------------
        |/~                `.  |     \        .     |  O    __.---------------
         |                   \ ;      \             |   _.-~
         |                    |        |            |  /  |
          |                   |         |           |/'  |''')
    print("You meet the Olum, best warrior in the world! you can't do anything.")
    print("Game over")
else:
    print("You visualize a rope that takes you to a hidden place.")
    choice2 = input('Use the rope? Type "yes" or "no". ').lower()
    if (choice2 == "yes"):
        print('''  ___
            . --.`-._^,
            |,;::;-._ `-._
            |`::::`; ;-. `_                             _,^,__
            | ;::::; ::`-. `,                       _,-'.  .. ` ---.____
            ; ;;;;` :::::`.`                      ;  :::` `:; `;;.     `---._
            | : ::' ::::::`.`                    ; .':::'  ;:. `.;;;;;;;;;
            ; :::`, :::::::`.`.     ^          .' /\ :::`, ':::.   `;;; ; ;;;
            : :::::` `;::::::`.`-._ / \   ______;,' ; ::::` :::::::. `.;;;;;;;
            | ::::::; |:::::::`-.   ) ,; '       `.( :::::; `::::::::. `;;;;;
            | ::::::` ::::::::: `   ; `;; ;\  _ _ ;/ ::: :`  ;: ::::::: ;;;;;
            ; ;:::::; |::::::::: )  `-.\( `o}' ` _(   ::: ;  '::::::::: `;;;;
            : ;::::::; ;:: :::::: \              `v'. :::::`; :::::::::`. ;;;;
            | :::::::|  ` :::::::: `.   `-._ `.-._;_; ::::::` `:::::::::: `;;;
            | :::::: :;;, `::::::::.`-.     `.`._`'`'  : :::;  ;:: :::::`. ;;;;
            | ::::::::  :  ;: :::::: .'      `-._;   ; :: ::`  ::::::::::: `;;;
            | ::::::::::`; `.::::::: `.   ::         : ::: ::. `.:::::::::: `;;
            | ;::::::::::: ;::::::::: :.    ;;  ;;  | :::::: `  `;: :::::::: ;;
            `v'.:::::::::: ;:::::::::: :      ;;   .'::::::::`;  ::::::::::: ;'
                ~~~`.::::: ;:::::::::: |           : :::::::::`. `::::::::/`v'
                    \:: .,;:::::::   _;'    :;;  .'_ ;;:::::::;  ,:::,'
                    ~\ ;;::::::: ,-',-':   `    :-.`_  ::::::`. ;;,-'
                    | ;--.::::: ;;  .:`.       ;..`.`. ;::::::  /
                    `v'    `-.; :; .... `------ ...`.: ,-'    : ;
                                )|| . ......; ;  ... :|/       `v
                                __;| .... ...; ` .... :|
                                ((c-.`._ .... `.`. . . ;`-.__
                                ""   `' `. ....`.`; .. ))~`-))
                                        `-. . ;.'. ,/"    ""
                                            `._ Y ,/
                                                \`/
            ''')
        print("You face a big bat!")
        choice3 = input("What do you gonna do? Type \"run\", \"fight\" or \"cry\". ").lower()
        if choice3 == "run":
            print("You run but is dark and you fall in a hole")
            print("Game over")
        elif choice3 == "cry":
            print("The bat is crying as well. You found a new friend! and He tell you where is the real treasure")
            print("You win!")
        else: 
            print("You use your magic powers but you get bitten")
            print("Game over")
    else:
        print("You still stand up for hours, thinking what to do. You decide to use your magic powers to teleport directly to the treasure. ")
        print(r"""
                            _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!      -._'-.
           \'.  ||:::::.-!           -'_.|
            '.'-;|:.-'             o.'\U||
              `>'-.!        .-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-\U/.-'    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
                '-._'-.|| |' `_.-'
                    '-.||_/.-
            """)
        print("But it\'s a trap!")
        print("Game over")