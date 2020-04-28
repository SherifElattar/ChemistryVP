import sqlite3
conn = sqlite3.connect('chemDemo.db')
c = conn.cursor()
c.execute('''CREATE TABLE reactions
             (elem1 text, elem2 text, result text, common text)''')
c.execute("INSERT INTO reactions VALUES ('hydrogen','oxygen','h2o','water')")
conn.commit()
conn.close()
