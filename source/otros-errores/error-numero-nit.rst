Error en número de NIT
======================

Si al intentar guardar una nueva ficha de cliente el sistema muestra el mensaje: "Error en número de NIT"

.. image:: /_static/otros/nit-invalido.png
   :alt: Error en número de NIT

Lo primero es verificar con la tarjeta de contribuyente del cliente que el NIT ingresado sea correcto. Si el NIT es correcto, pero el error persiste significa que tiene que el NIT tiene el código de un municipio nuevo que no ha sido agregado al sistema. Para agregarlo siga los siguientes pasos:

1. Vaya al menú de **Archivos Maestros** y luego **Maestro de municipios para validación de NIT**.

.. image:: /_static/otros/menu-validacion-nit.png
   :alt: Maestro de municipios para validación de NIT

2. Haga clic en **Nuevo** para agregar un nuevo municipio.

.. image:: /_static/otros/modulo-mant-mun-val-nit.png
   :alt: Nuevo municipio

3. En la casilla de **CODIGO** va los 4 primeros dígitos del NIT del cliente (que en el caso de este ejemplo corresponde a 0621) y en la casilla de **MUNICIPIO** va el nombre del nuevo municipio como por ejemplo **SAN SALVADOR CENTRO**.

4. Haga clic en **Guardar** para finalizar la creación del nuevo municipio.

Luego de seguir estos pasos el NIT del cliente debería ser aceptado sin problemas al intentar guardar la ficha del cliente nuevamente.

.. important:: 

   Si el módulo de **MAESTRO DE MUNICIPIOS PARA VALIDACIÓN DE NIT** no se muestra en el menú de archivos maestros, favor de contactar al administrador del sistema.


