import pandas as pd

# Leer el archivo CSV
data = pd.read_csv('C:/Users/rvarg/Desktop/personal/5to semestre/Modelado de datos/Prueba-proyecto/Enfermedades/Disease_symptom_and_patient_profile_dataset.csv', encoding='ISO-8859-1')

# Convertir a JSON
json_data = data.to_json(orient='records')

print(json_data)

with open('C:/Users/rvarg/Desktop/personal/5to semestre/Modelado de datos/Prueba-proyecto/Herramientas/prueba.json', 'w') as f:
    f.write(json_data)

