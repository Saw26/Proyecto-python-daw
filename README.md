# Proyecto-python-daw
Un repositorio para la asignatura de Fundamentos de Python de mi ciclo de Daw.
He subido la calculadora a otra rama pero voy a hacer una app de lista de tareas (sencilla) con 3 objetos o tareas principales ("personales", "laborales" sociales").

Para hacer las funcionalidades me he "inspirado" en nuestra asignatura de servidor en la que estamos trabajando con ficheros y he podido coger ideas, variables, maneras...
He definido las funciones necesarias para agregar una tarea a un ficherito que tendremos con formato "id;nombre;descripcion;prioridad;categoria"; listar todas las tareas que tenemos; buscar una en concreto; modificar algún dato de las tareas que tengamos y claro para borrar tareas y un menú.

He ido poniendo comentarios de los 2 tipos, los docStrings y los de toda la vida!

###  Actualización para la segunda entrega  del proyecto:
-He añadido la funcionalidad de exportar las tareas a un json (concretamente a mi archivo tareas.json) y al revés, importar tareas desde json a mi lista de tareas (mi tareas.txt).
 -He añadido los log que me ha pedido el profesor dentro de los except de mis funciones. -Como actualización extra he metido una clase Tarea y he cambiado la lógica de las funciones, en lugar de trabbajar diréctamente con el fichero trabajan sobre el objeto tarea.

### Actualización para la tercera entrega del proyecto:
 -He modificado la funcionalidad de añadir tareas para que pregunte qué tipo de tarea quiere crear, si normal o completa.
 (teniendo en cuenta que el resto de cosas que se pedían las hice préviamente en el examen):
 
 -He añadido una subclase hija de tareas llamada TareaCompleta con un nuevo atributo llamado "fecha".
 -He añadido métodos para buscar o "filtrar" tareas, por categoría o por palabra clave.
 -He cambiado la estructura de mi .json tal y como se me pidió.
 -He actualizado el menú, modificado las funcionalidades para que guarden un objeto en lugar de trabajar diréctamente con el fichero de tareas.txt.
 -He añadido la funcionalidad de "genera_reporte" que me sirve para ordenar las tareas y para tener un contador de tareas (por categorias y totales).

