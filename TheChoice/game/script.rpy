image calle = "calle.jpg"
image pressRoom = "Assets/Intro/PressRoom/intro.png"
image servicio = "Assets/Intro/EscenaPolicias/Intro3.png"
image sala4 = "sala4.png"
image manifestacion = "Mani.png"
image tertulia = "tertulia.png"
image sala1 = "bar_prueba2.png"
image sala3 = "sala3.png"
image Collins Saludando = "Assets/Collins/sala1/Poses/BocaCerradaSaludo.png"
image Collins Casual = "Assets/Collins/sala1/Poses/BocaCerradaCasual.png"
image Collins Casual2 = "collins_sala2.png"
image Collins Dudoso = "collins3_dudoso.png"
image Collins Casual3 =  "Collins_causal3.png"
image Collins Casual4 = "CollinsCasual4.png"
image Collins Dudoso4 = "collins4_dudoso.png"
image casa = "sala2.png"
image noticias = Movie(play="noticias.webm", size=(1920,1080),)
define click = "audio/click.mp3"
define d = Character("Collins")

label start:#
    $ androide_confiado = 0
    $ humano_sospechoso = 0
    $ androide_sospechoso = 0
    $ humano_confiado = 0
    $ personaje = True
    $ robot = False
    stop music

    transform alpha_dissolve:
        alpha 0.0
        linear 0.5 alpha 1.0
        on hide:
            linear 0.5 alpha 0
        # This is to fade the bar in and out, and is only required once in your script

    screen countdown:
        timer 0.01 repeat True action If(time > 0, true=SetVariable('time', time - 0.01), false=[Hide('countdown'), Call(timer_call)])

        if time > 1:
            bar value time range timer_range xalign 0.5 yalign 0.9 xmaximum 300 left_bar "#000000" right_bar "#807e7e" at alpha_dissolve # This is the timer bar.
            text str(time) xalign 0.5 yalign 0.9 color "#ffffff" at alpha_dissolve

        elif time>0.1:
            bar value time range timer_range xalign 0.5 yalign 0.9 xmaximum 300 left_bar "#000000" right_bar "#6e1818" at alpha_dissolve # This is the timer bar.
            text str(time) xalign 0.5 yalign 0.9 color "#ff1100" at alpha_dissolve

    init:# time = the time the timer takes to count down to 0.
        $ timer_range = 0 # timer_range = a number matching time (bar only)
        $ timer_call = 0 # timer_call = the label to call to when time runs out

    scene calle
    "Es el año 2632. Los androides son una parte esencial de la sociedad."
    "Forman parte de tareas como construcción, transporte, tareas del hogar. Pero solo son vistos como herramientas sin ningún prospecto de que eso cambie. "

    scene pressRoom
    "Hace tres días que se ha descubierto que la presidenta no era humana sino una androide."
    "Las ramificaciones de este acontecimiento aún no están definidas."

    scene servicio
    "Se han iniciado pequeñas manifestaciones en la ciudad debido a este descubrimiento"
    " ¿cómo ha llegado el androide a presidente?"
    scene manifestacion
    " ¿quién lo puso ahí?"
    " ¿ha sido capaz de engañarnos a todos y que nadie se diera cuenta? o lo que es peor, ¿hay más como él?"

    scene tertulia
    "A causa de esto están surgiendo distintas corrientes de pensamiento sobre cómo juzgar lo ocurrido."
    "Hay quienes quieren respuestas y justicia, otros sienten miedo ante lo que aún podría quedar por descubrir y algunos argumentan que el hecho de que sea un androide no debería ser motivo de preocupación."

    scene black
    "Elige tu personaje"
    menu:
        "Humano":
            play sound click
            $ personaje = True
        "Androide":
            play sound click
            $ personaje = False

    $ player_name = renpy.input("Enter name")
    $ player_name = player_name.strip()
    if player_name == "":
        $ player_name = "Alan Quim González"
