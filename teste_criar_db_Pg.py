import psycopg2

def conecta_db():
  con = psycopg2.connect(host='localhost', port="5001", 
                         database='dbteste2',
                         user='postgres', 
                         password='postgres')
  return con


def criar_db(sql):
  con = conecta_db()
  cur = con.cursor()
  cur.execute(sql)
  con.commit()
  con.close()


# sql = 'DROP TABLE IF EXISTS public.colaboradores'
# criar_db(sql)
sql = '''CREATE TABLE IF NOT EXISTS public.colaboradores 
      ( matricula     text PRIMARY KEY, 
        nome           text, 
        sobrenome          text, 
        cargo  text, 
        codigo_cargo    text, 
        lider       text, 
        matricula_lider text, 
        salario       text, 
        senha         text, 
        status_colaborador         text 
      )'''
criar_db(sql)



sql_data = '''INSERT INTO public.colaboradores VALUES (
  '1225', 
  'CLAUDIO', 
  'RABA',
  'GERENTE', 
  'G2', 
  'GILSON',
  'G3',
  '2000', 
  '157A', 
  'CONTRATADO' 
  )'''

def inserir_db(sql_data):
    con = conecta_db()
    cur = con.cursor()
    try:
        cur.execute(sql_data)
        con.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        con.rollback()
        cur.close()
        return 1
    cur.close()

inserir_db(sql_data)
