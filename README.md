# Explorando las Capacidades de Automatización de Pruebas con Selenium en Python

## Objetivo

El objetivo de este proyecto es investigar y adquirir conocimientos prácticos sobre la automatización de pruebas utilizando Selenium WebDriver con Python. Se abordan desde la configuración del entorno de desarrollo hasta la implementación de técnicas avanzadas, permitiendo validar la funcionalidad de aplicaciones web de manera automatizada.

## 1. Introducción a Selenium

Selenium es un framework de código abierto utilizado para automatizar la interacción con navegadores web. Permite simular acciones de usuario como clics, ingreso de texto y navegación entre páginas, lo que resulta esencial para la realización de pruebas funcionales, de regresión y de aceptación. Entre sus componentes destaca Selenium WebDriver, que actúa como puente entre el script en Python y el navegador, utilizando controladores (drivers) específicos para cada navegador (por ejemplo, ChromeDriver para...

## 2. Configuración del Entorno

### 2.1 Instalación de Python

- Descargar desde [python.org](https://www.python.org/downloads/)
- Verificar instalación:

```bash
python --version
# o
python3 --version
```

### 2.2 Crear un Entorno Virtual

#### En Windows:
```bash
python -m venv selenium_env
selenium_env\Scripts\activate
```

#### En macOS/Linux:
```bash
python3 -m venv selenium_env
source selenium_env/bin/activate
```

### 2.3 Instalación de Selenium

```bash
pip install selenium
```

### 2.4 Descargar y Configurar WebDriver

- Descargar [ChromeDriver](https://sites.google.com/chromium.org/driver/)
- Windows: colocar en `C:\WebDriver\` y agregar al PATH
- macOS/Linux:

```bash
sudo mv chromedriver /usr/local/bin
sudo chmod +x /usr/local/bin/chromedriver
```

### 2.5 Verificación del Entorno

```python
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.google.com")
time.sleep(3)
driver.quit()
```

## 3. Primeros Pasos con Selenium en Python

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://www.google.com")

search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Selenium WebDriver")
search_box.send_keys(Keys.RETURN)

time.sleep(3)
driver.quit()
```

## 4. Identificación de Elementos

```python
driver.find_element(By.ID, "username")
driver.find_element(By.NAME, "email")
driver.find_element(By.CLASS_NAME, "btn-primary")
driver.find_element(By.CSS_SELECTOR, "input[type='text']")
driver.find_element(By.XPATH, "//div[@class='form-group']/input[1]")
```

## 5. Manejo de Esperas

### Implícita:
```python
driver.implicitly_wait(10)
```

### Explícita:
```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

wait = WebDriverWait(driver, 10)
elemento = wait.until(EC.visibility_of_element_located((By.ID, "login-button")))
```

## 6. Elementos Dinámicos

```python
wait.until(EC.element_to_be_clickable((By.ID, "boton-dinamico"))).click()
```

```python
from selenium.webdriver.common.action_chains import ActionChains
menu = driver.find_element(By.ID, "menu")
ActionChains(driver).move_to_element(menu).perform()
```

## 7. Múltiples Navegadores

### Chrome:
```python
driver = webdriver.Chrome()
```

### Firefox:
```python
from selenium.webdriver.firefox.service import Service as FirefoxService
driver = webdriver.Firefox(service=FirefoxService())
```

### Edge:
```python
from selenium.webdriver.edge.service import Service as EdgeService
driver = webdriver.Edge(service=EdgeService())
```

## 8. Manejo de Ventanas y Frames

### Ventanas:
```python
ventanas = driver.window_handles
driver.switch_to.window(ventanas[1])
```

### Frames:
```python
driver.switch_to.frame("frame_name")
driver.switch_to.default_content()
```

## 9. Pruebas Avanzadas (POM, JS, Cookies)

### Page Object Model:

```python
class LoginPage:
    def __init__(self, driver):
        self.driver = driver
    def login(self, user, pwd):
        self.driver.find_element(By.ID, "username").send_keys(user)
        self.driver.find_element(By.ID, "password").send_keys(pwd)
        self.driver.find_element(By.ID, "loginBtn").click()
```

### JavaScript:
```python
driver.execute_script("alert('Hola desde Selenium!');")
```

### Cookies:
```python
cookies = driver.get_cookies()
driver.delete_all_cookies()
```

## 10. Informes y Logs

### Logging:
```python
import logging
logging.basicConfig(level=logging.INFO)
logging.info("Inicio de sesión exitoso")
```

### pytest-html:
```bash
pip install pytest-html
pytest --html=report.html
```
