# Pruebas para el parámetro nombre al crear un kit de usuario en UrbanGrocers
>PyCharm se utilizará para generar la autimización de las pruebas.
>Necesitas tener instalados los paquetes pytest y request para ejecutar las pruebas.
>Ejecutar todos los tests con el comando pytest.


## Proyecto Sprint 7: Introducción a la Automatización de Pruebas
En este proyecto, automatizamos las pruebas relacionadas con la función de creación de kits. Validamos el campo nombre implementando código Python: datos y métodos GET,POST.
Objetivos:
- Uso de GitHub.
- Automatización de pruebas con PyTest

## Tecnologías y técnicas utilizadas.

- Conectado a la cuenta de GitHub de TripleTen para clonar localmente el repositorio del proyecto.
- Trabajado localmente a través de PyCharm
- Instaladas las librerías requests y pytest.
- La dirección HTTP y las rutas para enviar las peticiones se configuraron en el archivo configuration.py.
- El archivo data.py contiene los cuerpos para generar el usuario.
- Se desarrollaron los métodos POST y GET para enviar y obtener datos para la creación de un KIt para Urban.Grocers.
- Se automatizó la lectura y modificación del cuerpo de la petición, para enviar datos variables y probar el campo nombre de la funcionalidad de creación de kits.
- Se crearon funciones de prueba positivas y negativas utilizando pytest.
- Se ejecutaron un total de 9 pruebas

_________________________________________________
### Comandos y Rutas utilizadas.

| Rutas de la API |
|-----------------|
| /api/v1/users/  |
| /api/v1/kits    |

| Usuario y Kit      | Comando                 |
|--------------------|-------------------------|
| Token para Usuario | get_new_user_token      |
| Crear un Kit       | get_new_user_token      |

| Códigos de Respuesta | 
|----------------------|
| positive_assert      |
| negative_assert      |

| Lista de Comprobación             | 
|-----------------------------------|
| positive_assert                   |
| negative_assert                   |
| test_only_one_character           |
| test_allow_number_of_characters   |
| test_characters_under_allowed     |
| test_characters_above_the_allowed |
| test_especial_characters_allowed  |
| test_spaces_are_allowed           |
| test_numbers_are_allowed          |
| test_dont_pass_without_characters |
| test_diferent_parameter           |