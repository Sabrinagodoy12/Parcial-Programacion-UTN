# Parcial-Programacion-UTN

En este repositorio se encuentra el parcial que debemos desarrollar para la materia Programación 1 de la Tecnicatura Universitaria en programación de la Universidad Tecnológica Nacional

## Enunciado:

La biblioteca escolar necesita un sistema de gestión sencillo para su catálogo de libros y las
copias disponibles. Se pide desarrollar un programa con una interfaz basada en menú que
utilice listas paralelas (una para titulos[] y otra para ejemplares[]). Cada título debe estar
vinculado a su número correspondiente de copias utilizando el mismo índice en ambas listas.
Se debe utilizar un bucle while para navegar por las opciones del menú hasta que el usuario
elija salir.

## Requerimientos del Menú

1. Ingresar títulos → Para agregar los títulos iniciales de los libros, el usuario indica la cantidad inicial.
2. Ingresar ejemplares → Para agregar una cantidad de copias para cada título.
3. Mostrar catálogo → Muestra todos los libros y su stock actual.
4. Consultar disponibilidad → Busca un título específico y muestra cuántos ejemplares hay.
5. Listar agotados → Muestra los títulos que tienen 0 ejemplares.
6. Agregar título → Permite añadir un nuevo libro y sus ejemplares disponibles al catálogo, respetando la sincronía de los índices en las listas.
7. Actualizar ejemplares (préstamo/devolución) → Permite modificar el stock de un libro, elegido por el usuario, para registrar préstamos o devoluciones.

- Préstamo -> Disminuye en 1 la cantidad de ejemplares del libro seleccionado, si hay unidades suficientes.
- Devolución -> Aumenta en 1 la cantidad de ejemplares del libro seleccionado.

8. Salir → Termina la ejecución del programa.

## Requerimientos de estructuras

Debes usar un bucle while para navegar por las opciones del menú hasta que el usuario elija salir. Se debe utilizar una estructura case (o su equivalente con if/elif/else) para el menú, así como estructuras condicionales y secuenciales de Python. Se permiten funciones para validar cadenas de texto como lower(), upper() o isdigit().
