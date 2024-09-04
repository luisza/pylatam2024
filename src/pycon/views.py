from django.shortcuts import render
from django.utils.translation import activate
from django.utils.translation import gettext as _

def home(request, lang='es'):
    activate(lang)
    keynote_speakers = [
        { 'name': 'Lynn Root',
         'description': _("Staff Engineer at Spotify and an professor at Columbia University's Graduate School of Engineering."),
         'image': 'Lynn Root.jpg'
         },   
        { 'name': 'Ariel Ortiz',
         'description': _('Professor at Tecnológico de Monterrey, Python expert, and international speaker.'),
         'image': 'Ariel Ortiz.jpg'
         },
        { 'name': 'Abigail Messreyames',
         'description': _('Open Source Programs Manager, researcher, and community builder with a focus on DEI in leadership.'),
         'image': 'Abigail Mesrenyame Dogbe.jpg' }
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
                    'bio': _('Gabriela es psicopedagoga amante de la literatura y la cocina...'),
                    'photo': 'default.jpg',
                    'role': _('Psicopedagoga')
                },
                {
                    'name': 'Denny Perez',
                    'bio': _('Denny es Analista de QA de Software con un título en contabilidad...'),
                    'photo': 'denny-perez.png',
                    'role': _('Analista de QA de Software')
                },
                {
                    'name': 'Paul Barajas',
                    'bio': _('Es un apasionado de la tecnología de código abierto...'),
                    'photo': 'paul-barajas.jpeg',
                }
            ]
        },
        'associated_organization': {
            'title': _('Organización Adjunta'),
            'members': [
                {
                    'name': 'Luis Zárate',
                    'bio': _('Es desarrollador Python con más de 14 años de experiencia...'),
                    'photo': 'luis-zarate.jpg'
                },
                {
                    'name': 'Ronald Perez',
                    'bio': _('Es profesor de Informática en la Universidad de Costa Rica...'),
                    'photo': 'ronald-perez.jpg'
                }
            ]
        },
        'collaboration_team': {
            'title': _('Equipo de Colaboración'),
            'members': [
                {
                    'name': 'Ivone Corona',
                    'bio': _('Es una psicóloga apasionada del psicoanálisis...'),
                    'photo': 'ivone-corona.jpeg'
                },
                {
                    'name': 'Andres Pineda',
                    'bio': _('Desarrollador de software con una pasión el UI...'),
                    'photo': 'andres-pineda.jpeg'
                },
            ]
        },
        'volunteering': {
            'title': _('Voluntariado'),
            'members': [
                {
                    'name': 'Ashley Rojas',
                    'bio': _('Estudiante autodidacta de Informática y Tecnología Multimedia...'),
                    'photo': 'ashley-rojas.jpeg'
                },
                {
                    'name': 'Jeremy Guzmán',
                    'bio': _('Jeremy es un estudiante de Informática en la Universidad de Costa Rica...'),
                    'photo': 'jeremy-guzman.jpeg'
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
        'name': _('Todos los participantes'),

        },
        '2': {
            'name': _('Personal administrativo')
        },
        '3': {
            'name': 'Lynn Root',
            'biography': _("Lynn Root is a Staff Engineer at Spotify and an adjunct professor at Columbia University's Graduate School of Engineering. She is a seasoned speaker on building and maintaining distributed systems, and is the tech lead for governance compliance for Spotify's ML/AI platform. Lynn is a global leader of diversity in the Python community, the Chair of the PyLadies Global Council, and a PSF fellow and the former Vice Chair of the PSF's Board of Directors. When her hands are not on a keyboard, they are usually holding a bass guitar."),
            'photo': 'Lynn Root.jpg'
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
            'name': 'Carla M. F. Román',
            'email': 'carli.f.roman@gmail.com',
            'biography': _('Carla es una apasionada de la Inteligencia Artificial, participa activamente en comunidades locales e internacionales de Machine Learning y Data Science. Actualmente es women techmaker ambassador. Participó como investigadora en inteligencia artificial en el Instituto de Inteligencia Artificial (IIC) de la Universidad Privada Boliviana, además es co fundadora de Menti Academy, una academia de enseñanza online para niños, creadora de contenido en redes sociales como TikTok e Instagram donde ayuda a la comunidad a iniciar con la programación específicamente en Python y actualmente parte del team de education en Platzi.'),
            'photo': 'Carla Marcela Florida.jpg'
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
            'email': 'soldavid@gmail.com'
        },
        '15': {
            'name': 'Gustavo Salvador Reynaga Aguilar',
            'email': 'gustavo.reynaga@gmail.com',
            'biography': _('Gustavo Reynaga es un apasionado de la tecnología y la enseñanza que ha explorado una amplia gama de tecnologías desde una temprana edad, incluyendo Arduino, Raspberry Pi, BeagleBone, impresión 3D, y computadoras retro como el ZX Spectrum y el Commodore 64. Actualmente es instructor en el CECATI 132, donde comparte su conocimiento con los estudiantes. Uno de sus proyectos más destacados es el OSHWi Octopus Badge, un distintivo electrónico diseñado para la conferencia OSHWDem en La Coruña, España, cuyo diseño y código están disponibles en GitHub. Gustavo también mantiene un sitio web personal donde documenta y comparte sus proyectos, contribuyendo al crecimiento de la comunidad tecnológica y ayudando a otros a desarrollar sus propias ideas. Su objetivo es continuar explorando nuevas tecnologías, innovando y enseñando para inspirar a futuras generaciones de tecnólogos.'),
            'photo': 'Gustavo Reynaga.png'
        },
        '16': {
            'name': _('Charlas generales')
        },
        '17': {
            'name': _('Personal administrativo')
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
            'name': _('Capitulos PyLadies alrededor de América Latina')
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
        }
    }
    data = {
        'day1': {
            'date': _('Jueves 19 de Septiembre'),
            'events': [
                {
                    'title': _('Bienvenida al evento'),
                    'duration': '6:00 pm - 8:00 pm',
                    'speaker': '1',
                    'image': 'bienvenida_evento.jpg'
                },
            ],
        },
        'day2': {
            'date': _('Viernes 20 de Septiembre'),
            'events': [
                {
                    'title': _('Bienvenida'),
                    'duration': '9:00 am - 9:30 am',
                    'speaker': '2',
                    'image': 'bienvenida_conferencia.jpg'
                },
                {
                    'title': _('Keynote de Apertura'),
                    'duration': '9:30 am - 10:15 am',
                    'speaker': '3',
                    'salon': _('Salón A'),
                    'image': 'Lynn.jpg'
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
                {
                    'title': _('Domina al Tiburón: Pipelines en Python para Wireshark'),
                    'duration': '12:00 pm - 12:40 pm',
                    'speaker': '9',
                    'salon': _('Salón B'),
                    'image': 'pipelines_python_wireshark.jpg'
                },
                {
                    'title': _('Espacios vectoriales con python y langchain'),
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
                    'speaker': '18',
                    'salon': _('Salón A'),
                    'image': 'keynote_apertura.jpg'
                },
                {
                    'title': _('Prompt engineering: la llave maestra para aprovechar al máximo la generative IA'),
                    'duration': '10:00 am - 10:40 am',
                    'speaker': '19',
                    'salon': _('Salón A'),
                    'image': 'prompt_engineering_ia.jpg'
                },
                {
                    'title': _('Reputación en Tiempo Real y Análisis de Sentimiento con Python'),
                    'duration': '10:00 am - 10:40 am',
                    'speaker': '20',
                    'salon': _('Salón B'),
                    'image': 'reputacion_analisis_sentimiento.webp'
                },
                {
                    'title': _('Revolutionizing CI/CD with Python and Generative AI: Next-Level Automation in DevOps'),
                    'duration': '10:45 am - 11:25 am',
                    'speaker': '21',
                    'salon': _('Salón A'),
                    'image': 'cicd_python_devops.jpg'
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
                    'title': _('PyLadies Panel'),
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
                    'speaker': '29',
                    'salon': _('Salón A'),
                    'image': 'Abigail.jpg'
                },
                {
                    'title': _('Cierre de Conferencia'),
                    'duration': '5:30 pm - 5:50 pm',
                    'speaker': '30',
                    'salon': _('Salón A'),
                    'image': 'cierre_conferencia.jpg'
                },
            ],
        }
    }

    context = {'data': data, 'speakers': speakers}

    return render(request, 'scheduled.html', context)