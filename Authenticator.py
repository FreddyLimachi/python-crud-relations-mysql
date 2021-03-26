from tkinter import messagebox

class Authenticator():	

	def ValidarApoderado(self):
		return len(self.APA.get())!=0 and len(self.AMA.get())!=0 and len(self.NomA.get())!=0 and len(self.DNIA.get())!=0

	def ValidarDNIA(self):
		return len(self.DNIA.get())==8 and self.DNIA.get().isdigit()

	def ValidarDNIP(self):		
		return self.DNIP.get()=='' or (len(self.DNIP.get())==8 and self.DNIP.get().isdigit())
		
	def ValidarDNIM(self):
		return self.DNIM.get()=='' or (len(self.DNIM.get())==8 and self.DNIM.get().isdigit())

	def ValidarDNIRep(self):
		return self.Datos.ValidarDNI(self.DNIA.get(),self.Default)
		
	def ValidarNCaracteres(self):
		return len(self.APP.get())<=20 and len(self.AMP.get())<=20 and len(self.NomP.get())<=30 and len(self.APM.get())<=20 and len(self.AMM.get())<=20 and len(self.NomM.get())<=30 and len(self.APA.get())<=20 and len(self.AMA.get())<=20 and len(self.NomA.get())<=30 and len(self.DirecP.get())<=30 and len(self.DirecM.get())<=30 and len(self.DirecA.get())<=30

	def ValidarMulta(self):
		try:
			float(self.Multa.get())
			return True
		except:
			return messagebox.showwarning('Mensaje','Digite un entero o decimal en el cuadro "Multa", procure usar punto "."\ny en caso de no existir escriba el número "0"')
		
	def ValidarDigitos(self):
		Valor=self.Multa.get()
		Punto=0
		ParteDecimal=0
		ParteEntera=0
		for i in Valor:
			if i==".":
				Punto=1
			else:
				if Punto==0:
					ParteEntera=ParteEntera+1
				else:
					ParteDecimal=ParteDecimal+1
		if ParteEntera<=4 and ParteDecimal<=2:
			return True
		else:
			return False

	def ValE1(self):
		if len(self.APE1.get())==0 or len(self.AME1.get())==0 or len(self.NomE1.get())==0 or len(self.DNIE1.get())==0 or self.Grado1.get()=='○' or self.Seccion1.get()=='○':
			messagebox.showwarning('Mensaje','Complete los datos del primer estudiante')
		else:
			return True
	
	def ValE2(self):
		if len(self.APE2.get())==0 or len(self.AME2.get())==0 or len(self.NomE2.get())==0 or len(self.DNIE2.get())==0 or self.Grado2.get()=='○' or self.Seccion2.get()=='○':
			messagebox.showwarning('Mensaje','Complete los datos del segundo estudiante')
		else:
			return True
	
	def ValE3(self):
		if len(self.APE3.get())==0 or len(self.AME3.get())==0 or len(self.NomE3.get())==0 or len(self.DNIE3.get())==0 or self.Grado3.get()=='○' or self.Seccion3.get()=='○':
			messagebox.showwarning('Mensaje','Complete los datos del tercer estudiante')
		else:
			return True
	
	def ValE4(self):
		if len(self.APE4.get())==0 or len(self.AME4.get())==0 or len(self.NomE4.get())==0 or len(self.DNIE4.get())==0 or self.Grado4.get()=='○' or self.Seccion4.get()=='○':
			messagebox.showwarning('Mensaje','Complete los datos del cuarto estudiante')
		else:
			return True

	def ValE5(self):
		if len(self.APE5.get())==0 or len(self.AME5.get())==0 or len(self.NomE5.get())==0 or len(self.DNIE5.get())==0 or self.Grado5.get()=='○' or self.Seccion5.get()=='○':
			messagebox.showwarning('Mensaje','Complete los datos del quinto estudiante')
		else:
			return True

	def ValE6(self):
		if len(self.APE6.get())==0 or len(self.AME6.get())==0 or len(self.NomE6.get())==0 or len(self.DNIE6.get())==0 or self.Grado6.get()=='○' or self.Seccion6.get()=='○':
			messagebox.showwarning('Mensaje','Complete los datos del sexto estudiante')
		else:
			return True

	def ValEM(self):
		if len(self.APEM.get())==0 or len(self.AMEM.get())==0 or len(self.NomEM.get())==0 or len(self.DNIEM.get())==0 or self.GradoM.get()=='○' or self.SeccionM.get()=='○':
			messagebox.showwarning('Mensaje','Complete los datos')
		else:
			return True

	def ValDNIE1(self):
		if len(self.DNIE1.get())!=8 or self.DNIE1.get().isdigit()==False:
			messagebox.showwarning('Mensaje','DNI incorrecto en el primer estudiante')
		else:
			return True

	def ValDNIE2(self):
		if len(self.DNIE2.get())!=8 or self.DNIE2.get().isdigit()==False:
			messagebox.showwarning('Mensaje','DNI incorrecto en el segundo estudiante')
		else:
			return True

	def ValDNIE3(self):
		if len(self.DNIE3.get())!=8 or self.DNIE3.get().isdigit()==False:
			messagebox.showwarning('Mensaje','DNI incorrecto en el tercer estudiante')
		else:
			return True

	def ValDNIE4(self):
		if len(self.DNIE4.get())!=8 or self.DNIE4.get().isdigit()==False:
			messagebox.showwarning('Mensaje','DNI incorrecto en el cuarto estudiante')
		else:
			return True

	def ValDNIE5(self):
		if len(self.DNIE5.get())!=8 or self.DNIE5.get().isdigit()==False:
			messagebox.showwarning('Mensaje','DNI incorrecto en el quinto estudiante')
		else:
			return True

	def ValDNIE6(self):
		if len(self.DNIE6.get())!=8 or self.DNIE6.get().isdigit()==False:
			messagebox.showwarning('Mensaje','DNI incorrecto en el sexto estudiante')
		else:
			return True

	def ValidarCuotaE1(self):
		Punto=0
		ParteDecimal=0
		ParteEntera=0
		for i in self.TipoPago1.get():
			if i==".":
				Punto=1
			else:
				if Punto==0:
					ParteEntera=ParteEntera+1
				else:
					ParteDecimal=ParteDecimal+1
		if ParteEntera<=4 and ParteDecimal<=2 and ParteEntera.isdigit() and ParteDecimal.isdigit():
			return True

		elif self.TipoPago1.get()=='Exonerado':
			return True

	def ValidarDNIMore(self):
		return self.DNIMore.get().isdigit() and len(self.DNIMore.get())==8

	def ValidarPagoMore(self):
		try:
			float(self.PagoMore.get())
			return True
		except:
			return False

	def ValidarCaracterMore(self):
		return len(self.NomMore.get())<=50

	def ValDecimal(self,Valor,Texto):
		Punto=0
		ParteDecimal=0
		ParteEntera=0
		for i in Valor:
			if i==".":
				Punto+=1
			else:
				if Punto==0:
					ParteEntera=ParteEntera+1
				else:
					ParteDecimal=ParteDecimal+1

		if Punto>1 or Valor.replace('.','').isdigit()==False:
			if Texto=='E':
				messagebox.showwarning('Mensaje','Digitación incorrecta en pago')
			else:
				messagebox.showwarning('Mensaje','Escriba correctamente el monto')
		elif ParteEntera>4 or ParteDecimal>2:
			if Texto=='E':
				messagebox.showwarning('Mensaje','Los cuadros "pago" solo admiten 4 cifras en la parte entera y 2 en la parte decimal')
			else:
				messagebox.showwarning('Mensaje','El cuadro "monto" solo admite 4 cifras en la parte entera y 2 en la parte decimal')
		else:
			return True

	def ValidarEstudiante(self):
		if self.NEstudiantes.get()=='1 Estudiante a cargo':
			if self.ValE1()!=True:
				pass
			elif self.ValDNIE1()!=True:
				pass
			elif self.TipoPago1.get()!='Exonerado' and self.ValDecimal(self.TipoPago1.get(),'E')!=True:
				pass
			else:
				return True

		elif self.NEstudiantes.get()=='2 Estudiantes a cargo':
			if self.ValE1()!=True or self.ValE2()!=True:
				pass
			elif self.ValDNIE1()!=True or self.ValDNIE2()!=True:
				pass
			elif self.TipoPago1.get()!='Exonerado' and self.ValDecimal(self.TipoPago1.get(),'E')!=True:
				pass
			elif self.TipoPago2.get()!='Exonerado' and self.ValDecimal(self.TipoPago2.get(),'E')!=True:
				pass
			else:
				return True

		elif self.NEstudiantes.get()=='3 Estudiantes a cargo':
			if self.ValE1()!=True or self.ValE2()!=True or self.ValE3()!=True:
				pass
			elif self.ValDNIE1()!=True or self.ValDNIE2()!=True or self.ValDNIE3()!=True:
				pass
			elif self.TipoPago1.get()!='Exonerado' and self.ValDecimal(self.TipoPago1.get(),'E')!=True:
				pass
			elif self.TipoPago2.get()!='Exonerado' and self.ValDecimal(self.TipoPago2.get(),'E')!=True:
				pass
			elif self.TipoPago3.get()!='Exonerado' and self.ValDecimal(self.TipoPago3.get(),'E')!=True:
				pass
			else:
				return True

		elif self.NEstudiantes.get()=='4 Estudiantes a cargo':
			if self.ValE1()!=True or self.ValE2()!=True or self.ValE3()!=True or self.ValE4()!=True:
				pass
			elif self.ValDNIE1()!=True or self.ValDNIE2()!=True or self.ValDNIE3()!=True or self.ValDNIE4()!=True:
				pass
			elif self.TipoPago1.get()!='Exonerado' and self.ValDecimal(self.TipoPago1.get(),'E')!=True:
				pass
			elif self.TipoPago2.get()!='Exonerado' and self.ValDecimal(self.TipoPago2.get(),'E')!=True:
				pass
			elif self.TipoPago3.get()!='Exonerado' and self.ValDecimal(self.TipoPago3.get(),'E')!=True:
				pass
			elif self.TipoPago4.get()!='Exonerado' and self.ValDecimal(self.TipoPago4.get(),'E')!=True:
				pass
			else:
				return True

		elif self.NEstudiantes.get()=='5 Estudiantes a cargo':
			if self.ValE1()!=True or self.ValE2()!=True or self.ValE3()!=True or self.ValE4()!=True or self.ValE5()!=True:
				pass
			elif self.ValDNIE1()!=True or self.ValDNIE2()!=True or self.ValDNIE3()!=True or self.ValDNIE4()!=True or self.ValDNIE5()!=True:
				pass
			elif self.TipoPago1.get()!='Exonerado' and self.ValDecimal(self.TipoPago1.get(),'E')!=True: 
				pass
			elif self.TipoPago2.get()!='Exonerado' and self.ValDecimal(self.TipoPago2.get(),'E')!=True: 
				pass
			elif self.TipoPago3.get()!='Exonerado' and self.ValDecimal(self.TipoPago3.get(),'E')!=True:
				pass
			elif self.TipoPago4.get()!='Exonerado' and self.ValDecimal(self.TipoPago4.get(),'E')!=True:
				pass
			elif self.TipoPago5.get()!='Exonerado' and self.ValDecimal(self.TipoPago5.get(),'E')!=True:
				pass
			else:
				return True
				
		elif self.NEstudiantes.get()=='6 Estudiantes a cargo':
			if self.ValE1()!=True or self.ValE2()!=True or self.ValE3()!=True or self.ValE4()!=True or self.ValE5()!=True or self.ValE6()!=True:
				pass
			elif self.ValDNIE1()!=True or self.ValDNIE2()!=True or self.ValDNIE3()!=True or self.ValDNIE4()!=True or self.ValDNIE5()!=True or self.ValDNIE6()!=True:
				pass
			elif self.TipoPago1.get()!='Exonerado' and self.ValDecimal(self.TipoPago1.get(),'E')!=True:
				pass 
			elif self.TipoPago2.get()!='Exonerado' and self.ValDecimal(self.TipoPago2.get(),'E')!=True:
				pass
			elif self.TipoPago3.get()!='Exonerado' and self.ValDecimal(self.TipoPago3.get(),'E')!=True:
				pass
			elif self.TipoPago4.get()!='Exonerado' and self.ValDecimal(self.TipoPago4.get(),'E')!=True:
				pass
			elif self.TipoPago5.get()!='Exonerado' and self.ValDecimal(self.TipoPago5.get(),'E')!=True:
				pass
			elif self.TipoPago6.get()!='Exonerado' and self.ValDecimal(self.TipoPago6.get(),'E')!=True:
				pass
			else:
				return True

	def ValidarDatosAPM(self):
		if self.ValidarApoderado()!=True:
			messagebox.showwarning('Mensaje','Complete los datos del apoderado')

		elif self.ValidarDNIA()!=True:
			messagebox.showwarning('Mensaje','Escriba correctamente el DNI del apoderado')

		elif self.ValidarDNIP()!=True:
			messagebox.showwarning('Mensaje','Escriba correctamente el DNI del padre')

		elif self.ValidarDNIM()!=True:
			messagebox.showwarning('Mensaje','Escriba correctamente el DNI de la madre')

		#elif self.ValidarDNIRep()!=True:
			#messagebox.showwarning('Mensaje','El DNI del apoderado ya existe')
		
		elif self.ValidarNCaracteres()!=True:
			messagebox.showwarning("Mensaje",'''Esta permitido para el ingreso de carácteres a los \ncuadros de la pestaña actual:
				\n> Apellido Paterno, un máximo de 20 carácteres
				\n> Apellido Materno, un máximo de 20 carácteres
				\n> Nombres, un máximo de 30 carácteres
				\n> DNI, un máximo de 8 carácteres
				\n> Dirección, un máximo de 30 carácteres''')

		elif self.CuotaAmapafa.get()=='Tipo de cuota':
			messagebox.showwarning('Mensaje','Seleccione Tipo de cuota')

		elif self.NEstudiantes.get()=='Numero de Estudiantes a cargo':
			messagebox.showwarning('Mensaje','Seleccione Numero de estudiantes a cargo del apoderado')

		elif self.ValidarEstudiante()!=True:
			pass

		else:
			return True

	def ValidarIG(self):

		if self.IngresoGasto.get()=='Seleccione una opción':
			messagebox.showwarning('Mensaje','Tipo de registro no seleccionado')

		elif len(self.NombreIG.get())==0 or len(self.MontoIG.get())==0:
			messagebox.showwarning('Mensaje','Complete los datos')

		elif self.Dia.get()=='Dia' or self.Mes.get()=='Mes' or self.Age.get()=='Año':
			messagebox.showwarning('Mensaje','Fecha no establecida')

		elif len(self.NombreIG.get())>100 or len(self.MontoIG.get())>10:
			messagebox.showwarning('Mensaje','Sobrepasó el máximo de 100 caracteres en el cuadro "Descripción"')

		elif self.ValDecimal(self.MontoIG.get(),'IG')!=True:
			pass

		else:
			return True

	def ValEM(self):

		if len(self.APEM.get())==0 or len(self.AMEM.get())==0 or len(self.NomEM.get())==0 or len(self.DNIEM.get())==0 or self.GradoM.get()=='○' or self.SeccionM.get()=='○':
			messagebox.showwarning('Mensaje','Complete los datos')
			self.TopAnadir.focus_set()

		elif self.DNIEM.get().isdigit()==False or len(self.DNIEM.get())!=8:
			messagebox.showwarning('Mensaje','Escriba correctamente el DNI')
			self.TopAnadir.focus_set()

		elif self.TipoPagoM.get()!='Exonerado' and self.ValDecimal(self.TipoPagoM.get(),'E')!=True:
			self.TopAnadir.focus_set()

		else:
			return True
		
