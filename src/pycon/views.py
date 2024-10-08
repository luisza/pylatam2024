from django.shortcuts import render
from django.utils.translation import activate
from django.utils.translation import gettext as _

def home(request, lang='es'):
    activate(lang)
    keynote_speakers = [
        # { 'name': 'Lorena Mesa',
        #  'description': _("A political analyst turned coder, also teach Python at University of Chicago in their Masters of Computer Science program"),
        #  'image': 'Lorena Mesa.jpg'
        #  },
        { 'name': 'Ariel Ortiz',
         'description': _('Professor at Tecnológico de Monterrey, Python expert, and international speaker.'),
         'image': 'Ariel Ortiz.jpg'
         },
        { 'name': 'Abigail Messreyames',
         'description': _('Open Source Programs Manager, researcher, and community builder with a focus on DEI in leadership.'),
         'image': 'Abigail Mesrenyame Dogbe.jpg' },
         { 'name': 'Bea Gandica',
         'description': _('Program Manager at Microsoft and founder of Nuevo Foundation, focused on Azure billing and community education.'),
         'image': 'Bea Mendez Gandica.jpeg' },
         
    ]
    context = {'data': keynote_speakers}
    return render(request, 'home.html', context)

def conduct(request, lang='es'):
    activate(lang)
    return render(request, 'conduct.html')

def tickets(request, lang='en'):
    activate(lang)
    return render(request, 'tickets.html')

def team(request, lang='es'):
    activate(lang)
    team_members = {
        'organizing_team': {
            'title': _('Equipo de Organización'),
            'members': [
                {
                    'name': 'Gabriela Villarreal',
                    'bio': _('Gabriela es psicopedagoga amante de la literatura y la cocina. Con más de 12 años de experiencia en la comunidad de Python, ha sido una activa colaboradora del equipo organizador de Python Monterrey. Desde 2019, ha desempeñado un rol destacado como organizadora de PyCon Latam. Su compromiso con la educación y la tecnología se refleja en su continuo esfuerzo por fomentar el desarrollo y la inclusión en la comunidad.'),
                    'photo': 'Gabriela-Villarreal.jpg',
                    'role': _('Psicopedagoga')
                },
                {
                    'name': 'Denny Perez',
                     'bio': _('Denny es Analista de QA de Software con un título en contabilidad, apasionada por la diversidad e inclusión en comunidades tecnológicas. Como manejadora de comunidades Python y Directora de la PSF desde 2023, empodera a las comunidades de habla hispana a través de PyLadies, organizando eventos diversos y mentorando dentro de la comunidad Python para promover un ambiente inclusivo.'),
                    'photo': 'denny-perez.png',
                    'role': _('Analista de QA de Software')
                },
                {
                    'name': 'Paul Barajas',
                      'bio': _('Es un apasionado de la tecnología de código abierto. Trabaja en un producto que demuestra cómo el código abierto puede impulsar nuevas tecnologías en sectores no industrializados, como la acuicultura. También es conferencista, motivando a las futuras generaciones a entender y utilizar el software de código abierto.'),
                    'photo': 'paul-barajas.jpeg',
                },
                {
                    'name': 'Luis Zárate',
                     'bio': _('Es desarrollador Python con más de 14 años de experiencia en la realización de proyectos por demanda para diversas empresas. Es fundador de Solvosoft y creador de proyectos como Gentelella Widgets y Organilab. Además, es colaborador del proyecto xhtml2pdf y ha sido profesor universitario en la Universidad de Costa Rica.'),
                    'photo': 'luis-zarate.jpg'
                },
                {
                    'name': 'Ronald Perez',
                     'bio': _('Es profesor de Informática en la Universidad de Costa Rica. Durante su doctorado, trabajó con Python para la limpieza y análisis de datos generados por cursos masivos en línea. Actualmente, coordina un grupo de investigación en Python, cuyo objetivo es introducir a los estudiantes universitarios en el desarrollo de aplicaciones con este lenguaje. Cuenta con experiencia en la organización de actividades como congresos internacionales, habiendo participado en eventos como Drupal Camp y el Encuentro Centroamericano de Software Libre.'),
                    'photo': 'ronald-perez.jpg'
                },
                {
                    'name': 'Ivone Corona',
                     'bio': _('Es una psicóloga apasionada del psicoanálisis y entusiasta de la tecnología. Durante casi 10 años, ha combinado su interés por comprender a las personas con el mundo del desarrollo de software, trabajando en reclutamiento y recursos humanos en esta industria. Siempre está emocionada por aprender y contribuir.'),
                    'photo': 'ivone-corona.jpeg'
                },
                {
                    'name': 'Andres Pineda',
                    'bio': _('Desarrollador de software con una pasión el UI. Especializado en la construcción de aplicaciones accesibles. Cree fuertemente en el poder de la colaboración y el intercambio de conocimiento para impulsar el crecimiento colectivo.'),
                    'photo': 'andres-pineda.jpeg'
                },
            ]
        },
        'volunteering': {
            'title': _('Voluntariado'),
            'members': [
                {
                    'name': 'Ashley Rojas',
                     'bio': _('Estudiante autodidacta de Informática y Tecnología Multimedia en la Universidad de Costa Rica. Apasionada por la tecnología y el diseño, está aprendiendo Python de manera autodidacta. Con un firme interés en integrarse más en la comunidad tecnológica, busca participar en proyectos innovadores que combinen tecnología y creatividad.'),
                    'photo': 'ashley-rojas.jpeg'
                },
                {
                    'name': 'Jeremy Guzmán',
                    'bio': _('Estudiante de Informática en la Universidad de Costa Rica, actualmente centrado en el desarrollo web con Django. Disciplinado y con una gran curiosidad por aprender nuevas tecnologías, busca involucrarse en proyectos colaborativos y contribuir con sus habilidades para crear soluciones innovadoras.'),
                    'photo': 'jeremy-guzman.jpeg'
                },
                {
                    'name': 'Juan Gabriel Camacho',
                    'bio': _('Estudiante de la carrera Informática y Tecnología Multimedia en la Universidad de Costa Rica, apasionado por el desarrollo de software y backend, autodidacta en el lenguaje de Python. Busca involucrarse en un ambiente laboral profesional para el desarrollo de proyectos innovadores.'),
                    'photo': 'juan-camacho.JPG'
                },
            ]
        }
    }
    context = {'team': team_members}
    return render(request, 'team.html', context)

