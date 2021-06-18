from tkinter import ttk
from tkinter import *

import sqlite3

class Product:

	db_name='db.db'

	def __init__(self,window):

		self.wind=window
		self.wind.title("Aplicacion Productos")

		#Creando un Frame Container
		frame=LabelFrame(self.wind, text="Registra un nuevo producto")
		frame.grid(row=0,column=0,columnspan=3,pady=20)

		#Name Input
		Label(frame, text='Nombre: ').grid(row=1,column=0)
		self.name=Entry(frame)
		self.name.focus()
		self.name.grid(row=1,column=1)

		#Price Input
		Label(frame, text='Precio: ').grid(row=2,column=0)
		self.price=Entry(frame)
		self.price.grid(row=2,column=1)

		#Boton Agregar Producto
		ttk.Button(frame, text='Guardar Producto', command=self.add_products).grid(row=3,columnspan=2,sticky=W+E)

		#Mensaje
		self.message=Label(text='',fg='red')
		self.message.grid(row=3,column=0,columnspan=2,sticky=W+E)

		#Tabla
		self.tree=ttk.Treeview(height=10,columns=2)
		self.tree.grid(row=4, column=0,columnspan=2)
		self.tree.heading('#0',text='Nombre',anchor=CENTER)
		self.tree.heading('#1',text='Precio',anchor=CENTER)

		#Llenado de la tabla
		self.get_products()

	#
	def run_query(self,query,parameters=()):
		with sqlite3.connect(self.db_name) as conn:
			cursor=conn.cursor()
			result=cursor.execute(query, parameters)
			conn.commit()
		return result

	#
	def get_products(self):
		#claeanding table
		records=self.tree.get_children()
		for element in records:
			self.tree.delete(element)
		#query data
		query='SELECT * FROM product ORDER BY name DESC'
		db_rows=self.run_query(query)
		#filling data
		for row in db_rows:
			#print(db_rows)
			self.tree.insert('',0,text=row[1],values=row[2])

	# User Input Validation
	def validation(self):
		return len(self.name.get()) != 0 and len(self.price.get()) != 0
	#Agregar Producto
	def add_products(self):
		if self.validation():
			query='INSERT INTO product VALUES(NULL, ?, ?)'
			parameters=(self.name.get(), self.price.get())
			self.run_query(query, parameters)
			self.message['text']='Producto {} ha sido agregado'.format(self.name.get())
			#print('Datos Guardados')
		else:
			self.message['text']='Nombre y Precio son requeridos'
			#print('Nombre y Precio son requeridos')
		self.get_products()



if __name__=='__main__':
	window=Tk()
	application=Product(window)
	window.mainloop()
