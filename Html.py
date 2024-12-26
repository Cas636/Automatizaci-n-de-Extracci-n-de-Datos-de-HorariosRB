from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import time


mes = "01"
año = 2025
# Iniciar el navegador
driver = webdriver.Chrome()

# Abrir la página de inicio de sesión
driver.get("https://andromeda.rbsas.co/malla/search")

# Esperar a que los campos estén disponibles
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "username"))
)

# Encontrar los campos de usuario y contraseña
usuario_input = driver.find_element(By.NAME, "username")
contraseña_input = driver.find_element(By.NAME, "password")

# Ingresar el usuario y la contraseña
usuario_input.send_keys("<USUARIO>")
contraseña_input.send_keys("<CONTRASEÑA>")

# Encontrar el botón de "Ingresar" y hacer clic
boton_ingresar = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
boton_ingresar.click()

driver.implicitly_wait(5)
# Encuentra el enlace "Malla" y haz clic en él
malla_link = driver.find_element(By.XPATH, "//a[contains(@href, '/malla')]")
malla_link.click()

# Esperar a que la tabla esté cargada (opcional, dependiendo de la página)

driver.implicitly_wait(5)

# Selecciona el campo de mes y asigna diciembre (por ejemplo, 2024-12 para diciembre de 2024)
mes_input = driver.find_element(By.NAME, "mes")
mes_input.send_keys(mes)  # Establece diciembre de 2024
mes_input.send_keys(Keys.TAB)
mes_input.send_keys(año) 

# Encuentra el botón de búsqueda y haz clic en él
buscar_button = driver.find_element(By.CLASS_NAME, "btn-primary")
buscar_button.click()


driver.implicitly_wait(15)
time.sleep(3)


# Extraer y guardar datos en CSV
csv_file = 'tabla.csv'
# Abrir el archivo CSV en modo append para agregar datos sin sobrescribir
with open(csv_file, mode='a', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    
    # Inicializar encabezados solo si el archivo está vacío
    if file.tell() == 0:
        rows = driver.find_elements(By.CLASS_NAME, 'tabulator-row')
        headers = []
        if rows:
            first_row_cells = rows[0].find_elements(By.CLASS_NAME, 'tabulator-cell')
            headers = [cell.get_attribute('tabulator-field') for cell in first_row_cells]
            writer.writerow(headers)
    
    # Extraer datos 
    for i in range(1, 32, 1):
        # Encuentra el botón de fecha y escribe la fecha
        input_fecha = driver.find_element(By.CSS_SELECTOR, '.tabulator-header-filter input[type="date"]')
        input_fecha.send_keys(i)  # Establece diciembre de 2024
        input_fecha.send_keys(Keys.TAB)
        input_fecha.send_keys(mes) 
        input_fecha.send_keys(año)
        
        input_search = driver.find_element(By.CSS_SELECTOR, '.tabulator-header-filter input[type="search"]')
        input_search.clear()  # Limpia el campo de búsqueda antes de enviar texto
        input_search.send_keys("")  # Enviar búsqueda vacía si aplica
        time.sleep(2)  # Esperar para que se actualicen los datos
        
        # Extraer filas de la tabla
        rows = driver.find_elements(By.CLASS_NAME, 'tabulator-row')
        
        # Verificar si no hay datos en la tabla
        if not rows:
            print(f"No hay datos para la fecha {año}-{mes}-{i}. Cerrando búsqueda.")
            break
        
        # Extraer datos de las filas
        data = []
        for row in rows:
            cells = row.find_elements(By.CLASS_NAME, 'tabulator-cell')
            row_data = [cell.text.strip() for cell in cells]
            data.append(row_data)
        
        # Escribir los datos extraídos
        writer.writerows(data)

# Cerrar el navegador
driver.quit()
