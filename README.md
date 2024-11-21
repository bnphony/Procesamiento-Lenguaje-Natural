<div align="center">
  
  # Procesamiento del Lenguaje Natural
</div>

<div align="center">
  <img src="https://raw.githubusercontent.com/bnphony/Sistema-Inventario/master/proyecto1/static/img/general.PNG" width="80%" alt="Main Screen">
  <br/><br/>
  
  ![GitHub](https://img.shields.io/github/last-commit/bnphony/Sistema-Inventario)
  [![Django](https://img.shields.io/badge/Framework-Django-green)](https://www.djangoproject.com/)
  [![Python](https://img.shields.io/badge/Code-Python-fd81f)](https://www.python.org/)
  [![D3js](https://img.shields.io/badge/Code-D3js-cc6d0e)](https://d3js.org/)
  [![PostgreSQL](https://img.shields.io/badge/DB-PostgreSQL-6598c3)](https://www.postgresql.org/)
  [![DataTables](https://img.shields.io/badge/Tables-DataTables-397ed3)](https://datatables.net/)
  [![JavaScript](https://img.shields.io/badge/Code-JavaSript-orange)](https://developer.mozilla.org/es/docs/Web/JavaScript)
  [![JQuery](https://img.shields.io/badge/Code-JQuery-0769ad)](https://jquery.com/) 

</div>

## Indice

- [Sistema de Inventario](#sistema-de-inventario)
  - [Descripción](#descripción)
     - [Tecnologías](#tecnologías)
  - [Dominio](#dominio)
     - [Usuario](#usuario)
     - [Categoría](#categoría)
     - [Producto](#producto)
     - [Cliente](#cliente)
     - [Venta](#venta)
     - [Descripción de la Venta](#descripción-de-la-venta)
  - [Funciones](#funciones)
  - [Autor](#autor)
     - [Contacto](#contacto)
  - [Licencia de Uso](#licencia-de-uso)
 
## Descripción
Prototipo para generar micro servicios a travez de un relato de usuario utilizando el Procesamiento del Lenguaje Natural. Funciones Principales:
- Ingresar un relato de usuario utilizando, una caja de texto, subir un archivo de text, reconocimiento de voz(voz a texto).
- Encontrar las acciones del relato del usuario.
- Transformar las acciones en Historias de Usuario.
- Agrupar las Historias de Usuario relacionadas para crear un microservicio.
- Calcular la posible dependencia que existe entre los microservicios.
- Cada Historia de Usuario se representa como un nodo y cada microservicio como una caja de las continiene, las historias de usuario relacionadas se conectan mediante links.
   
### Tecnologías

- Lenguaje del lado del Servidor: [Python](https://www.python.org/) - Interactuar con la base de datos, gestionar las peticiones del usuario.
- Web Framework: [Django](https://www.djangoproject.com/) - Facilitar el desarrollo web.
- Visualización de Información: [D3js](https://d3js.org/) - Graficar, agrupar y presentar la posible dependencia que existe entre los micoservicios.
- Base de Datos: [PostgreSQL](https://www.postgresql.org/) - Almacenar el relato del usuario, las historias de usuario y las acciones.
- Interacción con la Interfaz: [Java](https://www.java.com/es/) y [JQuery](https://jquery.com/) - Agregar comportamiento a los componentes de la UI.
- Cuadros de Confirmación: [jquery-confirm](https://craftpip.github.io/jquery-confirm/) - Cuadros de dialogos animados para confirmar procesos.
- Iconos: [Font Awesome](https://fontawesome.com/) - Mejorar la experiencia de usuario.
- Dashboard: [AdminLTE](https://adminlte.io/) - Plantilla para el Panel de Administración.
- Tablas de Información: [DataTables](https://datatables.net/) - Facilita la presentación e interación con la información, utilizando tablas responsivas.
- Framework de Diseño: [Bootstrap 5](https://getbootstrap.com/docs/5.0/getting-started/introduction/) - Facilitar una interfaz agradable y responsiva.
- Alertas personalizadas: [SweetAlert2](https://sweetalert2.github.io/) - Cuadros de alertas responsivos y llamativos.
  
## Dominio

Cualquier usuario puede acceder a las funcionalidades del sistema. 
- Un usuario ingresa su problema o relato acerda del sistema que quiere construir, utilizando una caja de texto, cargar un archivo de texto o hablando.
- El relato del usuario es procesado para generar las posibles acciones.
- Cada acción es filtrada y confirmada por el usuario para que puedan ser convertidas en Historias de Usuario.
- Las Historias de Usuario pueden ser ordenadas de acuerdo a una prioridad.
- Las Historias de Usuario que tengan mas relación se agrupan para formar un Microservicio.
- Estos microservicios pueden tener dependencia con otros.

### Relato de Usuario

| Campo         | Tipo    | Descripción        |
|---------------|---------|--------------------|
| id            | UUID    | Identificar único  |
| relatoUsuario | Varchar | Relato del Usuario |

### Historia de Usuario

| Campo     | Tipo    | Descripción                         |
|-----------|---------|-------------------------------------|
| id        | UUID    | Identificador único                 |
| actor     | Varchar | Actor de la Historia de Usuario     |
| accion    | Varchar | Acción de la Historia de Usuario    |
| proposito | Varchar | Propósito de la Historia de Usuario |

### Acción

| Campo    | Tipo     | Descripción                  |
|----------|----------|------------------------------|
| id       | UUID     | Identificar único            |
| actor    | Varchar  | Actor de la acción           |
| que      | Varchar  | El qué de la acción          |
| para_que | Varchar  | El objetivo de la acción     |
| grupo    | Integer  | Número de Grupo de la acción |
| nombre   | Varchar  | Nombre de la acción          |
| aux      | Auxiliar | Auxiliar de la acción        |

## Funciones
<table>
  
  <tr>
    <td width="50%">
      <h3 align="center">Iniciar Sesión</h3>
      <div align="center">
        <img src="https://raw.githubusercontent.com/bnphony/Sistema-Inventario/master/proyecto1/static/img/login.PNG" width="80%" alt="Login">
        <p>
          - Un Usuario puede iniciar sesión con su nombre de usuario y contraseña.
        </p>
      </div>
    </td>
    <td width="50%">
      <h3 align="center">Restablecer Contraseña</h3>
      <div align="center">
        <img src="https://raw.githubusercontent.com/bnphony/Sistema-Inventario/master/proyecto1/static/img/reset_password.PNG" width="80%" alt="Reset Password">
        <p>
          - Un Usuario puede cambiar su contraseña utilizando su nombre nombre de usuario, con esto se le envía un link a su email con el procedimiento correspondiente.
        </p>
      </div>
    </td>
  
  <tr>
    <td witdh="100%" colspan="2">
      <h3 align="center">Gestionar Categorías</h3>
      <div align="center">
        <img src="https://raw.githubusercontent.com/bnphony/Sistema-Inventario/master/proyecto1/static/img/categorias.PNG" width="80%" alt="Categories">
        <p>
          - Crear, actualizar, listar, eliminar categorías.
        </p>
      </div>
    </td>
  </tr>
  
  <tr>
    <td width="100%" colspan="2">
      <h3 align="center">Gestionar Productos</h3>
      <div align="center">
        <img src="https://raw.githubusercontent.com/bnphony/Sistema-Inventario/master/proyecto1/static/img/productos.PNG" width="80%" alt="Products">
        <p>
          - Crear, actualizar, listar, eliminar productos.
        </p>
      </div>
    </td>
  </tr>
  
  <tr>
    <td width="100%" colspan="2">
      <h3 align="center">Gestionar Clientes</h3>
      <div align="center">
        <img src="https://raw.githubusercontent.com/bnphony/Sistema-Inventario/master/proyecto1/static/img/clientes.PNG" width="80%" alt="Clients">
        <p>
          - Crear, actualizar, listar, eliminar clientes.
        </p>
      </div>
    </td>
  </tr>
  
  <tr>
    <td width="100%" colspan="2">
      <h3 align="center">Gestionar Ventas</h3>
      <div align="center">
        <img src="https://raw.githubusercontent.com/bnphony/Sistema-Inventario/master/proyecto1/static/img/ventas.PNG" width="80%" alt="Sales">
        <p>
          - Crear, actualizar, listar, eliminar ventas.          
        </p>
        <br/>
        <img src="https://raw.githubusercontent.com/bnphony/Sistema-Inventario/master/proyecto1/static/img/detalle_venta.PNG" width="80%" alt="Sales">
        <p>
          - Descripción de la venta: productos vendidos, cliente, fecha de la venta, subtotal, IVA y precio total.   
        </p>
      </div>
    </td>
  </tr>
  
  <tr>
    <td witdh="100%" colspan="2">
      <h3 align="center">Generación de Reportes de Ventas</h3>
      <div align="center">
        <img src="https://raw.githubusercontent.com/bnphony/Sistema-Inventario/master/proyecto1/static/img/date_picker.PNG" width="40%" alt="Date Range">
        <img src="https://raw.githubusercontent.com/bnphony/Sistema-Inventario/master/proyecto1/static/img/reporte.PNG" width="40%" alt="Report">
        <p>
          - El usuario puede escoger el rango de fecha de los reportes.
          - Opciones para descargar el reporte en formato excel o pdf.
        </p>
      </div>
    </td>
  </tr>
  
  <tr>
    <td width="100%" colspan="2">
      <h3 align="center">Gestionar Usuarios</h3>
      <div align="center">
        <img src="https://raw.githubusercontent.com/bnphony/Sistema-Inventario/master/proyecto1/static/img/usuarios.PNG" width="80%" alt="Users">
        <p>
          - Crear, actualizar, listar, eliminar usuarios. <br/>
          - Solo los usuarios de tipo administrador pueden acceder a esta opción.
        </p>
      </div>
    </td>
  </tr>
  
</table>


## Autor
Creado por [Universidad Técnica de Cotopaxi](https://www.utc.edu.ec/), codificado por [Bryan Jhoel Tarco Taipe](https://github.com/bnphony)

### Contacto
<a href="https://www.linkedin.com/in/bryan-tarco01" rel="noopener noreferrer" target="_blank">
  <img align="center" src="https://github.com/bnphony/Portafolio/blob/deployed/static/img/linkedin_icon.png" alt="LinkedIn" height="40" width="40" />
</a>
<a href="https://github.com/bnphony" rel="noopener noreferrer" target="blank">
  <img align="center" src="https://github.com/bnphony/Portafolio/blob/deployed/static/img/github_icon.png" alt="GitHub" height="40" width="40" />
</a>
<a href="mailto: bryan.tarco01@gmail.com" target="_blank">
  <img align="center" src="https://github.com/bnphony/Portafolio/blob/deployed/static/img/email_icon.png" alt="Email" height="40" width="40" />
</a>



## Licencia de Uso
Este repositorio y todo su contenido está licenciado bajo licencia **Creative Commons**. Por favor si compartes, usas o modificas este proyecto cita a su
autor, y usa las mismas condiciones para su uso docente, formativo o educativo y no comercial.
