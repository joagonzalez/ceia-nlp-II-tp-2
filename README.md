# ceia-nlp-II-tp-2
TP2 de la materia Procesamiento de Lenguaje Natural 2 de la carrera de esecialización en Inteligencia Artificial

TP1:
• Implementar un sistema de generación de texto (chatbot) que 
utilice la técnica de Retrieval-Augmented Generation (RAG). En 
este ejercicio, el chatbot será capaz de recuperar información de 
una base de datos (o un conjunto de documentos) y usarla para 
generar respuestas más completas, mejorando la calidad de las 
respuestas generadas.
• Entregables: Link a repo público y captura de video de chatbot
consultando al CV del alumno. Utilizar librería como Streamlit
(para capturar pantalla se puede utilizar OBS por ejemplo, es open 
source).  Link entregar: https://forms.gle/roAtRx2rXawaftjm7
• Se evalúa el código y la presentación (Repo con documentación).


Pasos
1. Preparación del entorno de trabajo: contar con IDE, cuenta de 
Pinecone (Starter), cuenta de Groq.
2. Cargar los CVs de los miembros del equipo y obtener los vectores 
de embeddings (ejemplo de modelo de embeddings).
3. Cargar los vectores a Pinecone.
4. Probar hacer una pregunta y, por medio de una comparación 
coseno, obtener el vector más cercano.
5. Implementar un simple chatbot para obtener respuestas sobre el 
documento cargado (CV del alumno).
