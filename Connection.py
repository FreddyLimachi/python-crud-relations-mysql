import mysql.connector
from mysql.connector import errorcode

class Connection:

	def Connect(self):
		try:
			connection=mysql.connector.connect(
				user='root',
				host='127.0.0.1',
				password='',
				database='sistema')
			return connection
	
		except mysql.connector.Error as err:

			if err.errno==errorcode.ER_ACCESS_DENIED_ERROR:
				self.MensajeError='Error_User'

			elif err.errno==errorcode.ER_BAD_DB_ERROR:
				self.MensajeError='Error_DB'

			else:
				self.MensajeError='Error_unknown'

	def CloseConnection(self,connection):
		connection.close()

