from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

class Emerging_Windows():

	def VentanaTexto(self):
		self.TopTexto=Toplevel()
		self.TopTexto.title("Cambiar Texto de Presentación")
		self.TopTexto.geometry("400x180+480+250")
		self.TopTexto.iconbitmap("img/My_icon.ico")
		self.TopTexto.resizable(0,0)
		self.TopTexto.focus_set()
		Frame1=Frame(self.TopTexto,width="400",height="35",bg=self.StyleBgColor)
		Frame1.pack()
		Label(Frame1,text="Optimal Data",bg=self.StyleBgColor,fg="white",font=("Arial Rounded MT Bold",10)).place(x=200,y=7)
		Frame2=Frame(self.TopTexto,width="400",height="150")
		Frame2.pack()
	
		Label(Frame2,text="Escriba el nuevo texto de presentación:").place(x=50,y=15)
		CCTP=ttk.Entry(Frame2,textvariable=self.EscribirTexto,width=58)
		CCTP.focus()
		CCTP.place(x=20,y=50)
		self.TopTexto.bind('<Return>',self.CambiarTexto)
		BotonCambiar=ttk.Button(Frame2,text="Cambiar",command=self.CambiarTexto)
		BotonCambiar.bind('<Button-1>',self.CambiarTexto)
		BotonCambiar.place(x=220,y=100)
		BotonCancelar=ttk.Button(Frame2,text="Cancelar",command=lambda:(self.TopTexto.destroy(),self.EscribirTexto.set("")))
		BotonCancelar.place(x=300,y=100)
		self.TopTexto.protocol("WM_DELETE_WINDOW", lambda:(self.TopTexto.destroy(),self.EscribirTexto.set("")))

	def VentanaConfigurar(self):
		self.TopPagos=Toplevel()
		self.TopPagos.title("Configurar Pagos")
		self.TopPagos.geometry("300x220+520+250")
		self.TopPagos.iconbitmap("img/My_icon.ico")
		self.TopPagos.resizable(0,0)
		self.TopPagos.focus_set()
		Frame1=Frame(self.TopPagos,width="300",height="50",bg=self.StyleBgColor)
		Frame1.pack()
		Label(Frame1,text="Optimal Data",bg=self.StyleBgColor,fg="white",font=("Arial Rounded MT Bold",10)).place(x=200,y=10)
		Frame2=Frame(self.TopPagos,width="300",height="170")
		Frame2.pack()

		Label(Frame2,text="Año {}".format(self.ValorAge.get())).place(x=100,y=10)
		Label(Frame2,text="Cuota para socio:").place(x=30,y=40)
		Label(Frame2,text="Cuota para ingresante:").place(x=30,y=70)
		Label(Frame2,text="S/").place(x=170,y=40)
		Label(Frame2,text="S/").place(x=170,y=70)

		ttk.Entry(Frame2,width=10,justify="right",textvariable=self.CuotaSocio).place(x=190,y=40)
		ttk.Entry(Frame2,width=10,justify="right",textvariable=self.CuotaIngresante).place(x=190,y=70)

		self.TopPagos.bind('<Return>',self.AplicarPagos)
		BotonCambiar=ttk.Button(Frame2,text="Aplicar",command=self.AplicarPagos)
		BotonCambiar.bind('<Button-1>',self.AplicarPagos)
		BotonCambiar.place(x=100,y=120)
		ttk.Button(Frame2,text="Cancelar",command=lambda:(self.TopPagos.destroy())).place(x=190,y=120)

	def CopyToStu1(self):
		self.APE1.insert(0,self.APP.get())
		self.AME1.insert(0,self.APM.get())

	def CopyToStu2(self):
		self.APE2.insert(0,self.APP.get())
		self.AME2.insert(0,self.APM.get())

	def CopyToStu3(self):
		self.APE3.insert(0,self.APP.get())
		self.AME3.insert(0,self.APM.get())

	def CopyToStu4(self):
		self.APE4.insert(0,self.APP.get())
		self.AME4.insert(0,self.APM.get())

	def CopyToStu5(self):
		self.APE5.insert(0,self.APP.get())
		self.AME5.insert(0,self.APM.get())

	def CopyToStu6(self):
		self.APE6.insert(0,self.APP.get())
		self.AME6.insert(0,self.APM.get())

	def SelecHijo1(self,Tipo):
		if Tipo=='R':
			self.LimpiarEstudiante(),self.HabiEstu1(),self.CopyToStu1()
		else:
			self.HabiEstu1()
		
	def SelecHijo2(self,Tipo):
		if Tipo=='R':
			self.LimpiarEstudiante(),self.HabiEstu1(),self.HabiEstu2(),self.CopyToStu1(),self.CopyToStu2()
		else:
			self.HabiEstu2()

	def SelecHijo3(self,Tipo):
		if Tipo=='R':
			self.LimpiarEstudiante(),self.HabiEstu1(),self.HabiEstu2(),self.HabiEstu3()
			self.CopyToStu1(),self.CopyToStu2(),self.CopyToStu3()
		else:
			self.HabiEstu3()

	def SelecHijo4(self,Tipo):
		if Tipo=='R':
			self.LimpiarEstudiante(),self.HabiEstu1(),self.HabiEstu2(),self.HabiEstu3(),self.HabiEstu4()
			self.CopyToStu1(),self.CopyToStu2(),self.CopyToStu3(),self.CopyToStu4()
		else:
			self.HabiEstu4()

	def SelecHijo5(self,Tipo):
		if Tipo=='R':
			self.LimpiarEstudiante(),self.HabiEstu1(),self.HabiEstu2(),self.HabiEstu3(),self.HabiEstu4(),self.HabiEstu5()
			self.CopyToStu1(),self.CopyToStu2(),self.CopyToStu3(),self.CopyToStu4(),self.CopyToStu5()
		else:
			self.HabiEstu5()

	def SelecHijo6(self,Tipo):
		if Tipo=='R':
			self.LimpiarEstudiante(),self.HabiEstu1(),self.HabiEstu2(),self.HabiEstu3(),self.HabiEstu4(),self.HabiEstu5(),self.HabiEstu6()
			self.CopyToStu1(),self.CopyToStu2(),self.CopyToStu3(),self.CopyToStu4(),self.CopyToStu5(),self.CopyToStu6()
		else:
			self.HabiEstu6()

	def HabiEstu1(self):
		self.APE1.config(state=NORMAL)
		self.AME1.config(state=NORMAL)
		self.NomE1.config(state=NORMAL)
		self.DNIE1.config(state=NORMAL)
		self.ComboGrado1.config(state='readonly')
		self.ComboSeccion1.config(state='readonly')
		self.ComboEstado1.config(state='readonly')
		self.ComboTipoPago1.config(state='readonly')

	def HabiEstu2(self):
		self.APE2.config(state=NORMAL)
		self.AME2.config(state=NORMAL)
		self.NomE2.config(state=NORMAL)
		self.DNIE2.config(state=NORMAL)
		self.ComboGrado2.config(state='readonly')
		self.ComboSeccion2.config(state='readonly')
		self.ComboEstado2.config(state='readonly')
		self.ComboTipoPago2.config(state='readonly')

	def HabiEstu3(self):
		self.APE3.config(state=NORMAL)
		self.AME3.config(state=NORMAL)
		self.NomE3.config(state=NORMAL)
		self.DNIE3.config(state=NORMAL)
		self.ComboGrado3.config(state='readonly')
		self.ComboSeccion3.config(state='readonly')
		self.ComboEstado3.config(state='readonly')
		self.ComboTipoPago3.config(state='readonly')

	def HabiEstu4(self):
		self.APE4.config(state=NORMAL)
		self.AME4.config(state=NORMAL)
		self.NomE4.config(state=NORMAL)
		self.DNIE4.config(state=NORMAL)
		self.ComboGrado4.config(state='readonly')
		self.ComboSeccion4.config(state='readonly')
		self.ComboEstado4.config(state='readonly')
		self.ComboTipoPago4.config(state='readonly')

	def HabiEstu5(self):
		self.APE5.config(state=NORMAL)
		self.AME5.config(state=NORMAL)
		self.NomE5.config(state=NORMAL)
		self.DNIE5.config(state=NORMAL)
		self.ComboGrado5.config(state='readonly')
		self.ComboSeccion5.config(state='readonly')
		self.ComboEstado5.config(state='readonly')
		self.ComboTipoPago5.config(state='readonly')

	def HabiEstu6(self):
		self.APE6.config(state=NORMAL)
		self.AME6.config(state=NORMAL)
		self.NomE6.config(state=NORMAL)
		self.DNIE6.config(state=NORMAL)
		self.ComboGrado6.config(state='readonly')
		self.ComboSeccion6.config(state='readonly')
		self.ComboEstado6.config(state='readonly')
		self.ComboTipoPago6.config(state='readonly')

	def SelecTipoCuota1(self,event):
		if self.TipoPago1.get()=='Pago':
			self.ComboTipoPago1.config(state='normal')
			self.TipoPago1.set('')
		elif self.TipoPago1.get()=='Exonerado':
			self.ComboTipoPago1.config(state='readonly')
			self.ValorPagoE1='100000.00'

	def SelecTipoCuota2(self,event):
		if self.TipoPago2.get()=='Pago':
			self.ComboTipoPago2.config(state='normal')
			self.TipoPago2.set('')
		elif self.TipoPago2.get()=='Exonerado':
			self.ComboTipoPago1.config(state='readonly')
			self.ValorPagoE2='100000.00'			

	def SelecTipoCuota3(self,event):
		if self.TipoPago3.get()=='Pago':
			self.ComboTipoPago3.config(state='normal')
			self.TipoPago3.set('')
		elif self.TipoPago3.get()=='Exonerado':
			self.ComboTipoPago3.config(state='readonly')
			self.ValorPagoE3='100000.00'

	def SelecTipoCuota4(self,event):
		if self.TipoPago4.get()=='Pago':
			self.ComboTipoPago4.config(state='normal')
			self.TipoPago4.set('')
		elif self.TipoPago4.get()=='Exonerado':
			self.ComboTipoPago4.config(state='readonly')
			self.ValorPagoE4='100000.00'

	def SelecTipoCuota5(self,event):
		if self.TipoPago5.get()=='Pago':
			self.ComboTipoPago5.config(state='normal')
			self.TipoPago5.set('')
		elif self.TipoPago5.get()=='Exonerado':
			self.ComboTipoPago5.config(state='readonly')
			self.ValorPagoE5='100000.00'

	def SelecTipoCuota6(self,event):
		if self.TipoPago6.get()=='Pago':
			self.ComboTipoPago6.config(state='normal')
			self.TipoPago6.set('')
		elif self.TipoPago6.get()=='Exonerado':
			self.ComboTipoPago6.config(state='readonly')
			self.ValorPagoE6='100000.00'

	def SelecTipoCuotaM(self,event):
		if self.TipoPagoM.get()=='Pago':
			self.ComboTipoPagoM.config(state='normal')
			self.TipoPagoM.set('')
		elif self.TipoPagoM.get()=='Exonerado':
			self.ComboTipoPagoM.config(state='readonly')
			self.ValorPagoEM='100000.00'

	def Create_Window_Change_Login(self):
		self.Top=Toplevel()
		self.Top.title("Cambiar Login")
		self.Top.geometry("300x240+520+200")
		self.Top.iconbitmap("img/My_icon.ico")
		self.Top.resizable(0,0)
		self.Top.focus_set()
		Frame1=Frame(self.Top,width="300",height="40",bg=self.StyleBgColor)
		Frame1.pack()
		Label(Frame1,text="Optimal Data",bg=self.StyleBgColor,fg="white",font=("Arial Rounded MT Bold",10)).place(x=200,y=10)
		Frame2=Frame(self.Top,width="300",height="190")
		Frame2.pack()
		Label(Frame2,text="Usuario:").place(x=20,y=20)
		Label(Frame2,text="Contraseña Actual:").place(x=20,y=50)
		Label(Frame2,text="Contraseña Nueva:").place(x=20,y=80)
		self.CuadroUsuario=ttk.Entry(Frame2,textvariable=self.Usuario)
		self.CuadroUsuario.place(x=135,y=20)
		self.Usuario.set(self.Default)
		self.CuadroUsuario.config(state='disabled')
		self.CuadroActual=ttk.Entry(Frame2,textvariable=self.ContraActual,show="•")
		self.CuadroActual.place(x=135,y=50)
		self.CuadroActual.focus()
		self.CajaContra=ttk.Entry(Frame2,show="•",textvariable=self.ContraNueva)
		self.CajaContra.place(x=135,y=80)
		self.Top.bind('<Return>',self.CambiarContra)
		Label(Frame2,text="Mostrar Contraseña").place(x=20,y=110)
		ttk.Checkbutton(Frame2,variable=self.MostrarContra,command=self.MostrarContrasena).place(x=135,y=110)
		BotonCambiar=ttk.Button(Frame2,text="Guardar",command=self.CambiarContra)
		BotonCambiar.bind('<Button-1>', self.CambiarContra)
		BotonCambiar.place(x=110,y=155)
		BotonCancelar=ttk.Button(Frame2,text="Cancelar",command=lambda:(self.ContraActual.set(""),self.ContraNueva.set(""),self.MostrarContra.set(0),self.Top.destroy()))
		BotonCancelar.place(x=190,y=155)
		self.Top.protocol("WM_DELETE_WINDOW", lambda:(self.ContraActual.set(""),self.ContraNueva.set(""),self.MostrarContra.set(0),self.Top.destroy()))

	def MostrarContrasena(self):
		if self.MostrarContra.get()==1:
			self.CajaContra.config(show="")
		else:
			self.CajaContra.config(show="•")

	def VentanaAnadir(self):

		if self.TablaPadre.item(self.TablaPadre.selection())["values"] or self.TablaMadre.item(self.TablaMadre.selection())["values"] or self.TablaEstudiante.item(self.TablaEstudiante.selection())["values"]:
   			messagebox.showinfo("Mensaje",'Esta opción solo es válida para la sección "Apoderado"')

		elif self.TablaApoderado.item(self.TablaApoderado.selection())["values"]:
			self.ValorN=self.TablaApoderado.item(self.TablaApoderado.selection())["text"]
			self.TopAnadir=Toplevel()
			self.TopAnadir.title("Agregar Estudiante")
			self.TopAnadir.geometry("615x111+400+275")
			self.TopAnadir.iconbitmap("img/My_icon.ico")
			self.TopAnadir.resizable(0,0)
			self.TopAnadir.focus_set()

			Frame1=Frame(self.TopAnadir,width="675",height=75,bg='#f1f6fc')
			Frame1.place(x=0,y=0)
			Frame2=Frame(self.TopAnadir,width="675",height=37,bg='#d4dce3')
			Frame2.place(x=0,y=75)

			FrameName=Frame(Frame1,width=854,height=20,bg='#f1f6fc')
			FrameName.place(x=-22,y=10)
			FraEst=Frame(Frame1,width=850,height=160,bg='#f1f6fc')
			FraEst.place(x=5,y=35)
			Label(FrameName,text="Apellido Paterno",bg='#f1f6fc').place(x=41,y=0)
			Label(FrameName,text="Apellido Materno",bg='#f1f6fc').place(x=135,y=0)
			Label(FrameName,text="Nombres",bg='#f1f6fc').place(x=260,y=0)
			Label(FrameName,text="DNI",bg='#f1f6fc').place(x=365,y=0)
			Label(FrameName,text="Grado",bg='#f1f6fc').place(x=415,y=0)
			Label(FrameName,text="Sección",bg='#f1f6fc').place(x=450,y=0)
			Label(FrameName,text='Estado',bg='#f1f6fc').place(x=505,y=0)
			Label(FrameName,text="Pago",bg='#f1f6fc').place(x=580,y=0)
			Label(FraEst,text="1",bg='#f1f6fc').grid(row=2,column=0,pady=5)
			self.APEM=ttk.Entry(FraEst,width=15)
			self.APEM.grid(row=2,column=1)
			self.AMEM=ttk.Entry(FraEst,width=15)
			self.AMEM.grid(row=2,column=2)
			self.NomEM=ttk.Entry(FraEst,width=17)
			self.NomEM.grid(row=2,column=3)
			self.DNIEM=ttk.Entry(FraEst,width=10)
			self.DNIEM.grid(row=2,column=4,padx=5)
			
			ttk.Combobox(FraEst,values=['○','1','2','3','4','5','6'],textvariable=self.GradoM,width=2,state='readonly').grid(row=2,column=5)
			ttk.Combobox(FraEst,values=['○','A','B','C'],textvariable=self.SeccionM,width=2,state='readonly').grid(row=2,column=6,padx=5)
			ttk.Combobox(FraEst,values=['Normal','Traslado','Retirado'],textvariable=self.EstadoM,width=7,state='readonly').grid(row=2,column=7)
			self.ComboTipoPagoM=ttk.Combobox(FraEst,values=['Pago','Exonerado'],textvariable=self.TipoPagoM,width=6,state='normal',justify='right')
			self.ComboTipoPagoM.grid(row=2,column=8,padx=5)
			self.ComboTipoPagoM.bind("<<ComboboxSelected>>", self.SelecTipoCuotaM)
			self.APEM.delete(0,END)
			self.AMEM.delete(0,END)
			self.NomEM.delete(0,END)
			self.DNIEM.delete(0,END)
			self.EstadoM.set('Normal')
			self.GradoM.set('○')
			self.SeccionM.set('○')
			self.EstadoM.set('Normal')
			self.TipoPagoM.set('0')

			self.TopAnadir.bind('<Return>',self.AnadirEstudiante)
			BotonCambiar=Button(Frame2,text="Agregar",bd=0,bg='#5c8cc5',activebackground='#5c8cc5',fg='white',width=15,command=self.AnadirEstudiante)
			BotonCambiar.bind('<Button-1>', self.AnadirEstudiante)
			BotonCambiar.place(x=370,y=6,height=25)
			Button(Frame2,text="Cancelar",bd=0,bg='#5c8cc5',fg='white',width=15,command=self.CancelarEstudiante).place(x=490,y=6,height=25)
			self.TopAnadir.protocol("WM_DELETE_WINDOW", self.CancelarEstudiante)

		else:
			messagebox.showinfo("Mensaje",'Seleccione un registro"')

	def RedimensionarVE(self,event):

		if self.ComboOrdenExp.get()=='Grado y Sección':
			self.ComboGradoExp.config(state='readonly')
			self.ComboSeccionExp.config(state='readonly')

		else:
			self.ComboGradoExp.config(state='disabled')
			self.ComboSeccionExp.config(state='disabled')

	def VentanaExportarIG(self):
		self.TopExportarIG=Toplevel()
		self.TopExportarIG.title("Exportar")
		self.TopExportarIG.geometry("300x180+520+250")
		self.TopExportarIG.iconbitmap("img/My_icon.ico")
		self.TopExportarIG.resizable(0,0)
		self.TopExportarIG.focus_set()
		Frame1=Frame(self.TopExportarIG,width="300",height="50",bg=self.StyleBgColor)
		Frame1.pack()
		Label(Frame1,text="Optimal Data",bg=self.StyleBgColor,fg="white",font=("Arial Rounded MT Bold",10)).place(x=200,y=10)
		Frame2=Frame(self.TopExportarIG,width="300",height="150")
		Frame2.pack()
	
		Label(Frame1,text="Los Datos serán Exportados\nen Formato '.CSV'",bg=self.StyleBgColor,fg="white").place(x=5,y=5)
		
		ttk.Button(Frame2,text="Ingresos\nAMAPAFA",width=17,command=self.ExportarIA).place(x=25,y=10)
		ttk.Button(Frame2,text="Egresos\nAMAPAFA",width=17,command=self.ExportarEA).place(x=150,y=10)
		ttk.Button(Frame2,text="Ingresos\nKaly Warma",width=17,command=self.ExportarIK).place(x=25,y=65)
		ttk.Button(Frame2,text="Egresos\nKaly Warma",width=17,command=self.ExportarEK).place(x=150,y=65)

	def Create_Window_Login(self,Window):
		self.WindowLogin=Window
		self.WindowLogin.title("Entrar a Optimal Data")
		self.WindowLogin.geometry("300x180+520+250")
		self.WindowLogin.iconbitmap("img/My_icon.ico")
		self.WindowLogin.resizable(0,0)
		Frame1=Frame(self.WindowLogin,width="300",height="50",bg='#466183')
		Frame1.pack()
		Label(Frame1,text="Optimal Data",bg='#466183',fg="white",font=("Arial Rounded MT Bold",10)).place(x=200,y=10)
		Frame2=Frame(self.WindowLogin,width="300",height="150")
		Frame2.pack()
		Label(Frame2,text="Usuario:").place(x=65,y=20)
		Label(Frame2,text="Contraseña:").place(x=47,y=50)
		self.CuadroUser=ttk.Entry(Frame2,textvariable=self.User)
		self.CuadroUser.place(x=120,y=20)
		self.CuadroUser.focus()
		self.CuadroPass=ttk.Entry(Frame2,show="•",textvariable=self.Password)
		self.CuadroPass.place(x=120,y=50)

		Imagen2=PhotoImage(file="img/My_ico_User.png")
		Label(Frame2,image=Imagen2).place(x=70,y=75)
		
		self.WindowLogin.bind('<Return>',self.Access)
		BotonEntrar=ttk.Button(Frame2,text="Iniciar",width="20",command=self.Access)
		BotonEntrar.bind('<Button-1>', self.Access)
		BotonEntrar.place(x=120,y=85)

	def CancelarEstudiante(self):
		Valor=messagebox.askquestion("Confirmar","¿Desea cancelar la operación?")
		if Valor=="yes":
			self.TopAnadir.destroy()
		else:
			self.TopAnadir.focus_set()

	def CargarEstudiante1(self):
		Lista=self.Datos.CargarEstudiante(str(self.ArregloEstudiante[0]),'N')				
		for m in Lista:
			self.APE1.insert(0,m[1])
			self.AME1.insert(0,m[2])
			self.NomE1.insert(0,m[3])
			self.DNIE1.insert(0,m[4])
			self.Grado1.set(m[5])
			self.Seccion1.set(m[6])
			if m[7]==100000.00:
				self.ComboTipoPago1.current(1)
				self.ValorPagoE1='100000.00'
			else: 
				self.TipoPago1.set('0')
				self.TextoMonto1['text']=m[7]
			self.Estado1.set(m[8])

	def CargarEstudiante2(self):
		Lista=self.Datos.CargarEstudiante(str(self.ArregloEstudiante[1]),'N')				
		for m in Lista:
			self.APE2.insert(0,m[1])
			self.AME2.insert(0,m[2])
			self.NomE2.insert(0,m[3])
			self.DNIE2.insert(0,m[4])
			self.Grado2.set(m[5])
			self.Seccion2.set(m[6])
			if m[7]==100000.00:
				self.ComboTipoPago2.current(1)
				self.ValorPagoE2='100000.00'
			else: 
				self.TipoPago2.set('0')
				self.TextoMonto2['text']=m[7]
			self.Estado2.set(m[8])

	def CargarEstudiante3(self):
		Lista=self.Datos.CargarEstudiante(str(self.ArregloEstudiante[2]),'N')				
		for m in Lista:
			self.APE3.insert(0,m[1])
			self.AME3.insert(0,m[2])
			self.NomE3.insert(0,m[3])
			self.DNIE3.insert(0,m[4])
			self.Grado3.set(m[5])
			self.Seccion3.set(m[6])
			if m[7]==100000.00:
				self.ComboTipoPago3.current(1)
				self.ValorPagoE3='100000.00'
			else: 
				self.TipoPago3.set('0')
				self.TextoMonto3['text']=m[7]
			self.Estado3.set(m[8])

	def CargarEstudiante4(self):
		Lista=self.Datos.CargarEstudiante(str(self.ArregloEstudiante[3]),'N')				
		for m in Lista:
			self.APE4.insert(0,m[1])
			self.AME4.insert(0,m[2])
			self.NomE4.insert(0,m[3])
			self.DNIE4.insert(0,m[4])
			self.Grado4.set(m[5])
			self.Seccion4.set(m[6])
			if m[7]==100000.00:
				self.ComboTipoPago4.current(1)
				self.ValorPagoE4='100000.00'
			else: 
				self.TipoPago4.set('0')
				self.TextoMonto4['text']=m[7]
			self.Estado4.set(m[8])

	def CargarEstudiante5(self):
		Lista=self.Datos.CargarEstudiante(str(self.ArregloEstudiante[4]),'N')
		for m in Lista:
			self.APE5.insert(0,m[1])
			self.AME5.insert(0,m[2])
			self.NomE5.insert(0,m[3])
			self.DNIE5.insert(0,m[4])
			self.Grado5.set(m[5])
			self.Seccion5.set(m[6])
			if m[7]==100000.00:
				self.ComboTipoPago5.current(1)
				self.ValorPagoE5='100000.00'
			else: 
				self.TipoPago5.set('0')
				self.TextoMonto5['text']=m[7]
			self.Estado5.set(m[8])

	def CargarEstudiante6(self):
		Lista=self.Datos.CargarEstudiante(str(self.ArregloEstudiante[5]),'N')
		for m in Lista:
			self.APE6.insert(0,m[1])
			self.AME6.insert(0,m[2])
			self.NomE6.insert(0,m[3])
			self.DNIE6.insert(0,m[4])
			self.Grado6.set(m[5])
			self.Seccion6.set(m[6])
			if m[7]==100000.00:
				self.ComboTipoPago6.current(1)
				self.ValorPagoE6='100000.00'
			else: 
				self.TipoPago6.set('0')
				self.TextoMonto6['text']=m[7]
			self.Estado6.set(m[8])

	def RegEstu1(self):
		self.Datos.RegistrarEstudiante(self.APE1.get().upper().strip(),self.AME1.get().upper().strip()," ".join(self.NomE1.get().upper().split()),self.DNIE1.get(),self.Grado1.get(),self.Seccion1.get(),self.ValorPagoE1,self.Estado1.get(),self.Relacion,str(self.ValorAge.get()),self.Default)

	def RegEstu2(self):
		self.Datos.RegistrarEstudiante(self.APE2.get().upper().strip(),self.AME2.get().upper().strip()," ".join(self.NomE2.get().upper().split()),self.DNIE2.get(),self.Grado2.get(),self.Seccion2.get(),self.ValorPagoE2,self.Estado2.get(),self.Relacion,str(self.ValorAge.get()),self.Default)

	def RegEstu3(self):
		self.Datos.RegistrarEstudiante(self.APE3.get().upper().strip(),self.AME3.get().upper().strip()," ".join(self.NomE3.get().upper().split()),self.DNIE3.get(),self.Grado3.get(),self.Seccion3.get(),self.ValorPagoE3,self.Estado3.get(),self.Relacion,str(self.ValorAge.get()),self.Default)

	def RegEstu4(self):
		self.Datos.RegistrarEstudiante(self.APE4.get().upper().strip(),self.AME4.get().upper().strip()," ".join(self.NomE4.get().upper().split()),self.DNIE4.get(),self.Grado4.get(),self.Seccion4.get(),self.ValorPagoE4,self.Estado4.get(),self.Relacion,str(self.ValorAge.get()),self.Default)

	def RegEstu5(self):
		self.Datos.RegistrarEstudiante(self.APE5.get().upper().strip(),self.AME5.get().upper().strip()," ".join(self.NomE5.get().upper().split()),self.DNIE5.get(),self.Grado5.get(),self.Seccion5.get(),self.ValorPagoE5,self.Estado5.get(),self.Relacion,str(self.ValorAge.get()),self.Default)

	def RegEstu6(self):
		self.Datos.RegistrarEstudiante(self.APE6.get().upper().strip(),self.AME6.get().upper().strip()," ".join(self.NomE6.get().upper().split()),self.DNIE6.get(),self.Grado6.get(),self.Seccion6.get(),self.ValorPagoE6,self.Estado6.get(),self.Relacion,str(self.ValorAge.get()),self.Default)
	
	def ModEstu1(self):
		self.SelecCuEstu1()
		self.Datos.ModificarEstudiante(str(self.ArregloEstudiante[0]),self.APE1.get().upper().strip(),self.AME1.get().upper().strip()," ".join(self.NomE1.get().upper().split()),self.DNIE1.get(),self.Grado1.get(),self.Seccion1.get(),self.ValorPagoE1,self.Estado1.get())

	def ModEstu2(self):
		self.SelecCuEstu2()
		self.Datos.ModificarEstudiante(str(self.ArregloEstudiante[1]),self.APE2.get().upper().strip(),self.AME2.get().upper().strip()," ".join(self.NomE2.get().upper().split()),self.DNIE2.get(),self.Grado2.get(),self.Seccion2.get(),self.ValorPagoE2,self.Estado2.get())

	def ModEstu3(self):
		self.SelecCuEstu3()
		self.Datos.ModificarEstudiante(str(self.ArregloEstudiante[2]),self.APE3.get().upper().strip(),self.AME3.get().upper().strip()," ".join(self.NomE3.get().upper().split()),self.DNIE3.get(),self.Grado3.get(),self.Seccion3.get(),self.ValorPagoE3,self.Estado3.get())

	def ModEstu4(self):
		self.SelecCuEstu4()
		self.Datos.ModificarEstudiante(str(self.ArregloEstudiante[3]),self.APE4.get().upper().strip(),self.AME4.get().upper().strip()," ".join(self.NomE4.get().upper().split()),self.DNIE4.get(),self.Grado4.get(),self.Seccion4.get(),self.ValorPagoE4,self.Estado4.get())

	def ModEstu5(self):
		self.SelecCuEstu5()
		self.Datos.ModificarEstudiante(str(self.ArregloEstudiante[4]),self.APE5.get().upper().strip(),self.AME5.get().upper().strip()," ".join(self.NomE5.get().upper().split()),self.DNIE5.get(),self.Grado5.get(),self.Seccion5.get(),self.ValorPagoE5,self.Estado5.get())

	def ModEstu6(self):
		self.SelecCuEstu6()
		self.Datos.ModificarEstudiante(str(self.ArregloEstudiante[5]),self.APE6.get().upper().strip(),self.AME6.get().upper().strip()," ".join(self.NomE6.get().upper().split()),self.DNIE6.get(),self.Grado6.get(),self.Seccion6.get(),self.ValorPagoE6,self.Estado6.get())

	def SelecCuEstu1(self):
		if self.TipoPago1.get()!='Exonerado':
   			for i in self.Datos.CargarEstudiante(str(self.ArregloEstudiante[0]),'N'):
   				K=i[7]
   			if K<100000:
   				self.ValorPagoE1=str(float(self.TipoPago1.get())+float(K))
   			else:
   				self.ValorPagoE1=self.TipoPago1.get()

	def SelecCuEstu2(self):
   		if self.TipoPago2.get()!='Exonerado':
   			for i in self.Datos.CargarEstudiante(str(self.ArregloEstudiante[1]),'N'):
   				K=i[7]
   			if K<100000:
   				self.ValorPagoE2=str(float(self.TipoPago2.get())+float(K))
   			else:
   				self.ValorPagoE2=self.TipoPago2.get()

	def SelecCuEstu3(self):
   		if self.TipoPago3.get()!='Exonerado':
   			for i in self.Datos.CargarEstudiante(str(self.ArregloEstudiante[2]),'N'):
   				K=i[7]
   			if K<100000:
   				self.ValorPagoE3=str(float(self.TipoPago3.get())+float(K))
   			else:
   				self.ValorPagoE3=self.TipoPago3.get()

	def SelecCuEstu4(self):
   		if self.TipoPago4.get()!='Exonerado':
   			for i in self.Datos.CargarEstudiante(str(self.ArregloEstudiante[3]),'N'):
   				K=i[7]
   			if K<100000:
   				self.ValorPagoE4=str(float(self.TipoPago4.get())+float(K))
   			else:
   				self.ValorPagoE4=self.TipoPago4.get()

	def SelecCuEstu5(self):
   		if self.TipoPago5.get()!='Exonerado':
   			for i in self.Datos.CargarEstudiante(str(self.ArregloEstudiante[4]),'N'):
   				K=i[7]
   			if K<100000:
   				self.ValorPagoE5=str(float(self.TipoPago5.get())+float(K))
   			else:
   				self.ValorPagoE5=self.TipoPago5.get()

	def SelecCuEstu6(self):
   		if self.TipoPago6.get()!='Exonerado':
   			for i in self.Datos.CargarEstudiante(str(self.ArregloEstudiante[5]),'N'):
   				K=i[7]
   			if K<100000:
   				self.ValorPagoE6=str(float(self.TipoPago6.get())+float(K))
   			else:
   				self.ValorPagoE6=self.TipoPago6.get()

	
	def SelecIngreso(self,event):

		if self.IngresoGasto.get()=='Seleccione una Opción':
			self.Comprobante.config(state='normal')
			self.NCP.config(state='normal')
		
		if self.IngresoGasto.get()=='Ingreso AMAPAFA':
			self.Comprobante.delete(0,END)
			self.NCP.delete(0,END)
			self.Comprobante.config(state='readonly')
			self.NCP.config(state='readonly')
			self.ValorIG='IA'

		elif self.IngresoGasto.get()=='Egreso AMAPAFA':
			self.Comprobante.config(state='normal')
			self.NCP.config(state='normal')
			self.ValorIG='EA'

		elif self.IngresoGasto.get()=='Ingreso Kaly Warma':
			self.Comprobante.delete(0,END)
			self.NCP.delete(0,END)
			self.Comprobante.config(state='disabled')
			self.NCP.config(state='disabled')
			self.ValorIG='IK'

		elif self.IngresoGasto.get()=='Egreso Kaly Warma':
			self.Comprobante.config(state=NORMAL)
			self.NCP.config(state=NORMAL)
			self.ValorIG='EK'

	def SelecPesInicio(self,event):
		self.Pestana.select(self.Pes1)
		self.PesInicio.config(bg='#5c8cc5')
		self.PesRegSocio.config(bg='#d4dce3',fg='black')
		self.PesRegIG.config(bg='#d4dce3',fg='black')
		self.PesVerReg.config(bg='#d4dce3',fg='black')
		self.PesGenRep.config(bg='#d4dce3',fg='black')
		self.PesInicio.bind('<Leave>',lambda event: self.PesInicio.config(bg='#5c8cc5',fg='white'))
		self.PesRegSocio.bind('<Leave>',lambda event: self.PesRegSocio.config(bg='#d4dce3',fg='black'))
		self.PesRegIG.bind('<Leave>',lambda event: self.PesRegIG.config(bg='#d4dce3',fg='black'))
		self.PesVerReg.bind('<Leave>',lambda event: self.PesVerReg.config(bg='#d4dce3',fg='black'))
		self.PesGenRep.bind('<Leave>',lambda event: self.PesGenRep.config(bg='#d4dce3',fg='black'))

	def SelecPesRegSocio(self,event):
		self.Pestana.select(self.Pes2)
		self.PesInicio.config(bg='#d4dce3',fg='black')
		self.PesRegSocio.config(bg='#5c8cc5')
		self.PesRegIG.config(bg='#d4dce3',fg='black')
		self.PesVerReg.config(bg='#d4dce3',fg='black')
		self.PesGenRep.config(bg='#d4dce3',fg='black')
		self.PesInicio.bind('<Leave>',lambda event: self.PesInicio.config(bg='#d4dce3',fg='black'))
		self.PesRegSocio.bind('<Leave>',lambda event: self.PesRegSocio.config(bg='#5c8cc5',fg='white'))
		self.PesRegIG.bind('<Leave>',lambda event: self.PesRegIG.config(bg='#d4dce3',fg='black'))
		self.PesVerReg.bind('<Leave>',lambda event: self.PesVerReg.config(bg='#d4dce3',fg='black'))
		self.PesGenRep.bind('<Leave>',lambda event: self.PesGenRep.config(bg='#d4dce3',fg='black'))

	def SelecPesRegIG(self,event):
		self.Pestana.select(self.Pes3)
		self.PesInicio.config(bg='#d4dce3',fg='black')
		self.PesRegSocio.config(bg='#d4dce3',fg='black')
		self.PesRegIG.config(bg='#5c8cc5')
		self.PesVerReg.config(bg='#d4dce3',fg='black')
		self.PesGenRep.config(bg='#d4dce3',fg='black')
		self.PesInicio.bind('<Leave>',lambda event: self.PesInicio.config(bg='#d4dce3',fg='black'))
		self.PesRegSocio.bind('<Leave>',lambda event: self.PesRegSocio.config(bg='#d4dce3',fg='black'))
		self.PesRegIG.bind('<Leave>',lambda event: self.PesRegIG.config(bg='#5c8cc5',fg='white'))
		self.PesVerReg.bind('<Leave>',lambda event: self.PesVerReg.config(bg='#d4dce3',fg='black'))
		self.PesGenRep.bind('<Leave>',lambda event: self.PesGenRep.config(bg='#d4dce3',fg='black'))

	def SelecPesVerReg(self,event):
		self.Pestana.select(self.Pes4)
		self.PesInicio.config(bg='#d4dce3',fg='black')
		self.PesRegSocio.config(bg='#d4dce3',fg='black')
		self.PesRegIG.config(bg='#d4dce3',fg='black')
		self.PesVerReg.config(bg='#5c8cc5')
		self.PesGenRep.config(bg='#d4dce3',fg='black')
		self.PesInicio.bind('<Leave>',lambda event: self.PesInicio.config(bg='#d4dce3',fg='black'))
		self.PesRegSocio.bind('<Leave>',lambda event: self.PesRegSocio.config(bg='#d4dce3',fg='black'))
		self.PesRegIG.bind('<Leave>',lambda event: self.PesRegIG.config(bg='#d4dce3',fg='black'))
		self.PesVerReg.bind('<Leave>',lambda event: self.PesVerReg.config(bg='#5c8cc5',fg='white'))
		self.PesGenRep.bind('<Leave>',lambda event: self.PesGenRep.config(bg='#d4dce3',fg='black'))

	def SelecPesGenRep(self,event):
		self.Pestana.select(self.Pes5)
		self.PesInicio.config(bg='#d4dce3',fg='black')
		self.PesRegSocio.config(bg='#d4dce3',fg='black')
		self.PesRegIG.config(bg='#d4dce3',fg='black')
		self.PesVerReg.config(bg='#d4dce3',fg='black')
		self.PesGenRep.config(bg='#5c8cc5')	
		self.PesInicio.bind('<Leave>',lambda event: self.PesInicio.config(bg='#d4dce3',fg='black'))
		self.PesRegSocio.bind('<Leave>',lambda event: self.PesRegSocio.config(bg='#d4dce3',fg='black'))
		self.PesRegIG.bind('<Leave>',lambda event: self.PesRegIG.config(bg='#d4dce3',fg='black'))
		self.PesVerReg.bind('<Leave>',lambda event: self.PesVerReg.config(bg='#d4dce3',fg='black'))
		self.PesGenRep.bind('<Leave>',lambda event: self.PesGenRep.config(bg='#5c8cc5',fg='white'))

	def SelecPesApoderado(self,event):
		self.SubPestana.select(self.SubPes1)
		self.PesApoderado.config(bg='#5c8cc5')
		self.PesEstudiante.config(bg='#f1f6fc',fg=self.StyleBgColor)
		self.PesPadre.config(bg='#f1f6fc',fg=self.StyleBgColor)
		self.PesMadre.config(bg='#f1f6fc',fg=self.StyleBgColor)
		self.PesIA.config(bg='#f1f6fc',fg=self.StyleBgColor)
		self.PesEA.config(bg='#f1f6fc',fg=self.StyleBgColor)
		self.PesIK.config(bg='#f1f6fc',fg=self.StyleBgColor)
		self.PesEK.config(bg='#f1f6fc',fg=self.StyleBgColor)
		self.PesApoderado.bind('<Leave>',lambda event: self.PesApoderado.config(bg='#5c8cc5',fg='white'))
		self.PesEstudiante.bind('<Leave>',lambda event: self.PesEstudiante.config(bg='#f1f6fc',fg=self.StyleBgColor))
		self.PesPadre.bind('<Leave>',lambda event: self.PesPadre.config(bg='#f1f6fc',fg=self.StyleBgColor))
		self.PesMadre.bind('<Leave>',lambda event: self.PesMadre.config(bg='#f1f6fc',fg=self.StyleBgColor))
		self.PesIA.bind('<Leave>',lambda event: self.PesIA.config(bg='#f1f6fc',fg=self.StyleBgColor))
		self.PesEA.bind('<Leave>',lambda event: self.PesEA.config(bg='#f1f6fc',fg=self.StyleBgColor))
		self.PesIK.bind('<Leave>',lambda event: self.PesIK.config(bg='#f1f6fc',fg=self.StyleBgColor))
		self.PesEK.bind('<Leave>',lambda event: self.PesEK.config(bg='#f1f6fc',fg=self.StyleBgColor))

	def SelecPesEstudiante(self,event):
		self.SubPestana.select(self.SubPes2)
		self.PesApoderado.config(bg='#f1f6fc',fg=self.StyleBgColor)
		self.PesEstudiante.config(bg='#5c8cc5')
		self.PesPadre.config(bg='#f1f6fc',fg=self.StyleBgColor)
		self.PesMadre.config(bg='#f1f6fc',fg=self.StyleBgColor)
		self.PesIA.config(bg='#f1f6fc',fg=self.StyleBgColor)
		self.PesEA.config(bg='#f1f6fc',fg=self.StyleBgColor)
		self.PesIK.config(bg='#f1f6fc',fg=self.StyleBgColor)
		self.PesEK.config(bg='#f1f6fc',fg=self.StyleBgColor)
		self.PesApoderado.bind('<Leave>',lambda event: self.PesApoderado.config(bg='#f1f6fc',fg=self.StyleBgColor))
		self.PesEstudiante.bind('<Leave>',lambda event: self.PesEstudiante.config(bg='#5c8cc5',fg='white'))
		self.PesPadre.bind('<Leave>',lambda event: self.PesPadre.config(bg='#f1f6fc',fg=self.StyleBgColor))
		self.PesMadre.bind('<Leave>',lambda event: self.PesMadre.config(bg='#f1f6fc',fg=self.StyleBgColor))
		self.PesIA.bind('<Leave>',lambda event: self.PesIA.config(bg='#f1f6fc',fg=self.StyleBgColor))
		self.PesEA.bind('<Leave>',lambda event: self.PesEA.config(bg='#f1f6fc',fg=self.StyleBgColor))
		self.PesIK.bind('<Leave>',lambda event: self.PesIK.config(bg='#f1f6fc',fg=self.StyleBgColor))
		self.PesEK.bind('<Leave>',lambda event: self.PesEK.config(bg='#f1f6fc',fg=self.StyleBgColor))

	def SelecPesPadre(self,event):
		self.SubPestana.select(self.SubPes3)
		self.PesApoderado.config(bg='#f1f6fc',fg=self.StyleBgColor)
		self.PesEstudiante.config(bg='#f1f6fc',fg=self.StyleBgColor)
		self.PesPadre.config(bg='#5c8cc5')
		self.PesMadre.config(bg='#f1f6fc',fg=self.StyleBgColor)
		self.PesIA.config(bg='#f1f6fc',fg=self.StyleBgColor)
		self.PesEA.config(bg='#f1f6fc',fg=self.StyleBgColor)
		self.PesIK.config(bg='#f1f6fc',fg=self.StyleBgColor)
		self.PesEK.config(bg='#f1f6fc',fg=self.StyleBgColor)
		self.PesApoderado.bind('<Leave>',lambda event: self.PesApoderado.config(bg='#f1f6fc',fg=self.StyleBgColor))
		self.PesEstudiante.bind('<Leave>',lambda event: self.PesEstudiante.config(bg='#f1f6fc',fg=self.StyleBgColor))
		self.PesPadre.bind('<Leave>',lambda event: self.PesPadre.config(bg='#5c8cc5',fg='white'))
		self.PesMadre.bind('<Leave>',lambda event: self.PesMadre.config(bg='#f1f6fc',fg=self.StyleBgColor))
		self.PesIA.bind('<Leave>',lambda event: self.PesIA.config(bg='#f1f6fc',fg=self.StyleBgColor))
		self.PesEA.bind('<Leave>',lambda event: self.PesEA.config(bg='#f1f6fc',fg=self.StyleBgColor))
		self.PesIK.bind('<Leave>',lambda event: self.PesIK.config(bg='#f1f6fc',fg=self.StyleBgColor))
		self.PesEK.bind('<Leave>',lambda event: self.PesEK.config(bg='#f1f6fc',fg=self.StyleBgColor))

	def SelecPesMadre(self,event):
		self.SubPestana.select(self.SubPes4)
		self.PesApoderado.config(bg='#f1f6fc',fg=self.StyleBgColor)
		self.PesEstudiante.config(bg='#f1f6fc',fg=self.StyleBgColor)
		self.PesPadre.config(bg='#f1f6fc',fg=self.StyleBgColor)
		self.PesMadre.config(bg='#5c8cc5')
		self.PesIA.config(bg='#f1f6fc',fg=self.StyleBgColor)
		self.PesEA.config(bg='#f1f6fc',fg=self.StyleBgColor)
		self.PesIK.config(bg='#f1f6fc',fg=self.StyleBgColor)
		self.PesEK.config(bg='#f1f6fc',fg=self.StyleBgColor)
		self.PesApoderado.bind('<Leave>',lambda event: self.PesApoderado.config(bg='#f1f6fc',fg=self.StyleBgColor))
		self.PesEstudiante.bind('<Leave>',lambda event: self.PesEstudiante.config(bg='#f1f6fc',fg=self.StyleBgColor))
		self.PesPadre.bind('<Leave>',lambda event: self.PesPadre.config(bg='#f1f6fc',fg=self.StyleBgColor))
		self.PesMadre.bind('<Leave>',lambda event: self.PesMadre.config(bg='#5c8cc5',fg='white'))
		self.PesIA.bind('<Leave>',lambda event: self.PesIA.config(bg='#f1f6fc',fg=self.StyleBgColor))
		self.PesEA.bind('<Leave>',lambda event: self.PesEA.config(bg='#f1f6fc',fg=self.StyleBgColor))
		self.PesIK.bind('<Leave>',lambda event: self.PesIK.config(bg='#f1f6fc',fg=self.StyleBgColor))
		self.PesEK.bind('<Leave>',lambda event: self.PesEK.config(bg='#f1f6fc',fg=self.StyleBgColor))

	def SelecPesIA(self,event):
		self.SubPestana.select(self.SubPesIG1)
		self.PesApoderado.config(bg='#f1f6fc',fg=self.StyleBgColor)
		self.PesEstudiante.config(bg='#f1f6fc',fg=self.StyleBgColor)
		self.PesPadre.config(bg='#f1f6fc',fg=self.StyleBgColor)
		self.PesMadre.config(bg='#f1f6fc',fg=self.StyleBgColor)
		self.PesIA.config(bg='#5c8cc5')
		self.PesEA.config(bg='#f1f6fc',fg=self.StyleBgColor)
		self.PesIK.config(bg='#f1f6fc',fg=self.StyleBgColor)
		self.PesEK.config(bg='#f1f6fc',fg=self.StyleBgColor)
		self.PesApoderado.bind('<Leave>',lambda event: self.PesApoderado.config(bg='#f1f6fc',fg=self.StyleBgColor))
		self.PesEstudiante.bind('<Leave>',lambda event: self.PesEstudiante.config(bg='#f1f6fc',fg=self.StyleBgColor))
		self.PesPadre.bind('<Leave>',lambda event: self.PesPadre.config(bg='#f1f6fc',fg=self.StyleBgColor))
		self.PesMadre.bind('<Leave>',lambda event: self.PesMadre.config(bg='#f1f6fc',fg=self.StyleBgColor))
		self.PesIA.bind('<Leave>',lambda event: self.PesIA.config(bg='#5c8cc5',fg='white'))
		self.PesEA.bind('<Leave>',lambda event: self.PesEA.config(bg='#f1f6fc',fg=self.StyleBgColor))
		self.PesIK.bind('<Leave>',lambda event: self.PesIK.config(bg='#f1f6fc',fg=self.StyleBgColor))
		self.PesEK.bind('<Leave>',lambda event: self.PesEK.config(bg='#f1f6fc',fg=self.StyleBgColor))

	def SelecPesEA(self,event):
		self.SubPestana.select(self.SubPesIG2)
		self.PesApoderado.config(bg='#f1f6fc',fg=self.StyleBgColor)
		self.PesEstudiante.config(bg='#f1f6fc',fg=self.StyleBgColor)
		self.PesPadre.config(bg='#f1f6fc',fg=self.StyleBgColor)
		self.PesMadre.config(bg='#f1f6fc',fg=self.StyleBgColor)
		self.PesIA.config(bg='#f1f6fc',fg=self.StyleBgColor)
		self.PesEA.config(bg='#5c8cc5')
		self.PesIK.config(bg='#f1f6fc',fg=self.StyleBgColor)
		self.PesEK.config(bg='#f1f6fc',fg=self.StyleBgColor)
		self.PesApoderado.bind('<Leave>',lambda event: self.PesApoderado.config(bg='#f1f6fc',fg=self.StyleBgColor))
		self.PesEstudiante.bind('<Leave>',lambda event: self.PesEstudiante.config(bg='#f1f6fc',fg=self.StyleBgColor))
		self.PesPadre.bind('<Leave>',lambda event: self.PesPadre.config(bg='#f1f6fc',fg=self.StyleBgColor))
		self.PesMadre.bind('<Leave>',lambda event: self.PesMadre.config(bg='#f1f6fc',fg=self.StyleBgColor))
		self.PesIA.bind('<Leave>',lambda event: self.PesIA.config(bg='#f1f6fc',fg=self.StyleBgColor))
		self.PesEA.bind('<Leave>',lambda event: self.PesEA.config(bg='#5c8cc5',fg='white'))
		self.PesIK.bind('<Leave>',lambda event: self.PesIK.config(bg='#f1f6fc',fg=self.StyleBgColor))
		self.PesEK.bind('<Leave>',lambda event: self.PesEK.config(bg='#f1f6fc',fg=self.StyleBgColor))

	def SelecPesIK(self,event):
		self.SubPestana.select(self.SubPesIG3)
		self.PesApoderado.config(bg='#f1f6fc',fg=self.StyleBgColor)
		self.PesEstudiante.config(bg='#f1f6fc',fg=self.StyleBgColor)
		self.PesPadre.config(bg='#f1f6fc',fg=self.StyleBgColor)
		self.PesMadre.config(bg='#f1f6fc',fg=self.StyleBgColor)
		self.PesIA.config(bg='#f1f6fc',fg=self.StyleBgColor)
		self.PesEA.config(bg='#f1f6fc',fg=self.StyleBgColor)
		self.PesIK.config(bg='#5c8cc5')
		self.PesEK.config(bg='#f1f6fc',fg=self.StyleBgColor)
		self.PesApoderado.bind('<Leave>',lambda event: self.PesApoderado.config(bg='#f1f6fc',fg=self.StyleBgColor))
		self.PesEstudiante.bind('<Leave>',lambda event: self.PesEstudiante.config(bg='#f1f6fc',fg=self.StyleBgColor))
		self.PesPadre.bind('<Leave>',lambda event: self.PesPadre.config(bg='#f1f6fc',fg=self.StyleBgColor))
		self.PesMadre.bind('<Leave>',lambda event: self.PesMadre.config(bg='#f1f6fc',fg=self.StyleBgColor))
		self.PesIA.bind('<Leave>',lambda event: self.PesIA.config(bg='#f1f6fc',fg=self.StyleBgColor))
		self.PesEA.bind('<Leave>',lambda event: self.PesEA.config(bg='#f1f6fc',fg=self.StyleBgColor))
		self.PesIK.bind('<Leave>',lambda event: self.PesIK.config(bg='#5c8cc5',fg='white'))
		self.PesEK.bind('<Leave>',lambda event: self.PesEK.config(bg='#f1f6fc',fg=self.StyleBgColor))

	def SelecPesEK(self,event):
		self.SubPestana.select(self.SubPesIG4)
		self.PesApoderado.config(bg='#f1f6fc',fg=self.StyleBgColor)
		self.PesEstudiante.config(bg='#f1f6fc',fg=self.StyleBgColor)
		self.PesPadre.config(bg='#f1f6fc',fg=self.StyleBgColor)
		self.PesMadre.config(bg='#f1f6fc',fg=self.StyleBgColor)
		self.PesIA.config(bg='#f1f6fc',fg=self.StyleBgColor)
		self.PesEA.config(bg='#f1f6fc',fg=self.StyleBgColor)
		self.PesIK.config(bg='#f1f6fc',fg=self.StyleBgColor)
		self.PesEK.config(bg='#5c8cc5')
		self.PesApoderado.bind('<Leave>',lambda event: self.PesApoderado.config(bg='#f1f6fc',fg=self.StyleBgColor))
		self.PesEstudiante.bind('<Leave>',lambda event: self.PesEstudiante.config(bg='#f1f6fc',fg=self.StyleBgColor))
		self.PesPadre.bind('<Leave>',lambda event: self.PesPadre.config(bg='#f1f6fc',fg=self.StyleBgColor))
		self.PesMadre.bind('<Leave>',lambda event: self.PesMadre.config(bg='#f1f6fc',fg=self.StyleBgColor))
		self.PesIA.bind('<Leave>',lambda event: self.PesIA.config(bg='#f1f6fc',fg=self.StyleBgColor))
		self.PesEA.bind('<Leave>',lambda event: self.PesEA.config(bg='#f1f6fc',fg=self.StyleBgColor))
		self.PesIK.bind('<Leave>',lambda event: self.PesIK.config(bg='#f1f6fc',fg=self.StyleBgColor))
		self.PesEK.bind('<Leave>',lambda event: self.PesEK.config(bg='#5c8cc5',fg='white'))
		
	
