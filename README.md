<div align="center">
  
  # Procesamiento del Lenguaje Natural
</div>

<div align="center">
  <img src="https://raw.githubusercontent.com/bnphony/Procesamiento-Lenguaje-Natural/master/prueba_2/static/img/general.PNG" width="80%" alt="Main Screen">
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

- [Procesamiento del Lenguaje Natural](#procesamiento-del-lenguaje-natural)
  - [Descripción](#descripción)
     - [Tecnologías](#tecnologías)
  - [Dominio](#dominio)
     - [Relato de Usuario](#relato-de-usuario)
     - [Historia de Usuario](#historia-de-usuario)
     - [Acción](#acción)
  - [Funciones](#funciones)
  - [Autor](#autor)
     - [Contacto](#contacto)
  - [Licencia de Uso](#licencia-de-uso)
 
## Descripción
Prototipo para generar micro servicios a través de un relato de usuario utilizando el Procesamiento del Lenguaje Natural. Funciones Principales:
- Ingresar un relato de usuario utilizando: una caja de texto, subir un archivo de texto, utilizar el micrófono, o subir un archivo de audio.
- Encontrar las Historias de Usuario en base al relato ingresado.
- Transformar las Historias de Usuario en funciones con su prioridad respectiva.
- Agrupar las Historias de Usuario relacionadas para crear un micro servicio.
- Calcular la posible dependencia que existe entre los micro servicios.
- Cada Historia de Usuario se representa como un nodo y cada micro servicio como una caja de las contiene, las historias de usuario relacionadas se conectan mediante links.
   
### Tecnologías

- Lenguaje del lado del Servidor: [Python](https://www.python.org/) - Interactuar con la base de datos, gestionar las peticiones del usuario.
- Web Framework: [Django](https://www.djangoproject.com/) - Facilitar el desarrollo web.
- Visualización de Información: [D3js](https://d3js.org/) - Gráfica, agrupa y presenta la posible dependencia que existe entre los Micro servicios.
- Base de Datos: [PostgreSQL](https://www.postgresql.org/) - Almacenar el relato del usuario, las historias de usuario y las acciones.
- Interacción con la Interfaz: [Java](https://www.java.com/es/) y [JQuery](https://jquery.com/) - Agregar comportamiento a los componentes de la UI.
- Cuadros de Confirmación: [jquery-confirm](https://craftpip.github.io/jquery-confirm/) - Cuadros de diálogos animados para confirmar procesos.
- Iconos: [Font Awesome](https://fontawesome.com/) - Mejorar la experiencia de usuario.
- Dashboard: [AdminLTE](https://adminlte.io/) - Plantilla para el Panel de Administración.
- Tablas de Información: [DataTables](https://datatables.net/) - Facilita la presentación e interacción con la información, utilizando tablas responsivas.
- Framework de Diseño: [Bootstrap 5](https://getbootstrap.com/docs/5.0/getting-started/introduction/) - Facilitar una interfaz agradable y responsiva.
- Alertas personalizadas: [SweetAlert2](https://sweetalert2.github.io/) - Cuadros de alertas responsivos y llamativos.
  
## Dominio

Cualquier usuario puede acceder a las funcionalidades del sistema. 
- Un usuario ingresa su problema o relato acerca del sistema que quiere construir, utilizando una caja de texto, cargar un archivo de texto/audio o hablando.
- El relato del usuario es procesado para generar las posibles historias de usuario.
- Cada historia de usuario es filtrada y confirmada por el usuario para que puedan ser convertidas en funciones.
- Las funciones pueden ser ordenadas de acuerdo a la prioridad.
- Las Historias de Usuario que tengan mas relación se agrupan para formar un Micro servicio.
- Estos Micro servicios pueden tener dependencia con otros.

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
    <td width="100%">
      <h3 align="center">Ingresar el relato del Usuario</h3>
      <div align="center">
        <img src="https://raw.githubusercontent.com/bnphony/Procesamiento-Lenguaje-Natural/master/prueba_2/static/img/relato_usuario.PNG" width="80%" alt="User Story">
        <p>
          - Pantalla Principal donde el usuario puede ingresar todos los requerimientos que necesite para su proyecto. Esto en formato de historia normal, sin reglas ni restricciones.
        </p>
      </div>
    </td>
  </tr>
  
  <tr>
    <td witdh="100%">
      <h3 align="center">Opciones para ingresar el relato del Usuario</h3>
      <div align="center">
        <img src="https://raw.githubusercontent.com/bnphony/Procesamiento-Lenguaje-Natural/master/prueba_2/static/img/opciones_ingreso.PNG" width="80%" alt="Input Options">
        <p>
          - Formas de ingresar el relato del usuario: 1) Caja de Texto, 2) Utilizar el micrófono para grabar la voz del usuario, 3) Subir un archivo de texto, 4) Subir un archivo de audio (.mp3).
        </p>
      </div>
    </td>
  </tr>
  
  <tr>
    <td width="100%">
      <h3 align="center">Historias de Usuario Encontradas</h3>
      <div align="center">
        <img src="https://raw.githubusercontent.com/bnphony/Procesamiento-Lenguaje-Natural/master/prueba_2/static/img/hu.PNG" width="80%" alt="UH Founded">
        <p>
          - Presentación de las Historias de Usuario encontradas en base al relato ingresado.<br/>
          - El usuario puede eliminar las que tengan errores o que no esten correctas de acuerdo a su critério.
        </p>
      </div>
    </td>
  </tr>
  
  <tr>
    <td width="100%">
      <h3 align="center">Product Backlog</h3>
      <div align="center">
        <img src="https://raw.githubusercontent.com/bnphony/Procesamiento-Lenguaje-Natural/master/prueba_2/static/img/backlog.PNG" width="80%" alt="Product Backlog">
        <p>
          - Lista de funciones creadas en base a las Historias de Usuario aceptadas por el usuario. <br/>
          - El usuario puede arrastras cada función para cambiar su prioridad.
        </p>
      </div>
    </td>
  </tr>
  
  <tr>
    <td width="100%">
      <h3 align="center">Grafico de los Micro Servicios y su posible Dependencia</h3>
      <div align="center">
        <img src="https://raw.githubusercontent.com/bnphony/Procesamiento-Lenguaje-Natural/master/prueba_2/static/img/microservicios.PNG" width="80%" alt="Micro Services">
        <p>
          - Mostrar los posibles Micro servicios y su dependencia encontrados por el sistema en base al relato del usuario.
        </p>
        <br/>
        <img src="https://raw.githubusercontent.com/bnphony/Procesamiento-Lenguaje-Natural/master/prueba_2/static/img/opciones_relato.PNG" width="80%" alt="UH Information">
        <p>
          - Al hacer click sobre una Historia de Usuario(nodo), se abre un cuadro de diálogo con su nombre, descripción y dependencias. <br/>
          - Para una mejor visualización de las conexiones(links) los nodos pueden ser arrastrados momentaneamente.
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
