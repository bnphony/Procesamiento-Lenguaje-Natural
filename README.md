<div align="center">
  
  # Procesamiento del Lenguaje Natural
</div>

<div align="center">
  <img src="https://raw.githubusercontent.com/bnphony/Sistema-Inventario/master/proyecto1/static/img/general.PNG" width="80%" alt="Main Screen">
  <br/><br/>
  
  ![GitHub](https://img.shields.io/github/last-commit/bnphony/Sistema-Inventario)
  [![Django](https://img.shields.io/badge/Framework-Django-green)](https://www.djangoproject.com/)
  [![Python](https://img.shields.io/badge/Code-Python-fd81f)](https://www.python.org/)
  [![DataTables](https://img.shields.io/badge/Tables-DataTables-397ed3)](https://datatables.net/)
  [![Bootstrap 5](https://img.shields.io/badge/Framework-Bootstrap%205-7952b3)](https://getbootstrap.com/docs/5.0/getting-started/introduction/)
  [![PostgreSQL](https://img.shields.io/badge/DB-PostgreSQL-6598c3)](https://www.postgresql.org/)
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
- Ingresar un relato de usuario utilizando, una caja de texto, subir un archivo de text .txt, reconocimiento de voz.
- Gestionar Usuarios.
- Gestionar Categorías.
- Gestionar Productos.
- Gestionar Clientes.
- Gestionar Ventas.
- Generar reportes de ventas.
- Exportar en formato Excel y PDF los reportes de ventas.
- Visualizar el porcentaje de ventas utilizando gráficos de barras y de sectores (pastel).

   
### Tecnologías

- Lenguaje del lado del Servidor: [Python](https://www.python.org/) - Interactuar con la base de datos, gestionar las peticiones del usuario.
- Web Framework: [Django](https://www.djangoproject.com/) - Facilitar el desarrollo web.
- Interacción con la Interfaz: [Java](https://www.java.com/es/) y [JQuery](https://jquery.com/) - Agregar comportamiento a los componentes de la UI.
- Cuadros de Confirmación: [jquery-confirm](https://craftpip.github.io/jquery-confirm/) - Cuadros de dialogos animados para confirmar procesos.
- Iconos: [Font Awesome](https://fontawesome.com/) - Mejorar la experiencia de usuario.
- Dashboard: [AdminLTE](https://adminlte.io/) - Plantilla para el Panel de Administración.
- Tablas de Información: [DataTables](https://datatables.net/) - Facilita la presentación e interación con la información, utilizando tablas responsivas.
- Selección de Fechas: [DateRangePicker](https://www.daterangepicker.com/) - Mejorar la experiencia del usuario al ingresar fechas en los formularios.
- Framework de Diseño: [Bootstrap 5](https://getbootstrap.com/docs/5.0/getting-started/introduction/) - Facilitar una interfaz agradable y responsiva.
- Caja de Selección: [Select2](https://select2.org/) - Facilitar la presentación de información en las cajas de selección.
  
## Dominio

Gestionar usuarios, categorías, productos, clientes, ventas, generar reportes.
- Solo un usuario con privilegios de administrador puede crear nuevos usuarios, desde dentro del sistema.
- Los usuarios pueden iniciar sesión, restablecer su contraseña, editar su perfil.
- Un usuario puede crear, actualizar, listar, eliminar categorías.
- Un usuario puede crear, actualizar, listar, eliminar productos, cada productos pertenece a una categoría.
- Un usuario puede crear, actualizar, listar, eliminar clientes.
- Un usuario puede crear, actualizar, listar, eliminar, imprimir en pdf las ventas.
- Cada venta contiene información sobre los productos vendidos y sobre el cliente que compra dichos productos.
- Un usuario puede generar reportes de las ventas acorde a un rango de fechas y exportarlos en formato excel o pdf.

### Usuario

| Campo      | Tipo    | Descripción                 |
|------------|---------|-----------------------------|
| id         | UUID    | Identificar único           |
| image      | Varchar | Imagen del Usuario          |
| token      | UUID    | Token de Acceso del Usuario |
| username   | Varchar | Nombre de Usuario           |
| first_name | Varchar | Primer Nombre del Usuario   |
| last_name  | Varchar | Apellido del Usuario        |
| email      | Varchar | Email del Usuario           |
| password   | Varchar | Contraseña del Usuario      |

### Categoría

| Campo         | Tipo    | Descripción                 |
|---------------|---------|-----------------------------|
| id            | UUID    | Identificar único           |
| nombre        | Varchar | Nombre de la Categoría      |
| desc          | Varchar | Descripción de la Categoría |
| user_creation | Usuario | Usuario de la Categoría     |

### Producto

| Campo  | Tipo      | Descripción            |
|--------|-----------|------------------------|
| id     | UUID      | Identificar único      |
| nombre | Varchar   | Nombre del Producto    |
| image  | Varchar   | Imagen del Producto    |
| stock  | Integer   | Cantidad del Producto  |
| pvp    | Decimal   | Precio del Producto    |
| cat    | Categoría | Categoría del Producto |

### Cliente

| Campo         | Tipo     | Descripción                     |
|---------------|----------|---------------------------------|
| id            | UUID     | Identificar único               |
| nombres       | Varchar  | Nombres del Cliente             |
| apellidos     | Varchar  | Apellidos del Cliente           |
| dni           | Varchar  | Cédula del Cliente              |
| date_birthday | DateTime | Fecha de Nacimiento del Cliente |
| address       | Varchar  | Dirección del Cliente           |
| gender        | Varchar  | Género del Cliente              |

### Venta

| Campo       | Tipo     | Descripción                  |
|-------------|----------|------------------------------|
| id          | UUID     | Identificar único            |
| date_joined | DateTime | Fecha de Creación            |
| subtotal    | Decimal  | Precio Sub-total de la Venta |
| iva         | Decimal  | IVA de la Venta              |
| total       | Decimal  | Precio Total de la Venta     |
| cli         | Cliente  | Cliente de la Venta          |

### Descripción de la Venta

| Campo    | Tipo     | Descripción                                     |
|----------|----------|-------------------------------------------------|
| id       | UUID     | Identificar único                               |
| price    | Decimal  | Precio del Producto                             |
| cant     | Integer  | Cantidad a vender                               |
| subtotal | Decimal  | Precio Sub-total de la venta de este producto/s |
| sale     | Venta    | Venta de la Descripción de la Venta             |
| prod     | Producto | Producto de la Descripción de la Venta          |

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
Codificado por [Bryan Jhoel Tarco Taipe](https://github.com/bnphony), basado en el tutorial [Curso de Django3](https://youtu.be/XclfcvFjN48?si=cKXKIUnwvoaoEQpc) por [William Jair Dávila Vargas](https://algorisoft.com/)

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
Este repositorio y todo su contenido está licenciado bajo licencia **Creative Commons**. Por favor si compartes, usas o modificas este proyecto cita a sus
autores, y usa las mismas condiciones para su uso docente, formativo o educativo y no comercial.
