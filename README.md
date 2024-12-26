# Proyecto: Automatización de Extracción de Datos de HorariosRB

Este proyecto utiliza Selenium para automatizar la extracción de datos desde una tabla web interactiva. La aplicación realiza búsquedas en fechas específicas, recopila los datos disponibles y los almacena en un archivo CSV.

## Requisitos

### Software

- Python 3.8 o superior
- Google Chrome (navegador)
- ChromeDriver (compatible con la versión de Chrome instalada)

### Bibliotecas de Python

Instalar las dependencias utilizando `pip`:

```bash
pip install selenium
```

## Configuración

1. Descargar e instalar Google Chrome.
2. Descargar el binario de ChromeDriver correspondiente a la versión de Google Chrome instalada y asegurarse de que esté en el PATH del sistema o en el directorio del proyecto.
3. Configurar las credenciales de acceso en el código:
   ```python
   usuario_input.send_keys("<USUARIO>")
   contraseña_input.send_keys("<CONTRASEÑA>")
   ```

## Estructura del Proyecto

- `Html.py`: Archivo principal que contiene el código de automatización.
- `tabla.csv`: Archivo donde se almacenan los datos extraídos (se crea automáticamente si no existe).

## Funcionalidades

1. **Inicio de sesión automático**: El bot accede a la página web e inicia sesión con las credenciales proporcionadas.
2. **Búsqueda de datos por fecha**: Se realizan búsquedas iterativas para cada día de un mes especificado.
3. **Extracción de datos**: Se extraen los datos visibles de la tabla para cada fecha y se almacenan en un archivo CSV.
4. **Control de datos inexistentes**: Si no hay datos disponibles para una fecha, el bot finaliza la búsqueda.

## Uso

1. Ejecutar el script:
   ```bash
   python Html.py
   ```
2. El script abrirá el navegador, iniciará sesión y comenzará a buscar datos.
3. Los datos extraídos se guardarán en el archivo `tabla.csv` en el directorio del proyecto.
4. Los datos del archivo tabla.csv pueden ser copiados y pegados en columnas en la hoja del mismo nombre en el archivo Turnos RB, para una mejor visualización en la hoja formulada TURNOS



