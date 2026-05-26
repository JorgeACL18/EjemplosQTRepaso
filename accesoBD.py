import sqlite3 as dbapi

bbdd = dbapi.connect("bbddUsuarios.dat")
#print(bbdd)

cursor = bbdd.cursor()
#cursor.execute("""create table usuarios (nombre text, dni text, genero text, fallecido text, edad number)""")
'''
cursor.execute("""insert into Usuarios values ('Ana', '1234R', 'Femenino', 'True', 90)""")
cursor.execute("""insert into Usuarios values ('Pedro', '5678P', 'Masculino', 'False', 50)""")
cursor.execute("""insert into Usuarios values ('Luis', '91011L', 'Masculino', 'False', 20)""")
'''

#bbdd.commit()

cursor.execute("""select * from Usuarios""")

for usuario in cursor.fetchall():
    print(usuario)