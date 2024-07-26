import os
import requests
from PIL import Image
from io import BytesIO
import json

api_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiMGNkMjFmOGUtZTIyOC00ZTI4LTgwYjEtZjlkYTRmZDVmNGFmIiwidHlwZSI6ImFwaV90b2tlbiJ9.96hnVH1Sk4u-2TMoNoOlPOxjeHaJoPod0BWBqRtJtoY"

def generate_image(prompt, file_name):
    url = "https://api.edenai.run/v2/image/generation"
    payload = {
        "response_as_dict": True,
        "attributes_as_list": False,
        "show_base_64": False, 
        "show_original_response": True,
        "num_images": 1,
        "providers": ["amazon"],
        "text": prompt,
        "resolution": "1024x1024"
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": f"Bearer {api_key}"
    }
    
    response = requests.post(url, json=payload, headers=headers)
    data = response.json()
    
    if data["amazon"]["status"] == "success":
        image_url = data["amazon"]["items"][0]["image_resource_url"]
        image_data = requests.get(image_url).content
        
        # Guardar la imagen
        with open(file_name, 'wb') as file:
            file.write(image_data)
        
        print(f"Imagen guardada: {file_name}")
        print(f"URL de la imagen: {image_url}")
    else:
        print(f"Error al generar la imagen para '{prompt}': {data['amazon']['status']}")

# Lista de eventos
events = [
    {'prompt': 'Bienvenida al evento de programación en python', 'file_name': 'bienvenida_evento.jpg'},
    {'prompt': 'Conferencia de bienvenida del evento de programación de python', 'file_name': 'bienvenida_conferencia.jpg'},
    {'prompt': 'Conviértete en un maestro de la automatización: Aprende a implementar RPA y PYTHON en el sector financiero.', 'file_name': 'rpa_python_sector_financiero.jpg'},
    {'prompt': 'Seguridad en el Ecosistema de Paquetes Python', 'file_name': 'seguridad_paquetes_python.jpg'},
    {'prompt': 'DeepSignBridge: Traductor de Lenguaje de Señas en Tiempo Real Usando Transformers y Visión Computacional', 'file_name': 'deep_sign_bridge.jpg'},
    {'prompt': 'De pixeles a predicciones: Transformando la experiencia de videos con python', 'file_name': 'videos_python.jpg'},
    {'prompt': 'Desplegando tu aplicación Python sin morir en el intento', 'file_name': 'desplegando_python.jpg'},
    {'prompt': 'Pipelines en Python para Wireshark', 'file_name': 'pipelines_python_wireshark.jpg'},
    {'prompt': 'Espacios vectoriales con python y langchain', 'file_name': 'espacios_vectoriales_langchain.jpg'},
    {'prompt': 'Whisper y PyQt python en Acción', 'file_name': 'whisper_pyqt_accion.jpg'},
    {'prompt': 'How to organize a good environment in python', 'file_name': 'dependency_hell.jpg'},
    {'prompt': 'Insights Ocultos: Cómo la Estadística y Python Empoderan Decisiones Estratégicas', 'file_name': 'estadistica_python_decisiones.jpg'},
    {'prompt': 'Borges y las Narrativas Infinitas con LLMs', 'file_name': 'laberintos_lenguaje_llms.jpg'},
    {'prompt': 'Micropython First Contact', 'file_name': 'micropython_first_contact.jpg'},
    {'prompt': 'Charlas de programación', 'file_name': 'charlas_relampago.jpg'},
    {'prompt': 'Keynote programación', 'file_name': 'keynote_2.jpg'},
    {'prompt': 'Prompt engineering: la llave maestra para aprovechar al máximo la generative IA', 'file_name': 'prompt_engineering_ia.jpg'},
    {'prompt': 'Reputación en Tiempo Real y Análisis de Sentimiento con Python', 'file_name': 'reputacion_analisis_sentimiento.webp'},
    {'prompt': 'Revolutionizing CI/CD with Python and Generative AI: Next-Level Automation in DevOps', 'file_name': 'cicd_python_devops.jpg'},
    {'prompt': 'Supercharge Python with Nuitka', 'file_name': 'nuitka_supercharge.png'},
    {'prompt': 'Tests efectivos con pytest, o sobre como escribir código duro de fallar', 'file_name': 'tests_pytest.jpg'},
    {'prompt': 'Todo lo que necesitas saber de Unicode', 'file_name': 'unicode_python.png'},
    {'prompt': 'PyLadies Panel de mujeres programadoras', 'file_name': 'pyladies_panel.jpg'},
    {'prompt': 'Introducción al análisis de datos topológicos', 'file_name': 'analisis_datos_topologicos.jpg'},
    {'prompt': 'Python y los esquemas ETL: El Pivote Esencial para la Inteligencia Artificial', 'file_name': 'python_etl.jpeg'},
    {'prompt': "A Journey into MLOps: Kubeflow's Magic Revealed", 'file_name': 'mlops_kubeflow.jpg'},
    {'prompt': 'La Historia de un Ingeniero Convertido en Líder de Python', 'file_name': 'oro_negro_digital.jpg'},
    {'prompt': 'Transformando Startups con Kubernetes: Gestión de Aplicaciones Django para un Crecimiento Explosivo', 'file_name': 'startups_kubernetes_django.jpg'},
    {'prompt': 'Sculpting Data for Machine Learning using Python: Generative AI edition', 'file_name': 'sculpting_data_ml.jpg'},
    {'prompt': 'Keynote 4', 'file_name': 'keynote_4.jpg'},
    {'prompt': 'Cierre de Conferencia', 'file_name': 'cierre_conferencia.jpg'}
]

# Directorio donde se guardan las imágenes
directory_path = 'src/pycon/static/img/events'

# Crear el directorio si no existe
if not os.path.exists(directory_path):
    os.makedirs(directory_path)

# Eliminar imágenes anteriores
for file_name in os.listdir(directory_path):
    if file_name in [event['file_name'] for event in events]:
        file_path = os.path.join(directory_path, file_name)
        if os.path.isfile(file_path):
            os.remove(file_path)

# Generar nuevas imágenes
for event in events:
    file_path = os.path.join(directory_path, event['file_name']) 
    generate_image(event['prompt'], file_path)