from django.shortcuts import render
from django.utils.translation import activate
from django.utils.translation import gettext as _

def home(request, lang='es'):
    activate(lang)
    return render(request, 'home.html')

def conduct(request, lang='es'):
    activate(lang)
    return render(request, 'conduct.html')

def scheduled(request, lang='es'):
    activate(lang)

    data = {
        'day1': {
            'date': _('Jueves 19 de Septiembre'),
            'events': [
                {
                    'title': _('Bienvenida al evento'),
                    'duration': '6:00 pm - 8:00 pm',
                    'speaker': _('Personal administrativo'),
                    'image': 'bienvenida_evento.jpg'
                },
            ],
        },
        'day2': {
            'date': _('Viernes 20 de Septiembre'),
            'events': [
                {
                    'title': _('Bienvenida conferencia'),
                    'duration': '9:00 am - 9:30 am',
                    'speaker': _('Personal administrativo'),
                    'image': 'bienvenida_conferencia.jpg'
                },
                {
                    'title': _('Keynote 1'),
                    'duration': '9:30 am - 10:15 am',
                    'speaker': 'Lynn',
                    'image': 'keynote_1.jpg'
                },
                {
                    'title': _('Conviértete en un maestro de la automatización: Aprende a implementar RPA y PYTHON en el sector financiero.'),
                    'duration': '10:30 am - 11:10 am',
                    'speaker': 'Nadie Ayala',
                    'salon': _('Salon A'),
                    'image': 'rpa_python_sector_financiero.jpg'
                },
                {
                    'title': _('De Bichos y Serpientes: Seguridad en el Ecosistema de Paquetes Python'),
                    'duration': '10:30 am - 11:10 am',
                    'speaker': 'Oscar Cortez',
                    'salon': _('Salon B'),
                    'image': 'seguridad_paquetes_python.jpg'
                },
                {
                    'title': _('DeepSignBridge: Traductor de Lenguaje de Señas en Tiempo Real Usando Transformers y Visión Computacional'),
                    'duration': '11:15 am - 11:55 am',
                    'speaker': 'Gerardo Vilcamiza',
                    'salon': _('Salon A'),
                    'image': 'rpa_python_sector_financiero_gerardo.jpg'
                },
                {
                    'title': _('De pixeles a predicciones: Transformando la experiencia de videos con python'),
                    'duration': '11:15 am - 11:55 am',
                    'speaker': 'Fernanda Ochoa',
                    'salon': _('Salon B'),
                    'image': 'videos_python.jpg'
                },
                {
                    'title': _('Desplegando tu aplicación Python sin morir en el intento'),
                    'duration': '12:00 pm - 12:40 pm',
                    'speaker': 'Adolfo Fitoria',
                    'salon': _('Salon A'),
                    'image': 'desplegando_python.jpg'
                },
                {
                    'title': _('Domina al Tiburón: Pipelines en Python para Wireshark'),
                    'duration': '12:00 pm - 12:40 pm',
                    'speaker': 'Kevin Jahaziel Leon Morales',
                    'salon': _('Salon B'),
                    'image': 'pipelines_python_wireshark.jpg'
                },
                {
                    'title': _('Espacios vectoriales con python y langchain'),
                    'duration': '2:10 pm - 2:50 pm',
                    'speaker': 'Carla M. F. Román',
                    'salon': _('Salon A'),
                    'image': 'espacios_vectoriales_langchain.jpg'
                },
                {
                    'title': _('Fortaleciendo el acceso a la justicia: Whisper y PyQt en Acción'),
                    'duration': '2:10 pm - 2:50 pm',
                    'speaker': 'Angel Serrano',
                    'salon': _('Salon B'),
                    'image': 'whisper_pyqt_accion.jpg'
                },
                {
                    'title': _('From Dependency Hell to Environment Heaven'),
                    'duration': '2:55 pm - 3:35 pm',
                    'speaker': 'Ori Ber-ilan',
                    'salon': _('Salon A'),
                    'image': 'dependency_hell.jpg'
                },
                {
                    'title': _('Insights Ocultos: Cómo la Estadística y Python Empoderan Decisiones Estratégicas'),
                    'duration': '2:55 pm - 3:35 pm',
                    'speaker': 'Carlos Giles',
                    'salon': _('Salon B'),
                    'image': 'estadistica_python_decisiones.jpg'
                },
                {
                    'title': _('Laberintos del Lenguaje: Borges y las Narrativas Infinitas con LLMs'),
                    'duration': '3:40 pm - 4:20 pm',
                    'speaker': 'Maris Botero',
                    'salon': _('Salon A'),
                    'image': 'laberintos_lenguaje_llms.jpg'
                },
                {
                    'title': _('Micropython First Contact'),
                    'duration': '3:40 pm - 4:20 pm',
                    'speaker': 'Gustavo Salvador Reynaga Aguilar',
                    'salon': _('Salon B'),
                    'image': 'micropython_first_contact.jpg'
                },
                {
                    'title': _('Charlas Relámpago'),
                    'duration': '4:35 pm - 5:20 pm',
                    'speaker': _('Personal administrativo'),
                    'image': 'charlas_relampago.jpg'
                },
                {
                    'title': _('Keynote 2'),
                    'duration': '5:25 pm - 6:10 pm',
                    'speaker': _('Personal administrativo'),
                    'image': 'keynote_2.jpg'
                },
            ],
        },
        'day3': {
            'date': _('Sábado 21 de Septiembre'),
            'events': [
                {
                    'title': _('Keynote 3'),
                    'duration': '9:00 am - 9:45 am',
                    'speaker': 'Abigail Messreyames',
                    'image': 'keynote_3.jpg'
                },
                {
                    'title': _('Prompt engineering: la llave maestra para aprovechar al máximo la generative IA'),
                    'duration': '10:00 am - 10:40 am',
                    'speaker': 'Elizabeth Fuentes Leone',
                    'salon': _('Salon A'),
                    'image': 'prompt_engineering_ia.jpg'
                },
                {
                    'title': _('Reputación en Tiempo Real y Análisis de Sentimiento con Python'),
                    'duration': '10:00 am - 10:40 am',
                    'speaker': 'Fabio Pinto Oviedo',
                    'salon': _('Salon B'),
                    'image': 'reputacion_analisis_sentimiento.jpg'
                },
                {
                    'title': _('Revolutionizing CI/CD with Python and Generative AI: Next-Level Automation in DevOps'),
                    'duration': '10:45 am - 11:25 am',
                    'speaker': 'Alex Parra',
                    'salon': _('Salon A'),
                    'image': 'cicd_python_devops.jpg'
                },
                {
                    'title': _('Supercharge Python with Nuitka: Witness a 10-Year Plan Come to Life!'),
                    'duration': '10:45 am - 11:25 am',
                    'speaker': 'Kay Hayen',
                    'salon': _('Salon B'),
                    'image': 'nuitka_supercharge.jpg'
                },
                {
                    'title': _('Tests efectivos con pytest, o sobre como escribir código duro de fallar'),
                    'duration': '11:30 am - 12:10 pm',
                    'speaker': 'Diego Alberto Barriga Martínez',
                    'salon': _('Salon A'),
                    'image': 'tests_pytest.jpg'
                },
                {
                    'title': _('Todo lo que necesitas saber sobre Unicode, pero nunca se te ocurrió preguntar'),
                    'duration': '11:30 am - 12:10 pm',
                    'speaker': 'Ariel Ortiz',
                    'salon': _('Salon B'),
                    'image': 'unicode_python.jpg'
                },
                {
                    'title': _('PyLadies Panel'),
                    'duration': '1:30 pm - 2:20 pm',
                    'speaker': _('Capitulos PyLadies alrededor de América Latina'),
                    'image': 'pyladies_panel.jpg'
                },
                {
                    'title': _('Una introducción al análisis de datos topológicos'),
                    'duration': '2:20 pm - 3:00 pm',
                    'speaker': 'Kaled Corona',
                    'salon': _('Salon A'),
                    'image': 'analisis_datos_topologicos.jpg'
                },
                {
                    'title': _('Python y los esquemas ETL: El Pivote Esencial para la Inteligencia Artificial'),
                    'duration': '2:20 pm - 3:00 pm',
                    'speaker': 'Hugo Ramírez',
                    'salon': _('Salon B'),
                    'image': 'python_etl.jpg'
                },
                {
                    'title': _("A Journey into MLOps: Kubeflow's Magic Revealed"),
                    'duration': '3:05 pm - 3:45 pm',
                    'speaker': 'César Leandro Higuita Pérez',
                    'salon': _('Salon A'),
                    'image': 'mlops_kubeflow.jpg'
                },
                {
                    'title': _('Del Oro Negro al Oro Digital: La Historia de un Ingeniero Convertido en Líder de Python'),
                    'duration': '3:05 pm - 3:45 pm',
                    'speaker': 'Ivan Castañeda',
                    'salon': _('Salon B'),
                    'image': 'oro_negro_digital.jpg'
                },
                {
                    'title': _('Transformando Startups con Kubernetes: Gestión de Aplicaciones Django para un Crecimiento Explosivo'),
                    'duration': '3:50 pm - 4:30 pm',
                    'speaker': 'Osiel Jacobo Torres',
                    'salon': _('Salon A'),
                    'image': 'startups_kubernetes_django.jpg'
                },
                {
                    'title': _('Sculpting Data for Machine Learning using Python: Generative AI edition'),
                    'duration': '3:50 pm - 4:30 pm',
                    'speaker': 'Jigyasa Grover',
                    'salon': _('Salon B'),
                    'image': 'sculpting_data_ml.jpg'
                },
                {
                    'title': _('Keynote 4'),
                    'duration': '4:45 pm - 5:30 pm',
                    'speaker': _('Personal administrativo'),
                    'image': 'keynote_4.jpg'
                },
                {
                    'title': _('Cierre de Conferencia'),
                    'duration': '5:30 pm - 5:50 pm',
                    'speaker': _('Personal administrativo'),
                    'image': 'cierre_conferencia.jpg'
                },
            ],
        }
    }

    context = {'data': data}

    return render(request, 'scheduled.html', context)
