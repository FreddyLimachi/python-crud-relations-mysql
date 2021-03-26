from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from Database_Interaction import *
from tkinter import filedialog
from Authenticator import *
import time
import webbrowser
from PIL import Image, ImageTk
import itertools
from random import randint
from statistics import mean
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import openpyxl
import calendar, locale
import tkinter as Tkinter
import tkinter.font as tkFont
#import os

class Functionality(Authenticator):

	def Access(self,event):
		Obj=Usuario()
		Validar=Obj.Consultar(self.User.get(),self.Password.get())
		if Validar=="Administrador":
			self.Default=self.User.get()
			self.WindowLogin.destroy()
			self.Privilege_Value=0
			self.Create_Main_Window()
			
		elif Validar=="AMAPAFA":
			self.Default=self.User.get()
			self.WindowLogin.destroy()
			self.Privilege_Value=1
			self.Create_Main_Window()
			
		elif Validar=="Qaliwarma":
			self.Default=self.User.get()
			self.WindowLogin.destroy()
			self.Privilege_Value=2
			self.Create_Main_Window()

		elif Validar=='Error_User':
			messagebox.showwarning('Mensaje','Error de contraseña de la base de datos')

		elif Validar=='Error_DB':
			messagebox.showwarning('Mensaje','La base de datos no existe')

		elif Validar=='Error_unknown':
			messagebox.showwarning('Mensaje','Se nego la conexion con la base de datos, consulte con el administrador de la aplicación')

		else:
			messagebox.showinfo("Mensaje","Login Incorrecto")
			self.CuadroUser.delete(0,END)
			self.CuadroPass.delete(0,END)
			self.CuadroUser.focus()

	def InsertarAge(self):
		pass

	def AgregarAge(self):
		for age in self.Datos.ConsultarYear():
			self.AgeAnterior.insert_radiobutton(index=0,label=" Ver Año "+str(age[1]+'       '),variable=self.ValorAge,value=int(age[1]),command=self.SeleccionarAge)
	
	def SeleccionarAge(self):
		try:
			self.InsertarTabla()
			self.InsertarIG()
			self.IngresoTotal()
			self.InsertarIG()
						
		except AttributeError:
			pass
	
	def SalirAplicacion(self):
		Valor=messagebox.askquestion("Salir","¿Deseas salir de la aplicación?")
		if Valor=="yes":
			self.WindowMain.destroy()	
		
	def CambiarTexto(self,event):
		Datos=ModInterfaz()
		if len(self.EscribirTexto.get())>90 or len(self.EscribirTexto.get())<10:
			messagebox.showwarning("Mensaje",'El texto debe de contener un mímino de 10 carácteres y un máximo de 90 carácteres')
			self.TopTexto.focus_set()
		else:	
			try:
				Datos.ModificarTexto(self.EscribirTexto.get())
				self.InsertarTexto()
				messagebox.showinfo("Mensaje","El texto de presentación ha sido modificado con éxito")
				self.Pestana.select(self.Pes1)
				self.EscribirTexto.set("")
				self.TopTexto.destroy()
			except:
				messagebox.showinfo("Mensaje","Use comillas dobles")
				self.TopTexto.focus_set()

	def InsertarTexto(self):
		Datos=ModInterfaz()
		self.MensajeBienvenida['text']=''.join(x for x in Datos.ConsultarTexto() if x not in '()')

	def CambiarImagen(self):
		Datos=ModInterfaz()
		file_name=filedialog.askopenfilename(title='Cargar',filetypes=[('GIF FILES', '*.png')])
		Datos.ModificarImagen(str(file_name))

		self.InsertarImagen()
		messagebox.showinfo("Mensaje","La Imagen de Presentación ha sido Actualizada con Éxito")

	def InsertarImagen(self):
		global LabelImagen
		Datos=ModInterfaz()
		pil_img = Image.open(Datos.ConsultarImagen("1"))
		pil_img = pil_img.resize((300, 250), Image.ANTIALIAS)
		pil_img = ImageTk.PhotoImage(pil_img)
		self.LabelImagen.config(image=pil_img)
		self.LabelImagen.image=pil_img

	def AplicarPagos(self,event):
		self.Datos.ConfigurarPago(self.CuotaSocio.get(),self.CuotaIngresante.get(),str(self.ValorAge.get()),self.Default)
		messagebox.showinfo("Mensaje","Configuración establecida con éxito")
		self.ConsultarPagos()
		self.TopPagos.destroy()

	def ConsultarPagos(self):
		Arreglo=self.Datos.ConsultarPago(str(self.ValorAge.get()),self.Default)
		for row in Arreglo:
			self.CuotaSocio.set(row[1])
			self.CuotaIngresante.set(row[2])

	def AnadirEstudiante(self,event):

		if self.ValEM()!=True:
			pass
		
		else:
			'''for i in self.Datos.CargarApoderado(str(self.ValorN),'datos_apoderado','Apoderado'):
   				N=i[8]
			self.Datos.ModNEstudiante(str(K),'Sumar')
			if self.CuotaParteMore.get()==1:
				self.Datos.RegistrarEstudiante(self.APEMore.get().upper().strip(),self.AMEMore.get().upper().strip()," ".join(self.NomEMore.get().upper().split()),self.DNIEMore.get(),self.GradoMore.get(),self.SeccionMore.get(),'100000.00',str(self.ValorN),self.EstadoMore.get(),str(self.ValorAge.get()),self.Default)
			if self.CuotaParteMore.get()==2:
				self.Datos.RegistrarEstudiante(self.APEMore.get().upper().strip(),self.AMEMore.get().upper().strip()," ".join(self.NomEMore.get().upper().split()),self.DNIEMore.get(),self.GradoMore.get(),self.SeccionMore.get(),self.PagoMore.get(),str(self.ValorN),self.EstadoMore.get(),str(self.ValorAge.get()),self.Default)

			self.TopAnadir.destroy()
			self.NomMore.set("")
			self.DNIMore.set("")
			self.GradoMore.set("")
			self.SeccionMore.set("")	
			self.PagoMore.set("0")
			self.CuotaParteMore.set(None)
			self.EstadoMore.set('Normal')
			self.SeleccionarAge(),self.ConsultarNA()'''
			messagebox.showinfo("Mensaje","El estudiante ah sido agregado con éxito")

	def DesaparecerGris(self,event):
		
		if self.DNIAll.get()=="Escriba el DNI":
			self.CuadroPasar.delete(0, END)
			self.CuadroPasar.config(foreground = 'black',justify="right")
		
		elif self.DNIAll.get() == "":
			self.CuadroPasar.insert(0,"Escriba el DNI")
			self.CuadroPasar.config(foreground = 'gray',justify="left")

	def GrisBuscar(self,event):
		if self.CuadroBuscar.get()=="Buscar":
			self.CuadroBuscar.delete(0, END)
			self.CuadroBuscar.config(foreground = 'black')
		
		elif self.CuadroBuscar.get() == "":
			self.CuadroBuscar.insert(0,"Buscar")
			self.CuadroBuscar.config(foreground = 'gray')

	def CargarAll(self):

		if self.DNIAll.get().isdigit()==False:
			messagebox.showinfo("Mensaje","Ingrese cáracteres numéricos")

		elif len(self.DNIAll.get())<8 or len(self.DNIAll.get())>8:
			messagebox.showinfo("Mensaje","Ingrese correctamente el DNI")

		else:
			try:
				for m in self.Datos.CargarDNIApoderado(self.DNIAll.get(),self.Default):
					N=str(m[1])
					self.APA.set(m[1])
					self.AMA.set(m[2])
					self.NomA.set(m[3])
					self.DNIA.set(m[4])
					self.DirecA.set(m[5])
					cont=m[8]
					self.APP.set(m[9])
					self.AMP.set(m[10])
					self.NomP.set(m[11])
					self.DNIP.set(m[12])
					self.APM.set(m[13])
					self.AMM.set(m[14])
					self.NomM.set(m[15])
					self.DNIM.set(m[16])

				self.ArregloEstudiante=[]
				for i in range(1,cont+1):
					self.ArregloEstudiante.append(i)
				
				self.TipoRoM='C'
				self.ComboNEstudiantes.current(cont-1)
				self.SelecNEstudiantes(self.ComboNEstudiantes)

				if cont==1:
						self.CargarEstudiante1()
				elif cont==2:
						self.CargarEstudiante1(),self.CargarEstudiante2()
				elif cont==3:
						self.CargarEstudiante1(),self.CargarEstudiante2(),self.CargarEstudiante3()
				elif cont==4:
						self.CargarEstudiante1(),self.CargarEstudiante2(),self.CargarEstudiante3(),self.CargarEstudiante4()
				elif cont==5:
					self.CargarEstudiante1(),self.CargarEstudiante2(),self.CargarEstudiante3(),self.CargarEstudiante4(),self.CargarEstudiante5()
				elif cont==6:
					self.CargarEstudiante1(),self.CargarEstudiante2(),self.CargarEstudiante3(),self.CargarEstudiante4(),self.CargarEstudiante5(),self.CargarEstudiante6()
				
				self.DNIAll.set("")
			except UnboundLocalError:
				messagebox.showinfo('Mensaje','No existe un registro con ese DNI')
				self.DNIAll.set("")

	def SeleccionarApoderado(self,event):
		if self.ComboApoderado.get()=='Padre':
			self.APA.set(self.APP.get())
			self.AMA.set(self.AMP.get())
			self.NomA.set(self.NomP.get())
			self.DNIA.set(self.DNIP.get())
			self.DirecA.set(self.DirecP.get())
			
		if self.ComboApoderado.get()=='Madre':
			self.APA.set(self.APM.get())
			self.AMA.set(self.AMM.get())
			self.NomA.set(self.NomM.get())
			self.DNIA.set(self.DNIM.get())
			self.DirecA.set(self.DirecM.get())
		
		if self.ComboApoderado.get()=='Otro':
			self.APA.set("")
			self.AMA.set("")
			self.NomA.set("")
			self.DNIA.set("")
			self.DirecA.set("")			

	def SelecCuotaAmapafa(self,event):
		if self.ComboCuota.get()=='Socio':
			self.CuotaApoderado=self.CuotaSocio.get()
		elif self.ComboCuota.get()=='Ingresante':
			self.CuotaApoderado=self.CuotaIngresante.get()
		elif self.ComboCuota.get()=='Exonerado':
			self.CuotaApoderado='100000.00'

	def SelecCuotaEstudiante(self):
		if self.TipoPago1.get()!='Exonerado':
			self.ValorPagoE1=self.TipoPago1.get()

		if self.TipoPago2.get()!='Exonerado':
			self.ValorPagoE2=self.TipoPago2.get()

		if self.TipoPago3.get()!='Exonerado':
			self.ValorPagoE3=self.TipoPago3.get()

		if self.TipoPago4.get()!='Exonerado':
			self.ValorPagoE4=self.TipoPago4.get()

		if self.TipoPago5.get()!='Exonerado':
			self.ValorPagoE5=self.TipoPago5.get()

		if self.TipoPago6.get()!='Exonerado':
			self.ValorPagoE6=self.TipoPago6.get()

	def Registrar(self):

		#if self.ValidarDatos()!=True:
		#	pass

		if self.ValidarDatosAPM()!=True:
			pass

		else:
		
			'''self.SelecCuotaEstudiante()
			self.RelacionarEstudiante()
			
			if self.NEstudiantes.get()=='1 Estudiante a cargo':
				self.RegEstu1()
				ValorNEstudiante='1'
			elif self.NEstudiantes.get()=='2 Estudiantes a cargo':
				self.RegEstu1(),self.RegEstu2()
				ValorNEstudiante='2'
			elif self.NEstudiantes.get()=='3 Estudiantes a cargo':
				self.RegEstu1(),self.RegEstu2(),self.RegEstu3()
				ValorNEstudiante='3'
			elif self.NEstudiantes.get()=='4 Estudiantes a cargo':
				self.RegEstu1(),self.RegEstu2(),self.RegEstu3(),self.RegEstu4()
				ValorNEstudiante='4'
			elif self.NEstudiantes.get()=='5 Estudiantes a cargo':	
				self.RegEstu1(),self.RegEstu2(),self.RegEstu3(),self.RegEstu4(),self.RegEstu5()
				ValorNEstudiante='5'
			elif self.NEstudiantes.get()=='6 Estudiantes a cargo':
				self.RegEstu1(),self.RegEstu2(),self.RegEstu3(),self.RegEstu4(),self.RegEstu5(),self.RegEstu6()
				ValorNEstudiante='6'

			self.Datos.RegistrarApoderado(
			self.APA.get().upper().strip(),
			self.AMA.get().upper().strip(),
			" ".join(self.NomA.get().upper().split()),
			self.DNIA.get(),
			" ".join(self.DirecA.get().upper().split()),
			str(self.CuotaApoderado),
			self.Multa.get(),
			ValorNEstudiante,
			self.APP.get().upper().strip(),
			self.AMP.get().upper().strip(),
			" ".join(self.NomP.get().upper().split()),
			self.DNIP.get(),
			self.APM.get().upper().strip(),
			self.AMM.get().upper().strip(),
			" ".join(self.NomM.get().upper().split()),
			self.DNIM.get(),
			str(self.ValorAge.get()),
			self.Default)'''
			
			messagebox.showinfo("Mensaje","Los datos han sido registrados con éxito")
			#self.SeleccionarAge(),self.ConsultarNM(),self.ConsultarNA(),self.LimpiarDatos()
			
	def SelecNEstudiantes(self,event):
		if self.TipoRoM=='R':
			T='R'
		else:
			T='C'
		if self.NEstudiantes.get()=="1 Estudiante a cargo":
			self.SelecHijo1(T)
		elif self.NEstudiantes.get()=="2 Estudiantes a cargo":
			self.SelecHijo1(T),self.SelecHijo2(T)
		elif self.NEstudiantes.get()=="3 Estudiantes a cargo":
			self.SelecHijo1(T),self.SelecHijo2(T),self.SelecHijo3(T)
		elif self.NEstudiantes.get()=="4 Estudiantes a cargo":
			self.SelecHijo1(T),self.SelecHijo2(T),self.SelecHijo3(T),self.SelecHijo4(T)
		elif self.NEstudiantes.get()=="5 Estudiantes a cargo":
			self.SelecHijo1(T),self.SelecHijo2(T),self.SelecHijo3(T),self.SelecHijo4(T),self.SelecHijo5(T)
		elif self.NEstudiantes.get()=="6 Estudiantes a cargo":
			self.SelecHijo1(T),self.SelecHijo2(T),self.SelecHijo3(T),self.SelecHijo4(T),self.SelecHijo5(T),self.SelecHijo6(T)

	def RelacionarEstudiante(self):
		Relacion=self.Datos.RelacionarEstudiante()
		if Relacion==None:
			self.Relacion='1'
		else:
			self.Relacion=str(Relacion+1)

	def LimpiarDatos(self):
		self.APP.set("")
		self.AMP.set("")
		self.NomP.set("")
		self.DNIP.set("")
		self.DirecP.set("")
		self.APM.set("")
		self.AMM.set("")
		self.NomM.set("")
		self.DNIM.set("")
		self.DirecM.set("")
		self.APA.set("")
		self.AMA.set("")
		self.NomA.set("")
		self.DNIA.set("")
		self.DirecA.set("")
		self.Apoderado.set('Apoderado')
		self.CuotaAmapafa.set('Tipo de cuota')
		self.Multa.set("0")
		self.CuadroMulta.config(text='0.00')
		self.BotonModificar.config(state='disabled')
		self.BotonModificar.place(y=1000)
		self.BotonCancel.config(state='disabled')
		self.BotonCancel.place(y=1000)
		self.BotonRegistrar.config(state='normal')
		self.BotonDeshacer.config(state='normal')
		self.BotonRegistrar.place(x=460,y=6,height=25)
		self.BotonDeshacer.place(x=580,y=6,height=25)
		self.BotonAll.config(state='normal')
		self.LimpiarEstudiante()
		self.ComboNEstudiantes.config(state='readonly')
		self.NEstudiantes.set('Numero de Estudiantes a cargo')
		self.TipoRoM='R'

	def LimpiarEstudiante(self):
		self.APE1.delete(0,END)
		self.APE2.delete(0,END)
		self.APE3.delete(0,END)
		self.APE4.delete(0,END)
		self.APE5.delete(0,END)
		self.APE6.delete(0,END)
		self.AME1.delete(0,END)
		self.AME2.delete(0,END)
		self.AME3.delete(0,END)
		self.AME4.delete(0,END)
		self.AME5.delete(0,END)
		self.AME6.delete(0,END)
		self.NomE1.delete(0,END)
		self.NomE2.delete(0,END)
		self.NomE3.delete(0,END)
		self.NomE4.delete(0,END)
		self.NomE5.delete(0,END)
		self.NomE6.delete(0,END)
		self.DNIE1.delete(0,END)
		self.DNIE2.delete(0,END)
		self.DNIE3.delete(0,END)
		self.DNIE4.delete(0,END)
		self.DNIE5.delete(0,END)
		self.DNIE6.delete(0,END)
		self.Grado1.set('○')
		self.Grado2.set('○')
		self.Grado3.set('○')
		self.Grado4.set('○')
		self.Grado5.set('○')
		self.Grado6.set('○')
		self.Seccion1.set('○')
		self.Seccion2.set('○')
		self.Seccion3.set('○')
		self.Seccion4.set('○')
		self.Seccion5.set('○')
		self.Seccion6.set('○')
		self.TipoPago1.set('0')
		self.TipoPago2.set('0')
		self.TipoPago3.set('0')
		self.TipoPago4.set('0')
		self.TipoPago5.set('0')
		self.TipoPago6.set('0')
		self.ComboEstado1.current(0)
		self.ComboEstado2.current(0)
		self.ComboEstado3.current(0)
		self.ComboEstado4.current(0)
		self.ComboEstado5.current(0)
		self.ComboEstado6.current(0)
		self.TextoMonto1['text']='0.00'
		self.TextoMonto2['text']='0.00'
		self.TextoMonto3['text']='0.00'
		self.TextoMonto4['text']='0.00'
		self.TextoMonto5['text']='0.00'
		self.TextoMonto6['text']='0.00'

		self.APE1.config(state='disabled')
		self.AME1.config(state='disabled')
		self.NomE1.config(state='disabled')
		self.DNIE1.config(state='disabled')
		self.ComboGrado1.config(state='disabled')
		self.ComboSeccion1.config(state='disabled')
		self.ComboEstado1.config(state='disabled')
		self.ComboTipoPago1.config(state='disabled')
		self.APE2.config(state='disabled')
		self.AME2.config(state='disabled')
		self.NomE2.config(state='disabled')
		self.DNIE2.config(state='disabled')
		self.ComboGrado2.config(state='disabled')
		self.ComboSeccion2.config(state='disabled')
		self.ComboEstado2.config(state='disabled')
		self.ComboTipoPago2.config(state='disabled')
		self.APE3.config(state='disabled')
		self.AME3.config(state='disabled')
		self.NomE3.config(state='disabled')
		self.DNIE3.config(state='disabled')
		self.ComboGrado3.config(state='disabled')
		self.ComboSeccion3.config(state='disabled')
		self.ComboEstado3.config(state='disabled')
		self.ComboTipoPago3.config(state='disabled')
		self.APE4.config(state='disabled')
		self.AME4.config(state='disabled')
		self.NomE4.config(state='disabled')
		self.DNIE4.config(state='disabled')
		self.ComboGrado4.config(state='disabled')
		self.ComboSeccion4.config(state='disabled')
		self.ComboEstado4.config(state='disabled')
		self.ComboTipoPago4.config(state='disabled')
		self.APE5.config(state='disabled')
		self.AME5.config(state='disabled')
		self.NomE5.config(state='disabled')
		self.DNIE5.config(state='disabled')
		self.ComboGrado5.config(state='disabled')
		self.ComboSeccion5.config(state='disabled')
		self.ComboEstado5.config(state='disabled')
		self.ComboTipoPago5.config(state='disabled')
		self.APE6.config(state='disabled')
		self.AME6.config(state='disabled')
		self.NomE6.config(state='disabled')
		self.DNIE6.config(state='disabled')
		self.ComboGrado6.config(state='disabled')
		self.ComboSeccion6.config(state='disabled')
		self.ComboEstado6.config(state='disabled')
		self.ComboTipoPago6.config(state='disabled')
		
	def CancelarDatos(self):
		Valor=messagebox.askquestion("Confirmar","¿Desea Cancelar la Operación?")
		if Valor=="yes":	
			self.Pestana.select(self.Pes4)
			self.LimpiarDatos()		

	def CambiarOrden(self):
		if self.ValorOrdenar.get()==0:
			self.OrdenReg='N'
		elif self.ValorOrdenar.get()==1:
			self.OrdenReg='OA'
		else:
			self.OrdenReg='GS'
		self.InsertarTabla()

	def InsertarTabla(self):

		Tabla=self.TablaApoderado.get_children()
		for elemento in Tabla:
			self.TablaApoderado.delete(elemento)
		Arreglo=self.Datos.ConsultarApoderado(self.OrdenReg,str(self.ValorAge.get()),self.Default)
		cont=1
		for row in Arreglo:
			if cont % 2 != 0:
				if row[6]<100000.00:
					self.TablaApoderado.insert("",index="end",text=row[0],values=(cont,row[1]+' '+row[2]+' '+row[3],row[4], row[5],row[6],row[7],row[8]), tags=('LineaBlanco',))
				else:
					self.TablaApoderado.insert("",index="end",text=row[0],values=(cont,row[1]+' '+row[2]+' '+row[3],row[4], row[5],'Exonerado',row[7],row[8]), tags=('LineaBlanco',))
			elif cont % 2 == 0:
				if row[6]<100000.00:
					self.TablaApoderado.insert("",index="end",text=row[0],values=(cont,row[1]+' '+row[2]+' '+row[3],row[4], row[5],row[6],row[7],row[8]), tags=('LineaColor',))
				else:
					self.TablaApoderado.insert("",index="end",text=row[0],values=(cont,row[1]+' '+row[2]+' '+row[3],row[4], row[5],'Exonerado',row[7],row[8]), tags=('LineaColor',))
			cont=cont+1

		Tabla=self.TablaEstudiante.get_children()
		for elemento in Tabla:
			self.TablaEstudiante.delete(elemento)
		Arreglo=self.Datos.ConsultarEstudiante(self.OrdenReg,str(self.ValorAge.get()),self.Default)
		cont=1
		for row in Arreglo:
			if cont % 2 != 0:
				if row[7]<100000.00:
					self.TablaEstudiante.insert("",index="end",text=row[0],values=(cont,row[1]+' '+row[2]+' '+row[3],row[4],row[5],row[6],row[7]), tags=('LineaBlanco',))
				else:
					self.TablaEstudiante.insert("",index="end",text=row[0],values=(cont,row[1]+' '+row[2]+' '+row[3],row[4],row[5],row[6],'Exonerado'), tags=('LineaBlanco',))
			elif cont % 2 == 0:
				if row[7]<100000.00:
					self.TablaEstudiante.insert("",index="end",text=row[0],values=(cont,row[1]+' '+row[2]+' '+row[3],row[4],row[5],row[6],row[7]), tags=('LineaColor',))
				else:
					self.TablaEstudiante.insert("",index="end",text=row[0],values=(cont,row[1]+' '+row[2]+' '+row[3],row[4],row[5],row[6],'Exonerado'), tags=('LineaColor',))
			cont=cont+1
		
		Tabla=self.TablaPadre.get_children()
		for elemento in Tabla:
			self.TablaPadre.delete(elemento)
		Arreglo=self.Datos.ConsultarPadre(self.OrdenReg,str(self.ValorAge.get()),self.Default)
		cont=1
		for row in Arreglo:		           
				if cont % 2 != 0:
					self.TablaPadre.insert("",index="end",text=row[0],values=(cont,row[1]+' '+row[2]+' '+row[3],row[4], row[5]), tags=('LineaBlanca',))
				elif cont % 2 == 0:
					self.TablaPadre.insert("",index="end",text=row[0],values=(cont,row[1]+' '+row[2]+' '+row[3],row[4], row[5]), tags=('LineaColor',))
				cont=cont+1

		Tabla=self.TablaMadre.get_children()
		for elemento in Tabla:
			self.TablaMadre.delete(elemento)
		Arreglo=self.Datos.ConsultarMadre(self.OrdenReg,str(self.ValorAge.get()),self.Default)
		cont=1
		for row in Arreglo:
			if cont % 2 != 0:
				self.TablaMadre.insert("",index="end",text=row[0],values=(cont,row[1]+' '+row[2]+' '+row[3],row[4], row[5]), tags=('LineaBlanco',))
			elif cont % 2 == 0:
				self.TablaMadre.insert("",index="end",text=row[0],values=(cont,row[1]+' '+row[2]+' '+row[3],row[4], row[5]), tags=('LineaColor',))
			cont=cont+1

	def EliminarDatos(self):

		try:
			if self.TablaApoderado.item(self.TablaApoderado.selection())["values"]:
				Valor=messagebox.askquestion("Mensaje",'Al eliminar este registro lo haras en paquete junto a los registros correspondientes de las secciones "Padre", "Madre" y "Estudiante", ¿desea continuar?')
				if Valor=="yes":
					self.Datos.EliminarSocio(str(self.TablaApoderado.item(self.TablaApoderado.selection())["text"]))

					self.SeleccionarAge(),self.ConsultarNM(),self.ConsultarNA()
					messagebox.showinfo("Mensaje","El socio ha sido eliminado con éxito")

			elif self.TablaPadre.item(self.TablaPadre.selection())["values"] or self.TablaMadre.item(self.TablaMadre.selection())["values"]:
				messagebox.showinfo("Mensaje",'Si quiere eliminar este registro hagalo en paquete desde la sección "Apoderado"')

			elif self.TablaEstudiante.item(self.TablaEstudiante.selection())["values"]:
				ValorN=str(self.TablaEstudiante.item(self.TablaEstudiante.selection())["text"])

				for i in self.Datos.CargarEstudiante(ValorN,'N'):
	   				K=i[9]
				for i in self.Datos.CargarApoderado(str(K),'Apoderado'):
	   				N=i[7]
				if N>1:
					Valor=messagebox.askquestion("Mensaje","¿Desea eliminar este registro?")
					if Valor=="yes":
						self.Datos.EliminarDatos(ValorN,'datos_estudiante')
						self.Datos.ModNEstudiante(str(K),'Restar')
						self.SeleccionarAge(),self.ConsultarNM(),self.ConsultarNA()

						messagebox.showinfo("Mensaje","El Estudiante ha sido eliminado con éxito")
				else:
					for m in self.Datos.CargarApoderado(str(K),'Apoderado'):
						APA=m[0]
						AMA=m[1]
						NomA=m[2]
					if str(self.ValorAge)==time.strftime("%Y"):
						Palabra='apodera'
					else:
						Palabra='apoderó'
					Valor=messagebox.askquestion("Mensaje",'Este es el único Estudiante en el año {} que {} el(la) Sr(a):"{} {} {}", si elimina este registro tambien se eliminará los registros correspondientes de las secciones "Apoderado", "Padre" y "Madre"; ¿desea continuar?'.format(self.ValorAge,Palabra,NomA,APA,AMA))
					if Valor=="yes":
						self.Datos.EliminarSocio(str(K))
						self.SeleccionarAge(),self.ConsultarNM(),self.ConsultarNA()
						messagebox.showinfo("Mensaje","El socio ha sido eliminado con éxito")

			elif self.TablaIA.item(self.TablaIA.selection())["values"]:
				if str(self.TablaIA.item(self.TablaIA.selection())['text'])=='1' or str(self.TablaIA.item(self.TablaIA.selection())['text'])=='2' or str(self.TablaIA.item(self.TablaIA.selection())['text'])=='3' or str(self.TablaIA.item(self.TablaIA.selection())['text'])=='4' :
					messagebox.showwarning('Mensaje','Este registro no puede ser eliminado')
				else:
					Valor=messagebox.askquestion('Confirmar','¿Desea eliminar este registro?')
					if Valor=='yes':
						self.Datos.EliminarDatos(str(self.TablaIA.item(self.TablaIA.selection())["text"]),'datos_ingreso')
						self.InsertarIG()
						self.IngresoTotal()
						messagebox.showinfo('Mensaje','El registro ha sido eliminado con éxito')

			elif self.TablaEA.item(self.TablaEA.selection())["values"]:
				Valor=messagebox.askquestion('Confirmar','¿Desea eliminar este registro?')
				if Valor=='yes':
					self.Datos.EliminarDatos(str(self.TablaEA.item(self.TablaEA.selection())["text"]),'datos_ingreso')
					self.InsertarIG()
					self.IngresoTotal()
					messagebox.showinfo('Mensaje','El registro ha sido eliminado con éxito')

			elif self.TablaIK.item(self.TablaIK.selection())["values"]:
				if str(self.TablaIK.item(self.TablaIK.selection())['text'])=='5' or str(self.TablaIK.item(self.TablaIK.selection())['text'])=='6':
					messagebox.showwarning('Mensaje','Este registro no puede ser eliminado')
				else:
					Valor=messagebox.askquestion('Confirmar','¿Desea eliminar este registro?')
					if Valor=='yes':
						self.Datos.EliminarDatos(str(self.TablaIK.item(self.TablaIK.selection())["text"]),'datos_ingreso')
						self.InsertarIG()
						self.IngresoTotal()
						messagebox.showinfo('Mensaje','El registro ha sido eliminado con éxito')

			elif self.TablaEK.item(self.TablaEK.selection())["values"]:
				Valor=messagebox.askquestion('Confirmar','¿Desea eliminar este registro?')
				if Valor=='yes':
					self.Datos.EliminarDatos(str(self.TablaEK.item(self.TablaEK.selection())["text"]),'datos_ingreso')
					self.InsertarIG()
					self.IngresoTotal()
					messagebox.showinfo('Mensaje','El registro ha sido eliminado con éxito')
			else: 
				messagebox.showinfo('Mensaje','Ningún registro seleccionado')
		
		except TclError:
			messagebox.showwarning('Mensaje','Seleccione un solo registro')

	def BuscarDatos(self,Key):
		if self.CuadroBuscar.get()=="":
			self.InsertarTabla()
		else:
			Tabla=self.TablaApoderado.get_children()
			for elemento in Tabla:
				self.TablaApoderado.delete(elemento)
			Arreglo=self.Datos.BuscarApoderado(self.CuadroBuscar.get(),self.OrdenReg,str(self.ValorAge.get()),self.Default)
			cont=1
			for row in Arreglo:
				if cont % 2 != 0:
					if row[6]<100000.00:
						self.TablaApoderado.insert("",index="end",text=row[0],values=(cont,row[1]+' '+row[2]+' '+row[3],row[4], row[5], row[6], row[7], row[8]), tags=('LineaBlanca',))
					else:
						self.TablaApoderado.insert("",index="end",text=row[0],values=(cont,row[1]+' '+row[2]+' '+row[3],row[4], row[5],'Exonerado', row[7], row[8]), tags=('LineaBlanca',))
				else:
					if row[6]<100000.00:
						self.TablaApoderado.insert("",index="end",text=row[0],values=(cont,row[1]+' '+row[2]+' '+row[3],row[4], row[5], row[6], row[7], row[8]), tags=('LineaColor',))
					else:
						self.TablaApoderado.insert("",index="end",text=row[0],values=(cont,row[1]+' '+row[2]+' '+row[3],row[4], row[5],'Exonerado', row[7], row[8]), tags=('LineaColor',))
				cont=cont+1

			Tabla=self.TablaEstudiante.get_children()
			for elemento in Tabla:
				self.TablaEstudiante.delete(elemento)
			Arreglo=self.Datos.BuscarEstudiante(self.CuadroBuscar.get(),self.OrdenReg,str(self.ValorAge.get()),self.Default)
			cont=1
			for row in Arreglo:
				if cont % 2 != 0:
					if row[7]<100000.00:
						self.TablaEstudiante.insert("",index="end",text=row[0],values=(cont,row[1]+' '+row[2]+' '+row[3],row[4], row[5],row[6],row[7]), tags=('LineaBlanca',))
					else:
						self.TablaEstudiante.insert("",index="end",text=row[0],values=(cont,row[1]+' '+row[2]+' '+row[3],row[4],row[6],row[7], 'Exonerado'), tags=('LineaBlanca',))
				else:
					if row[7]<100000.00:
						self.TablaEstudiante.insert("",index="end",text=row[0],values=(cont,row[1]+' '+row[2]+' '+row[3],row[4], row[5],row[6],row[7]), tags=('LineaColor',))
					else:
						self.TablaEstudiante.insert("",index="end",text=row[0],values=(cont,row[1]+' '+row[2]+' '+row[3],row[4],row[6],row[7], 'Exonerado'), tags=('LineaColor',))
			Tabla=self.TablaPadre.get_children()
			for elemento in Tabla:
				self.TablaPadre.delete(elemento)
			Arreglo=self.Datos.BuscarPadre(self.CuadroBuscar.get(),self.OrdenReg,str(self.ValorAge.get()),self.Default)
			cont=1
			for row in Arreglo:
				if cont % 2 != 0:
					self.TablaPadre.insert("",index="end",text=row[0],values=(cont,row[1]+' '+row[2]+' '+row[3],row[4], row[5]), tags=('LineaBlanca',))
				else:
					self.TablaPadre.insert("",index="end",text=row[0],values=(cont,row[1]+' '+row[2]+' '+row[3],row[4], row[5]), tags=('LineaColor',))
				cont=cont+1

			Tabla=self.TablaMadre.get_children()
			for elemento in Tabla:
				self.TablaMadre.delete(elemento)
			cont=1
			Arreglo=self.Datos.BuscarMadre(self.CuadroBuscar.get(),self.OrdenReg,str(self.ValorAge.get()),self.Default)
			for row in Arreglo:
				if cont % 2 != 0:
					self.TablaMadre.insert("",index="end",text=row[0],values=(cont,row[1]+' '+row[2]+' '+row[3],row[4], row[5]), tags=('LineaBlanca',))
				else:
					self.TablaMadre.insert("",index="end",text=row[0],values=(cont,row[1]+' '+row[2]+' '+row[3],row[4], row[5]), tags=('LineaColor',))
				cont=cont+1

	
	def ModificarDatos(self):
		
		#elif self.Datos.ValidarDNI(self.DNIA.get(),self.Default)==True:
			#messagebox.showwarning("Mensaje","El DNI del apoderado ya existe")

		#if self.ValidarDatos()!=True:
			#pass

		if self.ComboCuota.get()=='Apoderado':
			messagebox.showwarning("Mensaje",'Seleccione una opción dentro del cuadro "Cuota AMAPAFA"')

		#elif self.ValidarMulta()==False:
   			#messagebox.showwarning('Mensaje','Digite un entero o decimal en el cuadro "Multa", procure usar punto "."\ny en caso de no existir escriba el número "0"')
		
		#elif self.ValidarEstudiante==False:
   			#messagebox.showwarning("Mensaje",'Es requerido ingresar los datos al menos de un Estudiante')

		else:
			self.SelecCuotaAmapafa(self.ComboCuota)
			self.Datos.ModificarApoderado(
				str(self.ValorN),
				self.APA.get().upper(),
				self.AMA.get().upper(),
				" ".join(self.NomA.get().upper().split()),
				self.DNIA.get(),
				" ".join(self.DirecA.get().upper().split()),
				str(self.CuotaApoderado),
				self.Multa.get(),
				self.APP.get().upper(),
				self.AMP.get().upper(),
				" ".join(self.NomP.get().upper().split()),
				self.DNIP.get(),
				self.APM.get().upper(),
				self.AMM.get().upper(),
				" ".join(self.NomM.get().upper().split()),
				self.DNIM.get())	
			self.SelecCuotaEstudiante()
			if self.NEstudiantes.get()=='1 Estudiante a cargo':
				self.ModEstu1()
			elif self.NEstudiantes.get()=='2 Estudiantes a cargo':
				self.ModEstu1(),self.ModEstu2()
			elif self.NEstudiantes.get()=='3 Estudiantes a cargo':
				self.ModEstu1(),self.ModEstu2(),self.ModEstu3()
			elif self.NEstudiantes.get()=='4 Estudiantes a cargo':
				self.ModEstu1(),self.ModEstu2(),self.ModEstu3(),self.ModEstu4()
			elif self.NEstudiantes.get()=='5 Estudiantes a cargo':
				self.ModEstu1(),self.ModEstu2(),self.ModEstu3(),self.ModEstu4(),self.ModEstu5()
			elif self.NEstudiantes.get()=='6 Estudiantes a cargo':
				self.ModEstu1(),self.ModEstu2(),self.ModEstu3(),self.ModEstu4(),self.ModEstu5(),self.ModEstu6()
			
			messagebox.showinfo("Mensaje","Los datos del Socio han sido Actualizados con Éxito")
			self.SeleccionarAge(),self.LimpiarDatos(),self.ConsultarNM(),self.ConsultarNA()

			#self.BotonAll.config(state='disabled')

	def CargarDatos(self):

		try:
			if self.TablaApoderado.item(self.TablaApoderado.selection())["values"] or self.TablaEstudiante.item(self.TablaEstudiante.selection())["values"] or self.TablaPadre.item(self.TablaPadre.selection())["values"] or self.TablaMadre.item(self.TablaMadre.selection())["values"]:
				self.Pestana.select(self.Pes2)
				self.BotonRegistrar.config(state='disabled')
				self.BotonDeshacer.config(state='disabled')
				self.BotonModificar.config(state='normal')
				self.BotonModificar.place(x=460,y=6,height=25)
				self.BotonCancel.config(state='normal')
				self.BotonCancel.place(x=580,y=6,height=25)
				self.BotonAll.config(state='disabled')
					  			
				cont=0
				self.ArregloEstudiante=[]
				if self.TablaApoderado.item(self.TablaApoderado.selection())["text"]:
					self.ValorN=self.TablaApoderado.item(self.TablaApoderado.selection())["text"]
					for i in self.Datos.CargarEstudiante(str(self.ValorN),'ID'):
						self.ArregloEstudiante.append(i[0])
						cont=cont+1
				
				elif self.TablaEstudiante.item(self.TablaEstudiante.selection())["text"]:
					for i in self.Datos.CargarEstudiante(str(self.TablaEstudiante.item(self.TablaEstudiante.selection())["text"]),'N'):
						self.ValorN=i[9]
					for n in self.Datos.CargarEstudiante(str(self.ValorN),'ID'):
						self.ArregloEstudiante.append(n[0])
						cont=cont+1

				elif self.TablaPadre.item(self.TablaPadre.selection())["text"]:
					self.ValorN=self.TablaPadre.item(self.TablaPadre.selection())["text"]
					for i in self.Datos.CargarEstudiante(str(self.ValorN),'ID'):
	   					self.ArregloEstudiante.append(i[0])
	   					cont=cont+1
				
				elif self.TablaMadre.item(self.TablaMadre.selection())["text"]:
					self.ValorN=self.TablaMadre.item(self.TablaMadre.selection())["text"]
					for i in self.Datos.CargarEstudiante(str(self.ValorN),'ID'):
	   					self.ArregloEstudiante.append(i[0])
	   					cont=cont+1
		
				Arreglo=self.Datos.CargarApoderado(str(self.ValorN),'Apoderado')
				for m in Arreglo:	
					self.APA.set(m[0])
					self.AMA.set(m[1])
					self.NomA.set(m[2])
					self.DNIA.set(m[3])
					self.DirecA.set(m[4])
					if str(m[5])==self.CuotaSocio.get():
						self.ComboCuota.current(0)
					if str(m[5])==self.CuotaIngresante.get():
						self.ComboCuota.current(1)
					if str(m[5])=='100000.00':
						self.ComboCuota.current(2)
					self.CuadroMulta.config(text=m[6])

				Arreglo=self.Datos.CargarApoderado(str(self.ValorN),'Padre')
				for m in Arreglo:
					self.APP.set(m[0])
					self.AMP.set(m[1])
					self.NomP.set(m[2])
					self.DNIP.set(m[3])

				Arreglo=self.Datos.CargarApoderado(str(self.ValorN),'Madre')
				for m in Arreglo:
					self.APM.set(m[0])
					self.AMM.set(m[1])
					self.NomM.set(m[2])
					self.DNIM.set(m[3])			

				self.TipoRoM='C'
				self.ComboNEstudiantes.current(cont-1)
				self.SelecNEstudiantes(self.ComboNEstudiantes)

				if cont==1:
	   				self.CargarEstudiante1()
				elif cont==2:
	   				self.CargarEstudiante1(),self.CargarEstudiante2()
				elif cont==3:
	   				self.CargarEstudiante1(),self.CargarEstudiante2(),self.CargarEstudiante3()
				elif cont==4:
	   				self.CargarEstudiante1(),self.CargarEstudiante2(),self.CargarEstudiante3(),self.CargarEstudiante4()
				elif cont==5:
					self.CargarEstudiante1(),self.CargarEstudiante2(),self.CargarEstudiante3(),self.CargarEstudiante4(),self.CargarEstudiante5()
				elif cont==6:
					self.CargarEstudiante1(),self.CargarEstudiante2(),self.CargarEstudiante3(),self.CargarEstudiante4(),self.CargarEstudiante5(),self.CargarEstudiante6()
				
				self.ComboNEstudiantes.config(state='disabled')

			elif self.TablaIA.item(self.TablaIA.selection())["values"]:
				self.ValorN=str(self.TablaIA.item(self.TablaIA.selection())["text"])
				self.ComboIG.current(0)
				if self.ValorN=='1' or self.ValorN=='2' or self.ValorN=='3' or self.ValorN=='4':
					self.CuadroMonto.config(state='disabled')	
				self.Pestana.select(self.Pes4)
				Arreglo=self.Datos.CargarIngreso(self.ValorN)
				for m in Arreglo:
					self.Dia.set(str(m[1])[8:10])
					self.Mes.set(self.ArregloMeses[int(str(m[1])[5:7])])
					self.Age.set(str(m[1])[0:4])
					self.MontoIG.set(m[4])
					self.NombreIG.set(m[5])
					self.TextoComentario.insert('1.0',m[6])
				#self.BotonCancelIG.config(state=NORMAL)
				#self.BotonModIG.config(state=NORMAL)
				self.BotonRegIG.config(state='disabled')
				self.BotonCancelIG.config(state='normal')
				self.BotonCancelIG.place(x=460,y=6,height=25)
				self.BotonModIG.config(state='normal')
				self.BotonModIG.place(x=580,y=6,height=25)

			elif self.TablaEA.item(self.TablaEA.selection())["values"]:
				self.ValorN=str(self.TablaEA.item(self.TablaEA.selection())["text"])
				self.Pestana.select(self.Pes4)
				self.ComboIG.current(1)	
				Arreglo=self.Datos.CargarIngreso(self.ValorN)
				for m in Arreglo:
					self.Dia.set(str(m[1])[8:10])
					self.Mes.set(self.ArregloMeses[int(str(m[1])[5:7])])
					self.Age.set(str(m[1])[0:4])
					self.Comprobante.insert(0,m[2])
					self.NCP.insert(0,m[3])
					self.MontoIG.set(m[4])
					self.NombreIG.set(m[5])
					self.TextoComentario.insert('1.0',m[6])
				self.BotonRegIG.config(state='disabled')
				self.BotonCancelIG.config(state='normal')
				self.BotonCancelIG.place(x=460,y=6,height=25)
				self.BotonModIG.config(state='normal')
				self.BotonModIG.place(x=580,y=6,height=25)

			elif self.TablaIK.item(self.TablaIK.selection())["values"]:	
				self.ValorN=str(self.TablaIK.item(self.TablaIK.selection())["text"])
				if self.ValorN=='1' or self.ValorN=='2':
					pass
				self.Pestana.select(self.Pes4)
				self.ComboIG.current(2)
				Arreglo=self.Datos.CargarIngreso(self.ValorN)
				for m in Arreglo:
					self.Dia.set(str(m[1])[8:10])
					self.Mes.set(self.ArregloMeses[int(str(m[1])[5:7])])
					self.Age.set(str(m[1])[0:4])
					self.MontoIG.set(m[4])
					self.NombreIG.set(m[5])
					self.TextoComentario.insert('1.0',m[6])
				self.BotonRegIG.config(state='disabled')
				self.BotonCancelIG.config(state='normal')
				self.BotonCancelIG.place(x=460,y=6,height=25)
				self.BotonModIG.config(state='normal')
				self.BotonModIG.place(x=580,y=6,height=25)

			elif self.TablaEK.item(self.TablaEK.selection())["values"]:
				self.ValorN=str(self.TablaEK.item(self.TablaEK.selection())["text"])
				self.Pestana.select(self.Pes4)
				self.ComboIG.current(3)
				Arreglo=self.Datos.CargarIngreso(self.ValorN)
				for m in Arreglo:
					self.Dia.set(str(m[1])[8:10])
					self.Mes.set(self.ArregloMeses[int(str(m[1])[5:7])])
					self.Age.set(str(m[1])[0:4])
					self.Comprobante.insert(0,m[2])
					self.NCP.insert(0,m[3])
					self.MontoIG.set(m[4])
					self.NombreIG.set(m[5])
					self.TextoComentario.insert('1.0',m[6])
				self.BotonRegIG.config(state='disabled')
				self.BotonCancelIG.config(state='normal')
				self.BotonCancelIG.place(x=460,y=6,height=25)
				self.BotonModIG.config(state='normal')
				self.BotonModIG.place(x=580,y=6,height=25)
			else: 
				messagebox.showinfo('Mensaje','Ningún registro seleccionado')
	
		except TclError:
			messagebox.showwarning('Mensaje','Seleccione un solo registro')

	def Desseleccionar(self,event):
		if len(self.TablaPadre.selection()) > 0:
   		    self.TablaPadre.selection_remove(self.TablaPadre.selection()[0])
		
		elif len(self.TablaMadre.selection()) > 0:
		    self.TablaMadre.selection_remove(self.TablaMadre.selection()[0])

		elif len(self.TablaApoderado.selection()) > 0:
 		    self.TablaApoderado.selection_remove(self.TablaApoderado.selection()[0])

		elif len(self.TablaEstudiante.selection()) > 0:
 		    self.TablaEstudiante.selection_remove(self.TablaEstudiante.selection()[0])
		
		elif len(self.TablaIA.selection()) > 0:
			self.TablaIA.selection_remove(self.TablaIA.selection()[0])
		
		elif len(self.TablaEA.selection()) > 0:
			self.TablaEA.selection_remove(self.TablaEA.selection()[0])

		elif len(self.TablaIK.selection()) > 0:
 		    self.TablaIK.selection_remove(self.TablaIK.selection()[0])

		elif len(self.TablaEK.selection()) > 0:
 		    self.TablaEK.selection_remove(self.TablaEK.selection()[0])		

	def CambiarContra(self,event):
		Datos=Usuario()
		Validar=Datos.ValidarContra(self.Usuario.get(),self.ContraActual.get())

		if Validar==True:
			if len(self.ContraNueva.get())>=8:
				Cambiar=Datos.CambiarLogin(self.Usuario.get(),self.ContraNueva.get())
				self.Top.destroy()
				messagebox.showinfo("Mensaje","La contraseña ha sido modificada con éxito")
				self.ContraActual.set("")
				self.ContraNueva.set("")
				self.MostrarContra.set(0)
			else:
				messagebox.showwarning("Mensaje",'La contraseña nueva debe contener como mímino 8 carácteres')
				self.Top.focus_set()
				self.CajaContra.focus()
				self.ContraNueva.set("")
		else:
			messagebox.showinfo("Mensaje","El usuario y/o la contraseña actual es incorrecta")
			self.ContraActual.set("")
			self.ContraNueva.set("")
			self.Top.focus_set()
			self.CuadroActual.focus()


	def ExportarDatos(self):

		def grouper(iterable, n):
			args = [iter(iterable)] * n
			return itertools.zip_longest(*args)

		def export_to_pdf(data,Tipo):

			Fichero=filedialog.asksaveasfilename(title="Exportar",defaultextension=".pdf")
			c = canvas.Canvas(Fichero, pagesize=A4)
			w, h = A4
			max_rows_per_page = 45
			x_offset = 0
			y_offset = 100
			padding = 15
			c.drawImage("img/Insignia.png", 515, h - 80,mask='auto', width=75, height=50, )
			c.drawImage("img/Escudo.png", 50, h - 90,mask='auto', width=60, height=80, )

			c.line(25, 70 , 50, 70)
			if Tipo=='Apoderado': 
				xlist = [x + x_offset for x in [25,70,250, 330, 430, 480, 530, 570]]
			elif Tipo=='Estudiante':
				xlist = [x + x_offset for x in [25,55,380, 440, 455, 470, 515, 570]]
			elif Tipo=='Padre' or Tipo=='Madre':
				xlist = [x + x_offset for x in [25,70 ,250, 330]]
			

			ylist = [h - y_offset - i*padding for i in range(max_rows_per_page + 1)]  
			for rows in grouper(data, max_rows_per_page):
				rows = tuple(filter(bool, rows))
				c.grid(xlist, ylist[:len(rows) + 1])
				c.drawImage("img/Insignia.png", 515, h - 80,mask='auto', width=75, height=50,)
				c.drawImage("img/Escudo.png", 50, h - 90,mask='auto', width=60, height=80,)
				for y, row in zip(ylist[:-1], rows):
					for x, cell in zip(xlist, row):
						c.drawString(x + 2, y - padding + 3, str(cell))
				c.showPage()
			c.save()
		
		if self.ComboDatosExp.get()=='Apoderado':
			data = [('N°',"APELLIDOS Y NOMBRES", "DNI", "DIRECCION", "CUOTA", "MULTA", "N° A")]
			for i in self.Datos.ConsultarApoderado(self.ComboOrdenExp.get(),str(self.ValorAge.get()),self.Default):
				data.append((i[0],i[1]+' '+i[2]+' '+i[3], i[4], i[5], i[6],i[7],i[8]))

		elif self.ComboDatosExp.get()=='Padre':
			data = [('N°',"APELLIDOS Y NOMBRES", "DNI")]
			for i in self.Datos.ConsultarPadre(self.ComboOrdenExp.get(),str(self.ValorAge.get()),self.Default):
				data.append((i[0],i[1]+' '+i[2]+' '+i[3], i[4]))

		elif self.ComboDatosExp.get()=='Madre':
			data = [('N°',"APELLIDOS Y NOMBRES", "DNI")]
			for i in self.Datos.ConsultarMadre(self.ComboOrdenExp.get(),str(self.ValorAge.get()),self.Default):
				data.append((i[0],i[1]+' '+i[2]+' '+i[3], i[4]))

		elif self.ComboDatosExp.get()=='Estudiante':
			data = [('N°',"APELLIDOS Y NOMBRES", "DNI", "G", "S", "CUOTA", "ESTADO")]
			for i in self.Datos.ConsultarEstudiante(self.ComboOrdenExp.get(),str(self.ValorAge.get()),self.Default):
				if i[7]<100000.00:
					data.append((i[0],i[1]+' '+i[2]+' '+i[3], i[4], i[5], i[6],i[7],i[8]))
				else:
					data.append((i[0],i[1]+' '+i[2]+' '+i[3], i[4], i[5], i[6],'Exoner.',i[8]))

		elif self.ComboDatosExp.get()=='Ingreso AMAPAFA':
			data = [('N°',"APELLIDOS Y NOMBRES", "DNI", "GRADO", "SECCIÓN", "CUOTA", "ESTADO")]
			for i in self.Datos.ConsultarEstudiante(self.ComboOrdenExp.get(),str(self.ValorAge.get()),self.Default):
				data.append((i[1]+' '+i[2]+' '+i[3], i[4], i[5], i[6],i[7],i[8]))

		elif self.ComboDatosExp.get()=='Egreso AMAPAFA':
			data = [('N°',"APELLIDOS Y NOMBRES", "DNI", "GRADO", "SECCIÓN", "CUOTA", "ESTADO")]
			for i in self.Datos.ConsultarEstudiante(self.ComboOrdenExp.get(),str(self.ValorAge.get()),self.Default):
				data.append((i[1]+' '+i[2]+' '+i[3], i[4], i[5], i[6],i[7],i[8]))

		elif self.ComboDatosExp.get()=='Ingreso Kaly Warma':
			data = [('N°',"APELLIDOS Y NOMBRES", "DNI", "GRADO", "SECCIÓN", "CUOTA", "ESTADO")]
			for i in self.Datos.ConsultarEstudiante(self.ComboOrdenExp.get(),str(self.ValorAge.get()),self.Default):
				data.append((i[1]+' '+i[2]+' '+i[3], i[4], i[5], i[6],i[7],i[8]))

		elif self.ComboDatosExp.get()=='Egreso Kaly Warma':
			data = [('N°',"APELLIDOS Y NOMBRES", "DNI", "GRADO", "SECCIÓN", "CUOTA", "ESTADO")]
			for i in self.Datos.ConsultarEstudiante(self.ComboOrdenExp.get(),str(self.ValorAge.get()),self.Default):
				data.append((i[1]+' '+i[2]+' '+i[3], i[4], i[5], i[6],i[7],i[8]))

		try:
			export_to_pdf(data,self.ComboDatosExp.get())
			messagebox.showinfo("Mensaje",'Los datos han sido exportados con éxito')
		except FileNotFoundError:
			pass


	def RegistrarIG(self):

		if self.ValidarIG()!=True:
			pass

		else:
			#Fecha=self.Age.get()+'-'+str(self.ArregloMeses.index(self.Mes.get()))+'-'+self.Dia.get()
			#self.Datos.RegistrarIngreso(Fecha,self.Comprobante.get(),self.NCP.get(),self.MontoIG.get(),self.NombreIG.get(),self.TextoComentario.get('1.0',END),'0','0',self.ValorIG,str(self.ValorAge.get()),self.Default)
			messagebox.showinfo('Mensaje','Los datos han sido registrados con éxito')
			#self.InsertarIG(),self.IngresoTotal(),self.LimpiarIG()

	def InsertarIG(self):

		Tabla=self.TablaIA.get_children()
		for elemento in Tabla:
			self.TablaIA.delete(elemento)
		Arreglo=self.Datos.ConsultarIngreso('IA',str(self.ValorAge.get()),self.Default)
		cont=1
		for row in Arreglo:
			if cont % 2 != 0:
				if row[4]<100000.00:
					self.TablaIA.insert("",index="end",text=row[0],values=(cont,row[5],row[7],row[8],row[4]), tags=('LineaBlanca',))
				else:
					self.TablaIA.insert("",index="end",text=row[0],values=(cont,row[5],row[7],row[8],'0.00'), tags=('LineaBlanca',))
			else:
				if row[4]<100000.00:
					self.TablaIA.insert("",index="end",text=row[0],values=(cont,row[5],row[7],row[8],row[4]), tags=('LineaColor',))
				else:
					self.TablaIA.insert("",index="end",text=row[0],values=(cont,row[5],row[7],row[8],'0.00'), tags=('LineaColor',))
			cont=cont+1

		Tabla=self.TablaEA.get_children()
		for elemento in Tabla:
			self.TablaEA.delete(elemento)
		Arreglo=self.Datos.ConsultarIngreso('EA',str(self.ValorAge.get()),self.Default)
		cont=1
		for row in Arreglo:
			if cont % 2 != 0:
				self.TablaEA.insert("",index="end",text=row[0],values=(cont,row[1], row[2], row[3],row[5], row[4]), tags=('LineaBlanca',))
			else:
				self.TablaEA.insert("",index="end",text=row[0],values=(cont,row[1], row[2], row[3],row[5], row[4]), tags=('LineaColor',))
			cont=cont+1

		Tabla=self.TablaIK.get_children()
		for elemento in Tabla:
			self.TablaIK.delete(elemento)
		Arreglo=self.Datos.ConsultarIngreso('IK',str(self.ValorAge.get()),self.Default)
		cont=1
		for row in Arreglo:
			if cont % 2 != 0:
				if row[4]<100000.00:
					self.TablaIK.insert("",index="end",text=row[0],values=(cont,row[5],row[7],row[4]), tags=('LineaBlanca',))
				else:
					self.TablaIK.insert("",index="end",text=row[0],values=(cont,row[5],row[7],'0.00'), tags=('LineaBlanca',))
			else:
				if row[4]<100000.00:
					self.TablaIK.insert("",index="end",text=row[0],values=(cont,row[5],row[7],row[4]), tags=('LineaColor',))
				else:
					self.TablaIK.insert("",index="end",text=row[0],values=(cont,row[5],row[7],'0.00'), tags=('LineaColor',))
			cont=cont+1

		Tabla=self.TablaEK.get_children()
		for elemento in Tabla:
			self.TablaEK.delete(elemento)
		Arreglo=self.Datos.ConsultarIngreso('EK',str(self.ValorAge.get()),self.Default)
		cont=1
		for row in Arreglo:
			if cont % 2 != 0:
				self.TablaEK.insert("",index="end",text=row[0],values=(cont,row[1], row[2], row[3],row[5], row[4]), tags=('LineaBlanca',))
			else:
				self.TablaEK.insert("",index="end",text=row[0],values=(cont,row[1], row[2], row[3],row[5], row[4]), tags=('LineaColor',))
			cont=cont+1

	def BloquearPes(self):
		self.Pestana.tab(0, state='disabled')
		self.Pestana.tab(3, state='disabled')
		self.Pestana.tab(5, state='disabled')
		self.Archivo.entryconfig(0, state = 'disabled')
		self.Archivo.entryconfig(1, state = 'disabled')
		self.Archivo.entryconfig(2, state = 'disabled')
		self.Archivo.entryconfig(4, state = 'disabled')
		self.Edicion.entryconfig(0, state = 'disabled')
		self.Edicion.entryconfig(1, state = 'disabled')
		self.Herramientas.entryconfig(0,state= 'disabled')

	def DesbloquearPes(self):
		self.Pestana.tab(0, state=NORMAL)
		self.Pestana.tab(1, state=NORMAL)
		self.Pestana.tab(3, state=NORMAL)
		self.Pestana.tab(4, state=NORMAL)
		self.Pestana.tab(5, state=NORMAL)
		self.Archivo.entryconfig(0, state = NORMAL)
		self.Archivo.entryconfig(1, state = NORMAL)
		self.Archivo.entryconfig(2, state = NORMAL)
		self.Archivo.entryconfig(4, state = NORMAL)
		self.Edicion.entryconfig(0, state = NORMAL)
		self.Edicion.entryconfig(1, state = NORMAL)
		self.Herramientas.entryconfig(0,state= NORMAL)

	def ModificarIG(self):
		if self.IngresoGasto.get()=='Seleccione una opción':
			messagebox.showwarning('Mensaje','Seleccione una opción')

		else:
			self.SelecIngreso(self.ComboIG)
			Fecha=self.Age.get()+'-'+str(self.ArregloMeses.index(self.Mes.get()))+'-'+self.Dia.get()
			self.Datos.ModificarIngreso(str(self.ValorN),Fecha,self.Comprobante.get(),self.NCP.get(),self.MontoIG.get(),self.NombreIG.get(),self.TextoComentario.get('1.0',END),self.ValorIG)
			messagebox.showinfo('Mensaje','Los datos han sido actualizados con éxito')
			self.Pestana.select(self.Pes3)
			self.InsertarIG(),self.IngresoTotal(),self.LimpiarIG()

	def CancelarIG(self):
		Valor=messagebox.askquestion('Confirmar','¿Desea cancelar la operación')
		if Valor=='yes':
			self.Pestana.select(self.Pes3)
			self.LimpiarIG()

	def LimpiarIG(self):
		self.IngresoGasto.set('Seleccione una opción')
		self.NombreIG.set('')
		self.Comprobante.delete(0,END)
		self.NCP.delete(0,END)
		self.MontoIG.set('')
		self.TextoComentario.delete('1.0',END)
		self.BotonCancelIG.config(state='disabled')
		self.BotonModIG.config(state='disabled')
		self.BotonModIG.place(y=1000)
		self.BotonRegIG.config(state='normal')
		self.BotonRegIG.place(x=580,y=6,height=25)

	def IngresoTotal(self):
		
		TotalIA=0
		for i in self.Datos.ConsultarIngreso('IA',str(self.ValorAge.get()),self.Default):
			TotalIA=TotalIA+i[4]
		self.LabelIA.config(text=TotalIA)
		TotalEA=0
		for i in self.Datos.ConsultarIngreso('EA',str(self.ValorAge.get()),self.Default):
			TotalEA=TotalEA+i[4]
		self.LabelEA.config(text=TotalEA)
		TotalIK=0
		for i in self.Datos.ConsultarIngreso('IK',str(self.ValorAge.get()),self.Default):
			TotalIK=TotalIK+i[4]
		self.LabelIK.config(text=TotalIK)
		TotalEK=0
		for i in self.Datos.ConsultarIngreso('EK',str(self.ValorAge.get()),self.Default):
			TotalEK=TotalEK+i[4]
		self.LabelEK.config(text=TotalEK)
		TotalSaldoA=TotalIA-TotalEA
		self.SaldoA.config(text=TotalSaldoA)

		TotalSaldoK=TotalIK-TotalEK
		self.SaldoK.config(text=TotalSaldoK)

	def ConsultarNM(self):
		
		for i in self.Datos.ConsultarNMiembros(self.CuotaSocio.get(),str(self.ValorAge.get()),self.Default):
			NS=i[0]
		self.Datos.MultiMonto('2',str(NS),self.CuotaSocio.get())

		for i in self.Datos.ConsultarNMiembros(self.CuotaIngresante.get(),str(self.ValorAge.get()),self.Default):
			NI=i[0]
		self.Datos.MultiMonto('3',str(NI),self.CuotaIngresante.get())

		for i in self.Datos.ConsultarNMiembros('100000.00',str(self.ValorAge.get()),self.Default):
			NE=i[0]
		self.Datos.MultiMonto('1',str(NE),'0')

		for i in self.Datos.ConsultarMultas('0.00',str(self.ValorAge.get()),self.Default):
			SM=i[0]
		self.Datos.ModMonto('4',str(SM),'0')

	def ConsultarNA(self):
		
		for i in self.Datos.ConsultarNEstudiantes('100000.00','Normal',str(self.ValorAge.get()),self.Default):
			MAC=i[0]
			NAC=i[1]
		self.Datos.ModMonto('6',str(NAC),str(MAC))

		for i in self.Datos.ConsultarNMiembros('100000.00',str(self.ValorAge.get()),self.Default):
			NAE=i[0]
		self.Datos.MultiMonto('5',str(NAE),'0')

		
		for i in self.Datos.ConsultarNEstudiantes('100000.00','Traslado',str(self.ValorAge.get()),self.Default):
			MAC=i[0]
			NAC=i[1]
		self.Datos.ModMonto('7',str(NAC),str(MAC))

		
		for i in self.Datos.ConsultarNEstudiantes('100000.00','Retirado',str(self.ValorAge.get()),self.Default):
			MAC=i[0]
			NAC=i[1]
		self.Datos.ModMonto('8',str(NAC),str(MAC))

	def MenuRightClick(self, window):
		self.ClickMenu = Menu(window, tearoff=0)
		self.ClickMenu.add_command(label='Agregar Estudiante a su cargo',command=self.VentanaAnadir)
		self.ClickMenu.add_command(label='Modificar', command=self.CargarDatos)
		self.ClickMenu.add_command(label='Eliminar', command=self.EliminarDatos)

	def MenuClickNull(self, window):
		#if self.TablaPadre.item(self.TablaPadre.selection())["values"] or self.TablaMadre.item(self.TablaMadre.selection())["values"] or self.TablaApoderado.item(self.TablaApoderado.selection())["values"]:
		self.MenuNull = Menu(window, tearoff=0)
		self.MenuOrdenar=Menu(self.WindowMain)
		
		self.MenuOrdenar=Menu(self.MenuNull,tearoff=0)
		self.MenuOrdenar.add_radiobutton(label='Orden de matrícula',variable=self.ValorOrdenar,value=0,command=self.CambiarOrden)
		self.MenuOrdenar.add_radiobutton(label='Apellidos y nombres',variable=self.ValorOrdenar,value=1,command=self.CambiarOrden)
		self.MenuOrdenar.add_radiobutton(label='Grado y Sección',variable=self.ValorOrdenar,value=2,command=self.CambiarOrden)
		self.MenuNull.add_cascade(label='Ordenar por', menu=self.MenuOrdenar)
		self.MenuNull.add_command(label='Exportar', command=lambda: self.Pestana.select(self.Pes5))

	def Popup(self, event):
		try:
			if  self.TablaPadre.item(self.TablaPadre.selection())["values"] or self.TablaMadre.item(self.TablaMadre.selection())["values"] or self.TablaApoderado.item(self.TablaApoderado.selection())["values"] or self.TablaEstudiante.item(self.TablaEstudiante.selection())["values"]:
				self.MenuRightClick(self.WindowMain)
				self.ClickMenu.post(event.x_root, event.y_root)

			else:
				self.MenuClickNull(self.WindowMain)
				self.MenuNull.post(event.x_root, event.y_root)
				#self.TablaEstudiante_item = self.TablaEstudiante.focus()
		
		except TclError:
			messagebox.showwarning('Mensaje','Seleccione solo un registro')

	def Click(self,event):
		if self.TablaApoderado.identify_region(event.x, event.y) == "separator":
			return "break"
		elif self.TablaEstudiante.identify_region(event.x, event.y) == "separator":
			return "break"
		elif self.TablaPadre.identify_region(event.x, event.y) == "separator":
			return "break"
		elif self.TablaMadre.identify_region(event.x, event.y) == "separator":
			return "break"
		elif self.TablaIA.identify_region(event.x, event.y) == "separator":
			return "break"
		elif self.TablaEA.identify_region(event.x, event.y) == "separator":
			return "break"
		elif self.TablaIK.identify_region(event.x, event.y) == "separator":
			return "break"
		elif self.TablaEK.identify_region(event.x, event.y) == "separator":
			return "break"
		elif self.TablaGenerar.identify_region(event.x, event.y) == "separator":
			return "break"

	def Calendario(self):

		self.Suma+=1
		if self.Suma%2==0:
			self.FrameCal.place(x=1000,y=0)
		else:
			self.FrameCal.place(x=575,y=230,height=200,width=226)
			ttkcal = Calendar(self.FrameCal,firstweekday=calendar.SUNDAY)
			ttkcal.pack(expand=1, fill='both')  	
			def Fun():
			    Fecha=ttkcal.selection()
			    try:
			    	self.Mes.set(self.ArregloMeses[int(str(Fecha)[5:7])])
			    	self.Age.set(str(Fecha)[0:4])
			    	self.Dia.set(str(Fecha)[8:10])
			    except ValueError:
			    	pass
			    self.FrameCal.place(x=1000,y=0)
			    self.Suma+=1
			Button(self.FrameCal,text='Guardar Fecha',bd=0,bg='#d4dce3',width=30,command=Fun).pack(expand='yes',side='bottom')

	def CalendInicio(self):
		frame=Frame(self.Pes4,bd=4,bg='#5c8cc5')
		frame.place(x=355,y=90,height=210,width=226)
		ttkcal = Calendar(frame,firstweekday=calendar.SUNDAY)
		ttkcal.pack(expand=1, fill='both')  	
		def Fun():
		    Fecha=ttkcal.selection()
		    self.DiaIni.set(str(Fecha)[8:10])
		    self.MesIni.set(self.ArregloMeses[int(str(Fecha)[5:7])])
		    self.AgeIni.set(str(Fecha)[0:4])
		    frame.place(x=1000,y=0)
		Button(frame,text='Guardar Fecha',bd=0,bg='#d4dce3',width=30,command=Fun).pack(expand='yes',side='bottom')


	def CalendFinal(self):
		frame=Frame(self.Pes4,bd=4,bg='#5c8cc5')
		frame.place(x=340,y=90,height=210,width=226)
		ttkcal = Calendar(frame,firstweekday=calendar.SUNDAY)
		ttkcal.pack(expand=1, fill='both')  	
		def Fun():
		    Fecha=ttkcal.selection()
		    self.DiaFin.set(str(Fecha)[8:10])
		    self.MesFin.set(self.ArregloMeses[int(str(Fecha)[5:7])])
		    self.AgeFin.set(str(Fecha)[0:4])
		    frame.place(x=1000,y=0)
		Button(frame,text='Guardar Fecha',bd=0,bg='#d4dce3',width=30,command=Fun).pack(expand='yes',side='bottom')

