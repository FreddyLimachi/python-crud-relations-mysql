from Connection import *

class Data(Connection):

	def ConsultarYear(self):
		cnx=self.Connect()
		Cursor=cnx.cursor()
		Cursor.execute("SELECT N, Age FROM save_year")
		Arreglo=[]
		for elemento in Cursor:
			Arreglo.append(elemento)
		self.CloseConnection(cnx)
		return Arreglo		

	def RegistrarApoderado(self,APA,AMA,NomA,DNIA,Direc,Cuota,Multa,NAlum,APP,AMP,NomP,DNIP,APM,AMM,NomM,DNIM,Age,IE):
		cnx=self.Connect()
		Cursor=cnx.cursor()
		Cursor.execute('CALL registrar_apoderado ("null","'+APA+'","'+AMA+'","'+NomA+'","'+DNIA+'","'+Direc+'","'+Cuota+'","'+Multa+'","'+NAlum+'","'+APP+'","'+AMP+'","'+NomP+'","'+DNIP+'","'+APM+'","'+AMM+'","'+NomM+'","'+DNIM+'","'+Age+'","'+IE+'")')
		cnx.commit()
		self.CloseConnection(cnx)

	def RegistrarEstudiante(self,APE,AME,NomE,DNI,Grado,Seccion,Cuota,Estado,Relacion,Age,IE):
		cnx=self.Connect()
		Cursor=cnx.cursor()
		Cursor.execute('CALL registrar_estudiante ("null","'+APE+'","'+AME+'","'+NomE+'","'+DNI+'","'+Grado+'","'+Seccion+'","'+Cuota+'","'+Estado+'","'+Relacion+'","'+Age+'","'+IE+'")')
		cnx.commit()
		self.CloseConnection(cnx)

	def ModificarApoderado(self,N,APA,AMA,NomA,DNIA,Direc,Cuota,Multa,APP,AMP,NomP,DNIP,APM,AMM,NomM,DNIM):
		cnx=self.Connect()
		Cursor=cnx.cursor()
		Cursor.execute('CALL modificar_apoderado ("'+N+'","'+APA+'","'+AMA+'","'+NomA+'","'+DNIA+'","'+Direc+'","'+Cuota+'","'+Multa+'","'+APP+'","'+AMP+'","'+NomP+'","'+DNIP+'","'+APM+'","'+AMM+'","'+NomM+'","'+DNIM+'")')
		cnx.commit()
		self.CloseConnection(cnx)

	def ModificarEstudiante(self,N,APE,AME,NomE,DNI,Grado,Seccion,Cuota,Estado):
		cnx=self.Connect()
		Cursor=cnx.cursor()
		Cursor.execute('CALL modificar_estudiante ("'+N+'","'+APE+'","'+AME+'","'+NomE+'","'+DNI+'","'+Grado+'","'+Seccion+'","'+Cuota+'","'+Estado+'")')
		cnx.commit()
		self.CloseConnection(cnx)

	def ModNEstudiante(self,N,Tipo):
		cnx=self.Connect()
		Cursor=cnx.cursor()
		Cursor.execute("CALL mod_nestudiante ('"+N+"','"+Tipo+"')")
		cnx.commit()
		self.CloseConnection(cnx)

	def EliminarDatos(self,N,tabla):
		cnx=self.Connect()
		Cursor=cnx.cursor()
		Cursor.execute("CALL eliminar_datos('"+tabla+"','"+N+"')")
		cnx.commit()
		self.CloseConnection(cnx)

	def EliminarSocio(self,N):
		cnx=self.Connect()
		Cursor=cnx.cursor()
		Cursor.execute("CALL eliminar_socio('"+N+"')")
		cnx.commit()
		self.CloseConnection(cnx)
	
	def ConsultarApoderado(self,Orden,Age,IE):
		cnx=self.Connect()
		Cursor=cnx.cursor(buffered=True)
		for result in Cursor.execute('CALL consultar_apoderado ("'+Orden+'","'+Age+'","'+IE+'")',multi=True):
	  		if result.with_rows:
	  			Lista=result.fetchall()
		self.CloseConnection(cnx)
		return Lista

	def ConsultarEstudiante(self,Orden,Age,IE):
		cnx=self.Connect()
		Cursor=cnx.cursor(buffered=True)
		for result in Cursor.execute("CALL consultar_estudiante ('"+Orden+"','"+Age+"','"+IE+"')",multi=True):
	  		if result.with_rows:
	  			Lista=result.fetchall()
		self.CloseConnection(cnx)
		return Lista

	def ConsultarPadre(self,Orden,Age,IE):
		cnx=self.Connect()
		Cursor=cnx.cursor(buffered=True)
		for result in Cursor.execute("CALL consultar_padre ('"+Orden+"','"+Age+"','"+IE+"')",multi=True):
	  		if result.with_rows:
	  			Lista=result.fetchall()
		self.CloseConnection(cnx)
		return Lista

	def ConsultarMadre(self,Orden,Age,IE):
		cnx=self.Connect()
		Cursor=cnx.cursor(buffered=True)
		for result in Cursor.execute("CALL consultar_madre ('"+Orden+"','"+Age+"','"+IE+"')",multi=True):
	  		if result.with_rows:
	  			Lista=result.fetchall()
		self.CloseConnection(cnx)
		return Lista

	def BuscarApoderado(self,Cadena,Orden,Age,IE):
		cnx=self.Connect()
		Cursor=cnx.cursor(buffered=True)
		for result in Cursor.execute('CALL buscar_apoderado ("'+Cadena+'%","'+Orden+'","'+Age+'","'+IE+'")',multi=True):
			if result.with_rows:
	  			Lista=result.fetchall()
		self.CloseConnection(cnx)
		return Lista

	def BuscarEstudiante(self,Cadena,Orden,Age,IE):
		cnx=self.Connect()
		Cursor=cnx.cursor(buffered=True)
		for result in Cursor.execute('CALL buscar_estudiante ("'+Cadena+'%","'+Orden+'","'+Age+'","'+IE+'")',multi=True):
			if result.with_rows:
	  			Lista=result.fetchall()
		self.CloseConnection(cnx)
		return Lista

	def BuscarPadre(self,Cadena,Orden,Age,IE):
		cnx=self.Connect()
		Cursor=cnx.cursor(buffered=True)
		for result in Cursor.execute('CALL buscar_padre ("'+Cadena+'%","'+Orden+'","'+Age+'","'+IE+'")',multi=True):
			if result.with_rows:
	  			Lista=result.fetchall()
		self.CloseConnection(cnx)
		return Lista

	def BuscarMadre(self,Cadena,Orden,Age,IE):
		cnx=self.Connect()
		Cursor=cnx.cursor(buffered=True)
		for result in Cursor.execute('CALL buscar_madre ("'+Cadena+'%","'+Orden+'","'+Age+'","'+IE+'")',multi=True):
			if result.with_rows:
	  			Lista=result.fetchall()
		self.CloseConnection(cnx)
		return Lista

	def CargarApoderado(self,N,Tipo):
		cnx=self.Connect()
		Cursor=cnx.cursor()
		for result in Cursor.execute("CALL cargar_apoderado ('"+N+"','"+Tipo+"')",multi=True):
	  		if result.with_rows:
	  			Lista=result.fetchall()
		self.CloseConnection(cnx)
		return Lista

	def CargarEstudiante(self,N,Tipo):
		cnx=self.Connect()
		Cursor=cnx.cursor()
		for result in Cursor.execute("CALL cargar_estudiante ('"+N+"','"+Tipo+"')",multi=True):
	  		if result.with_rows:
	  			Lista=result.fetchall()
		self.CloseConnection(cnx)
		return Lista

	def CargarDNIApoderado(self,DNI,IE):
		cnx=self.Connect()
		Cursor=cnx.cursor()
		for result in Cursor.execute('CALL alldni_apoderado ("'+DNI+'","'+IE+'")',multi=True):
			if result.with_rows:
	  			Lista=result.fetchall()
		self.CloseConnection(cnx)
		return Lista

	def ConfirmarDatos(self):
		cnx=self.Connect()
		Cursor=cnx.cursor()
		Cursor.execute("SHOW tables like 'datos_estudiante2019'")	
		for n in Cursor:
			return n	
		self.CloseConnection(cnx)

	def ValidarDNI(self,D,tabla):
		cnx=self.Connect()
		Cursor=cnx.cursor()
		for result in Cursor.execute("CALL consultar_datos ('"+tabla+"')",multi=True):
			if result.with_rows:
	  			Lista=result.fetchall()
		for dni in Lista:
			if dni[4]==D:
				return True
		self.CloseConnection(cnx)
		return False

	def ValidarDNIEstudiante(self,D,tabla):
		cnx=self.Connect()
		Cursor=cnx.cursor()
		Cursor.execute("CALL consultar_datos ('"+tabla+"')",multi=True)
		for dni in Cursor:
			if dni[2]==D:
				return True
		self.CloseConnection(cnx)
		return False

	def RelacionarEstudiante(self):
		cnx=self.Connect()
		Cursor=cnx.cursor(buffered=True)
		for result in Cursor.execute("CALL relacionar_estudiante ()",multi=True):
			if result.with_rows:
	  			Lista=result.fetchall()
		cnx.commit()
		Arreglo=[]
		for dato in Lista:
			Arreglo=dato[0]
		self.CloseConnection(cnx)
		return Arreglo

	def RegistrarIngreso(self,Fecha,Comprobante,NCP,Monto,Descripcion,Comentario,Miembro,Unidad,tipo,Age,IE):
		cnx=self.Connect()
		Cursor=cnx.cursor()
		Cursor.execute("CALL registrar_ingreso (null,'"+Fecha+"','"+Comprobante+"','"+NCP+"','"+Monto+"','"+Descripcion+"','"+Comentario+"','"+Miembro+"','"+Unidad+"','"+tipo+"','"+Age+"','"+IE+"')")		
		cnx.commit()
		self.CloseConnection(cnx)

	def ConsultarIngreso(self,tipo,Age,IE):
		cnx=self.Connect()
		Cursor=cnx.cursor(buffered=True)
		for result in Cursor.execute("CALL consultar_ingreso ('"+tipo+"','"+Age+"','"+IE+"')",multi=True):
	  		if result.with_rows:
	  			Lista=result.fetchall()
		self.CloseConnection(cnx)
		return Lista

	def ModificarIngreso(self,N,Fecha,Comprobante,NCP,Monto,Descripcion,Comentario,tipo):
		cnx=self.Connect()
		Cursor=cnx.cursor()
		Cursor.execute("CALL modificar_ingreso ('"+N+"','"+Fecha+"','"+Comprobante+"','"+NCP+"','"+Monto+"','"+Descripcion+"','"+Comentario+"','"+tipo+"')")		
		cnx.commit()
		self.CloseConnection(cnx)

	def CargarIngreso(self,N):
		cnx=self.Connect()
		Cursor=cnx.cursor()
		for result in Cursor.execute("CALL cargar_ingreso ('"+N+"')",multi=True):
	  		if result.with_rows:
	  			Lista=result.fetchall()
		self.CloseConnection(cnx)
		return Lista

	def MultiMonto(self,N,Miembro,Unidad):
		cnx=self.Connect()
		Cursor=cnx.cursor()
		Cursor.execute("CALL multi_monto ('"+N+"','"+Miembro+"','"+Unidad+"')")
		cnx.commit()
		self.CloseConnection(cnx)

	def ConsultarMultas(self,Multa,Age,IE):
		cnx=self.Connect()
		Cursor=cnx.cursor()
		for result in Cursor.execute("CALL consultar_multas ('"+Multa+"','"+Age+"','"+IE+"')",multi=True):
	  		if result.with_rows:
	  			Lista=result.fetchall()
		self.CloseConnection(cnx)
		return Lista

	def ConsultarNMiembros(self,Monto,Age,IE):
		cnx=self.Connect()
		Cursor=cnx.cursor()
		for result in Cursor.execute("CALL consultar_miembros ('"+Monto+"','"+Age+"','"+IE+"')",multi=True):
	  		if result.with_rows:
	  			Lista=result.fetchall()
		self.CloseConnection(cnx)
		return Lista

	def ConsultarNEstudiantes(self,Monto,Estado,Age,IE):
		cnx=self.Connect()
		Cursor=cnx.cursor()
		for result in Cursor.execute("CALL consultar_estupago ('"+Age+"','"+IE+"','"+Monto+"','"+Estado+"')",multi=True):
	  		if result.with_rows:
	  			Lista=result.fetchall()
		self.CloseConnection(cnx)
		return Lista

	def ModMonto(self,N,Monto,Miembro):
		cnx=self.Connect()
		Cursor=cnx.cursor()
		Cursor.execute("CALL modificar_monto ('"+N+"','"+Monto+"','"+Miembro+"')")
		cnx.commit()
		self.CloseConnection(cnx)

	def ConfigurarPago(self,CS,CI,Age,IE):
		cnx=self.Connect()
		Cursor=cnx.cursor()
		Cursor.execute("CALL modificar_confi ('"+CS+"','"+CI+"','"+Age+"','"+IE+"')")
		cnx.commit()
		self.CloseConnection(cnx)

	def InsertarPago(self,tabla):
		cnx=self.Connect()
		Cursor=cnx.cursor()
		Cursor.execute("CALL insertar_confi ('"+tabla+"',null,'0','0')")
		cnx.commit()
		self.CloseConnection(cnx)

	def ConsultarPago(self,Age,IE):
		cnx=self.Connect()
		Cursor=cnx.cursor(buffered=True)
		for result in Cursor.execute("CALL consultar_confi ('"+Age+"','"+IE+"')",multi=True):
	  		if result.with_rows:
	  			Lista=result.fetchall()
		self.CloseConnection(cnx)
		return Lista

