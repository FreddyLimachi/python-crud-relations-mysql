CREATE DATABASE sistema;
USE sistema;

CREATE TABLE IF NOT EXISTS datos_interfaz (
            `N` INT AUTO_INCREMENT,
            `Texto` VARCHAR(100),
            `Imagen` BLOB,            
            PRIMARY KEY (`N`)
        );

CREATE TABLE IF NOT EXISTS login (
            `N` INT AUTO_INCREMENT,
            `Usuario` VARCHAR(20),
            `Contra` VARCHAR(20),            
            PRIMARY KEY (`N`)
        );

CREATE TABLE IF NOT EXISTS filtrar_age (
            `N` INT AUTO_INCREMENT,
            `Age` VARCHAR(4),            
            PRIMARY KEY (`N`)
        );

INSERT INTO filtrar_age VALUES ('1','2019');
INSERT INTO login VALUES ('1','admin','');
INSERT INTO login VALUES ('2','amapafa','amapafa123');
INSERT INTO login VALUES ('3','kalywarma','kalywarma123');
INSERT INTO datos_interfaz VALUES ('1','Bienvenido a Optimal data',null);

CREATE TABLE IF NOT EXISTS guardar_age (
            `N` INT AUTO_INCREMENT,
            `Age` VARCHAR(4),            
            PRIMARY KEY (`N`)
        );

CREATE TABLE IF NOT EXISTS datos_apoderado2019 (
            `N` INT AUTO_INCREMENT,
            `ApellidoPaterno` VARCHAR(20),
            `ApellidoMaterno` VARCHAR(20),
            `Nombres` VARCHAR(30),
            `DNI` VARCHAR(10),
            `Direccion` VARCHAR(30),
            `Cuota` DECIMAL(8,2),
	    `Multa` DECIMAL(8,2),
	    `Alumnos` INT,
            PRIMARY KEY (`N`)
        );

CREATE TABLE IF NOT EXISTS datos_alumno2019 (
            `N` INT AUTO_INCREMENT,
            `ApellidosNombres` VARCHAR(50),
            `DNI` VARCHAR(8),
            `Grado` VARCHAR(3),
            `Seccion` VARCHAR(3),
            `Cuota` DECIMAL(8,2),
	    `ID` VARCHAR(10),
	    `Estado` VARCHAR(12),
            PRIMARY KEY (`N`)
        );

CREATE TABLE IF NOT EXISTS datos_confi2019 (
            `N` INT AUTO_INCREMENT,
            `Socio` DECIMAL(8,2),
            `Ingresante` DECIMAL(8,2),
            PRIMARY KEY (`N`)
        );

CREATE TABLE IF NOT EXISTS datos_ingreso2019 (
	    `N` INT AUTO_INCREMENT,
	    `Fecha` DATE,
            `Comprobante` VARCHAR(50),
	    `NCP` vARCHAR(10),
            `Monto` DECIMAL(8,2),
            `Descripcion` VARCHAR(100),
	    `Comentario` TEXT, 
            `Miembro` INT,
            `Unidad` DECIMAL(8,2),
   	    `Tipo` VARCHAR(5), 
	    PRIMARY KEY (`N`)       
        );

CREATE TABLE IF NOT EXISTS datos_madre2019 (
            `N` INT AUTO_INCREMENT,
            `ApellidoPaterno` VARCHAR(20),
            `ApellidoMaterno` VARCHAR(20),
            `Nombres` VARCHAR(30),
            `DNI` VARCHAR(8),
            `Direccion` VARCHAR(30),
            PRIMARY KEY (`N`)
        );

CREATE TABLE IF NOT EXISTS datos_padre2019 (
            `N` INT AUTO_INCREMENT,
            `ApellidoPaterno` VARCHAR(20),
            `ApellidoMaterno` VARCHAR(20),
            `Nombres` VARCHAR(30),
            `DNI` VARCHAR(8),
            `Direccion` VARCHAR(30),
            PRIMARY KEY (`N`)
        );


