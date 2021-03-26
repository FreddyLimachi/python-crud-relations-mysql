from Functionality import *
from Graphic_interface2 import *
from PIL import Image, ImageTk

class Main_Window(Functionality,Emerging_Windows):
	
	def __init__(self,Window,Value,Name):
	
		self.WindowMain=Window
		self.EscribirTexto=StringVar()		
		self.ValorAge=IntVar()    

		#---Variables-Datos-Padre-Madre-Estudiante--#
		self.APP=StringVar()
		self.AMP=StringVar()
		self.NomP=StringVar()
		self.DNIP=StringVar()
		self.DirecP=StringVar()
		self.APM=StringVar()
		self.AMM=StringVar()
		self.NomM=StringVar()
		self.DNIM=StringVar()
		self.DirecM=StringVar()
		self.APA=StringVar()
		self.AMA=StringVar()
		self.NomA=StringVar()
		self.DNIA=StringVar()
		self.DirecA=StringVar()
		self.Apoderado=StringVar()

		self.CuotaAmapafa=StringVar()
		self.Multa=StringVar()
		self.ModMulta=StringVar()
		self.DNIAll=StringVar()
		
		#-------Hijos-----------#		
		self.GradoM=StringVar()
		self.SeccionM=StringVar()
		self.TipoPagoM=StringVar()
		self.PagoM=StringVar()
		self.EstadoM=StringVar()

		#------Congifurar-Pagos---------#
		self.CuotaSocio=StringVar()
		self.CuotaIngresante=StringVar()

		self.Guardar=StringVar()
		self.Modificar=StringVar()
		self.Eliminando=StringVar()
		self.Cargar=StringVar()

		self.NExportar=StringVar()
		self.Buscando=StringVar()
		self.ValorOrdenar=IntVar()

		self.Usuario=StringVar()
		self.ContraActual=StringVar()
		self.ContraNueva=StringVar()
		self.MostrarContra=BooleanVar()

		self.IngresoGasto=StringVar()
		self.NombreIG=StringVar()
		self.MontoIG=StringVar()

		self.DiaIni=StringVar()
		self.MesIni=StringVar()
		self.AgeIni=StringVar()
		self.DiaFin=StringVar()
		self.MesFin=StringVar()
		self.AgeFin=StringVar()
		self.Dia=StringVar()
		self.Mes=StringVar()
		self.Age=StringVar()

		self.Grado1=StringVar()
		self.Grado2=StringVar()
		self.Grado3=StringVar()
		self.Grado4=StringVar()
		self.Grado5=StringVar()
		self.Grado6=StringVar()
		self.Seccion1=StringVar()
		self.Seccion2=StringVar()
		self.Seccion3=StringVar()
		self.Seccion4=StringVar()
		self.Seccion5=StringVar()
		self.Seccion6=StringVar()
		
		self.TipoPago1=StringVar()
		self.TipoPago2=StringVar()
		self.TipoPago3=StringVar()
		self.TipoPago4=StringVar()
		self.TipoPago5=StringVar()
		self.TipoPago6=StringVar()
		self.Estado1=StringVar()
		self.Estado2=StringVar()
		self.Estado3=StringVar()
		self.Estado4=StringVar()
		self.Estado5=StringVar()
		self.Estado6=StringVar()
		self.NEstudiantes=StringVar()

		#------Ventana-Exportar----------#
		self.CEDNom=IntVar()
		self.CEDDNI=IntVar()
		self.CEDDirec=IntVar()
		self.CEDMulta=IntVar()
		self.CEDNAlum=IntVar()
		style = ttk.Style(self.WindowMain)
		self.StyleBgColor='#466183'
		style.layout('TNotebook.Tab', [])

		self.Datos=Data()

		self.ImagenInicio=PhotoImage(file='img/ImageHome.png')
		self.ImagenEliminar=PhotoImage(file='img/ImageRemove.png')
		self.ImagenCargar=PhotoImage(file='img/ImageLoad.png')
		self.ImagenExportar=PhotoImage(file='img/ImageReport.png')
		self.ImagenRegSocio=PhotoImage(file='img/ImageAdd.png')
		self.ImagenIngreso=PhotoImage(file='img/ImageIncome.png')
		self.ImagenRegIG=PhotoImage(file='img/ImageReg.png')
		self.ImagenCalendar=PhotoImage(file='img/ImageCalendar.png')
		self.MainWindow(Value,Name)

		

		########################Menu########################

	def MainWindow(self,Value,Name):
		self.WindowMain.title("Optimal Data")
		self.WindowMain.geometry("887x480+200+75")
		self.WindowMain.iconbitmap("img/My_icon.ico")
		self.WindowMain.resizable(0,0)
		self.Default=Name

		BarraMenu=Menu(self.WindowMain)
		self.AgeAnterior=Menu(self.WindowMain)
		self.WindowMain.config(menu=BarraMenu,width=300,height=300)

		self.Archivo=Menu(BarraMenu,tearoff=0)
		self.Archivo.add_command(label="Año Activo                                   ",command=lambda:(self.AgeAnterior.invoke(0)))
		self.Archivo.add_command(label="Insertar Nuevo Año ",command=self.InsertarAge)
		
		self.AgeAnterior=Menu(self.Archivo,tearoff=0)
		self.AgregarAge()
		
		self.Archivo.add_cascade(label="Ver todos los años",menu=self.AgeAnterior)
		self.Archivo.add_separator()
		
		self.Archivo.add_command(label="Cambiar Contraseña",command=self.Create_Window_Change_Login)
		self.Archivo.add_command(label="Salir",command=self.SalirAplicacion)

		self.Edicion=Menu(BarraMenu,tearoff=0)
		self.Edicion.add_command(label="Cambiar texto de presentación",command=self.VentanaTexto)
		self.Edicion.add_command(label="Cambiar imagen de presentación",command=self.CambiarImagen)
		self.AgeAnterior.invoke(0)
		self.ConsultarPagos()

		Ayuda=Menu(BarraMenu, tearoff=0)
		Ayuda.add_command(label="Ver la Ayuda           ",command=lambda:(messagebox.showinfo('Mensaje','Pronto estara disponible en proximas versiones')))
		Ayuda.add_separator()
		Ayuda.add_command(label="Acerca de",command=lambda:(messagebox.showinfo("Mensaje","Esta es la versión 1.0 de Optimal Data y esta sujeto a errores, no dude en reportarnos cualquier error para asi en proximas versiones mejorar y regular tanto errores como bugs.")))
		
		self.Herramientas=Menu(BarraMenu,tearoff=0)
		self.Herramientas.add_command(label="Configurar Cuota AMAPAFA",command=self.VentanaConfigurar)

		BarraMenu.add_cascade(label="Archivo",menu=self.Archivo)
		BarraMenu.add_cascade(label="Edicion",menu=self.Edicion)
		BarraMenu.add_cascade(label="Herramientas",menu=self.Herramientas)
		BarraMenu.add_cascade(label="Ayuda",menu=Ayuda)

		#--------------Construccion-de-Pestañas-y-Diseño-de-Interfaz-----------------#
		#↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓#
		
		self.Pestana=ttk.Notebook(self.WindowMain)
		self.Pestana.place(x=175,y=0)
		global LabelImagen
		FrameFondo=Frame(self.WindowMain,width=176,height=81)
		FrameFondo.place(x=-2,y=-2)
		ImagenFondo=Image.open('img/ImageFond.png')
		ImagenFondo = ImagenFondo.resize((900, 62), Image.ANTIALIAS)
		ImagenFondo = ImageTk.PhotoImage(ImagenFondo)
		
		LabelImagen=Label(FrameFondo,image=ImagenFondo)
		LabelImagen.pack()
		LabelImagen.image=ImagenFondo
		
		FramePes=Frame(self.WindowMain,bg='#d4dce3',width=175,height=367)
		FramePes.place(x=0,y=62)
		
		self.Pes1=ttk.Frame(self.Pestana)
		self.Pestana.add(self.Pes1)
		self.Pes2=ttk.Frame(self.Pestana)
		self.Pestana.add(self.Pes2)
		self.Pes3=ttk.Frame(self.Pestana)
		self.Pestana.add(self.Pes3)
		self.Pes4=ttk.Frame(self.Pestana)
		self.Pestana.add(self.Pes4)
		self.Pes5=ttk.Frame(self.Pestana)
		self.Pestana.add(self.Pes5)
		self.Pes6=ttk.Frame(self.Pestana)
		self.Pestana.add(self.Pes6)

		self.PesInicio=Button(FramePes,text="   Inicio                        ",bg='#5c8cc5',fg='white',activebackground='#5c8cc5',relief='sunken',activeforeground='white',width=175,height=40,bd=0,image=self.ImagenInicio,compound=LEFT)
		self.PesInicio.place(x=0,y=50)
		self.PesRegSocio=Button(FramePes,text="   Nuevo Socio             ",bg='#d4dce3',activebackground='#5c8cc5',activeforeground='white',relief='sunken',width=175,height=40,bd=0,image=self.ImagenRegSocio,compound=LEFT)
		self.PesRegSocio.place(x=0,y=95)
		self.PesRegIG=Button(FramePes,text="   Ver Registros           ",bg='#d4dce3',activebackground='#5c8cc5',activeforeground='white',relief='sunken',width=175,height=40,bd=0,image=self.ImagenRegIG,compound=LEFT)
		self.PesRegIG.place(x=0,y=140)
		self.PesVerReg=Button(FramePes,text="   Ingresos Egresos    ",bg='#d4dce3',activebackground='#5c8cc5',activeforeground='white',relief='sunken',width=175,height=40,bd=0,image=self.ImagenIngreso,compound=LEFT)
		self.PesVerReg.place(x=0,y=185)
		self.PesGenRep=Button(FramePes,text="   Generar Reporte     ",bg='#d4dce3',activebackground='#5c8cc5',activeforeground='white',relief='sunken',width=175,height=40,bd=0,image=self.ImagenExportar,compound=LEFT)
		self.PesGenRep.place(x=0,y=230)

		self.PesInicio.bind('<Enter>',lambda event: self.PesInicio.config(bg='#5c8cc5',fg='white'))
		self.PesInicio.bind('<Button-1>',self.SelecPesInicio)
		self.PesRegSocio.bind('<Enter>',lambda event: self.PesRegSocio.config(bg='#5c8cc5',fg='white'))
		self.PesRegSocio.bind('<Leave>',lambda event: self.PesRegSocio.config(bg='#d4dce3',fg='black'))
		self.PesRegSocio.bind('<Button-1>',self.SelecPesRegSocio)
		self.PesRegIG.bind('<Enter>',lambda event: self.PesRegIG.config(bg='#5c8cc5',fg='white'))
		self.PesRegIG.bind('<Leave>',lambda event: self.PesRegIG.config(bg='#d4dce3',fg='black'))
		self.PesRegIG.bind('<Button-1>',self.SelecPesRegIG)
		self.PesVerReg.bind('<Enter>',lambda event: self.PesVerReg.config(bg='#5c8cc5',fg='white'))
		self.PesVerReg.bind('<Leave>',lambda event: self.PesVerReg.config(bg='#d4dce3',fg='black'))
		self.PesVerReg.bind('<Button-1>',self.SelecPesVerReg)
		self.PesGenRep.bind('<Enter>',lambda event: self.PesGenRep.config(bg='#5c8cc5',fg='white'))
		self.PesGenRep.bind('<Leave>',lambda event: self.PesGenRep.config(bg='#d4dce3',fg='black'))
		self.PesGenRep.bind('<Button-1>',self.SelecPesGenRep)

		Frame(self.WindowMain,width=887,bg='black').place(x=0,y=62,height=2)
		Frame(self.WindowMain,width=887,bg='black').place(x=0,y=427,height=1)
		FramePie=Frame(self.WindowMain,height='32',width='887',bg='#bcbcbc')
		FramePie.place(x=0,y=428)

		Label(FramePie,text='Presione F1 para obtener',bg='#bcbcbc').place(x=25,y=5)
		LinkAyuda=Label(FramePie,text="ayuda",fg="blue",bg='#bcbcbc',cursor="hand2")
		LinkAyuda.place(x=159,y=5)
		LinkAyuda.bind("<Button-1>",lambda url:(webbrowser.open_new("http://www.youtube.com")))

		#↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑#
		#------------------------------------------------------------------------------#
		
		#-------------------Construccion-y-diseño-de-la-Pestaña-Inicio-------------------#
		#↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓#

		BloqueA1=Frame(self.Pes1,width=712,height=363,bg='#f1f6fc')
		BloqueA1.place(x=0,y=61)

		FrameTexto=Frame(BloqueA1)
		FrameTexto.place(x=25,y=100)
		self.MensajeBienvenida=Label(FrameTexto,bg='#f1f6fc',font=("Arial Rounded MT Bold",30),wraplength=450)
		self.MensajeBienvenida.pack()
		self.InsertarTexto()
		FrameImagen=Frame(BloqueA1,width="500",height="500")
		FrameImagen.place(x=425,y=80)
		self.LabelImagen=Label(FrameImagen,compound='left',anchor='e',bg='#f1f6fc')
		self.LabelImagen.pack()
		self.InsertarImagen()

		#↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑#
		#------------------------------------------------------------------------------------#
	
		#------Construccion-y-Diseño-de-la-Pestaña-Registrar-Padres-y-Estudiantes-----------#
		#↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓#

		Frame(self.Pes2,width=1048,height="70",bg='#f1f6fc').pack()

		self.BloqueB2=Frame(self.Pes2,height="400",width="1050",bg='#f1f6fc')
		self.BloqueB2.pack()

		BloqueB1=Frame(self.Pes2,height='37',width='800',bg='#d4dce3')
		BloqueB1.place(x=0,y=387)


		self.BotonAll=Button(BloqueB1,text="Cargar",cursor="hand2",bd=0,bg='#5c8cc5',fg='white',activebackground='#5c8cc5',command=self.CargarAll)
		self.BotonAll.place(x=126,y=5,height=21)

		self.CuadroPasar=ttk.Entry(BloqueB1)
		self.CuadroPasar.config(foreground="Gray",width=15,textvariable=self.DNIAll)
		self.CuadroPasar.place(x=30,y=5)
		self.DNIAll.set("Escriba el DNI")
		self.CuadroPasar.bind("<FocusIn>", self.DesaparecerGris)
		self.CuadroPasar.bind("<FocusOut>", self.DesaparecerGris)

		self.BotonRegistrar=Button(BloqueB1,text="Registrar",bd=0,bg='#5c8cc5',fg='white',width=15,command=self.Registrar)
		self.BotonDeshacer=Button(BloqueB1,text="Deshacer",bd=0,bg='#5c8cc5',fg='white',width=15,command=self.LimpiarDatos)
		self.BotonModificar=Button(BloqueB1,text="Modificar",bd=0,bg='#5c8cc5',fg='white',width=15,command=self.ModificarDatos)
		self.BotonCancel=Button(BloqueB1,text="Cancelar",bd=0,bg='#5c8cc5',fg='white',width=15,command=self.CancelarDatos)

		#---------------Bloque-para-el-relleno-de-datos-del-Padre-Madre-Apodeado-------------#	
		BloqueAPM=Frame(self.BloqueB2,width=850,height=210,padx=5,bg='#f1f6fc')
		BloqueAPM.place(x=20,y=0)
		
		Label(BloqueAPM,text="Apellido Paterno",bg='#f1f6fc').grid(row=0,column=2,sticky='w')
		Label(BloqueAPM,text="Apellido Materno",bg='#f1f6fc').grid(row=0,column=3,sticky='w')
		Label(BloqueAPM,text="Nombres",bg='#f1f6fc').grid(row=0,column=4,sticky='w')		
		Label(BloqueAPM,text="DNI",bg='#f1f6fc').grid(row=0,column=5,sticky='w',padx=10)

		Label(BloqueAPM,text='Padre',bg='#f1f6fc').grid(row=1,column=1,sticky='e',pady=5)
		ttk.Entry(BloqueAPM,textvariable=self.APP).grid(row=1,column=2)
		ttk.Entry(BloqueAPM,textvariable=self.AMP).grid(row=1,column=3)
		ttk.Entry(BloqueAPM,textvariable=self.NomP).grid(row=1,column=4)
		ttk.Entry(BloqueAPM,textvariable=self.DNIP,width=10).grid(row=1,column=5,padx=10)

		Label(BloqueAPM,text='Madre',bg='#f1f6fc').grid(row=2,column=1,sticky='e',pady=5)
		ttk.Entry(BloqueAPM,textvariable=self.APM).grid(row=2,column=2)
		ttk.Entry(BloqueAPM,textvariable=self.AMM).grid(row=2,column=3)
		ttk.Entry(BloqueAPM,textvariable=self.NomM).grid(row=2,column=4)
		ttk.Entry(BloqueAPM,textvariable=self.DNIM,width=10).grid(row=2,column=5)
		
		Label(BloqueAPM,text='Apoderado',bg='#f1f6fc').grid(row=3,column=1,sticky='e',pady=5)
		ttk.Entry(BloqueAPM,textvariable=self.APA).grid(row=3,column=2)
		ttk.Entry(BloqueAPM,textvariable=self.AMA).grid(row=3,column=3)
		ttk.Entry(BloqueAPM,textvariable=self.NomA).grid(row=3,column=4)
		ttk.Entry(BloqueAPM,textvariable=self.DNIA,width=10).grid(row=3,column=5)
		ttk.Entry(BloqueAPM,textvariable=self.DirecA,width=19).grid(row=3,column=6)
		
		#-------------------Selecionar-Apoderado----------------------#
		
		self.ComboCuota=ttk.Combobox(BloqueAPM,textvariable=self.CuotaAmapafa,width=10,state='readonly')
		self.ComboCuota.grid(row=1,column=6,sticky='we')
		self.ComboCuota['values']=['Socio','Ingresante','Exonerado']
		self.ComboCuota.bind("<<ComboboxSelected>>", self.SelecCuotaAmapafa)

		self.ComboApoderado=ttk.Combobox(BloqueAPM,textvariable=self.Apoderado,width=9,state='readonly')
		self.ComboApoderado.grid(row=2,column=6,sticky='we')
		self.ComboApoderado['values']=['Padre','Madre','Otro']
		self.ComboApoderado.bind("<<ComboboxSelected>>", self.SeleccionarApoderado)

		#Frame(BloqueAPM,width=20).grid(row=4,column=9)

		Label(BloqueAPM,text="Multa",bg='#f1f6fc').grid(row=4,column=3)
		Label(BloqueAPM,text='S/',bg='#f1f6fc').grid(row=4,column=3,sticky='w')
		ttk.Entry(BloqueAPM,width=10,justify="right",textvariable=self.Multa).grid(row=4,column=4)
		Label(BloqueAPM,text="Cancelado",bg='#f1f6fc').grid(row=4,column=5)
		Label(BloqueAPM,text='S/',bg='#f1f6fc').grid(row=4,column=5,sticky='w')
		self.CuadroMulta=Label(BloqueAPM,text="0.00",bg='#f1f6fc')
		self.CuadroMulta.grid(row=4,column=6)
		
		NH=["1 Estudiante a cargo",
			"2 Estudiantes a cargo",
			"3 Estudiantes a cargo",
			"4 Estudiantes a cargo",
			"5 Estudiantes a cargo",
			"6 Estudiantes a cargo"]
		
		self.ComboNEstudiantes=ttk.Combobox(BloqueAPM,values=NH,textvariable=self.NEstudiantes,state='readonly')
		self.ComboNEstudiantes.grid(row=4,column=1,columnspan=2,sticky='we',pady=5)
		self.ComboNEstudiantes.bind("<<ComboboxSelected>>", self.SelecNEstudiantes)

		'''self.BotonRegistrar=ttk.Button(self.BloqueB1,text="Registrar",command=self.Registrar)
		self.BotonRegistrar.place(x=800,y=25)
		self.BotonRegistrar.config(state=NORMAL)
		self.BotonModRegistro=ttk.Button(self.BloqueB1,text="Modificar",command=self.ModificarEstudiante)
		self.BotonModRegistro.place(x=700,y=25)
		self.BotonModRegistro.config(state=DISABLED)
		ttk.Button(self.BloqueB1,text="Cancelar",command=self.CancelModEstudiante).place(x=600,y=25)'''

		#--------------------Datos-de-los-Hijos---------------#
		def myfunction(event):
			canvas.configure(scrollregion=canvas.bbox("all"),width=660,height=90)

		canvas=Canvas(self.BloqueB2,bg='#f1f6fc')
		canvas.place(x=25,y=180)

		self.BloqueHijos=Frame(canvas,bg='#f1f6fc')
		self.BloqueHijos.bind("<Configure>",myfunction)
		self.BloqueHijos.pack()
		myscrollbar=Scrollbar(self.BloqueB2,orient="vertical",command=canvas.yview)
		canvas.configure(yscrollcommand=myscrollbar.set)
		myscrollbar.place(x=670,y=182,height=90)
		
		canvas.create_window((0,0),window=self.BloqueHijos,anchor='nw')

		FrameName=Frame(self.BloqueB2,width=854,height=20,bg='#f1f6fc')
		FrameName.place(x=-2,y=160)
		Label(FrameName,text="Apellido Paterno",bg='#f1f6fc').place(x=41,y=0)
		Label(FrameName,text="Apellido Materno",bg='#f1f6fc').place(x=135,y=0)
		Label(FrameName,text="Nombres",bg='#f1f6fc').place(x=260,y=0)
		Label(FrameName,text="DNI",bg='#f1f6fc').place(x=365,y=0)
		Label(FrameName,text="Grado",bg='#f1f6fc').place(x=415,y=0)
		Label(FrameName,text="Sección",bg='#f1f6fc').place(x=450,y=0)
		Label(FrameName,text='Estado',bg='#f1f6fc').place(x=505,y=0)
		Label(FrameName,text="Pago",bg='#f1f6fc').place(x=580,y=0)
		Label(FrameName,text="Cancelado",bg='#f1f6fc').place(x=625,y=0)
		Label(self.BloqueHijos,text="1",bg='#f1f6fc').grid(row=2,column=0,pady=5)
		self.APE1=ttk.Entry(self.BloqueHijos,width=15)
		self.APE1.grid(row=2,column=1)
		self.AME1=ttk.Entry(self.BloqueHijos,width=15)
		self.AME1.grid(row=2,column=2)
		self.NomE1=ttk.Entry(self.BloqueHijos,width=17)
		self.NomE1.grid(row=2,column=3)
		self.DNIE1=ttk.Entry(self.BloqueHijos,width=10)
		self.DNIE1.grid(row=2,column=4,padx=5)
		
		self.ComboGrado1=ttk.Combobox(self.BloqueHijos,textvariable=self.Grado1,width=2,state='readonly')
		self.ComboGrado1.grid(row=2,column=5)
		self.ComboGrado1['values']=['○','1','2','3','4','5','6']

		self.ComboSeccion1=ttk.Combobox(self.BloqueHijos,textvariable=self.Seccion1,width=2,state='readonly')
		self.ComboSeccion1.grid(row=2,column=6,padx=5)
		self.ComboSeccion1['values']=['○','A','B','C']

		self.ComboEstado1=ttk.Combobox(self.BloqueHijos,textvariable=self.Estado1,width=7,state='readonly')
		self.ComboEstado1.grid(row=2,column=7)
		self.ComboEstado1['values']=['Normal','Traslado','Retirado']

		self.ComboTipoPago1=ttk.Combobox(self.BloqueHijos,textvariable=self.TipoPago1,width=6,state='normal',justify='right')
		self.ComboTipoPago1.grid(row=2,column=8,padx=5)
		self.ComboTipoPago1['values']=['Pago','Exonerado']
		self.ComboTipoPago1.bind("<<ComboboxSelected>>", self.SelecTipoCuota1)

		self.TextoMonto1=Label(self.BloqueHijos,bg='#f1f6fc')
		self.TextoMonto1.grid(row=2,column=10)

		Label(self.BloqueHijos,text="2",bg='#f1f6fc').grid(row=3,column=0,pady=5)
		self.APE2=ttk.Entry(self.BloqueHijos,width=15)
		self.APE2.grid(row=3,column=1)
		self.AME2=ttk.Entry(self.BloqueHijos,width=15)
		self.AME2.grid(row=3,column=2)
		self.NomE2=ttk.Entry(self.BloqueHijos,width=17)
		self.NomE2.grid(row=3,column=3)
		self.DNIE2=ttk.Entry(self.BloqueHijos,width=10)
		self.DNIE2.grid(row=3,column=4)
		
		self.ComboGrado2=ttk.Combobox(self.BloqueHijos,textvariable=self.Grado2,width=2,state='readonly')
		self.ComboGrado2.grid(row=3,column=5)
		self.ComboGrado2['values']=['○','1','2','3','4','5','6']

		self.ComboSeccion2=ttk.Combobox(self.BloqueHijos,textvariable=self.Seccion2,width=2,state='readonly')
		self.ComboSeccion2.grid(row=3,column=6)
		self.ComboSeccion2['values']=['○','A','B','C']

		self.ComboEstado2=ttk.Combobox(self.BloqueHijos,textvariable=self.Estado2,width=7,state='readonly')
		self.ComboEstado2.grid(row=3,column=7)
		self.ComboEstado2['values']=['Normal','Traslado','Retirado']

		self.ComboTipoPago2=ttk.Combobox(self.BloqueHijos,textvariable=self.TipoPago2,width=6,state='readonly',justify='right')
		self.ComboTipoPago2.grid(row=3,column=8)
		self.ComboTipoPago2['values']=['Pago','Exonerado']
		self.ComboTipoPago2.bind("<<ComboboxSelected>>", self.SelecTipoCuota2)

		self.TextoMonto2=Label(self.BloqueHijos,bg='#f1f6fc')
		self.TextoMonto2.grid(row=3,column=10)

		Label(self.BloqueHijos,text="3",bg='#f1f6fc').grid(row=4,column=0,pady=5)
		self.APE3=ttk.Entry(self.BloqueHijos,width=15)
		self.APE3.grid(row=4,column=1)
		self.AME3=ttk.Entry(self.BloqueHijos,width=15)
		self.AME3.grid(row=4,column=2)
		self.NomE3=ttk.Entry(self.BloqueHijos,width=17)
		self.NomE3.grid(row=4,column=3)
		self.DNIE3=ttk.Entry(self.BloqueHijos,width=10)
		self.DNIE3.grid(row=4,column=4)

		self.ComboGrado3=ttk.Combobox(self.BloqueHijos,textvariable=self.Grado3,width=2,state='readonly')
		self.ComboGrado3.grid(row=4,column=5)
		self.ComboGrado3['values']=['1','2','3','4','5','6']

		self.ComboSeccion3=ttk.Combobox(self.BloqueHijos,textvariable=self.Seccion3,width=2,state='readonly')
		self.ComboSeccion3.grid(row=4,column=6)
		self.ComboSeccion3['values']=['○','A','B','C']

		self.ComboEstado3=ttk.Combobox(self.BloqueHijos,textvariable=self.Estado3,width=7,state='readonly')
		self.ComboEstado3.grid(row=4,column=7)
		self.ComboEstado3['values']=['Normal','Traslado','Retirado']

		self.ComboTipoPago3=ttk.Combobox(self.BloqueHijos,textvariable=self.TipoPago3,width=6,state='readonly',justify='right')
		self.ComboTipoPago3.grid(row=4,column=8)
		self.ComboTipoPago3['values']=['Pago','Exonerado']
		self.ComboTipoPago3.bind("<<ComboboxSelected>>", self.SelecTipoCuota3)

		self.TextoMonto3=Label(self.BloqueHijos,bg='#f1f6fc')
		self.TextoMonto3.grid(row=4,column=10)

		Label(self.BloqueHijos,text="4",bg='#f1f6fc').grid(row=5,column=0,pady=5)
		self.APE4=ttk.Entry(self.BloqueHijos,width=15)
		self.APE4.grid(row=5,column=1)
		self.AME4=ttk.Entry(self.BloqueHijos,width=15)
		self.AME4.grid(row=5,column=2)
		self.NomE4=ttk.Entry(self.BloqueHijos,width=17)
		self.NomE4.grid(row=5,column=3)
		self.DNIE4=ttk.Entry(self.BloqueHijos,width=10)
		self.DNIE4.grid(row=5,column=4)

		self.ComboGrado4=ttk.Combobox(self.BloqueHijos,textvariable=self.Grado4,width=2,state='readonly')
		self.ComboGrado4.grid(row=5,column=5)
		self.ComboGrado4['values']=['○','1','2','3','4','5','6']

		self.ComboSeccion4=ttk.Combobox(self.BloqueHijos,textvariable=self.Seccion4,width=2,state='readonly')
		self.ComboSeccion4.grid(row=5,column=6)
		self.ComboSeccion4['values']=['○','A','B','C']

		self.ComboEstado4=ttk.Combobox(self.BloqueHijos,textvariable=self.Estado4,width=7,state='readonly')
		self.ComboEstado4.grid(row=5,column=7)
		self.ComboEstado4['values']=['Normal','Traslado','Retirado']

		self.ComboTipoPago4=ttk.Combobox(self.BloqueHijos,textvariable=self.TipoPago4,width=6,state='readonly',justify='right')
		self.ComboTipoPago4.grid(row=5,column=8)
		self.ComboTipoPago4['values']=['Pago','Exonerado']
		self.ComboTipoPago4.bind("<<ComboboxSelected>>", self.SelecTipoCuota4)

		self.TextoMonto4=Label(self.BloqueHijos,bg='#f1f6fc')
		self.TextoMonto4.grid(row=5,column=10)
		
		Label(self.BloqueHijos,text="5",bg='#f1f6fc').grid(row=6,column=0,pady=5)
		self.APE5=ttk.Entry(self.BloqueHijos,width=15)
		self.APE5.grid(row=6,column=1)
		self.AME5=ttk.Entry(self.BloqueHijos,width=15)
		self.AME5.grid(row=6,column=2)
		self.NomE5=ttk.Entry(self.BloqueHijos,width=17)
		self.NomE5.grid(row=6,column=3)
		self.DNIE5=ttk.Entry(self.BloqueHijos,width=10)
		self.DNIE5.grid(row=6,column=4)
		
		self.ComboGrado5=ttk.Combobox(self.BloqueHijos,textvariable=self.Grado5,width=2,state='readonly')
		self.ComboGrado5.grid(row=6,column=5)
		self.ComboGrado5['values']=['○','1','2','3','4','5','6']

		self.ComboSeccion5=ttk.Combobox(self.BloqueHijos,textvariable=self.Seccion5,width=2,state='readonly')
		self.ComboSeccion5.grid(row=6,column=6)
		self.ComboSeccion5['values']=['○','A','B','C']

		self.ComboEstado5=ttk.Combobox(self.BloqueHijos,textvariable=self.Estado5,width=7,state='readonly')
		self.ComboEstado5.grid(row=6,column=7)
		self.ComboEstado5['values']=['Normal','Traslado','Retirado']

		self.ComboTipoPago5=ttk.Combobox(self.BloqueHijos,textvariable=self.TipoPago5,width=6,state='readonly',justify='right')
		self.ComboTipoPago5.grid(row=6,column=8)
		self.ComboTipoPago5['values']=['Pago','Exonerado']
		self.ComboTipoPago5.bind("<<ComboboxSelected>>", self.SelecTipoCuota5)

		self.TextoMonto5=Label(self.BloqueHijos,bg='#f1f6fc')
		self.TextoMonto5.grid(row=6,column=10)

		Label(self.BloqueHijos,text="6",bg='#f1f6fc').grid(row=7,column=0,pady=5)
		self.APE6=ttk.Entry(self.BloqueHijos,width=15)
		self.APE6.grid(row=7,column=1)
		self.AME6=ttk.Entry(self.BloqueHijos,width=15)
		self.AME6.grid(row=7,column=2)
		self.NomE6=ttk.Entry(self.BloqueHijos,width=17)
		self.NomE6.grid(row=7,column=3)
		self.DNIE6=ttk.Entry(self.BloqueHijos,width=10)
		self.DNIE6.grid(row=7,column=4)

		self.ComboGrado6=ttk.Combobox(self.BloqueHijos,textvariable=self.Grado6,width=2,state='readonly')
		self.ComboGrado6.grid(row=7,column=5)
		self.ComboGrado6['values']=['○','1','2','3','4','5','6']

		self.ComboSeccion6=ttk.Combobox(self.BloqueHijos,textvariable=self.Seccion6,width=2,state='readonly')
		self.ComboSeccion6.grid(row=7,column=6)
		self.ComboSeccion6['values']=['○','A','B','C']

		self.ComboEstado6=ttk.Combobox(self.BloqueHijos,textvariable=self.Estado6,width=7,state='readonly')
		self.ComboEstado6.grid(row=7,column=7)
		self.ComboEstado6['values']=['Normal','Traslado','Retirado']

		self.ComboTipoPago6=ttk.Combobox(self.BloqueHijos,textvariable=self.TipoPago6,width=6,state='readonly',justify='right')
		self.ComboTipoPago6.grid(row=7,column=8)
		self.ComboTipoPago6['values']=['Pago','Exonerado']
		self.ComboTipoPago6.bind("<<ComboboxSelected>>", self.SelecTipoCuota6)

		self.TextoMonto6=Label(self.BloqueHijos,bg='#f1f6fc')
		self.TextoMonto6.grid(row=7,column=10)

		#ttk.Separator(self.Pes2).place(x=25, y=110,width=660)
		#Frame(self.Pes2,width=660,height=5,bg='#5c8cc5').place(x=25,y=110)
		#Frame(self.Pes2,width=662,height=1,bg='gray').place(x=25,y=277)
		#Frame(self.Pes2,width=662,height=1,bg='gray').place(x=25,y=300)
		#Frame(self.Pes2,width=662,height=1,bg='gray').place(x=25,y=392)
		#Frame(self.Pes2,width=1,height=116,bg='gray').place(x=25,y=277)
		#Frame(self.Pes2,width=1,height=116,bg='gray').place(x=687,y=277)
		#Frame(self.Pes2,width=1,height=93,bg='gray').place(x=668,y=300)
		self.LimpiarDatos()

		#↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑#
		#------------------------------------------------------------------------------------#

		#------------------Construccion-y-Diseño-de-la-Pestaña-Ver-Registros-----------------#
		#↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓#

		Frame(self.Pes3,height="60").pack()

		self.BloqueC2=Frame(self.Pes3,height="420",width="800",bg='#f1f6fc')
		self.BloqueC2.place(x=0,y=60)

		BloqueC3=Frame(self.Pes3,height='37',width='711',bg='#d4dce3')
		BloqueC3.place(x=0,y=387)

		self.CuadroBuscar=ttk.Entry(BloqueC3,foreground="Gray",width=25)
		self.CuadroBuscar.insert(0,"Buscar")
		self.CuadroBuscar.bind("<KeyRelease>",self.BuscarDatos)
		self.CuadroBuscar.bind("<FocusIn>", self.GrisBuscar)
		self.CuadroBuscar.bind("<FocusOut>", self.GrisBuscar)
		self.CuadroBuscar.place(x=20,y=6,height=25)

		Button(BloqueC3,text='Modificar',bd=0,bg='#5c8cc5',fg='white',width=15,command=self.CargarDatos).place(x=460,y=6,height=25)
		Button(BloqueC3,text='Eliminar',bd=0,bg='#5c8cc5',fg='white',width=15,command=self.EliminarDatos).place(x=581,y=6,height=25)		

		self.SubPestana=ttk.Notebook(self.BloqueC2)
		self.SubPestana.place(x=0,y=20,width=730,height=330)

		self.SubPes1=ttk.Frame(self.SubPestana)
		self.SubPestana.add(self.SubPes1,text="Apoderado")

		self.SubPes2=ttk.Frame(self.SubPestana)
		self.SubPestana.add(self.SubPes2,text="Estudiantes")

		self.SubPes3=ttk.Frame(self.SubPestana)
		self.SubPestana.add(self.SubPes3,text="Padre")

		self.SubPes4=ttk.Frame(self.SubPestana)
		self.SubPestana.add(self.SubPes4,text="Madre")

		self.SubPesIG1=ttk.Frame(self.SubPestana)
		self.SubPestana.add(self.SubPesIG1,text="Ingreso A")

		self.SubPesIG2=ttk.Frame(self.SubPestana)
		self.SubPestana.add(self.SubPesIG2,text="Egreso A")

		self.SubPesIG3=ttk.Frame(self.SubPestana)
		self.SubPestana.add(self.SubPesIG3,text="Ingresos KW")

		self.SubPesIG4=ttk.Frame(self.SubPestana)
		self.SubPestana.add(self.SubPesIG4,text="Egresos KW ")
		
		self.SubPestana.bind("<<NotebookTabChanged>>",self.Desseleccionar)

		self.PesApoderado=Button(self.BloqueC2,text='Apoderado',bg='#5c8cc5',fg='white',activebackground='#5c8cc5',bd=0,relief='sunken',activeforeground='white')
		self.PesApoderado.place(x=0,y=0,width=89)
		self.PesEstudiante=Button(self.BloqueC2,text='Estudiantes',bg='#f1f6fc',activebackground='#5c8cc5',fg=self.StyleBgColor,bd=0,relief='sunken',activeforeground='white')
		self.PesEstudiante.place(x=89,y=0,width=89)
		self.PesPadre=Button(self.BloqueC2,text='Padre',bg='#f1f6fc',activebackground='#5c8cc5',fg=self.StyleBgColor,bd=0,relief='sunken',activeforeground='white')
		self.PesPadre.place(x=178,y=0,width=89)
		self.PesMadre=Button(self.BloqueC2,text='Madre',bg='#f1f6fc',activebackground='#5c8cc5',fg=self.StyleBgColor,bd=0,relief='sunken',activeforeground='white')
		self.PesMadre.place(x=267,y=0,width=89)
		self.PesIA=Button(self.BloqueC2,text='I AMAPAFA',bg='#f1f6fc',activebackground='#5c8cc5',fg=self.StyleBgColor,bd=0,relief='sunken',activeforeground='white')
		self.PesIA.place(x=356,y=0,width=89)
		self.PesEA=Button(self.BloqueC2,text='E AMAPAFA',bg='#f1f6fc',activebackground='#5c8cc5',fg=self.StyleBgColor,bd=0,relief='sunken',activeforeground='white')
		self.PesEA.place(x=445,y=0,width=89)
		self.PesIK=Button(self.BloqueC2,text='I K.Warma',bg='#f1f6fc',activebackground='#5c8cc5',fg=self.StyleBgColor,bd=0,relief='sunken',activeforeground='white')
		self.PesIK.place(x=534,y=0,width=89)
		self.PesEK=Button(self.BloqueC2,text='E K.Warma',bg='#f1f6fc',activebackground='#5c8cc5',fg=self.StyleBgColor,bd=0,relief='sunken',activeforeground='white')
		self.PesEK.place(x=623,y=0,width=89)

		self.PesApoderado.bind('<Enter>',lambda event: self.PesApoderado.config(bg='#5c8cc5',fg='white'))
		self.PesApoderado.bind('<Button-1>',self.SelecPesApoderado)
		self.PesEstudiante.bind('<Enter>',lambda event: self.PesEstudiante.config(bg='#5c8cc5',fg='white'))
		self.PesEstudiante.bind('<Leave>',lambda event: self.PesEstudiante.config(bg='#f1f6fc',fg=self.StyleBgColor))
		self.PesEstudiante.bind('<Button-1>',self.SelecPesEstudiante)
		self.PesPadre.bind('<Enter>',lambda event: self.PesPadre.config(bg='#5c8cc5',fg='white'))
		self.PesPadre.bind('<Leave>',lambda event: self.PesPadre.config(bg='#f1f6fc',fg=self.StyleBgColor))
		self.PesPadre.bind('<Button-1>',self.SelecPesPadre)
		self.PesMadre.bind('<Enter>',lambda event: self.PesMadre.config(bg='#5c8cc5',fg='white'))
		self.PesMadre.bind('<Leave>',lambda event: self.PesMadre.config(bg='#f1f6fc',fg=self.StyleBgColor))
		self.PesMadre.bind('<Button-1>',self.SelecPesMadre)
		self.PesIA.bind('<Enter>',lambda event: self.PesIA.config(bg='#5c8cc5',fg='white'))
		self.PesIA.bind('<Leave>',lambda event: self.PesIA.config(bg='#f1f6fc',fg=self.StyleBgColor))
		self.PesIA.bind('<Button-1>',self.SelecPesIA)
		self.PesEA.bind('<Enter>',lambda event: self.PesEA.config(bg='#5c8cc5',fg='white'))
		self.PesEA.bind('<Leave>',lambda event: self.PesEA.config(bg='#f1f6fc',fg=self.StyleBgColor))
		self.PesEA.bind('<Button-1>',self.SelecPesEA)
		self.PesIK.bind('<Enter>',lambda event: self.PesIK.config(bg='#5c8cc5',fg='white'))
		self.PesIK.bind('<Leave>',lambda event: self.PesIK.config(bg='#f1f6fc',fg=self.StyleBgColor))
		self.PesIK.bind('<Button-1>',self.SelecPesIK)
		self.PesEK.bind('<Enter>',lambda event: self.PesEK.config(bg='#5c8cc5',fg='white'))
		self.PesEK.bind('<Leave>',lambda event: self.PesEK.config(bg='#f1f6fc',fg=self.StyleBgColor))
		self.PesEK.bind('<Button-1>',self.SelecPesEK)

		#------------------------Tabla-del-Apoderado-------------------------#
		self.TablaApoderado =ttk.Treeview(self.SubPes1,height=13,columns=("#1","#2","#3","#4","#5","#6","#7"))
		self.TablaApoderado.place(x=0,y=0,width=692)
		self.TablaApoderado.heading("#0", text="N")
		self.TablaApoderado.column("#0",width=0,stretch=0)
		self.TablaApoderado.heading("#1", text="N°") 
		self.TablaApoderado.column("#1",width=50,stretch=0,anchor=N)
		self.TablaApoderado.heading("#2", text="Apellidos y Nombres")
		self.TablaApoderado.column("#2",width=300,stretch=0)
		self.TablaApoderado.heading("#3", text="DNI") 
		self.TablaApoderado.column("#3",width=100,stretch=0)
		self.TablaApoderado.heading("#4", text="Dirección") 
		self.TablaApoderado.column("#4",width=200,stretch=0)
		self.TablaApoderado.heading("#5", text="Cuota") 
		self.TablaApoderado.column("#5",width=80,stretch=0)
		self.TablaApoderado.heading("#6", text="Multa") 
		self.TablaApoderado.column("#6",width=80,stretch=0)
		self.TablaApoderado.heading("#7", text="N° Estudiantes") 
		self.TablaApoderado.column("#7",width=80,stretch=0)
		ScrollVertical=ttk.Scrollbar(self.SubPes1,command=self.TablaApoderado.yview,orient=VERTICAL)
		ScrollHorizontal=ttk.Scrollbar(self.SubPes1,command=self.TablaApoderado.xview,orient=HORIZONTAL)
		self.TablaApoderado.configure(yscrollcommand=ScrollVertical.set)
		self.TablaApoderado.configure(xscrollcommand=ScrollHorizontal.set)
		ScrollVertical.place(x=692,y=0,height=288)
		ScrollHorizontal.place(x=0,y=287,width=693)

		#--------------------------------Tabla del Estudiante---------------------------------------------------------#

		self.TablaEstudiante=ttk.Treeview(self.SubPes2,height=13,columns=("#1","#2","#3","#4","#5",'#6'))
		self.TablaEstudiante.place(x=0,y=0,width=692)
		self.TablaEstudiante.heading("#0", text="N")
		self.TablaEstudiante.column("#0",minwidth=0,width=0,stretch=NO)
		self.TablaEstudiante.heading("#1", text="N°")
		self.TablaEstudiante.column("#1",width=50,stretch=NO,anchor=N)
		self.TablaEstudiante.heading("#2", text="Apellidos y Nombres")
		self.TablaEstudiante.column("#2",width=352,stretch=NO)
		self.TablaEstudiante.heading("#3", text="DNI")   
		self.TablaEstudiante.column("#3",width=130,stretch=NO) 
		self.TablaEstudiante.heading("#4", text="Grado")
		self.TablaEstudiante.column("#4",width=100,stretch=NO)
		self.TablaEstudiante.heading("#5", text="Sección")
		self.TablaEstudiante.column("#5",width=100,stretch=NO)
		self.TablaEstudiante.heading("#6", text="Cuota") 
		self.TablaEstudiante.column("#6",width=140,stretch=NO)
		ScrollVertical=ttk.Scrollbar(self.SubPes2,orient="vertical",command=self.TablaEstudiante.yview)
		ScrollVertical.place(x=692,y=0,height=288)
		self.TablaEstudiante.configure(yscrollcommand=ScrollVertical.set)
		ScrollHorizontal=ttk.Scrollbar(self.SubPes2,command=self.TablaEstudiante.xview,orient=HORIZONTAL)
		ScrollHorizontal.place(x=0,y=287,width=693)
		self.TablaEstudiante.configure(xscrollcommand=ScrollHorizontal.set)

		self.TablaPadre =ttk.Treeview(self.SubPes3,height=13,columns=("#1","#2","#3","#4"))
		self.TablaPadre.place(x=0,y=0,width=692)
		self.TablaPadre.heading("#0", text="N")
		self.TablaPadre.column("#0",width=0,stretch=NO)
		self.TablaPadre.heading("#1", text="N°")
		self.TablaPadre.column("#1",width=50,stretch=NO,anchor=N)
		self.TablaPadre.heading("#2", text="Apellidos y Nombres")
		self.TablaPadre.column("#2",width=550,stretch=NO) 
		self.TablaPadre.heading("#3", text="DNI") 
		self.TablaPadre.column("#3",width=100,stretch=NO)
		self.TablaPadre.heading("#4", text="Dirección") 
		self.TablaPadre.column("#4",minwidth=0,width=172,stretch=NO)
		ScrollVertical=ttk.Scrollbar(self.SubPes3,orient="vertical",command=self.TablaPadre.yview)
		ScrollVertical.place(x=692,y=0,height=288)
		self.TablaPadre.configure(yscrollcommand=ScrollVertical.set)
		ScrollHorizontal=ttk.Scrollbar(self.SubPes3,command=self.TablaPadre.xview,orient=HORIZONTAL)
		ScrollHorizontal.place(x=0,y=287,width=693)
		self.TablaPadre.configure(xscrollcommand=ScrollHorizontal.set)

		#--------------------- ---Tabla-de-la-Madre-------------------------#
		self.TablaMadre =ttk.Treeview(self.SubPes4,height=13,columns=("#1","#2","#3","#4"))
		self.TablaMadre.place(x=0,y=0,width=692)
		self.TablaMadre.heading("#0", text="N")
		self.TablaMadre.column("#0",width=0,stretch=NO)
		self.TablaMadre.heading("#1", text="N°")
		self.TablaMadre.column("#1",width=50,stretch=NO,anchor=N)
		self.TablaMadre.heading("#2", text="Apellidos y Nombres")
		self.TablaMadre.column("#2",width=550,stretch=NO)
		self.TablaMadre.heading("#3", text="DNI") 
		self.TablaMadre.column("#3",width=100,stretch=NO)
		self.TablaMadre.heading("#4", text="Dirección") 
		self.TablaMadre.column("#4",width=172,stretch=NO)
		ScrollVertical=ttk.Scrollbar(self.SubPes4,orient="vertical",command=self.TablaMadre.yview)
		ScrollVertical.place(x=692,y=0,height=288)
		self.TablaMadre.configure(yscrollcommand=ScrollVertical.set)
		ScrollHorizontal=ttk.Scrollbar(self.SubPes4,command=self.TablaMadre.xview,orient=HORIZONTAL)
		ScrollHorizontal.place(x=0,y=287,width=693)
		self.TablaMadre.configure(xscrollcommand=ScrollHorizontal.set)

		self.TablaIA=ttk.Treeview(self.SubPesIG1,height=13,columns=("#1","#2","#3","#4",'#5'))
		self.TablaIA.place(x=0,y=0,width=692)
		self.TablaIA.heading("#0", text="N")
		self.TablaIA.column("#0",width=0,stretch=NO)
		self.TablaIA.heading("#1", text="N°")
		self.TablaIA.column("#1",width=50,stretch=NO,anchor=N)
		self.TablaIA.heading("#2", text="Descripción")
		self.TablaIA.column("#2",width=572,stretch=NO)
		self.TablaIA.heading("#3", text="N° Asociados")   
		self.TablaIA.column("#3",width=50,stretch=NO) 
		self.TablaIA.heading("#4", text="Monto/Unidad")   
		self.TablaIA.column("#4",width=100,stretch=NO)
		self.TablaIA.heading("#5", text="Monto Total")   
		self.TablaIA.column("#5",width=100,stretch=NO)
		ScrollVertical=ttk.Scrollbar(self.SubPesIG1,orient="vertical",command=self.TablaIA.yview)
		ScrollVertical.place(x=692,y=0,height=288)
		self.TablaIA.configure(yscrollcommand=ScrollVertical.set)
		ScrollHorizontal=ttk.Scrollbar(self.SubPesIG1,command=self.TablaIA.xview,orient=HORIZONTAL)
		ScrollHorizontal.place(x=0,y=287,width=693)
		self.TablaIA.configure(xscrollcommand=ScrollHorizontal.set)

		Label(self.SubPesIG1,text='Ingreso Total:  S/').place(x=680,y=320)
		self.LabelIA=Label(self.SubPesIG1)
		self.LabelIA.place(x=785,y=320)

		self.TablaEA =ttk.Treeview(self.SubPesIG2,height=13,columns=("#1","#2","#3","#4","#5",'#6'))
		self.TablaEA.place(x=0,y=0,width=692)
		self.TablaEA.heading("#0", text="N")
		self.TablaEA.column("#0",width=0,stretch=NO)
		self.TablaEA.heading("#1", text="N°")
		self.TablaEA.column("#1",width=50,stretch=NO,anchor=N)
		self.TablaEA.heading("#2", text="Fecha")
		self.TablaEA.column("#2",width=100,stretch=NO)
		self.TablaEA.heading("#3", text="Comprobante de Pago")   
		self.TablaEA.column("#3",width=200,stretch=NO) 
		self.TablaEA.heading("#4", text="N° de CP")   
		self.TablaEA.column("#4",width=100,stretch=NO)
		self.TablaEA.heading("#5", text="Descripción") 
		self.TablaEA.column("#5",width=342,stretch=NO)
		self.TablaEA.heading("#6", text="Monto") 
		self.TablaEA.column("#6",width=80,stretch=NO)
		ScrollVertical=ttk.Scrollbar(self.SubPesIG2,orient="vertical",command=self.TablaEA.yview)
		ScrollVertical.place(x=692,y=0,height=288)
		self.TablaEA.configure(yscrollcommand=ScrollVertical.set)
		ScrollHorizontal=ttk.Scrollbar(self.SubPesIG2,command=self.TablaEA.xview,orient=HORIZONTAL)
		ScrollHorizontal.place(x=0,y=287,width=693)
		self.TablaEA.configure(xscrollcommand=ScrollHorizontal.set)

		Label(self.SubPesIG2,text='Egreso Total:  S/').place(x=680,y=320)
		self.LabelEA=Label(self.SubPesIG2)
		self.LabelEA.place(x=785,y=320)

		self.TablaIK=ttk.Treeview(self.SubPesIG3,height=13,columns=("#1","#2","#3",'#4'))
		self.TablaIK.place(x=0,y=0,width=692)
		self.TablaIK.heading("#0", text="N")
		self.TablaIK.column("#0",width=0,stretch=NO)
		self.TablaIK.heading("#1", text="N°")
		self.TablaIK.column("#1",width=50,stretch=NO,anchor=N)
		self.TablaIK.heading("#2", text="Descripción")
		self.TablaIK.column("#2",width=672,stretch=NO)
		self.TablaIK.heading("#3", text="N° Estudiantes")
		self.TablaIK.column("#3",width=50,stretch=NO)
		self.TablaIK.heading("#4", text="Monto Total")
		self.TablaIK.column("#4",width=100,stretch=NO)
		ScrollVertical=ttk.Scrollbar(self.SubPesIG3,orient="vertical",command=self.TablaIK.yview)
		ScrollVertical.place(x=692,y=0,height=288)
		self.TablaIK.configure(yscrollcommand=ScrollVertical.set)
		ScrollHorizontal=ttk.Scrollbar(self.SubPesIG3,command=self.TablaIK.xview,orient=HORIZONTAL)
		ScrollHorizontal.place(x=0,y=287,width=693)
		self.TablaIK.configure(xscrollcommand=ScrollHorizontal.set)

		Label(self.SubPesIG3,text='Ingreso Total:  S/').place(x=680,y=320)
		self.LabelIK=Label(self.SubPesIG3)
		self.LabelIK.place(x=785,y=320)

		self.TablaEK=ttk.Treeview(self.SubPesIG4,height=13,columns=("#1","#2","#3",'#4','#5','#6'))
		self.TablaEK.place(x=0,y=0,width=692)
		self.TablaEK.heading("#0", text="N")
		self.TablaEK.column("#0",width=0,stretch=NO)
		self.TablaEK.heading("#1", text="N°")
		self.TablaEK.column("#1",width=50,stretch=NO,anchor=N)
		self.TablaEK.heading("#2", text="Fecha")
		self.TablaEK.column("#2",width=100,stretch=NO)
		self.TablaEK.heading("#3", text="Comprobante de Pago")  
		self.TablaEK.column("#3",width=200,stretch=NO)
		self.TablaEK.heading("#4", text="N° de CP")
		self.TablaEK.column("#4",width=100,stretch=NO)
		self.TablaEK.heading("#5", text="Descripción")
		self.TablaEK.column("#5",width=342,stretch=NO)
		self.TablaEK.heading("#6", text="Monto")
		self.TablaEK.column("#6",width=80,stretch=NO)
		ScrollVertical=ttk.Scrollbar(self.SubPesIG4,orient="vertical",command=self.TablaEK.yview)
		ScrollVertical.place(x=692,y=0,height=288)
		self.TablaEK.configure(yscrollcommand=ScrollVertical.set)
		ScrollHorizontal=ttk.Scrollbar(self.SubPesIG4,command=self.TablaEK.xview,orient=HORIZONTAL)
		ScrollHorizontal.place(x=0,y=287,width=693)
		self.TablaEK.configure(xscrollcommand=ScrollHorizontal.set)

		Label(self.SubPesIG4,text='Egreso Total:  S/').place(x=680,y=320)
		self.LabelEK=Label(self.SubPesIG4,text='24.00')
		self.LabelEK.place(x=785,y=320)
		
		self.ConsultarNM()
		self.ConsultarNA(),
		self.InsertarIG()
		#------------------------Color-de-filas-de-tablas-------------------------------#
		self.TablaIA.tag_configure("LineaBlanca",foreground='black')
		self.TablaIA.tag_configure("LineaColor",background='#f1f6fc',foreground='black')
		self.TablaEA.tag_configure("LineaBlanca",foreground='black')
		self.TablaEA.tag_configure("LineaColor",background='#f1f6fc',foreground='black')
		self.TablaIK.tag_configure("LineaBlanca",foreground='black')
		self.TablaIK.tag_configure("LineaColor",background='#f1f6fc',foreground='black')
		self.TablaEK.tag_configure("LineaBlanca",foreground='black')
		self.TablaEK.tag_configure("LineaColor",background='#f1f6fc',foreground='black')

		#----------------Eventos-en-las-tablas---------------------------------------------------#
		self.TablaIA.bind('<Button-1>', self.Click)
		self.TablaEA.bind('<Button-1>', self.Click)
		self.TablaIK.bind('<Button-1>', self.Click)
		self.TablaEK.bind('<Button-1>', self.Click)
		
		#------------------------Color-de-filas-de-tablas-------------------------------#
		self.TablaPadre.tag_configure("LineaBlanca",background='white')
		self.TablaPadre.tag_configure("LineaColor",background='#e4ecf8')
		self.TablaMadre.tag_configure("LineaBlanca",background='white')
		self.TablaMadre.tag_configure("LineaColor",background='#e4ecf8')
		self.TablaApoderado.tag_configure("LineaBlanca",background='white')
		self.TablaApoderado.tag_configure("LineaColor",background='#e4ecf8')
		self.TablaEstudiante.tag_configure("LineaBlanca",background='white')
		self.TablaEstudiante.tag_configure("LineaColor",background='#e4ecf8')

		#----------------Eventos-en-las-tablas---------------------------------------------------#
		self.ValorOrdenar.set(1)
		self.CambiarOrden()
		self.InsertarTabla()
		self.TablaApoderado.bind('<Button-1>', self.Click)
		self.TablaPadre.bind('<Button-1>', self.Click)
		self.TablaMadre.bind('<Button-1>', self.Click)
		self.TablaEstudiante.bind('<Button-1>', self.Click)
		self.TablaApoderado.bind('<Button-3>', self.Popup)
		self.TablaPadre.bind('<Button-3>', self.Popup)
		self.TablaMadre.bind('<Button-3>', self.Popup)
		self.TablaEstudiante.bind('<Button-3>', self.Popup)

		#↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑#
		#------------------------------------------------------------------------------------#

		#------------------Construccion-y-Diseño-de-la-Pestaña-RegistrosIngresos----------------#
		#↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓#

		self.BloqueD1=Frame(self.Pes4,height="370",width="800",bg='#f1f6fc')
		self.BloqueD1.place(x=0,y=50)

		BloqueD3=Frame(self.Pes4,height='37',width='800',bg='#d4dce3')
		BloqueD3.place(x=0,y=387)

		self.BotonCancelIG=Button(BloqueD3,text='Cancelar',width=15,bd=0,bg='#5c8cc5',fg='white',command=self.CancelarIG)
		self.BotonCancelIG.place(x=460,y=6,height=25)
		self.BotonRegIG=Button(BloqueD3,text='Registrar',width=15,bd=0,bg='#5c8cc5',fg='white',command=self.RegistrarIG)
		self.BotonRegIG.place(x=580,y=6,height=25)
		self.BotonModIG=Button(BloqueD3,text='Modificar',width=15,bd=0,bg='#5c8cc5',fg='white',command=self.ModificarIG)
		#self.BotonModIG.place(x=500,y=5)
		self.BotonCancelIG.config(state='disabled')
		#self.BotonModIG.config(state=DISABLED)
		self.ArregloMeses=['Mes','Ene','Feb','Mar','Abr','May','Jun','Jul','Ago','Sep','Oct','Nov','Dic']
		ArregloDias=['Dia']
		for i in range(1,32):
			ArregloDias.append(i)
		ArregloYears=['Año']
		for i in range(2019,2031):
			ArregloYears.append(i)

		ImagenCalendario=Image.open('img/ImageCalendar.png')
		ImagenCalendario = ImagenCalendario.resize((22, 22), Image.ANTIALIAS)
		ImagenCalendario = ImageTk.PhotoImage(ImagenCalendario)

		Label(self.BloqueD1,text='Ver reporte economico  -  De',bg='#f1f6fc').place(x=25,y=25)
		Label(self.BloqueD1,text='A',bg='#f1f6fc').place(x=375,y=25)
		ttk.Combobox(self.BloqueD1,values=ArregloDias,width=4,state='readonly',textvariable=self.DiaIni).place(x=190,y=25)
		ttk.Combobox(self.BloqueD1,values=self.ArregloMeses,width=4,state='readonly',textvariable=self.MesIni).place(x=238,y=25)
		ttk.Combobox(self.BloqueD1,values=ArregloYears,width=4,state='readonly',textvariable=self.AgeIni).place(x=286,y=25)

		Boton1=Button(self.BloqueD1,bd=0,image=ImagenCalendario,cursor="hand2",command=self.CalendInicio)
		Boton1.place(x=335,y=23)
		Boton1.image=ImagenCalendario
		ttk.Combobox(self.BloqueD1,values=ArregloDias,width=4,state='readonly',textvariable=self.DiaFin).place(x=405,y=25)
		ttk.Combobox(self.BloqueD1,values=self.ArregloMeses,width=4,state='readonly',textvariable=self.MesFin).place(x=453,y=25)
		ttk.Combobox(self.BloqueD1,values=ArregloYears,width=4,state='readonly',textvariable=self.AgeFin).place(x=501,y=25)
		Boton2=Button(self.BloqueD1,bd=0,image=ImagenCalendario,cursor="hand2",command=self.CalendFinal)
		Boton2.place(x=550,y=23)
		Boton2.image=ImagenCalendario

		self.DiaIni.set('Dia')
		self.MesIni.set('Mes')
		self.AgeIni.set('Año')
		self.DiaFin.set('Dia')
		self.MesFin.set('Mes')
		self.AgeFin.set('Año')
		Button(self.BloqueD1,text='  Generar  ',bd=0,bg='#5c8cc5',fg='white').place(x=622,y=23,height=24)

		self.TablaGenerar=ttk.Treeview(self.BloqueD1,height=3,columns=("#1","#2","#3"))
		self.TablaGenerar.place(x=25,y=55)
		self.TablaGenerar.heading("#0", text="N°")
		self.TablaGenerar.column("#0",width=50,stretch=NO)
		self.TablaGenerar.heading("#1", text="Opción")
		self.TablaGenerar.column("#1",width=270,stretch=NO)
		self.TablaGenerar.heading("#2", text="Monto") 
		self.TablaGenerar.column("#2",width=100,stretch=NO)
		self.TablaGenerar.heading("#3", text="Fecha") 
		self.TablaGenerar.column("#3",width=220,stretch=NO)
		ScrollVertical=ttk.Scrollbar(self.BloqueD1,orient="vertical",command=self.TablaGenerar.yview)
		ScrollVertical.place(x=665,y=55,height=87)
		self.TablaGenerar.configure(yscrollcommand=ScrollVertical.set)
		self.TablaGenerar.bind('<Button-1>', self.Click)

		self.TablaGenerar.tag_configure("LineaBlanca",background='white')
		self.TablaGenerar.tag_configure("LineaColor",background='#e4ecf8')

		Label(self.BloqueD1,text='Registrar:',bg='#f1f6fc').place(x=25,y=160)
		Datos=['Ingreso AMAPAFA','Egreso AMAPAFA','Ingreso Kaly Warma','Egreso Kaly Warma']
		self.ComboIG=ttk.Combobox(self.BloqueD1,width=45,state='readonly',values=Datos,textvariable=self.IngresoGasto)
		self.ComboIG.place(x=100,y=160)
		self.ComboIG.bind("<<ComboboxSelected>>", self.SelecIngreso)
		self.IngresoGasto.set('Seleccione una opción')

		Label(self.BloqueD1,text='Fecha:',bg='#f1f6fc').place(x=425,y=160)
		ttk.Combobox(self.BloqueD1,values=ArregloDias,width=4,state='readonly',textvariable=self.Dia).place(x=474,y=160)
		ttk.Combobox(self.BloqueD1,values=self.ArregloMeses,width=4,state='readonly',textvariable=self.Mes).place(x=522,y=160)
		ttk.Combobox(self.BloqueD1,values=ArregloYears,width=4,state='readonly',textvariable=self.Age).place(x=570,y=160)
		self.Suma=0
		self.FrameCal=Frame(self.WindowMain,bd=4,bg='#5c8cc5')
		Boton3=Button(self.BloqueD1,bd=0,image=ImagenCalendario,cursor="hand2",command=self.Calendario)
		Boton3.place(x=618,y=158)
		Boton3.image=ImagenCalendario

		self.Dia.set('Dia')
		self.Mes.set('Mes')
		self.Age.set('Año')

		Label(self.BloqueD1,text='Descripción:',bg='#f1f6fc').place(x=25,y=230)
		ttk.Entry(self.BloqueD1,textvariable=self.NombreIG).place(x=100,y=230,width=544)	

		Label(self.BloqueD1,text='Comprobante de pago:',bg='#f1f6fc').place(x=25,y=195)
		self.Comprobante=ttk.Entry(self.BloqueD1,width=30)
		self.Comprobante.place(x=160,y=195)
		
		Label(self.BloqueD1,text='N° de CP:',bg='#f1f6fc').place(x=365,y=195)
		self.NCP=ttk.Entry(self.BloqueD1,width=10,justify='right')
		self.NCP.place(x=425,y=195)

		Label(self.BloqueD1,text='Monto:  S/',bg='#f1f6fc').place(x=510,y=195)
		ttk.Entry(self.BloqueD1,justify='right',width=10,textvariable=self.MontoIG).place(x=575,y=195)
		self.MontoIG.set('0')

		Label(self.BloqueD1,text='Justificación:',bg='#f1f6fc').place(x=25,y=265)
		self.TextoComentario=Text(self.BloqueD1,height=3,bd=2,relief=GROOVE,bg='white',fg='black')
		self.TextoComentario.place(x=100,y=265,width=546)

		ScrollVertical=ttk.Scrollbar(self.BloqueD1,orient="vertical",command=self.TextoComentario.yview)
		ScrollVertical.place(x=645,y=265,height=53)
		self.TextoComentario.configure(yscrollcommand=ScrollVertical.set)

		#↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑#
		#------------------------------------------------------------------------------------#

		#------------------Construccion-y-Diseño-de-la-Pestaña-Generar-Reporte---------------#
		#↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓#

		BloqueE1=Frame(self.Pes5,bg='#f1f6fc')
		BloqueE1.place(x=0,y=61,width=711,height=363)

		FrameDatos=Frame(BloqueE1,bg='#f1f6fc')
		FrameDatos.place(x=25,y=20)

		Label(BloqueE1,text='Saldo AMAPAFA: ')
		self.SaldoA=Label(BloqueE1)
		Label(BloqueE1,text='Saldo Kaly Warma: ')
		self.SaldoK=Label(BloqueE1)

		#Label(Frame1,text="Optimal Data",bg=self.StyleBgColor,fg="white",font=("Arial Rounded MT Bold",10)).place(x=25,y=10)
		
		Label(FrameDatos,text='Datos de:',bg='#f1f6fc').grid(row=1,column=1,sticky='w',pady=5)
		self.ComboDatosExp=ttk.Combobox(FrameDatos,width=17,state='readonly')
		self.ComboDatosExp.grid(row=1,column=2)
		self.ComboDatosExp['values']=['Apoderado','Padre','Madre','Estudiante','Ingreso AMAPAFA','Ingreso Kaly Warma','Egreso AMAPAFA','Egreso Kaly Warma']
		self.ComboDatosExp.current(0)

		Label(FrameDatos,text='Ordenar por:',bg='#f1f6fc').grid(row=2,column=1,sticky='w',pady=5)
		self.ComboOrdenExp=ttk.Combobox(FrameDatos,width=17,state='readonly')
		self.ComboOrdenExp.grid(row=2,column=2)
		self.ComboOrdenExp['values']=['Orden alfabetico','Orden de matricula','Grado y Sección','Aleatorio']
		self.ComboOrdenExp.current(0)
		self.ComboOrdenExp.bind("<<ComboboxSelected>>", self.RedimensionarVE)

		Label(FrameDatos,text='Formato:',bg='#f1f6fc').grid(row=5,column=1,sticky='w',pady=5)
		ComboDatos=ttk.Combobox(FrameDatos,width=17,state='readonly')
		ComboDatos.grid(row=5,column=2,sticky='w')
		ComboDatos['values']=['PDF','xlsx - Excel']
		ComboDatos.current(0)

		Label(FrameDatos,text='Grado:',bg='#f1f6fc').grid(row=3,column=1,sticky='w',pady=5)
		self.ComboGradoExp=ttk.Combobox(FrameDatos,width=17,state='readonly',justify="right")
		self.ComboGradoExp.grid(row=3,column=2,sticky='w')
		self.ComboGradoExp['values']=['1','2','3','4','5','6']
		self.ComboGradoExp.current(0)

		Label(FrameDatos,text='Sección:',bg='#f1f6fc').grid(row=4,column=1,sticky='w',pady=5)
		self.ComboSeccionExp=ttk.Combobox(FrameDatos,width=17,state='readonly',justify="right")
		self.ComboSeccionExp.grid(row=4,column=2,sticky='w')
		self.ComboSeccionExp['values']=['A','B','C']
		self.ComboSeccionExp.current(0)

		Label(FrameDatos,text='       ',bg='#f1f6fc').grid(row=1,column=3)
		Label(FrameDatos,text='Nombres',bg='#f1f6fc').grid(row=1,column=5,sticky='w',pady=5)
		Label(FrameDatos,text='DNI',bg='#f1f6fc').grid(row=2,column=5,sticky='w',pady=5)
		Label(FrameDatos,text='Dirección',bg='#f1f6fc').grid(row=3,column=5,sticky='w',pady=5)
		Label(FrameDatos,text='Multa',bg='#f1f6fc').grid(row=4,column=5,sticky='w',pady=5)
		Label(FrameDatos,text='N° de Estudiantes',bg='#f1f6fc').grid(row=5,column=5,sticky='w',pady=5)
		ttk.Checkbutton(FrameDatos,variable=self.CEDNom).grid(row=1,column=4,sticky='w')
		ttk.Checkbutton(FrameDatos,variable=self.CEDDNI).grid(row=2,column=4,sticky='w')
		ttk.Checkbutton(FrameDatos,variable=self.CEDDirec).grid(row=3,column=4,sticky='w')
		ttk.Checkbutton(FrameDatos,variable=self.CEDMulta).grid(row=4,column=4,sticky='w')
		ttk.Checkbutton(FrameDatos,variable=self.CEDNAlum).grid(row=5,column=4,sticky='w')

		self.CEDNom.set(1)
		self.ComboGradoExp.config(state='disabled')
		self.ComboSeccionExp.config(state='disabled')
		Button(FrameDatos,text='Exportar',bd=0,fg='white',bg=self.StyleBgColor,command=self.ExportarDatos).grid(row=6,column=2)
		Button(FrameDatos,text='Imprimir',bd=0,fg='white',bg=self.StyleBgColor,command=lambda: print('ga')).grid(row=6,column=5)

 		#-------------------------Acabado-de-la-Interfaz-Grafica---------------------------------#
		

		self.IngresoTotal()

		if Value==1:
			self.SubPestanaIG.tab(2 ,state=DISABLED)
			self.SubPestanaIG.tab(3 ,state=DISABLED)
			self.SubPestana.tab(1,state=DISABLED)
			self.SelecIG['menu'].entryconfigure(3, state = "disabled")
			self.SelecIG['menu'].entryconfigure(4, state = "disabled")

		if Value==2:
			self.SubPestana.tab(2, state=DISABLED)
			self.SubPestana.tab(3, state=DISABLED)
			self.SubPestanaIG.tab(0 ,state=DISABLED)
			self.SubPestanaIG.tab(1 ,state=DISABLED)
			self.BotMod.config(state=DISABLED)
			self.SelecIG['menu'].entryconfigure(1, state = "disabled")
			self.SelecIG['menu'].entryconfigure(2, state = "disabled")

		cont=1
		for row in range(1,50):		           
 			if cont % 2 != 0:
 				self.TablaApoderado.insert("",index="end",text='a',values=(cont,'Freddy Limachi Ortega', 'row[2]', 'row[3]','row[4]', 'row[5]', 'row[6]'), tags=('LineaBlanca',))
 			elif cont % 2 == 0:
 				self.TablaApoderado.insert("",index="end",text='a',values=(cont,'Quispe Mamani Sebastian de Unde', 'row[2]', 'row[3]','row[4]', 'row[5]', 'row[6]'), tags=('LineaColor',))
 			cont=cont+1

		cont=1
		for row in range(1,10):		           
 			if cont % 2 != 0:
 				self.TablaGenerar.insert("",index="end",text=str(cont),values=('Ingreso Qali Warma', '25000.00', 'De    15 - 05 - 2019    a    15 - 06 - 2019'),tags=('LineaBlanca',))
 			elif cont % 2 == 0:
 				self.TablaGenerar.insert("",index="end",text=str(cont),values=('Saldo AMAPAFA', '12000.00', 'De    20 - 11 - 2019    a    20 - 11 - 2020'), tags=('LineaColor',))
 			cont=cont+1
		self.WindowMain.protocol("WM_DELETE_WINDOW", self.SalirAplicacion)

