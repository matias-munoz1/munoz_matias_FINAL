# Seminario - Lista de Inscritos

Este proyecto es una aplicación web desarrollada con **Django** para gestionar la lista de inscritos y las instituciones participantes en un seminario de gastronomía. Incluye funcionalidades para la gestión completa de datos y una API pública para integraciones futuras.

## 🚀 Características

- **Gestión de inscritos:**
  - Crear, listar, editar y eliminar inscritos.
  - Validaciones en los formularios para evitar datos inconsistentes.
  
- **Gestión de instituciones:**
  - Listar todas las instituciones registradas.
  - Consultar detalles de instituciones específicas mediante una API.

- **API pública:**
  - Endpoints para consultar inscritos e instituciones.
  - Respuesta en formato JSON para integraciones.

- **Interfaz moderna:**
  - Diseñada con **Bootstrap 5** para un diseño limpio, profesional y responsivo.

---

## 🛠️ Requisitos del Proyecto

Antes de comenzar, asegúrate de tener instalados los siguientes requisitos:

1. **Python**: Versión 3.8 o superior.
2. **MySQL**: Base de datos utilizada (puedes usar SQLite para desarrollo).
3. **Dependencias del proyecto**: Instaladas desde `requirements.txt`.

---

## ⚙️ Instalación

Sigue estos pasos para ejecutar el proyecto en tu máquina local:

# 1. Clona el repositorio
```bash
git clone https://github.com/matias-munoz1/munoz_matias_FINAL.git
cd munoz_matias_FINAL
```

# 2. Instala las dependencias
```bash
pip install -r requirements.txt
```

# 3. Configura la base de datos en el archivo settings.py o usando un archivo `.env` (opcional)

Ejemplo de configuración en `.env`:

```bash
DEBUG=True
SECRET_KEY=tu_clave_secreta
DATABASE_NAME=DJANGO_SEMINARIO
DATABASE_USER=root
DATABASE_PASSWORD=1234
DATABASE_HOST=localhost
DATABASE_PORT=3306
```

# 4. Aplica las migraciones de la base de datos
```bash
python manage.py makemigrations
python manage.py migrate
```

# 5. Ejecuta el servidor
```bash
python manage.py runserver
```

# 6. Accede a la aplicación en tu navegador
```bash
URL: http://127.0.0.1:8000
```