class Usuario(Connection):

	def Consultar(self,User,Pass):
		try:
			cnx=self.Connect()
			Cursor=cnx.cursor()
			Cursor.execute("SELECT * FROM login WHERE Usuario='"+User+"' AND Contra='"+Pass+"'")
			for login in Cursor:
				if login[1]==User and login[2]==Pass and login[0]==1:
					return "Administrador"
				if login[1]==User and login[2]==Pass and login[0]==2:
					return "AMAPAFA"
				if login[1]==User and login[2]==Pass and login[0]==3:
					return "Qaliwarma"
			self.CloseConnection(cnx)
			return False

		except AttributeError:
			return str(self.MensajeError)

	def CambiarLogin(self,User,Pass):
		cnx=self.Connect()
		Cursor=cnx.cursor()
		Cursor.execute("UPDATE login SET Contra='"+Pass+"' WHERE Usuario='"+User+"'")
		cnx.commit()
		self.CloseConnection(cnx)

	def ValidarContra(self,User,Pass):
		cnx=self.Connect()
		Cursor=cnx.cursor()
		Cursor.execute("SELECT * FROM login WHERE Usuario='"+User+"' AND Contra='"+Pass+"'")
		for login in Cursor:
			if login[1]==User and login[2]==Pass:
				self.CloseConnection(cnx)
				return True
		self.CloseConnection(cnx)
		return False

class ModInterfaz(Connection):

	def ModificarTexto(self,texto):
		cnx=self.Connect()
		Cursor=cnx.cursor()
		Cursor.execute("UPDATE datos_interfaz SET Texto='"+texto+"'")
		cnx.commit()
		self.CloseConnection(cnx)

	def ModificarImagen(self,imagen):
		cnx=self.Connect()
		Cursor=cnx.cursor()
		Cursor.execute("UPDATE datos_interfaz SET Imagen='"+imagen+"'")
		cnx.commit()
		self.CloseConnection(cnx)

	def ConsultarImagen(self,n):
		cnx=self.Connect()
		Cursor=cnx.cursor()
		Cursor.execute("SELECT * FROM datos_interfaz WHERE N=1")
		Arreglo=[]
		for elemento in Cursor:
			Arreglo=elemento[2]
		self.CloseConnection(cnx)
		return Arreglo

	def ConsultarTexto(self):
		cnx=self.Connect()
		Cursor=cnx.cursor()
		Cursor.execute("SELECT Texto FROM datos_interfaz WHERE N=1")
		Arreglo=""
		for elemento in Cursor:
			Arreglo=elemento
		self.CloseConnection(cnx)
		return Arreglo