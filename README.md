# PD03_04 Modelado de Datos
# E04:	CouchDB Integrantes: Rogerio Emmanuel Canto Romero, Diego Enrique Duran Pavia, Raul Alberto Kumul Varguez.


# Haciendo	uso	de	un	repositorio	de	Github,	documente	lo	siguiente:
# a. Agregar el	archivo	del	dataset 
Se puede localizar en nuestro repositorio  "PD03_04" el dataset original por el nombre de:
"Disease_symptom_and_patient_profile_dataset.csv" 

# El dataset:
El dataset fue rescatado de Kaggle:
![Imagenweb](imagenes/Kaggle.png)
Se decidió utilizar este archivo en específico, ya que se notaba bastante ordenado y comprensible, y consideramos que sería fácil trabajar con él.



Como sabemos los archivos CSV son un tipo de documento en formato abierto sencillo para representar datos en forma de tabla, en las que las columnas se separan por comas y las filas por saltos de línea, pero una de las particularidades de nuestra base de datos "Couch DB" es que solo maneja archivos en formato JSON, por lo que el primer paso es convertir el dataset de csv a JSON

# Convertin a JSON
![Imagenweb](imagenes/BING1.jpeg)

Usando La herramienta de inteligencia artificial de BING se generó un código en Python que nos permite transformar un archivo de Excel a JSON (el código se puede encontrar en nuestro repositorio por el nombre de "Excel-To-JSON.py"), como habíamos mencionado anteriormente nuestro data set se encuentra en formato csv, pero por las propiedades del mismo puede ser interpretado como un Excel, por lo que el código nos fue útil para conseguir que nuestro dataset este en formato JSON y listo para ser subido a nuestra base de datos (En CouchDB).

![Imagenweb](imagenes/exel-json.jpeg)

# b. Descripción	del	dataset
![Imagenweb](imagenes/dataset.jpeg)

El Data set cuenta con los datos de 349 pacientes, dentro de los que se recopila la siguiente información:

Enfermedad: El nombre de la enfermedad o condición medica.

Fiebre: Indica si el paciente tiene o no fiebre.

Tos: Indica si el paciente tiene o no tos.

Fatiga: Indica si el paciente presenta o no fatiga.

Dificultad para respirar: Indica si el paciente tiene o no dificultades para respirar.

Edad: La edad en años del paciente.

Sexo: Masculino o femenino.

Presión arterial: Indica el nivel de la presión arterial del paciente.

Nivel de colesterol: Nivel de colesterol del paciente.

Resultado del análisis: Muestra si el paciente está o no enfermo de lo que se esperaba.



# c. Descripción	del	diccionario	de	datos	del	dataset
Debido a que trabajamos con CouchDB y este tiene bastante encapsulamiento y modularidad, no hay una forma específica para agregar los documentos, a continuación mostraremos un ejemplo del formato que llevan los JSON de nuestra DB y un ejemplo tomada de la misma DB

![Alt text](imagenes/jason111.jpeg)
![Alt text](imagenes/json2.jpeg)

# d. Descripción	del	modelado	del	dataset	según	la	BD	NoSQL

# e. Descripción	de	la	BD	NoSQL	y	las	herramientas	que	se	utilizaron.
La base de datos NoSQL se centra en la relación entre varias enfermedades, los síntomas asociados, y los perfiles de pacientes. Es una herramienta valiosa para el análisis de datos en el campo de la medicina. 

•	Formato de Datos: Al estar en JSON, la base de datos es fácilmente accesible y manipulable, lo que permite realizar análisis y filtrar información de manera eficiente.

•	Potencial de Análisis Estadístico y de Datos: La estructura de la base de datos facilita la realización de análisis estadísticos, como la identificación de tendencias, correlaciones entre síntomas y enfermedades, y la evaluación de factores de riesgo.

Por otro lado, para la creación de esta base de datos se utilizó un programa en Python (subidor.py) para subir los documentos en formato JSON a la base que está en CouchDB, el código fue generado por la inteligencia artificial Bing, únicamente se modificaron la dirección de origen archivo que se va a subir y la dirección de destino a la base de datos. También se utilizo Visual Studio Code para realizar dichos cambios y verificar que todo funcione de manera adecuada.

# f. Descripción	de	la	importación	de	sus	datos.
Para esto ya debimos de haber creado nuestra base de datos.
Después, como ya habíamos comentado en el inciso e, generamos un código con la inteligencia artificial Bing, una vez generado el código y lo modificamos para poner nuestro usuario y contraseña de la base de datos procedemos a correr el codigo en el Visual studio code. 

![Alt text](imagenes/importacion1.jpeg)

Esperamos un momento a que se suban los archivos y luego observamos nuestra base de datos con los archivos.

![Alt text](imagenes/importacion2.jpeg)

# g. Definir	 y	 describir	 al	 menos	 5	 sentencias	 para	 cada	 una	 de	 las	
# operaciones	CRUD (Create,	Read,	Update,	Delete) en	la	BD.	