def scheduled(request, lang='es'):
    activate(lang)
    speakers = {
        '1': {
        'name': _('Todos los asistentes'),

        },
        '2': {
            'name': _('Personal administrativo')
        },
        '3': {
            'name': 'Lorena Mesa',
            'biography': _("Political scientist turned coder, Lorena Mesa is a data engineer, former Director & Chair of the Python Software Foundation, JOSS editor, and PyLadies Chicago co-organizer. Lorena's time at Obama for America and her subsequent graduate research required her to learn how to transform messy, incomplete data into intelligible analysis on topics like predicting Latinx voter behavior. It's this unique background in research and applied mathematics that drove Lorena to pursue a career in engineering and data science. One part activist, one part Star Wars fanatic, and another part Trekkie, Lorena abides by the motto to \"live long and prosper\""),
            'photo': 'Lorena Mesa.jpg'
        },
        '4': {
            'name': 'Nadia Ayala Hernandez',
            'email': 'nadiaayalah7@gmail.com',
            'biography': _('En un mundo donde la tecnología avanza a pasos agigantados, a Nadia Ayala Hernandez le apasiona descubrir cómo esta puede ser utilizada para mejorar la vida de las personas. Con más de tres años de experiencia en el ámbito del desarrollo de software, incluyendo el área de robots de software, se ha consolidado como una experta en la automatización de procesos. Su mayor satisfacción es presenciar el impacto positivo que los robots de software han tenido en las personas que los utilizan. Ha visto cómo estas herramientas han liberado tiempo, reducido el estrés y mejorado la calidad de vida de sus clientes.'),
            'photo': 'Nadia Ayala Hernandez.jpg'
        },
        '5': {
            'name': 'Oscar Cortez',
            'email': 'om.cortez.2010@gmail.com',
            'biography': _('Oscar, nacido en Nicaragua y radicado en Colombia, es un Ingeniero de Software que se especializa en la construcción de aplicaciones de alto rendimiento utilizando Python, Go y Rust. Con experiencia en ciberdefensa, datos abiertos, agricultura e inteligencia artificial, aporta perspectivas diversas de la industria a su código. Cuando él no está detrás de una sesión de tmux, Oscar empodera a otros desarrolladores a través de mentorías y encuentros, fomentando un ecosistema tecnológico vibrante e inclusivo en Nicaragua y más allá.'),
            'photo': 'Oscar Cortez.jpg'
        },
        '6': {
            'name': 'Gerardo Vilcamiza',
            'email': 'gerardo.vilcamiza@ieee.org',
            'biography': _('Gerardo Vilcamiza es Ingeniero Mecatrónico por la Universidad Peruana de Ciencias Aplicadas (UPC), donde se desempeña como investigador en el fascinante mundo de los satélites y la Visión Computacional. Actualmente, está finalizando una Maestría en Inteligencia Artificial en la Universidad de Buenos Aires, ampliando sus horizontes en esta revolucionaria área. Durante los últimos 4 años, ha combinado su pasión por enseñar y su experiencia en el campo tecnológico como docente de programación en Python, enfocado en Machine Learning, Procesamiento Digital de Señales y Robótica en institutos reconocidos de Perú. Además, en los últimos 3 años ha trabajado como Data Scientist y AI Engineer en una empresa multinacional, roles que le han permitido diseñar e implementar soluciones innovadoras en la industria. Su compromiso con la divulgación tecnológica lo ha llevado a compartir sus experiencias en diversos eventos académicos y profesionales, incluyendo charlas en congresos de IEEE en Perú, México y Colombia, ponencias en eventos empresariales para la industria tecnológica y participaciones destacadas como speaker en la comunidad de Python, en los Python Meetups Perú, PyDay Perú 2023 y Pycon Colombia 2024.'),
            'photo': 'Gerardo Vilcamiza.png'
        },
        '7': {
            'name': 'Fernanda Ochoa',
            'email': 'monsh8a@gmail.com',
            'biography': _('Fernanda Ochoa es Directora de Producto y Tecnología en Dalia Empower. Trabajó como Sherpa Digital de Data Science y Cloud Computing con Innovacción Virtual en Microsoft, así como Program Manager de Asistentes Inteligentes en Hackademy. Fernanda tiene una pasión por la producción de eventos, productora y host de 2 temporadas de LatinXperts un show para GitHub Education en Twitch, donde obtuvo los primeros lugares en los shows más vistos de Twitch. Tiene una amplia experiencia en diferentes industrias a nivel internacional.\n Fernanda Ochoa es conocida por su visión e innovación que ha reflejado en diversos proyectos que ha liderado. Está comprometida con la construcción de comunidades a través de la participación y la capacitación significativa que ayudan a los estudiantes a aprender, crecer y capacitar a otros en las tecnologías de nube. Es una coach y mentora enérgica y centrada en la cultura que proporciona una orientación clara a sus estudiantes.'),
            'photo': 'Fernanda Ochoa2.jpeg'
        },
        '8': {
            'name': 'Adolfo Fitoria',
            'email': 'adolfo.fitoria@gmail.com',
            'biography': _('Desarrollador de software originario de Managua, Nicaragua. Miembro de la comunidad de software libre de Nicaragua. Actualmente trabaja como desarrollador web con tecnologías Python/Django con más de 10 años de experiencia.'),
            'photo': 'Adolfo Fitoria2.jpg'
        },
        '9': {
            'name': 'Kevin Jahaziel Leon Morales',
            'email': 'jahaziel.lem@gmail.com',
            'biography': _('Es un apasionado desarrollador en Electronic Cats y PwnLabs. Con un gran interés en la ciberseguridad y el hardware, ha enfocado su perfil profesional en el desarrollo de firmware y en la realización de pruebas de penetración a dispositivos electrónicos IoT. Esta apasionante trayectoria le ha brindado la oportunidad de adentrarse en una amplia gama de tecnologías y de adquirir conocimientos en diversas áreas. Desde sus primeros días en Electronic Cats, se ha dedicado con entusiasmo a explorar los desafíos y las posibilidades que ofrece el mundo del hardware libre, contribuyendo así al desarrollo y la innovación en el campo de la tecnología. Está comprometido con su crecimiento profesional continuo y con seguir aprendiendo y creando soluciones innovadoras en el emocionante mundo de la tecnología y la ciberseguridad.'),
            'photo': 'Kevin Leon Morales.jpg'
        },
        '10': {
            'name': 'Eduardo Ramirez Rangel',
            'email': 'eduardo@ensitech.com',
            'biography': _('Eduardo H. Ramírez, Ph.D. es Doctor en Sistemas Inteligentes. Co-fundador y director de Inteligencia Artificial de Ensitech, empresa mexicana con presencia en Estados Unidos y América Latina. Ex-colaborador de Yahoo! Research y Microsoft Research. Fundador de la comunidad de Ciencia de Datos en Monterrey, miembro del Consejo de la Carrera de Matemáticas y Ciencia de datos del Tec de Monterrey y miembro del consejo de de Saturdays.AI, una iniciativa global de formación en Inteligencia artificial con impacto social. Es docente en el Tecnológico de Monterrey, la Escuela Superior Politécnica del Litoral en Ecuador y Neuromatch Academy. Es colaborador en revistas como Forbes y Software Gurú.'),
            'photo': 'Eduardo Ramirez.jpg'
        },
        '11': {
            'name': 'Angel Serrano',
            'email': 'angelserranogs@gmail.com'
        },
        '12': {
            'name': 'Osiel Jacobo Torres',
            'email': 'osiel.torres@mercadolibre.com.mx',
            'biography': _('Osiel Torres es Software Engineer de Cloud and Platform en Mercado Libre e Ingeniero en Tecnologías Computacionales por el Tecnológico de Monterrey. Con cinco años de experiencia gestionando aplicaciones Django en Kubernetes, Osiel es un apasionado de Python desde 2017. Le entusiasma compartir conocimientos a través de la escritura y cree firmemente que los grandes proyectos y startups se construyen sobre una buena cultura.'),
            'photo': 'Osiel Torres.png'

        },
        '13': {
            'name': 'Carlos Giles',
            'email': 'carlosgiles49@gmail.com',
            'biography': _('Carlos Giles es Ingeniero de Datos en DaliaEmpower con una sólida formación académica en Ingeniería Eléctrica y Electrónica por la UNAM, e Ingeniería en Sistemas Computacionales por la UVEG. Además, ha completado un diplomado en Uso y Aplicación de Energías Renovables en la Universidad Politécnica de Catalunya y está certificado por CONOCER en la instalación de sistemas fotovoltaicos para residencias, comercios e industrias.\n En su rol en DaliaEmpower, Carlos ha diseñado e implementado sistemas ETL y soluciones de visualización de datos para una plataforma de eLearning, transformando datos en herramientas valiosas para la toma de decisiones. Antes de unirse a DaliaEmpower, se desempeñó como ingeniero de redes informáticas, lo que le ha proporcionado una amplia experiencia en el campo de la tecnología y la ingeniería.'),
            'photo': 'CarlosGiles.jpeg'

        },
        '14': {
            'name': 'David Sol',
            'email': 'soldavid@gmail.com',
            'biography': _('Es un arquitecto de IT con experiencia en Computo de Nube e Ingeniería de Datos. Ha participado en importantes proyectos para empresas globales como Coca-Cola y Banco Colpatria. David desea difundir ideas para el avance de la tecnología, como su participación en el grupo AWS Community Builders confirma. Como orador, David ha ofrecido charlas sobre tecnologías en la Nube, Python, Inteligencia Artificial y otros temas, inspirando a las audiencias con su conocimiento y pasión por la innovación.'),
            'photo': 'default.jpg'
        },
        '15': {
            'name': 'Gustavo Salvador Reynaga Aguilar',
            'email': 'gustavo.reynaga@gmail.com',
            'biography': _('Gustavo Reynaga es un apasionado de la tecnología y la enseñanza que ha explorado una amplia gama de tecnologías desde una temprana edad, incluyendo Arduino, Raspberry Pi, BeagleBone, impresión 3D, y computadoras retro como el ZX Spectrum y el Commodore 64. Actualmente es instructor en el CECATI 132, donde comparte su conocimiento con los estudiantes. Uno de sus proyectos más destacados es el OSHWi Octopus Badge, un distintivo electrónico diseñado para la conferencia OSHWDem en La Coruña, España, cuyo diseño y código están disponibles en GitHub. Gustavo también mantiene un sitio web personal donde documenta y comparte sus proyectos, contribuyendo al crecimiento de la comunidad tecnológica y ayudando a otros a desarrollar sus propias ideas. Su objetivo es continuar explorando nuevas tecnologías, innovando y enseñando para inspirar a futuras generaciones de tecnólogos.'),
            'photo': 'Gustavo Reynaga.png'
        },
        '16': {
            'name': _('Charlas cortas de 5 minutos')
        },
        '17': {
            'name': _('Gabriela Villarreal y Denny Pérez')
        },
        '18': {
            'name': 'Ariel Ortiz',
            'biography': _('El profesor Ariel Ortiz Ramírez es originario de la Ciudad de México, aunque ha vivido la mayor parte de su vida en Cuautitlán Izcalli, Estado de México. Es Ingeniero en Sistemas Computacionales y Maestro en Ciencias Computacionales con especialidad en Inteligencia Artificial por parte del Tecnológico de Monterrey. Está certificado como programador de Python, Ruby, Java y C++, y es miembro de la _Association for Computing Machinery_ (ACM) y de la _Python Software Foundation_ (PSF). Desde hace 30 años, es profesor de planta del Tecnológico de Monterrey, Campus Estado de México. Ha recibido múltiples premios por parte de esta institución, incluyendo _Profesor Inspirador_ y _Profesor que Deja Huella_, en reconocimiento a su impacto y dedicación en la labor académica.\n El profesor Ortiz tuvo su primer encuentro con Python en el año 2001 y le gustó tanto que no ha dejado de usarlo desde entonces. Actualmente, lo utiliza para enseñar sus cursos de _Algoritmos Avanzados_ y _Diseño de Compiladores_ a estudiantes de ingeniería. En años recientes, ha sido presentador en _PyCon US_, _PyCon Latam_, _EuroPython_ y _Python Brasil_, compartiendo así su pasión, conocimiento y experiencia con la comunidad internacional de pythonistas. Es el autor de la [<a href="https://arielortiz.info/rip3/" target="_blank">RIP3: Referencia incompleta de Python 3</a>] y del blog [<a href="http://edupython.blogspot.com/" target="_blank">EduPython</a>], el cual promueve el uso del lenguaje Python en la educación.'),
            'photo': 'Ariel Ortiz.jpg'
        },
        '19': {
            'name': 'Elizabeth Fuentes Leone',
            'email': 'elizabethfuentes12@gmail.com',
            'biography': _('En mi rol de Especialista en Análisis de Datos y Aprendizaje Automático/Inteligencia Artificial (ML/AI), mi misión es simplificar conceptos complejos, traduciéndolos a un lenguaje accesible para todos. Me dedico a crear soluciones innovadoras que enfrentan de forma eficaz los retos que surgen en el mundo real. A través de mi participación en conferencias y la creación de recursos educativos, busco compartir mis conocimientos y experiencias con el fin de empoderar a los desarrolladores, ayudándoles a expandir sus habilidades y alcanzar sus objetivos profesionales.'),
            'photo': 'Elizabeth Fuentes.jpeg'
        },
        '20': {
            'name': 'Fabio Pinto Oviedo',
            'email': 'ingfabiopin@gmail.com',
            'biography': _('Fabio Andrés Pinto es Ingeniero Electrónico, Magíster en Ingeniería Matemática y Computación y doctorando en Estadística, Optimización y Matemática Aplicada. Trabaja con el Grupo de Métodos Estadísticos Avanzados de la Universidad Miguel Hernández de Elche. Fabio es Analista de Datos con más de 4 años de experiencia en Python, especializado en métodos de analítica, matemáticas computacionales y procesamiento de señales. Actualmente, se desempeña como Líder de Educación en BD GUIDANCE SAS y es docente en la Universidad El Bosque y en la Escuela Superior de Empresa, Ingeniería y Tecnología en Bogotá, Colombia.'),
            'photo': 'Fabio Pinto.jpg'
        },
        '21': {
            'name': 'Alex Parra',
            'email': 'parraletz@gmail.com',
            'biography': _("Soy Alejandro Parra, evangelista de tecnologías en la nube y el código abierto con más de 10 años de experiencia en IT. Comparto experiencias para inspirar un mundo más abierto, colaborativo e innovador donde 'Res publica non dominetur' sea una realidad."),
            'photo': 'Alex Parra.jpg'
        },
        '22': {
            'name': 'Kay Hayen',
            'email': 'kay.hayen@gmail.com',
            'biography': _('Kay Hayen is the founder of Nuitka Services, the commercial backend of Nuitka. For the past two years, he has made a living from the commercial side of Nuitka, after having worked on developing this Python compiler as a hobby for many years.'),
            'photo': 'Kay Hayen.jpg'

        },
        '23': {
            'name': 'Diego Alberto Barriga Martínez',
            'email': 'dbarriga@ciencias.unam.mx',
            'biography': _('Diego Barriga, Ingeniero en computación por la UNAM, trabajo con NLP y lenguas indigenas mexicanas. Es parte de Laboratorio de Investigacion y Desarrollo de Software Libre, Comunidad Elotl y actualmete desempeña un puesto como MLOps en mercado libre.\n Promotor de la cultura libre, la privacidad, neovim y de andar en bicicleta sin frenos :)'),
            'photo': 'Diego Alberto Barriga Martinez.jpg'
        },
        '24': {
            'name': 'Carlos Alarcón',
            'email': 'alarcon7a@gmail.com',
            'biography': _('Carlos Andrés Alarcón, ingeniero de sistemas y un destacado profesional en el campo de la ciencia de datos y la inteligencia artificial, con reconocimientos como Microsoft MVP en AI/ML y Google Developer Expert(GDE) en AI/ML . Ha ocupado diversos roles en el sector empresarial y en la plataforma de educación en línea Platzi, donde contribuyó al crecimiento de la compañía mediante la creación de métricas relevantes, la implementación de nuevas características basadas en IA para el producto y el fomento de una cultura basada en datos como director de la escuela de AI en Platzi. En su papel actual, se desempeña como CTO en Quix y consultor de AI asesorando a organizaciones en su transformación hacia un modelo guiado por datos y la inteligencia artificial. Carlos es un líder y divulgador reconocido en su campo, dedicado a impulsar la innovación y la eficiencia a través de la inteligencia artificial y el manejo de datos'),
            'photo': 'Carlos Alarcon.jpg'
        },
        '25': {
            'name': _('Conoce a nuestras participantes')
        },
        '26': {
            'name': 'Hugo Ramírez',
            'email': 'hughpythoneer@gmail.com',
            'biography': _('Estudió ciencias físicas e informática, y siempre buscó involucrarse en clases de filosofía. Se apasiona por temas relacionados con el pasado, presente y futuro de la humanidad, la ciencia, el voluntariado, los datos abiertos, el hacking y el open source. Combina siempre habilidades técnicas avanzadas con una profunda curiosidad intelectual y un fuerte compromiso con la comunidad, lo que lo ha convertido en un profesional versátil y dedicado. Actualmente, trabaja como científico de datos. Fue voluntario de la Free Software Foundation GNU/Linux en Venezuela y ha participado en el desarrollo a nivel Latam de la Televisión Digital Abierta (TDA). Fue miembro de PyVe (Venezuela) y ha participado en PyCon Argentina, PyCon México, y sigue trabajando en sostener su compromiso con el Manifiesto por la Guerrilla del Acceso Abierto con resiliencia, buena voluntad y eficacia desde hace más de 13 años. Es fundador del blog pybunker.org y actualmente forma parte activa de la comunidad Python CDMX.'),
            'photo': 'Hugo Ramirez.png'

        },
        '27': {
            'name': 'Juan Guillermo Gómez Torres',
            'email': 'juan.gomez01@gmail.com',
            'biography': _('Juan Guillermo coorganiza varios eventos globales y locales, como eventos de Google, Startup Weekend Colombia, PyCon, entre otros. Ha estado involucrado en tecnología y programación de software durante los últimos 20 años. Asiste a más de 30 eventos al año como orador invitado en toda América Latina, donde habla sobre temas como mobile, Android, cloud, Firebase, Kotlin, arquitectura de software y ML. Ha sido programador, arquitecto de software, líder tecnológico, profesor universitario y asesor en empresas de tecnología y departamentos de sistemas. Actualmente, es tech lead en WordBox. Juan es un GDE (Google Developer Expert) en Firebase, Machine Learning, GCP y Kotlin. Tiene una licenciatura en Ingeniería de Sistemas y una maestría en Ingeniería de Software por la Universidad San Buenaventura Cali.'),
            'photo': 'Juan Guillermo Gomez2.png'

        },
        '28': {
            'name': 'Ivan Castañeda',
            'email': 'ivan.castaneda.nazario@gmail.com',
            'biography': _('Héctor Iván Castañeda Nazario proviene de un pueblo agricultor en la Ciudad de México y estudió ingeniería petrolera en la UNAM. Aunque no pudo ejercer su profesión debido a circunstancias imprevistas, comenzó a estudiar Python para la inteligencia artificial a finales de 2019. Con cuatro años de experiencia como desarrollador BackEnd en una consultora mexicana, Héctor ha trabajado en proyectos de logística, observabilidad, recuperación ante desastres, análisis de datos y soporte a cliente. Actualmente, está creando el área de inteligencia artificial en su empresa y capacitando a sus compañeros para desarrollar proyectos que mejoren la vida de las personas. Además, tiene un proyecto personal llamado SMAEPYP, donde enseña Python, AWS, Notion, inteligencia artificial e ingeniería petrolera al público general de forma gratuita.'),
        },
        '29': {
            'name': 'Abigail Messreyames',
            'biography': _('Abigail, is an Open Source Programs Manager, Researcher and Community Builder. Her current research focuses on Improving DEI in Open Source Community Leadership. She is a contributor and community member in the African Python Software Community and has served as an organizer for local and international community events. Mesrenyame is a Fellow and a Community Service award winner at the Python Software Foundation.'),
            'photo': 'Abigail Mesrenyame Dogbe.jpg'
        },
        '30': {
            'name': _('Equipo organizador')
        },
        '31': {
                'name': 'Luis Zárate',
                'biography': _(
                    'Es desarrollador Python con más de 14 años de experiencia en la realización de proyectos por demanda para diversas empresas. Es fundador de Solvosoft y creador de proyectos como Gentelella Widgets y Organilab. Además, es colaborador del proyecto xhtml2pdf y ha sido profesor universitario en la Universidad de Costa Rica.'),
                'photo': 'luis-zarate.jpg'
        },
        '32': {
                'name': 'Danilo Britto',
                'biography': _('Soy Senior Software Engineer con más de 10 años de experiencia en el desarrollo y la arquitectura de aplicaciones. A lo largo de mi carrera, he tenido la oportunidad de contribuir a varios proyectos open source como Laravel, React Native, AWS Chalice, Zustand, Expo y cmder, entre otros.</br>He sido Community Lead en el Facebook Developer Circle: Lima, donde ayudé a impulsar la colaboración y el crecimiento de la comunidad de desarrolladores. Mi trabajo se enfoca en la optimización de performance, la experiencia de usuario (UX) y la experiencia del desarrollador (DX), siempre buscando crear soluciones eficientes y escalables.</br>Mi stack principal está basado en Python y React, pero también tengo experiencia en otros lenguajes como PHP, Java, C#, Lua, entre otros. A lo largo de mi trayectoria, he desempeñado diferentes roles, incluyendo Cloud Developer, Cloud DevOps Engineer, Cloud Native Application Architect y Senior Software Engineer.</br>Como Pythonista y apasionado por el desarrollo, sigo explorando nuevas tecnologías para aportar innovación y optimización en cada proyecto.'),
                'photo': 'Danilo Britto.png'
        },
        '33': 
            {
            'name': 'Bea Gandica',
            'biography': _("Beatris A. Mendez Gandica, originally from San Cristobal, Venezuela, is an engineer serving as a Program Manager at Microsoft. Her role focuses on managing the daily operations of Azure Data services' usage billing pipeline, ensuring secure, scalable, and accurate customer billing for Azure. Passionate about community impact, she founded Nuevo Foundation in 2018."),
            'photo': 'Bea Mendez Gandica.jpeg',
        },
        '34':{
            'name': 'Alejandra Pérez Castillo',
            'biography': _('Especialista en colaboración, productividad y tecnologías de nube de Microsoft, abarcando su implementación y adopción. Apasionada por compartir el conocimiento e impulsar a los equipos de trabajo moderno para el desarrollo de nuevas habilidades dentro de la industria tecnológica.'),
            'photo': 'Alejandra Pérez.jpeg',
        },
        
    }
    data = {
        'day1': {
            'date': _('Jueves 19 de Septiembre'),
            'events': [
                {
                    'title': _('Evento de Bienvenida'),
                    'duration': '7:00 pm - 9:00 pm',
                    'speaker': '1',
                    'salon': _('Bar del Cid Castilla'),
                    'image': 'bienvenida_evento.jpg'
                },
            ],
        },
        'day2': {
            'date': _('Viernes 20 de Septiembre'),
            'events': [
                {
                    'title': _('Presentacion e introduccion al evento'),
                    'duration': '9:00 am - 9:30 am',
                    'speaker': '2',
                    'image': 'bienvenida_conferencia.jpg'
                },
                {
                    'title': _('Keynote de apertura'),
                    'duration': '9:30 am - 10:15 am',
                    'speaker': '18',
                    'salon': _('Salón A'),
                    'image': 'Ariel Ortiz.jpg'
                },
                {
                    'title': _('Conviértete en un maestro de la automatización: Aprende a implementar RPA y PYTHON en el sector financiero.'),
                    'duration': '10:30 am - 11:10 am',
                    'speaker': '4',
                    'salon': _('Salón A'),
                    'image': 'rpa_python_sector_financiero.jpg'
                },
                {
                    'title': _('De Bichos y Serpientes: Seguridad en el Ecosistema de Paquetes Python'),
                    'duration': '10:30 am - 11:10 am',
                    'speaker': '5',
                    'salon': _('Salón B'),
                    'image': 'seguridad_paquetes_python.jpg'
                },
                {
                    'title': _('DeepSignBridge: Traductor de Lenguaje de Señas en Tiempo Real Usando Transformers y Visión Computacional'),
                    'duration': '11:15 am - 11:55 am',
                    'speaker': '6',
                    'salon': _('Salón A'),
                    'image': 'deep_sign_bridge.jpg'
                },
                {
                    'title': _('De pixeles a predicciones: Transformando la experiencia de videos con python'),
                    'duration': '11:15 am - 11:55 am',
                    'speaker': '7',
                    'salon': _('Salón B'),
                    'image': 'videos_python.jpg'
                },
                {
                    'title': _('Desplegando tu aplicación Python sin morir en el intento'),
                    'duration': '12:00 pm - 12:40 pm',
                    'speaker': '8',
                    'salon': _('Salón A'),
                    'image': 'desplegando_python.jpg'
                },
                # {
                #     'title': _('Domina al Tiburón: Pipelines en Python para Wireshark'),
                #     'duration': '12:00 pm - 12:40 pm',
                #     'speaker': '9',
                #     'salon': _('Salón B'),
                #     'image': 'pipelines_python_wireshark.jpg'
                # },
                {
                    'title': _('Aprendizaje por Refuerzo en Python: Optimización en el mundo real'),
                    'duration': '2:10 pm - 2:50 pm',
                    'speaker': '10',
                    'salon': _('Salón A'),
                    'image': 'espacios_vectoriales_langchain.jpg'
                },
                {
                    'title': _('Fortaleciendo el acceso a la justicia: Whisper y PyQt en Acción'),
                    'duration': '2:10 pm - 2:50 pm',
                    'speaker': '11',
                    'salon': _('Salón B'),
                    'image': 'whisper_pyqt_accion.jpg'
                },
                {
                    'title': _('Transformando Startups con Kubernetes: Gestión de Aplicaciones Django para un Crecimiento Explosivo'),
                    'duration': '2:55 pm - 3:35 pm',
                    'speaker': '12',
                    'salon': _('Salón A'),
                    'image': 'startups_kubernetes_django.jpg'
                },
                {
                    'title': _('Insights Ocultos: Cómo la Estadística y Python Empoderan Decisiones Estratégicas'),
                    'duration': '2:55 pm - 3:35 pm',
                    'speaker': '13',
                    'salon': _('Salón B'),
                    'image': 'estadistica_python_decisiones.jpg'
                },
                {
                    'title': _('Ambientes virtuales en Python: venv, Poetry, Conda, Docker y más allá'),
                    'duration': '3:40 pm - 4:20 pm',
                    'speaker': '14',
                    'salon': _('Salón A'),
                    'image': 'ambientes_virtuales.jpg'
                },
                {
                    'title': _('Micropython First Contact'),
                    'duration': '3:40 pm - 4:20 pm',
                    'speaker': '15',
                    'salon': _('Salón B'),
                    'image': 'micropython_first_contact.jpg'
                },
                {
                    'title': _('Charlas Relámpago'),
                    'duration': '4:35 pm - 5:20 pm',
                    'speaker': '16',
                    'salon': _('Salón A'),
                    'image': 'charlas_relampago.jpg'
                },
                {
                    'title': _('Keynote de cierre primer día'),
                    'duration': '5:25 pm - 6:10 pm',
                    'speaker': '17',
                    'salon': _('Salón A'),
                    'image': 'keynote_2.jpg'
                },
            ],
        },
        'day3': {
            'date': _('Sábado 21 de Septiembre'),
            'events': [
                {
                    'title': _('Keynote de apertura'),
                    'duration': '9:00 am - 9:45 am',
                    'speaker': '29',
                    'salon': _('Salón A'),
                    'image': 'Abigail.jpg'
                },
                {
                    'title': _('Prompt engineering: la llave maestra para aprovechar al máximo la generative IA'),
                    'duration': '10:00 am - 10:40 am',
                    'speaker': '19',
                    'salon': _('Salón A'),
                    'image': 'prompt_engineering_ia.jpg'
                },
                {
                    'title': _('Data Compression is not enough'),
                    'duration': '10:00 am - 10:40 am',
                    'speaker': '32',
                    'salon': _('Salón B'),
                    'image': 'data_compression.webp'
                },
                {
                    'title': _('GitHub Codespaces para potenciar tu trabajo como desarrollador/a'),
                    'duration': '10:45 am - 11:25 am',
                    'speaker': '34',
                    'salon': _('Salón A'),
                    'image': 'github_code.webp'
                },
                {
                    'title': _('Supercharge Python with Nuitka: Witness a 10-Year Plan Come to Life!'),
                    'duration': '10:45 am - 11:25 am',
                    'speaker': '22',
                    'salon': _('Salón B'),
                    'image': 'nuitka_supercharge.png'
                },
                {
                    'title': _('Tests efectivos con pytest, o sobre como escribir código duro de fallar'),
                    'duration': '11:30 am - 12:10 pm',
                    'speaker': '23',
                    'salon': _('Salón A'),
                    'image': 'tests_pytest.jpg'
                },
                {
                    'title': _('IA Multimodal en Educación: Transformando el Aprendizaje con Python'),
                    'duration': '11:30 am - 12:10 pm',
                    'speaker': '24',
                    'salon': _('Salón B'),
                    'image': 'ia_multimodial_educacion.jpg'
                },
                {
                    'title': _('PyLadies Panel - Importancia de la diversidad y mujeres en tecnología'),
                    'duration': '1:30 pm - 2:20 pm',
                    'speaker': '25',
                    'image': 'pyladies_panel.jpg'
                },
                # TBD
                {
                    'title': _('Python y los esquemas ETL: El Pivote Esencial para la Inteligencia Artificial'),
                    'duration': '2:20 pm - 3:00 pm',
                    'speaker': '26',
                    'salon': _('Salón B'),
                    'image': 'python_etl.jpeg'
                },
                {
                    'title': _('Organilab, un administrador de laboratoríos químicos potenciado con Django Gentelella Widgets.'),
                    'duration': '2:20 pm - 3:00 pm',
                    'speaker': '31',
                    'salon': _('Salón A'),
                    'image': 'organilab.png'
                },
                {
                    'title': _('Revealing the power of multimodal embeddings: bridging the gap between text, images, videos and more'),
                    'duration': '3:05 pm - 3:45 pm',
                    'speaker': '27',
                    'salon': _('Salón A'),
                    'image': 'multimodal_embeddings.jpg'
                },
                {
                    'title': _('Del Oro Negro al Oro Digital: La Historia de un Ingeniero Convertido en Líder de Python'),
                    'duration': '3:05 pm - 3:45 pm',
                    'speaker': '28',
                    'salon': _('Salón B'),
                    'image': 'oro_negro_digital.jpg'
                },
                # TBD
                # {
                #     'title': _('title'),
                #     'duration': '3:50 pm - 4:30 pm',
                #     'speaker': 'speaker',
                #     'salon': _('Salón A'),
                #     'image': 'x.jpg'
                # },
                # TBD
                # {
                #     'title': _('title'),
                #     'duration': '3:50 pm - 4:30 pm',
                #     'speaker': 'speaker',
                #     'salon': _('Salón B'),
                #     'image': 'x.jpg'
                # },
                {
                    'title': _('Keynote cierre de conferencia'),
                    'duration': '4:45 pm - 5:30 pm',
                    'speaker': '33',
                    'salon': _('Salón A'),
                    'image': 'Bea Mendez Gandica.jpeg'
                },
                {
                    'title': _('Cierre de Conferencia'),
                    'duration': '5:30 pm - 5:50 pm',
                    'speaker': '30',
                    'salon': _('Salón A'),
                    'image': 'cierre_conferencia.jpg'
                },
                {
                    'title': _('Fotografía del grupo de participantes'),
                    'duration': '6:00 pm - 6:15 pm',
                    'speaker': '1',
                    'image': 'foto-grupal.webp'
                },
            ],
        }
    }

    context = {'data': data, 'speakers': speakers}

    return render(request, 'scheduled.html', context)