DELIMITER $$
CREATE PROCEDURE aumentar_alumno (name VARCHAR(25), N VARCHAR(10), NAlum VARCHAR(10))
BEGIN
    SET @tableName = name;
    SET @NName= N;
    SET @NAlumName = NAlum;
    SET @q = CONCAT('UPDATE `',@tableName,'` SET Alumnos=?+1 WHERE N=?');
    PREPARE stmt FROM @q;
    EXECUTE stmt USING @NAlumName, @NName;
    DEALLOCATE PREPARE stmt;
END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE buscar_alumno (name VARCHAR(25), CAD VARCHAR(50))
BEGIN
    SET @tableName = name;
    SET @CADName = CAD;
    SET @q = CONCAT('SELECT * FROM `',@tableName,'` WHERE DNI LIKE ? OR CONCAT (Grado,Seccion) LIKE ? OR ApellidosNombres LIKE ?');
    PREPARE stmt FROM @q;
    EXECUTE stmt USING @CADName,@CADName,@CADName;
    DEALLOCATE PREPARE stmt;
END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE buscar_datos (name VARCHAR(25), CAD VARCHAR(50))
BEGIN
    SET @tableName = name;
    SET @CADName = CAD;
    SET @q = CONCAT('SELECT * FROM `',@tableName,'` WHERE DNI LIKE ? OR CONCAT(ApellidoPaterno," ",ApellidoMaterno," ",Nombres ) LIKE ? OR CONCAT(Nombres," ",ApellidoPaterno," ",ApellidoMaterno) LIKE ?');
    PREPARE stmt FROM @q;
    EXECUTE stmt USING @CADName,@CADName,@CADName;
    DEALLOCATE PREPARE stmt;
END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE cargar_alumnos (name VARCHAR(25), ID VARCHAR(10))
BEGIN
    SET @tableName = name;
    SET @IDName = ID;
    SET @q = CONCAT('SELECT * FROM `',@tableName,'` WHERE ID=?');
    PREPARE stmt FROM @q;
    EXECUTE stmt USING @IDName;
    DEALLOCATE PREPARE stmt;
END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE cargar_datos (name VARCHAR(25), N VARCHAR(10)) 
BEGIN
    SET @tableName = name;
    SET @NName = N;
    SET @q = CONCAT('SELECT * FROM `',@tableName,'` WHERE N=?');
    PREPARE stmt FROM @q;
    EXECUTE stmt USING @NName;
    DEALLOCATE PREPARE stmt;
END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE consultar_alumnos (tabla VARCHAR(25), cuota VARCHAR(10), Estado VARCHAR(12))
BEGIN
    SET @tableName = tabla;
    SET @CuotaName = cuota;
    SET @EstadoName = Estado;
    SET @q = CONCAT('SELECT COUNT(*),sum(Cuota) FROM `',@tableName,'` WHERE Cuota<? AND Estado=?');
    PREPARE stmt FROM @q;
    EXECUTE stmt USING @CuotaName ,@EstadoName;
    DEALLOCATE PREPARE stmt;
END $$ 
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE consultar_datos (name VARCHAR(25))
BEGIN
    SET @tableName = name;
    SET @q = CONCAT('SELECT * FROM `',@tableName,'`');
    PREPARE stmt FROM @q;
    EXECUTE stmt;
    DEALLOCATE PREPARE stmt;
END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE consultar_datosoa (name VARCHAR(25))
BEGIN
    SET @tableName = name;
    SET @q = CONCAT('SELECT * FROM `',@tableName,'` ORDER BY ApellidoPaterno , ApellidoMaterno , Nombres');
    PREPARE stmt FROM @q;
    EXECUTE stmt;
    DEALLOCATE PREPARE stmt;
END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE consultar_datosoaa (name VARCHAR(25))
BEGIN
    SET @tableName = name;
    SET @q = CONCAT('SELECT * FROM `',@tableName,'` ORDER BY ApellidosNombres');
    PREPARE stmt FROM @q;
    EXECUTE stmt;
    DEALLOCATE PREPARE stmt;
END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE consultar_ingreso (name VARCHAR(25), tipo VARCHAR(5))
BEGIN
    SET @tableName = name;
    SET @TipoName = tipo;
    SET @q = CONCAT('SELECT * FROM `',@tableName,'` WHERE Tipo=?');
    PREPARE stmt FROM @q;
    EXECUTE stmt USING @TipoName;
    DEALLOCATE PREPARE stmt;