label sala1:

    scene sala1
    play music "audio/Bar.mp3" fadein 2 fadeout 2
    show Collins Saludando
    d "Buenas, soy el detective Collins, ¿es usted ..."
    menu:
        "Emm… [player_name].": #humano
            play sound click
            $ humano_sospechoso +=1
            hide   Collins Saludando
            show Collins Casual
            d "Tranquilo hombre, como habrá oído, estamos investigando el caso de la presidenta, hemos hecho un descanso en la investigación y he venido a por una copa. Y usted, ¿qué hace aquí?"

        "[player_name], ¿qué quiere?": #androide
            play sound click
            $ androide_confiado +=1
            hide   Collins Saludando
            show Collins Casual
            d "Tranquilo hombre, como habrá oído, estamos investigando el caso de la presidenta, hemos hecho un descanso en la investigación y he venido a por una copa. Y usted, ¿qué hace aquí?"

        "Afirmativo":
            play sound click
            $ androide_sospechoso +=1
            hide   Collins Saludando
            show Collins Casual
            d "Tranquilo hombre, como habrá oído, estamos investigando el caso de la presidenta, hemos hecho un descanso en la investigación y he venido a por una copa. Y usted, ¿qué hace aquí?"


        "Soy [player_name], ¿Nos conocemos?":
            play sound click
            $ humano_confiado +=1
            hide   Collins Saludando
            show Collins Casual
            d "Todavía no, como habrá oído, estamos investigando el caso de la presidenta, hemos hecho un descanso en la investigación y he venido a por una copa. Y usted, ¿qué hace aquí?"

    menu:
        "He quedado con alguien y como he llegado pronto estoy haciendo tiempo.":
            play sound click
            $ humano_confiado +=1
        "Me apetecía una copa y he venido, ¿a qué viene tanta pregunta?":
            play sound click
            $ humano_sospechoso +=1
        "He venido a buscar refrigerante para mi aparato digestivo y a la vez estimularme.":
            play sound click
            $ androide_sospechoso +=1
        "Estaba paseando y he decidido tomar un café en el sitio más cercano.":
            play sound click
            $ androide_confiado +=1

    d "Perdona, ¿te estoy incomodando?, no puedo dejar la profesión ni para tomar un café jaja"
    $ time = 10                                    ### set variable time to 3
    $ timer_range = 10                             ### set variable timer_range to 3 (this is for purposes of showing a bar)
    $ timer_call = 'respuestaRapida'               ### set where you want to jump once the timer runs out
    show screen countdown                          ### call and start the timer
    play music "audio/tic_tac.mp3" fadein 2
    menu:
        "No tranquilo… ja ja…":
            play sound click
            stop music
            hide screen countdown                  ### stop the timer
            $ humano_sospechoso +=1
        "No no, perdón por la sequedad, un mal día.":
            play sound click
            stop music
            hide screen countdown                  ### stop the timer
            $ androide_confiado +=1
            d "¡Qué me dices!, ¿qué ha pasado?"
            menu:
                "Eeeeh… Nada nada, he dormido mal, en el trabajo me he llevado bronca… En fin… ":
                    play sound click
                    $ humano_sospechoso +=1
                "Nada importante, pequeñas tonterías acumuladas…":
                    play sound click
                    $ androide_confiado +=1
        " Tranquilo, a todos nos ocurre lo mismo hoy en día con lo que está ocurriendo":
            play sound click
            stop music
            hide screen countdown                  ### stop the timer
            $ humano_confiado +=1

    d "Bueno, dejo de molestarle más, adiós, y alegre esa cara!"

    menu:
        "(Con una sonrisa torcida) ¡Adiós!":
            play sound click
            $ humano_sospechoso +=1
        "(Cara seria) Adiós.":
            play sound click
            $ androide_confiado +=1
        "(Sonríe rápidamente y de forma brusca) ¡Como desee!":
            play sound click
            $ androide_sospechoso +=1
        "(Sonriendo normal) ¡No me ha molestado para nada! Que tenga un buen dia":
            play sound click
            $ humano_confiado +=1
    stop music