def pyladies(request, lang='es'):
    activate(lang)
    ladies  = [
        {
            'name': 'Alejandra Pérez Castillo',
                    'bio': _('Especialista en colaboración, productividad y tecnologías de nube de Microsoft, abarcando su implementación y adopción. Apasionada por compartir el conocimiento e impulsar a los equipos de trabajo moderno para el desarrollo de nuevas habilidades dentro de la industria tecnológica.'),
                    'photo': 'Alejandra Pérez.jpeg',
        },
        {
            'name': 'Bea Gandica',
                    'bio': _("Beatris A. Mendez Gandica, originally from San Cristobal, Venezuela, is an engineer serving as a Program Manager at Microsoft. Her role focuses on managing the daily operations of Azure Data services' usage billing pipeline, ensuring secure, scalable, and accurate customer billing for Azure. Passionate about community impact, she founded Nuevo Foundation in 2018."),
                    'photo': 'Bea Mendez Gandica.jpeg',
        },
        {
            'name': 'Ashley Rojas Pérez',
                    'bio': _("Ashley es una estudiante autodidacta de Informática y Tecnología Multimedia en la Universidad de Costa Rica. Apasionada por la tecnología y el diseño, ha aprendido Python por su cuenta para contribuir a proyectos como PyConLatam 2024. Con un firme interés en involucrarse más en la comunidad tecnológica, busca colaborar en iniciativas que integren la informática, el diseño y el contenido multimedia."),
                    'photo': 'AshleyRojas - AP.png',
        },
        {
            'name': 'Geraldine Echavarria',
                    'bio': _("Ingeniera de sistemas, apasionada por la ciencia y los datos. Ha trabajado como backend developer con Python y como ingeniera de datos. Ha contribuido a comunidades y eventos en tecnología, ha participado en eventos de Python en logística y alguna vez en charla."),
                    'photo': 'default.jpg',
        },
        {
            'name': 'Tatiana Andrea Delgadillo',
                    'bio': _("Tatiana Delgadillo es una profesional multifacética con sólida formación en informática y pasión por el análisis de datos y la inteligencia artificial. Ha acumulado experiencia en diversas industrias. En su rol actual cómo Data Scientist dentro de una StartUp de educación, combina su experiencia en informática y estadística para diseñar soluciones innovadoras en el ámbito educativo."),
                    'photo': 'Tatiana Delgadillo.jpg',
        }
    ]

    context = {'ladies': ladies}

    return render(request, 'pyladies.html', context)