END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE consultar_miembros (tabla VARCHAR (25), cuota VARCHAR(10))
BEGIN
    SET @tableName = tabla;
    SET @CuotaName = cuota;
    SET @q = CONCAT('SELECT COUNT(*) FROM `',@tableName,'` WHERE Cuota=?');
    PREPARE stmt FROM @q;
    EXECUTE stmt USING @CuotaName;
    DEALLOCATE PREPARE stmt;
END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE consultar_multas (tabla VARCHAR(25), multa VARCHAR(10))
BEGIN
    SET @tableName = tabla;
    SET @MultaName = multa;
    SET @q = CONCAT('SELECT sum(Multa) FROM `',@tableName,'` WHERE Multa>?');
    PREPARE stmt FROM @q;
    EXECUTE stmt USING @MultaName;
    DEALLOCATE PREPARE stmt;
END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE crear_alumno (name VARCHAR(25))
BEGIN
    SET @tableName = name;
    SET @q = CONCAT('
        CREATE TABLE IF NOT EXISTS `' , @tableName, '` (
            `N` INT AUTO_INCREMENT,
            `ApellidosNombres` VARCHAR(50),
            `DNI` VARCHAR(8),
            `Grado` VARCHAR(3),
            `Seccion` VARCHAR(3),
            `Cuota` DECIMAL(8,2),
	    `ID` VARCHAR(10),
	    `Estado` VARCHAR(12),
            PRIMARY KEY (`N`)
        )
    ');
    PREPARE stmt FROM @q;
    EXECUTE stmt;
    DEALLOCATE PREPARE stmt;
END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE crear_apoderado (name VARCHAR(25))
BEGIN
    SET @tableName = name;
    SET @q = CONCAT('
        CREATE TABLE IF NOT EXISTS `' , @tableName, '` (
            `N` INT AUTO_INCREMENT,
            `ApellidoPaterno` VARCHAR(20),
            `ApellidoMaterno` VARCHAR(20),
            `Nombres` VARCHAR(30),
            `DNI` VARCHAR(15),
            `Direccion` VARCHAR(30),
	    `Cuota` DECIMAL(8,2),
	    `Multa` DECIMAL(8,2),
	    `Alumnos` INT,
            PRIMARY KEY (`N`)
        )
    ');
    PREPARE stmt FROM @q;
    EXECUTE stmt;
    DEALLOCATE PREPARE stmt;
END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE crear_confi (name VARCHAR(25))
BEGIN
    SET @tableName = name;
    SET @q = CONCAT('
        CREATE TABLE IF NOT EXISTS `' , @tableName, '` (
            `N` INT AUTO_INCREMENT,
            `Socio` DECIMAL(8,2),
            `Ingresante` DECIMAL(8,2),
            PRIMARY KEY (`N`)
        )
    ');
    PREPARE stmt FROM @q;
    EXECUTE stmt;
    DEALLOCATE PREPARE stmt;
END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE crear_ingresos (name VARCHAR(25))
BEGIN
    SET @tableName = name;
    SET @q = CONCAT('
        CREATE TABLE IF NOT EXISTS `' , @tableName, '` (
	    `N` INT AUTO_INCREMENT,
	    `Fecha` DATE,
            `Comprobante` VARCHAR(50),
	    `NCP` vARCHAR(10),
            `Monto` DECIMAL(8,2),
            `Descripcion` VARCHAR(100),
	    `Comentario` TEXT, 
            `Miembro` INT,
            `Unidad` DECIMAL(8,2),
   	    `Tipo` VARCHAR(5), 
	    PRIMARY KEY (`N`)       
        )
    ');
    PREPARE stmt FROM @q;
    EXECUTE stmt;
    DEALLOCATE PREPARE stmt;
END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE crear_tablas (name VARCHAR(25))
BEGIN
    SET @tableName = name;
    SET @q = CONCAT('
        CREATE TABLE IF NOT EXISTS `' , @tableName, '` (
            `N` INT AUTO_INCREMENT,
            `ApellidoPaterno` VARCHAR(20),
            `ApellidoMaterno` VARCHAR(20),
            `Nombres` VARCHAR(30),
            `DNI` VARCHAR(8),
            `Direccion` VARCHAR(30),
            PRIMARY KEY (`N`)
        )
    ');
    PREPARE stmt FROM @q;
    EXECUTE stmt;
    DEALLOCATE PREPARE stmt;
END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE eliminar_datos (name VARCHAR(25), N VARCHAR(10))
BEGIN
    SET @tableName = name;
    SET @NName = N;
    SET @q = CONCAT('DELETE FROM `',@tableName,'` WHERE N=?');
    PREPARE stmt FROM @q;
    EXECUTE stmt USING @NName;
    DEALLOCATE PREPARE stmt;
END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE exportar_alumno (name VARCHAR(25), path VARCHAR(50))
BEGIN
    SET @q = CONCAT('SELECT ApellidosNombres,DNI,Grado,Seccion,Cuota INTO OUTFILE ',char(39),path,char(39),' FIELDS 
        TERMINATED BY "," LINES TERMINATED BY "
" FROM ',name,' ORDER BY ApellidosNombres');
     PREPARE stmt from @q;
     EXECUTE stmt ;
     DEALLOCATE PREPARE stmt;
END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE exportar_alumnooa (name VARCHAR(25), path VARCHAR(100))
BEGIN
    SET @q = CONCAT('(SELECT "APELLIDOS y NOMBRES","DNI","GRADO", "SECCI�N","CUOTA") UNION (SELECT ApellidosNombres,DNI,Grado,Seccion,Cuota INTO OUTFILE ',char(39),path,char(39),' FIELDS 
        TERMINATED BY "," LINES TERMINATED BY "
" FROM ',name,')');
     PREPARE stmt from @q;
     EXECUTE stmt ;
     DEALLOCATE PREPARE stmt;
END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE exportar_datos (name VARCHAR(25), path VARCHAR(50))
BEGIN
    SET @q = CONCAT('SELECT ApellidoPaterno,ApellidoMaterno,Nombres,DNI,Direccion INTO OUTFILE ',char(39),path,char(39),' FIELDS 
        TERMINATED BY "," LINES TERMINATED BY "
" FROM ',name,' ORDER BY ApellidoPaterno , ApellidoMaterno , Nombres');
     PREPARE stmt from @q;
     EXECUTE stmt ;
     DEALLOCATE PREPARE stmt;
END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE exportar_datosoa (name VARCHAR(25), path VARCHAR(100))
BEGIN
    SET @q = CONCAT('(SELECT "APELLIDO PATERNO","APELLIDO MATERNO","NOMBRES", "DNI","DIRECCI�N") UNION (SELECT ApellidoPaterno,ApellidoMaterno,Nombres,DNI,Direccion INTO OUTFILE ',char(39),path,char(39),' FIELDS 
        TERMINATED BY "," LINES TERMINATED BY "
" FROM ',name,')');
     PREPARE stmt from @q;
     EXECUTE stmt ;
     DEALLOCATE PREPARE stmt;
END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE insertar_alumno (name VARCHAR(25), N VARCHAR(10), AN VARCHAR(50), DNI VARCHAR(8),
GR VARCHAR(3), SC VARCHAR(2), CU VARCHAR(10), ID VARCHAR(10), Estado VARCHAR(12))
BEGIN
    SET @tableName = name;
    SET @NName= N;
    SET @ANName = AN;
    SET @DNIName = DNI;
    SET @GRName = GR;
    SET @SCName = SC;
    SET @CUName = CU;
    SET @IDName = ID;
    SET @EstadoName = Estado;
    SET @q = CONCAT('INSERT INTO `' , @tableName, '` VALUES(?,?,?,?,?,?,?,?)');
    PREPARE stmt FROM @q;
    EXECUTE stmt USING @NName, @ANName, @DNIName, @GRName, @SCName, @CUName, @IDName, @EstadoName;
    DEALLOCATE PREPARE stmt;
END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE exportar_ea (name VARCHAR(25), path VARCHAR(100))
BEGIN
    SET @q = CONCAT('(SELECT "N�","Fecha","Comprobante de pago","N� de CP","Descripcion","Monto Total") UNION (SELECT N,Fecha,Comprobante,NCP,Descripcion,Monto INTO OUTFILE ',char(39),path,char(39),' FIELDS 
        TERMINATED BY "," LINES TERMINATED BY "
" FROM ',name,' WHERE Tipo="EA")');
     PREPARE stmt from @q;
     EXECUTE stmt ;
     DEALLOCATE PREPARE stmt;
END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE exportar_ek (name VARCHAR(25), path VARCHAR(100))
BEGIN
    SET @q = CONCAT('(SELECT "N�","Fecha","Comprobante de pago","N� de CP","Descripcion","Monto Total") UNION (SELECT N,Descripcion,Miembro,Unidad,Monto INTO OUTFILE ',char(39),path,char(39),' FIELDS 
        TERMINATED BY "," LINES TERMINATED BY "
" FROM ',name,' WHERE Tipo="EK")');
     PREPARE stmt from @q;
     EXECUTE stmt ;
     DEALLOCATE PREPARE stmt;
END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE exportar_ia (name VARCHAR(25), path VARCHAR(100))
BEGIN
    SET @q = CONCAT('(SELECT "N�","Descripcion","N� Miembros","Pago/Unidad","Monto Total") UNION (SELECT N,Descripcion,Miembro,Unidad,Monto INTO OUTFILE ',char(39),path,char(39),' FIELDS 
        TERMINATED BY "," LINES TERMINATED BY "
" FROM ',name,' WHERE Tipo="IA")');
     PREPARE stmt from @q;
     EXECUTE stmt ;
     DEALLOCATE PREPARE stmt;
END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE exportar_ik (name VARCHAR(25), path VARCHAR(100))
BEGIN
    SET @q = CONCAT('(SELECT "N�","Descripcion","N� Miembros","Monto Total") UNION (SELECT N,Descripcion,Miembro,Monto INTO OUTFILE ',char(39),path,char(39),' FIELDS 
        TERMINATED BY "," LINES TERMINATED BY "
" FROM ',name,' WHERE Tipo="IK")');
     PREPARE stmt from @q;
     EXECUTE stmt ;
     DEALLOCATE PREPARE stmt;
END $$
DELIMITER ;


DELIMITER $$
CREATE PROCEDURE insertar_apoderado (name VARCHAR(25), N VARCHAR(10), AP VARCHAR(20), AM VARCHAR(20),
Nom VARCHAR(30), DNI varchar(8), Direc VARCHAR(30), Cuota VARCHAR(15), Multa VARCHAR(10), Alumnos VARCHAR(10))
BEGIN
    SET @tableName = name;
    SET @NName= N;
    SET @APName = AP;
    SET @AMName = AM;
    SET @NomName = Nom;
    SET @DNIName = DNI;
    SET @DirecName = Direc;
    SET @CuotaName = Cuota;
    SET @MultaName = Multa;
    SET @AlumnosName = Alumnos;
    SET @q = CONCAT('INSERT INTO `' , @tableName, '` VALUES(?,?,?,?,?,?,?,?,?)');
    PREPARE stmt FROM @q;
    EXECUTE stmt USING @NName, @APName, @AMName, @NomName, @DNIName, @DirecName, @CuotaName,@MultaName, @AlumnosName; 
    DEALLOCATE PREPARE stmt;
END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE insertar_confi (name VARCHAR(25), N VARCHAR(10), CS VARCHAR(10), CI VARCHAR(10))
BEGIN
    SET @tableName = name;
    SET @CSName = CS;
    SET @CIName = CI;
    SET @NName = N;
    SET @q = CONCAT('INSERT INTO `' , @tableName, '` VALUES(?,?,?)');
    PREPARE stmt FROM @q;
    EXECUTE stmt USING @NName, @CSName, @CIName;
    DEALLOCATE PREPARE stmt;
END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE insertar_datos (name VARCHAR(25), N VARCHAR(20), AP VARCHAR(20), AM VARCHAR(20),
 Nom VARCHAR(30), DNI VARCHAR(8), Direc VARCHAR(30))
BEGIN
    SET @tableName = name;
    SET @NName= N;
    SET @APName = AP;
    SET @AMName = AM;
    SET @NomName = Nom;
    SET @DNIName = DNI;
    SET @DirecName = Direc;
    SET @q = CONCAT('INSERT INTO `' , @tableName, '` VALUES(?,?,?,?,?,?)');
    PREPARE stmt FROM @q;
    EXECUTE stmt USING @NName, @APName, @AMName, @NomName, @DNIName, @DirecName;
    DEALLOCATE PREPARE stmt;
END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE modificar_alumno (name VARCHAR(25), N VARCHAR(10), AN VARCHAR(50), DNI VARCHAR(8),
 Grado VARCHAR(3), Seccion VARCHAR(2), Cuota VARCHAR(10), Estado VARCHAR(12))
BEGIN
    SET @tableName = name;
    SET @NName= N;
    SET @ANName = AN;
    SET @DNIName = DNI;
    SET @GrName = Grado;
    SET @SecName = Seccion;
    SET @CuotaName = Cuota;
    SET @EstadoName = Estado;
    SET @q = CONCAT('UPDATE `',@tableName,'` SET ApellidosNombres=?, DNI=?, Grado=?, Seccion=?, Cuota=?, Estado=? WHERE N=?');
    PREPARE stmt FROM @q;
    EXECUTE stmt USING @ANName, @DNIName, @GrName, @SecName, @CuotaName,@EstadoName, @NName;
    DEALLOCATE PREPARE stmt;
END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE modificar_apoderado (name VARCHAR(25), N VARCHAR(10), AP VARCHAR(20), AM VARCHAR(20),
 Nom VARCHAR(30), DNI vARCHAR(8), Direc VARCHAR(30), Cuota VARCHAR(12), Multa VARCHAR(10))
BEGIN
    SET @tableName = name;
    SET @NName= N;
    SET @APName = AP;
    SET @AMName = AM;
    SET @NomName = Nom;
    SET @DNIName = DNI;
    SET @DirecName = Direc;
    SET @CuotaName = Cuota;
    SET @MultaName = Multa;
    SET @q = CONCAT('UPDATE `',@tableName,'` SET ApellidoPaterno=?, ApellidoMaterno=?, Nombres=?, DNI=?, Direccion=?, Cuota=?, Multa=Multa+? WHERE N=?');
    PREPARE stmt FROM @q;
    EXECUTE stmt USING @APName,@AMName,@NomName,@DNIName,@DirecName, @CuotaName, @MultaName, @NName;
    DEALLOCATE PREPARE stmt;
END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE modificar_confi (name VARCHAR(25), socio VARCHAR(10), ingresante VARCHAR(10))
BEGIN
    SET @tableName = name;
    SET @SocioName = socio;
    SET @IngresanteName = ingresante;
    SET @q = CONCAT('UPDATE `',@tableName,'` SET Socio=?, Ingresante=?');
    PREPARE stmt FROM @q;
    EXECUTE stmt USING @SocioName,@IngresanteName;
    DEALLOCATE PREPARE stmt;
END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE modificar_datos (name VARCHAR(50), N VARCHAR(10), AP VARCHAR(20), AM VARCHAR(20),
Nom VARCHAR(30), DNI Varchar(8), Direc VARCHAR(30))
BEGIN
    SET @tableName = name;
    SET @NName= N;
    SET @APName = AP;
    SET @AMName = AM;
    SET @NomName = Nom;
    SET @DNIName = DNI;
    SET @DirecName = Direc;
    SET @q = CONCAT('UPDATE `',@tableName,'` SET ApellidoPaterno=?, ApellidoMaterno=?, Nombres=?, DNI=?, Direccion=? WHERE N=?');
    PREPARE stmt FROM @q;
    EXECUTE stmt USING @APName,@AMName,@NomName,@DNIName,@DirecName,@NName;
    DEALLOCATE PREPARE stmt;
END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE modificar_ingreso (name VARCHAR(25), N VARCHAR(10), Fecha VARCHAR(10), Comprobante VARCHAR(50),
NCP VARCHAR(10), Monto VARCHAR(10), Descripcion VARCHAR(100), Comentario text)
BEGIN
    SET @tableName = name;
    SET @NName = N;
    SET @FechaName = Fecha;
    SET @ComprobanteName = Comprobante;
    SET @NCPName = NCP;
    SET @MontoName = Monto;
    SET @DescripName = Descripcion;
    SET @ComentarioName = Comentario;
    SET @q = CONCAT('UPDATE `' , @tableName, '` SET Fecha=?,Comprobante=?,NCP=?,Monto=?,Descripcion=?,Comentario=? WHERE N=?');
    PREPARE stmt FROM @q;
    EXECUTE stmt USING @FechaName, @ComprobanteName, @NCPName, @MontoName, @DescripName, @ComentarioName, @NName; 
    DEALLOCATE PREPARE stmt;
END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE modificar_monto (tabla VARCHAR(25), N VARCHAR(10), monto VARCHAR(10), miembro VARCHAR(10))
BEGIN
    SET @tableName = tabla;
    SET @NName = N;
    SET @MontoName = monto;
    SET @MiembroName = miembro;
    SET @q = CONCAT('UPDATE `',@tableName,'` SET Monto=?, Miembro=? WHERE N=?');
    PREPARE stmt FROM @q;
    EXECUTE stmt USING @MontoName,@MiembroName,@NName;
    DEALLOCATE PREPARE stmt;
END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE multi_monto (tabla VARCHAR(25), N VARCHAR(10), miembro VARCHAR(10), Unidad VARCHAR(10))
BEGIN
    SET @tableName = tabla;
    SET @NName = N;
    SET @MiembroName = miembro;
    SET @UnidadName = unidad;
    SET @q = CONCAT('UPDATE `',@tableName,'` SET Monto=?*?, Miembro=?,Unidad=? WHERE N=?');
    PREPARE stmt FROM @q;
    EXECUTE stmt USING @MiembroName,@UnidadName,@MiembroName,@UnidadName,@NName;
    DEALLOCATE PREPARE stmt;
END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE quitar_alumno (NAME varchar(25), N VARCHAR(10), NAlum VARCHAR(10))
BEGIN
    SET @tableName = name;
    SET @NName= N;
    SET @NAlumName = NAlum;
    SET @q = CONCAT('UPDATE `',@tableName,'` SET Alumnos=?-1 WHERE N=?');
    PREPARE stmt FROM @q;
    EXECUTE stmt USING @NAlumName, @NName;
    DEALLOCATE PREPARE stmt;
END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE registrar_ingreso (name VARCHAR(25), N VARCHAR(10), Fecha VARCHAR(10), Comprobante VARCHAR(50),
NCP VARCHAR(10), Monto VARCHAR(10), Descripcion VARCHAR(100), Comentario TEXT, Miembro VARCHAR(5), Unidad VARCHAR(10),
tipo VARCHAR(5))
BEGIN
    SET @tableName = name;
    SET @NName = N;
    SET @FechaName = Fecha;
    SET @ComprobanteName = Comprobante;
    SET @NCPName = NCP;
    SET @MontoName = Monto;
    SET @DescripName = Descripcion;
    SET @ComentarioName = Comentario;
    SET @MiembroName = Miembro;
    SET @UnidadName = Unidad;
    SET @TipoName = tipo;
    SET @q = CONCAT('INSERT INTO `' , @tableName, '` VALUES(?,?,?,?,?,?,?,?,?,?)');
    PREPARE stmt FROM @q;
    EXECUTE stmt USING @NName, @FechaName, @ComprobanteName, @NCPName, @MontoName, @DescripName, @ComentarioName, @MiembroName, @UnidadName, @TipoName; 
    DEALLOCATE PREPARE stmt;
END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE relacionar_alumno (name VARCHAR(25))
BEGIN
    SET @tableName = name;
    SET @q = CONCAT('SELECT MAX(N) FROM `',@tableName,'`');
    PREPARE stmt FROM @q;
    EXECUTE stmt;
    DEALLOCATE PREPARE stmt;
END $$
DELIMITER ;


