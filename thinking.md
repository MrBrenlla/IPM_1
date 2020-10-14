 

# Priority guides

El programa estará formado por dos ventanas:

	-Ventana(Vista) principal: 

		La cual nos mostrará todos los posibles intervalos (sin diferenciar ascendente o descendente).	

	-Ventana(vista) secundaria: 

		A la cual accederemos después de 'pulsar' uno de los intervalos, se nos mostrará:

		 -Ejemplo de dos notas cuya distancia sea la del intervalo (en ascendente y descendente).

		 -Lista de canciones para ambos sentidos del intervalo.



## Vista princial



  * HeaderBar: "Seleccione un intervalo"

  * Action: Indicará al usuario que es lo que tiene que hacer en la ventana.



  * Button: "2m,2M,3m,3M" (Intervalos musicales)

  * Action: Cada propio botón abrirá una ventana secundaria que contendrá lo anteriormente mencionado.



  * FlowBox: Contenedor buttons

  * Action: Nos permitirá colocar los buttons de manera ordenada en la ventana



## Vista secundaria

  

  * Label: Orden del intervalo

  * Action: Nos permitirá indicar el orden intervalo correspondiente (asc o desc) y el conjunto de notas que cumple las condiciones anteriormente mencionadas.



  * Grid: Contenedor de labels y listbox

  * Action: Nos permitirá colocar las labels y listbox adecuadamente en la ventana



  * ListBox: Listas de canciones

  * Action: Contendrán las diferentes canciones para el orden de intervalo correspondiente





# Decisiones

* Hemos decidido mostrar todos los intervalos con botones y sin orden:

	-Con esto limitamos que el usuario tenga que introducir texto en una pantalla.

	-Además, no existen más intervalos músicales de los que ya conocemos y por tanto no se prevee unas actualizaciones futuras al software por esta parte, por tanto concluímos que el uso de los 		botones es adecuado.

	-Con esto no nos tenemos que preocupar de si los nombres son demasiado largos o cortos.

* A la hora de seleccionar un intervalo mostramos tanto el orden ascedente como descendente:

	-Así damos la posibilidad al usuario en todo momento de ver todo lo relacionado a un intervalo específico. (En caso de seleccionar el '2M' podemos ver las notas asc-des + canciones).

* Hemos decidido mostrar toda la lista de canciones para el intervalo:

	-Al tener la lista de canciones podemos hacer click en una canción cualquiera, así tenemos un fácil acceso para visualizar el link en el navegador (en caso de que lo hubiera).

	-Marcaremos en 'negrita' las canciones 'Favoritas'.

	-También se ha decidido 'truncar' el título de las canciones en caso de ser necesario para que quede acorde con la lista.

	