label sala2:

    show noticias:
        xpos 0 ypos 0
    "Con el paso de los días las manifestaciones han crecido y se han ido violentando, las personas quieren respuestas y el gobierno no las da."
    "Por otro lado, la presidenta ya ha sido destituida y se celebrarán elecciones en dos semanas, donde se asegurará que los candidatos sean humanos."
    scene black
    "Han llamado a la puerta, es el detective Collins, el del otro día, quiere hablar, entra en tu casa."
    scene casa
    show Collins Casual2
    d "Gracias por dejarme pasar, no se preocupe, es una pequeña entrevista rutinaria, se lo estamos haciendo a mucha gente."
    menu:
        "Entrevista… ¿Sobre qué?":
            play sound click
            $ humano_sospechoso +=1
            d "Supongo que está usted al día de las noticias, las manifestaciones son cada vez más multitudinarias…"
            d " ¿Ha ido usted a alguna?"

        "¿A qué se debe la invasión de mi perímetro? ":
            play sound click
            $ androide_sospechoso +=1
            d "Supongo que está usted al día de las noticias, las manifestaciones son cada vez más multitudinarias…"
            d " ¿Ha ido usted a alguna?"

        "Tranquilo, ningún problema. ¿Quiere agua, un café…?":
            play sound click
            $ humano_confiado +=1
            d "No gracias, me acabo de tomar un café en la comisaría. Supongo que está usted al día de las noticias, las manifestaciones son cada vez más multitudinarias…"
            d "¿Ha ido usted a alguna?"
    menu:
        " Sí, necesitamos explicaciones.":
            play sound click
            $ humano_confiado +=1
            d "Con que explicaciones… ¿Cómo cree usted que la presidenta nos ha podido engañar todo este tiempo?"
            menu:
                "No lo se. Y como debería saberlo yo? ¡No soy uno de esos androides!":
                    play sound click
                    $ humano_sospechoso +=1

                "¿Quién sabe? Se camuflan muy bien. Por lo que yo se usted podría ser uno.":
                    play sound click
                    $ humano_confiado +=1

                "Es muy simple imitar el aspecto de los seres humanos.":
                    play sound click
                    $ androide_sospechoso +=1

                "Es una cuestión muy compleja, siento no poder serle de más ayuda.":
                    play sound click
                    $ androide_confiado +=1

        "Emmm… No… Yo no estoy de acuerdo con estas manifestaciones. ":
            play sound click
            $ humano_sospechoso +=1
        "El acto de manifestación no es una forma lógica de conseguir resultados. ":
            play sound click
            $ androide_sospechoso +=1
        "No, pero lo he considerado.":
            play sound click
            $ androide_confiado +=1

    if personaje == False:
        d "Entiendo, veo que usted vive en un piso muy acogedor. Veo que no tiene fotografías, no es muy habitual si me lo permite."
        menu:
            "¿Usted cree? Yo he estado en muchas casas sin fotografías (mira nervioso por toda la casa al percatarse de que no tiene fotografías)":
                play sound click
                $ humano_sospechoso +=1

            "La verdad es que no me considero fotogénico.":
                play sound click
                $ humano_confiado +=1

            "No le veo la necesidad cuando puedo acceder a mi memoria para recordar los eventos.":
                play sound click
                $ androide_sospechoso +=1

            "Prefiero tenerlas en la nube y verlas en el ordenador.":
                play sound click
                $ androide_confiado +=1
    d "Bueno, tengo que irme a hacer más entrevistas rutinarias, gracias por su tiempo y tenga mi contacto, por si se entera de algo que pueda sernos de ayuda. ¡Nos vemos!"
    menu:
        "(Abriendo los ojos) ¡Adiós! ":
            play sound click
            $ humano_sospechoso +=1

        "(Con cara pensativa) Claro, por supuesto, ¡adiós!":
            play sound click
            $ humano_confiado +=1

        "(Inexpresivo) Adiós.":
            play sound click
            $ androide_sospechoso +=1

        "(Con cara pensativa) Como desee, ¡adiós! ":
            play sound click
            $ androide_confiado +=1

    show noticias:
        xpos 0 ypos 0
    "La situación en las calles es de caos absoluto."
    "Las manifestaciones se han convertido en acampadas violentas de gente que ocupan toda la calle principal, llevan ya una semana acampando."
    "Esto es debido a los sucesos de las elecciones, donde unos encapuchados bastante organizados entraron en varios colegios electorales a la vez impidiendo el voto de las personas."
    "Aún está por determinar la identidad de estos encapuchados y si son androides o humanos."
    hide noticias
    show black
    "El detective Collins te ha citado en comisaría."
    scene sala3
    show Collins Casual3
    d"Le hemos citado aquí porque le hemos visto en una de esas acampadas violentas que está haciendo la gente por toda la ciudad,  quemando contenedores, rompiendo escaparates, tirando piedras a los policías… "
    d "¿Qué pretenden conseguir con tanta violencia?"

    menu:
        "(Nervioso) Bueno… Tampoco… Yo no… ":
            play sound click
            $ humano_sospechoso +=1
            hide Collins Casual3
            show Collins Dudoso
            d "¡Déjese de tartamudeos! ¿Por qué estuvo en la manifestación?"
            menu:
                " (Con voz temblorosa) ¡Unos amigos me obligaron a ir! ":
                    play sound click
                    $ humano_sospechoso +=1

                " ¡Yo no hice nada! Solo estaba manifestándome cuando no se quien empezó a liarla.":
                    play sound click
                    $ humano_confiado +=1

                " Lo que queremos es votar, la violencia no es cosa nuestra.":
                    play sound click
                    $ androide_sospechoso +=1
            show Collins Casual3

        "(Alterado) ¡Explicaciones! Pensábamos que votando podríamos solucionar algo pero no nos dejaron y nadie dice ni hace nada!":
            play sound click
            $ humano_confiado +=1

        "(Monótono) Los androides no pueden dañar a los seres humanos… ":
            play sound click
            $ androide_sospechoso +=1

        "(Relajado) No participé en la violencia, aunque deberían haber explicaciones de por qué no podemos votar. ":
            play sound click
            $ androide_confiado +=1

    d "Y dígame… ¿cuál es su opinión acerca del uso o posesión de androides para los trabajos que los humanos no queremos hacer?"
    menu:
        "Bueno… Los creamos para eso, ¿no?":
            play sound click
            $ humano_sospechoso +=1

        "Nos facilitan mucho la vida, aunque también nos quitan puestos de trabajo y generan pobreza.":
            play sound click
            $ humano_confiado +=1

        "Es para lo que los androides fueron creados.":
            play sound click
            $ androide_sospechoso +=1

        "Supongo que ayudan, aunque se les podría tener en más consideración. ":
            play sound click
            $ androide_confiado -=1
    d " Y sobre la presidenta, ¿qué opina?"

    menu:
        "Que no sabemos cómo ha llegado ahí, y si son capaces de pensar por sí mismos, y si están entre nosotros y no lo sabemos, y si… (empieza a hiperventilar)":
            play sound click
            $ humano_sospechoso -=1

        "La verdad es que hizo una gran labor, aunque eso no quita el hecho de que nos engañó a todos.":
            play sound click
            $ humano_confiado +=1

        "Esa no es la función de un androide.":
            play sound click
            $ androide_sospechoso +=1

        " No sabemos cómo lo consiguió, pero su intención era buena, lo sé. ":
            play sound click
            $ androide_confiado -=1
            d " Con que lo sabe… No será usted cercano a la presidenta o a alguien de su círculo íntimo, ¿no?"
            menu:
                "¿QUÉ? Nonono… ":
                    play sound click
                    $ humano_sospechoso +=1

                " No, aunque me gustaría, así al menos tendría respuestas.":
                    play sound click
                    $ humano_confiado +=1

                "(Cara de duda) ":
                    play sound click
                    $ androide_sospechoso +=1

                "Por desgracia no, pero sería interesante.":
                    play sound click
                    $ androide_confiado -=1

    hide Collins Casual3
    show Collins Dudoso
    d "De acuerdo, puede irse, pero quédese en casa y no salga del país. Le estaremos vigilando."
    menu:
        "(Con la voz entrecortada y susurrando) De acuerdo. ":
            play sound click
            $ humano_sospechoso +=1

        "(Serio y sin mirarle a la cara) De acuerdo.":
            play sound click
            $ humano_confiado +=1

        "(Inexpresivo) De acuerdo.":
            play sound click
            $ androide_sospechoso +=1

        "(Mirándole a los ojos) De acuerdo. ":
            play sound click
            $ androide_confiado +=1

    show noticias:
        xpos 0 ypos 0
    "Por fin se ha conocido la identidad de los encapuchados, era un grupo de androides que pedían la igualdad y ser considerados humanos. "
    "Gracias a las nuevas leyes propuestas por el nuevo presidente, elegido de manera muy democrática, los androides fueron apagados ayer, junto con los androides descubiertos entre los manifestantes de las protestas."
    "Gracias a nuestro nuevo presidente, las calles y las personas vuelven a estar seguras."
    hide noticias
    show black
    "Te han venido a buscar a casa. Te vendan los ojos y te meten en un coche. No sabes dónde te están llevando. Tienes miedo."
    scene sala4
    show Collins Casual4
    d" ¿Por qué no intentó escapar? Viendo cómo están las cosas… "
    menu:
        " Yo no he… Usted…":
            play sound click
            $ humano_sospechoso +=1

        "No he hecho nada malo, usted como detective me dijo que no me fuera y confié en usted.":
            play sound click
            $ humano_confiado +=1

        "Me dio la orden de no marchar. ":
            play sound click
            $ androide_sospechoso +=1

        "No he hecho nada.":
            play sound click
            $ androide_confiado +=1
    show Collins Dudoso4
    d "Dejémonos de rodeos, ¿qué modelo eres?, ¿quién te ha fabricado?"
    menu:

        " (Llorando) ¿QUÉ? No, no… Yo no soy… ":
            play sound click
            $ humano_sospechoso -=1
            $ robot = False

        "(Alterado) No soy un androide, mi nombre es [player_name], ya se lo dije.":
            play sound click
            $ humano_confiado +=1
            $ robot = False

        "Soy el modelo AX483Z5G, mi creadora es la señora Emily Smith.":
            play sound click
            $ androide_sospechoso +=1
            $ robot = True
            d "¿Qué tramais los androides?"

        "(Desafiante) Ya sabe mi nombre. ":
            play sound click
            $ androide_confiado +=1
            $ robot = False
    if robot == False:
        d "¿Cómo lo haces para aparentar ser humano? ¿Te han enseñado o es algo que “surge” dentro de vosotros?"
        menu:
            "  (Llorando desconsoladamente) SOY un humano, no lo aparento, por favor, ¡sacadme de aquí!":
                play sound click
                $ humano_sospechoso -=1

            "(Muy alterado) ¿Qué dices? no lo aparento, ¡lo soy!":
                play sound click
                $ humano_confiado +=1

            "(Desafiante) No sé de qué me habla.":
                play sound click
                $ androide_confiado +=1

        d " ¡Corta el rollo! ¿Qué es lo que estáis tramando?"

    menu:
        "(Hiperventilando y llorando) ¡No lo sé! ¡Por favor, dejadme salir de aquí! ¡AYUDAAAA!":
            play sound click
            $ humano_sospechoso -=1
            $ robot = False

        "(Muy alterado) ¡No lo sé! ¡¿Cuántas veces tengo que decirte que no soy un androide?! ":
            play sound click
            $ humano_confiado +=1
            $ robot = False

        "No tengo esa información en mi base de datos. ":
            play sound click
            $ androide_sospechoso +=1
            $ robot = True
            d "¿Qué tramais los androides?"

        "(Desafiante) No lo sé, pero viendo como los estáis tratando… Seguro que solo quieren igualdad.":
            play sound click
            $ androide_confiado -=1
            $ robot = False

label final:
    scene black
    if androide_confiado > 5 & personaje == False:
        "Eres androide, te salvan porque les vas a dar información sobre los otros androides, traicionas a los tuyos para protegerte a ti mismo."

    if androide_confiado > 5 & personaje == True:
        "Eres humano, te matan aunque saben que no eres androide porque en realidad la existencia de los androides es mentira y es un complot para exterminar a gran parte de la humanidad."

    if humano_sospechoso >5 &  personaje == False:
        "Eres androide, te matan."

    if humano_sospechoso >5 &  personaje == True:
        "Eres un humano, lo haces fatal pareces un androide y te matan."

    if humano_confiado >5 &  personaje == False:
        "Eres androide, te salvas porque pareces un humano."

    if humano_confiado >5 &  personaje == True:
        "Eres un humano, te salvas."

    if androide_confiado> 5 & personaje == False:
        "Al final te descubrem pero te perdonan la vida."

    if androide_confiado> 5 & personaje == True:
        "Los androides se han alzado y estaban mirando si eres de los suyos."
return


label respuestaRapida:
    stop music
    play sound "audio/ring.mp3"
    d "Vaya estas tardando mucho en constestar no?"
