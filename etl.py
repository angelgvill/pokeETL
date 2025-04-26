import requests
import sqlite3

# Extracción de datos
response = requests.get('https://pokeapi.co/api/v2/pokemon/ditto')
data = response.json()

# Transformación de datos
transformed_data = {
    'id': data['id'],
    'name': data['name'],
    'height': data['height'],
    'weight': data['weight']
}

# Carga de datos
conn = sqlite3.connect('pokemon.db')
c = conn.cursor()

c.execute('''
    CREATE TABLE IF NOT EXISTS Pokemon (
        id INTEGER,
        name TEXT,
        height INTEGER,
        weight INTEGER
    )
''')

c.execute('''
    INSERT INTO Pokemon (id, name, height, weight)
    VALUES (:id, :name, :height, :weight)
''', transformed_data)

conn.commit()
conn.close()