def get_calendar(locale, fwday):
    # instantiate proper calendar class
    if locale is None:
        return calendar.TextCalendar(fwday)
    else:
        return calendar.LocaleTextCalendar(fwday, locale)

class Calendar(ttk.Frame):
    # XXX ToDo: cget and configure

    datetime = calendar.datetime.datetime
    timedelta = calendar.datetime.timedelta
    locale.setlocale(locale.LC_ALL, 'es-ES')
    def __init__(self, master, **kw):
        """
        WIDGET-SPECIFIC OPTIONS

        locale, firstweekday, year, month, selectbackground,
        selectforeground
        """
        # remove custom options from kw before initializating ttk.Frame
        fwday = kw.pop('firstweekday', calendar.MONDAY)
        year = kw.pop('year', self.datetime.now().year)
        month = kw.pop('month', self.datetime.now().month)
        day = kw.pop('day', self.datetime.now().day)
        locale = kw.pop('locale', None)
        sel_bg = kw.pop('selectbackground', '#5c8cc5')
        sel_fg = kw.pop('selectforeground', 'white')

        self._date = self.datetime(year, month, day)
        self._selection = None # no date selected

        ttk.Frame.__init__(self, master, **kw)

        self._cal = get_calendar(locale, fwday)

        self.__setup_styles()       # creates custom styles
        self.__place_widgets()      # pack/grid used widgets
        self.__config_calendar()    # adjust calendar columns and setup tags
        # configure a canvas, and proper bindings, for selecting dates
        self.__setup_selection(sel_bg, sel_fg)

        # store items ids, used for insertion later
        self._items = [self._calendar.insert('', 'end', values='')
                            for _ in range(6)]
        # insert dates in the currently empty calendar
        self._build_calendar()

        # set the minimal size for the widget
        self._calendar.bind('<Map>', self.__minsize)

    def __setitem__(self, item, value):
        if item in ('year', 'month'):
            raise AttributeError("attribute '%s' is not writeable" % item)
        elif item == 'selectbackground':
            self._canvas['background'] = value
        elif item == 'selectforeground':
            self._canvas.itemconfigure(self._canvas.text, item=value)
        else:
            ttk.Frame.__setitem__(self, item, value)

    def __getitem__(self, item):
        if item in ('year', 'month'):
            return getattr(self._date, item)
        elif item == 'selectbackground':
            return self._canvas['background']
        elif item == 'selectforeground':
            return self._canvas.itemcget(self._canvas.text, 'fill')
        else:
            r = ttk.tclobjs_to_py({item: ttk.Frame.__getitem__(self, item)})
            return r[item]

    def __setup_styles(self):
        # custom ttk styles
        style = ttk.Style(self.master)
        arrow_layout = lambda dir: (
            [('Button.focus', {'children': [('Button.%sarrow' % dir, None)]})]
        )
        style.layout('L.TButton', arrow_layout('left'))
        style.layout('R.TButton', arrow_layout('right'))

    def __place_widgets(self):
        # header frame and its widgets
        hframe = Frame(self)
        lbtn = ttk.Button(hframe, style='L.TButton', command=self._prev_month)
        rbtn = ttk.Button(hframe, style='R.TButton', command=self._next_month)
        self._header = ttk.Label(hframe, width=15, anchor='center')
        # the calendar
        self._calendar = ttk.Treeview(show='', selectmode='none', height=7)

        # pack the widgets
        hframe.pack(in_=self, side='top', pady=4, anchor='center')
        lbtn.grid(in_=hframe)
        self._header.grid(in_=hframe, column=1, row=0, padx=12)
        rbtn.grid(in_=hframe, column=2, row=0)
        self._calendar.pack(in_=self, expand=1, fill='both', side='bottom')

    def __config_calendar(self):
        cols = self._cal.formatweekheader(3).split()
        self._calendar['columns'] = cols
        self._calendar.tag_configure('header', background='grey90')
        self._calendar.insert('', 'end', values=cols, tag='header')
        # adjust its columns width
        font = tkFont.Font()
        maxwidth = max(font.measure(col) for col in cols)
        for col in cols:
            self._calendar.column(col, width=maxwidth, minwidth=maxwidth,
                anchor='e')

    def __setup_selection(self, sel_bg, sel_fg):
        self._font = tkFont.Font()
        self._canvas = canvas = Tkinter.Canvas(self._calendar, background=sel_bg, borderwidth=0, highlightthickness=0)
        canvas.text = canvas.create_text(0, 0, fill=sel_fg, anchor='w')

        canvas.bind('<ButtonPress-1>', lambda evt: canvas.place_forget())
        self._calendar.bind('<Configure>', lambda evt: canvas.place_forget())
        self._calendar.bind('<ButtonPress-1>', self._pressed)

    def __minsize(self, evt):
        width, height = self._calendar.master.geometry().split('x')
        height = height[:height.index('+')]
        self._calendar.master.minsize(width, height)

    def _build_calendar(self):
        year, month = self._date.year, self._date.month

        # update header text (Month, YEAR)
        header = self._cal.formatmonthname(year, month, 0)
        self._header['text'] = header.title()

        # update calendar shown dates
        cal = self._cal.monthdayscalendar(year, month)
        for indx, item in enumerate(self._items):
            week = cal[indx] if indx < len(cal) else []
            fmt_week = [('%02d' % day) if day else '' for day in week]
            self._calendar.item(item, values=fmt_week)

    def _show_selection(self, text, bbox):
        """Configure canvas for a new selection."""
        x, y, width, height = bbox

        textw = self._font.measure(text)

        canvas = self._canvas
        canvas.configure(width=width, height=height)
        canvas.coords(canvas.text, width - textw, height / 2 - 1)
        canvas.itemconfigure(canvas.text, text=text)
        canvas.place(in_=self._calendar, x=x, y=y)

    # Callbacks

    def _pressed(self, evt):
        """Clicked somewhere in the calendar."""
        x, y, widget = evt.x, evt.y, evt.widget
        item = widget.identify_row(y)
        column = widget.identify_column(x)

        if not column or not item in self._items:
            # clicked in the weekdays row or just outside the columns
            return

        item_values = widget.item(item)['values']
        if not len(item_values): # row is empty for this month
            return

        text = item_values[int(column[1]) - 1]
        if not text: # date is empty
            return

        bbox = widget.bbox(item, column)
        if not bbox: # calendar not visible yet
            return

        # update and then show selection
        text = '%02d' % text
        self._selection = (text, item, column)
        self._show_selection(text, bbox)

    def _prev_month(self):
        """Updated calendar to show the previous month."""
        self._canvas.place_forget()

        self._date = self._date - self.timedelta(days=1)
        self._date = self.datetime(self._date.year, self._date.month, 1)
        self._build_calendar() # reconstuct calendar

    def _next_month(self):
        """Update calendar to show the next month."""
        self._canvas.place_forget()

        year, month = self._date.year, self._date.month
        self._date = self._date + self.timedelta(
            days=calendar.monthrange(year, month)[1] + 1)
        self._date = self.datetime(self._date.year, self._date.month, 1)
        self._build_calendar() # reconstruct calendar

    # Properties

    #@property
    def selection(self):
        """Return a datetime representing the current selected date."""
        if not self._selection:
            return None

        year, month = self._date.year, self._date.month
        return self.datetime(year, month, int(self._selection[0]))


