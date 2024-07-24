from django.shortcuts import render
from django.utils.translation import activate

# Create your views here.

def home(request, lang='es'):
    activate(lang)
    return render(request, 'home.html')

def conduct(request, lang='es'):
    activate(lang)
    return render(request, 'conduct.html')

def scheduled(request, lang='es'):
    activate(lang)

    data = {
        'dia1': [
            {
                'title': 'Bienvenida al evento',
                'duration': '9:00 am - 9:30 am',
                'speaker': 'Personal administrativo',
                'image': 'bienvenida_evento.jpg'
            },
        ],
        'dia2': [
            {
                'title': 'Bienvenida a conferencia',
                'duration': '9:00 am - 9:30 am',
                'speaker': 'Personal administrativo',
                'image': 'bienvenida_conferencia.jpg'
            },
            {
                'title': 'Keynote 1',
                'duration': '9:30 am - 10:15 am',
                'speaker': 'Lynn',
                'image': 'keynote_1.jpg'
            },
            {
                'title': 'Conviértete en un maestro de la automatización: Aprende a implementar RPA y PYTHON en el sector financiero.',
                'duration': '10:30 am - 11:10 am',
                'speaker': 'Nadie Ayala',
                'salon': 'Salon A',
                'image': 'rpa_python_sector_financiero.jpg'
            },
            {
                'title': 'De Bichos y Serpientes: Seguridad en el Ecosistema de Paquetes Python',
                'duration': '10:30 am - 11:10 am',
                'speaker': 'Oscar Cortez',
                'salon': 'Salon B',
                'image': 'seguridad_paquetes_python.jpg'
            },
            {
                'title': 'Conviértete en un maestro de la automatización: Aprende a implementar RPA y PYTHON en el sector financiero.',
                'duration': '11:15 am - 11:55 am',
                'speaker': 'Gerardo Vilcamiza',
                'salon': 'Salon A',
                'image': 'rpa_python_sector_financiero_gerardo.jpg'
            },
            {
                'title': 'De pixeles a predicciones: Transformando la experiencia de videos con python.',
                'duration': '11:15 am - 11:55 am',
                'speaker': 'Fernanda Ochoa',
                'salon': 'Salon B',
                'image': 'videos_python.jpg'
            },
            {
                'title': 'Desplegando tu aplicación Python sin morir en el intento.',
                'duration': '12:00 pm - 12:40 pm',
                'speaker': 'Adolfo Fitoria',
                'salon': 'Salon A',
                'image': 'desplegando_python.jpg'
            },
            {
                'title': 'Domina al Tiburón: Pipelines en Python para Wireshark',
                'duration': '12:00 pm - 12:40 pm',
                'speaker': 'Kevin Jahaziel Leon Morales',
                'salon': 'Salon B',
                'image': 'pipelines_python_wireshark.jpg'
            },
            {
                'title': 'Espacios vectoriales con python y langchain',
                'duration': '2:10 pm - 2:50 pm',
                'speaker': 'Carla M. F. Román',
                'salon': 'Salon A',
                'image': 'espacios_vectoriales_langchain.jpg'
            },
            {
                'title': 'Fortaleciendo el acceso a la justicia: Whisper y PyQt en Acción',
                'duration': '2:10 pm - 2:50 pm',
                'speaker': 'Angel Serrano',
                'salon': 'Salon B',
                'image': 'whisper_pyqt_accion.jpg'
            },
            {
                'title': 'From Dependency Hell to Environment Heaven',
                'duration': '2:55 pm - 3:35 pm',
                'speaker': 'Ori Ber-ilan',
                'salon': 'Salon A',
                'image': 'dependency_hell.jpg'
            },
            {
                'title': 'Insights Ocultos: Cómo la Estadística y Python Empoderan Decisiones Estratégicas',
                'duration': '2:55 pm - 3:35 pm',
                'speaker': 'Carlos Giles',
                'salon': 'Salon B',
                'image': 'estadistica_python_decisiones.jpg'
            },
            {
                'title': 'Laberintos del Lenguaje: Borges y las Narrativas Infinitas con LLMs',
                'duration': '3:40 pm - 4:20 pm',
                'speaker': 'Maris Botero',
                'salon': 'Salon A',
                'image': 'laberintos_lenguaje_llms.jpg'
            },
            {
                'title': 'Micropython First Contact',
                'duration': '3:40 pm - 4:20 pm',
                'speaker': 'Gustavo Salvador Reynaga Aguilar',
                'salon': 'Salon B',
                'image': 'micropython_first_contact.jpg'
            },
            {
                'title': 'Charlas Relámpago',
                'duration': '4:35 pm - 5:20 pm',
                'speaker': 'Personal administrativo',
                'image': 'charlas_relampago.jpg'
            },
            {
                'title': 'Keynote 2',
                'duration': '5:25 pm - 6:10 pm',
                'speaker': 'Personal administrativo',
                'image': 'keynote_2.jpg'
            },
        ],
        'dia3': [
            {
                'title': 'Keynote 3',
                'duration': '9:00 am - 9:45 am',
                'speaker': 'Abigail',
                'image': 'keynote_3.jpg'
            },
            {
                'title': 'Prompt engineering: la llave maestra para aprovechar al máximo la generative IA',
                'duration': '10:00 am - 10:40 am',
                'speaker': 'Elizabeth Fuentes Leone',
                'salon': 'Salon A',
                'image': 'prompt_engineering_ia.jpg'
            },
            {
                'title': 'Reputación en Tiempo Real y Análisis de Sentimiento con Python',
                'duration': '10:00 am - 10:40 am',
                'speaker': 'Fabio Pinto Oviedo',
                'salon': 'Salon B',
                'image': 'reputacion_analisis_sentimiento.jpg'
            },
            {
                'title': 'Revolutionizing CI/CD with Python and Generative AI: Next-Level Automation in DevOps',
                'duration': '10:45 am - 11:25 am',
                'speaker': 'Alex Parra',
                'salon': 'Salon A',
                'image': 'cicd_python_devops.jpg'
            },
            {
                'title': 'Supercharge Python with Nuitka: Witness a 10-Year Plan Come to Life!',
                'duration': '10:45 am - 11:25 am',
                'speaker': 'Kay Hayen',
                'salon': 'Salon B',
                'image': 'nuitka_supercharge.jpg'
            },
            {
                'title': 'Tests efectivos con pytest, o sobre como escribir código duro de fallar',
                'duration': '11:30 am - 12:10 pm',
                'speaker': 'Diego Alberto Barriga Martínez',
                'salon': 'Salon A',
                'image': 'tests_pytest.jpg'
            },
            {
                'title': 'Todo lo que necesitas saber sobre Unicode, pero nunca se te ocurrió preguntar',
                'duration': '11:30 am - 12:10 pm',
                'speaker': 'Ariel Ortiz',
                'salon': 'Salon B',
                'image': 'unicode_python.jpg'
            },
            {
                'title': 'PyLadies Panel',
                'duration': '1:30 pm - 2:20 pm',
                'speaker': 'Capitulos PyLadies alrededor de América Latina',
                'image': 'pyladies_panel.jpg'
            },
            {
                'title': 'Una introducción al análisis de datos topológicos',
                'duration': '2:20 pm - 3:00 pm',
                'speaker': 'Kaled Corona',
                'salon': 'Salon A',
                'image': 'analisis_datos_topologicos.jpg'
            },
            {
                'title': 'Python y los esquemas ETL: El Pivote Esencial para la Inteligencia Artificial',
                'duration': '2:20 pm - 3:00 pm',
                'speaker': 'Hugo Ramírez',
                'salon': 'Salon B',
                'image': 'python_etl.jpg'
            },
            {
                'title': "A Journey into MLOps: Kubeflow's Magic Revealed",
                'duration': '3:05 pm - 3:45 pm',
                'speaker': 'César Leandro Higuita Pérez',
                'salon': 'Salon A',
                'image': 'mlops_kubeflow.jpg'
            },
            {
                'title': 'Del Oro Negro al Oro Digital: La Historia de un Ingeniero Convertido en Líder de Python',
                'duration': '3:05 pm - 3:45 pm',
                'speaker': 'Ivan Castañeda',
                'salon': 'Salon B',
                'image': 'oro_negro_digital.jpg'
            },
            {
                'title': 'Transformando Startups con Kubernetes: Gestión de Aplicaciones Django para un Crecimiento Explosivo',
                'duration': '3:50 pm - 4:30 pm',
                'speaker': 'Osiel Jacobo Torres',
                'salon': 'Salon A',
                'image': 'startups_kubernetes_django.jpg'
            },
            {
                'title': 'Sculpting Data for Machine Learning using Python: Generative AI edition',
                'duration': '3:50 pm - 4:30 pm',
                'speaker': 'Jigyasa Grover',
                'salon': 'Salon B',
                'image': 'sculpting_data_ml.jpg'
            },
            {
                'title': 'Keynote 4',
                'duration': '4:45 pm - 5:30 pm',
                'speaker': 'Personal administrativo',
                'image': 'keynote_4.jpg'
            },
            {
                'title': 'Cierre de Conferencia',
                'duration': '5:30 pm - 5:50 pm',
                'speaker': 'Personal administrativo',
                'image': 'cierre_conferencia.jpg'
            },
        ]
    }

    context = {'data': data}

    return render(request, 'scheduled.html', context)