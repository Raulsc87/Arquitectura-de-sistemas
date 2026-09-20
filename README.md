# Tarea 03 - API en Django

## Información

- **Estudiante:** Raúl Soto
- **Curso:** Arquitectura de Sistemas
- **Rama:** `hw-03`

## Descripción

En esta práctica se creó una API utilizando Django y Django REST Framework.

El proyecto permite administrar información de usuarios, clientes, productos, ventas y proveedores. También se crearon las migraciones necesarias para guardar la estructura de los modelos.

No se necesita configurar una base de datos externa porque el proyecto utiliza SQLite.

## Aplicaciones creadas

El proyecto contiene cinco aplicaciones:

1. **Usuarios**
   - Permisos
   - Roles
   - Usuarios

2. **Clientes**
   - Clientes
   - Direcciones
   - Contactos

3. **Productos**
   - Categorías
   - Productos
   - Inventarios

4. **Ventas**
   - Ventas
   - Detalles de venta
   - Pagos

5. **Proveedores**
   - Proveedores
   - Compras
   - Detalles de compra

## Características

Todos los modelos tienen:

- Un identificador UUID.
- Fecha de creación.
- Fecha de modificación.
- Eliminación lógica.
- Diferentes tipos de datos.
- Relaciones con otros modelos.

La eliminación lógica permite ocultar un registro sin borrarlo completamente de la base de datos.

## Cómo ejecutar el proyecto

### 1. Clonar el repositorio

```powershell
git clone https://github.com/Raulsc87/Arquitectura-de-sistemas.git
cd Arquitectura-de-sistemas
```

### 2. Cambiar a la rama de la tarea

```powershell
git switch hw-03
```

### 3. Crear el entorno virtual

```powershell
py -m venv .venv
```

### 4. Activar el entorno virtual

```powershell
.\.venv\Scripts\Activate.ps1
```

Si PowerShell no permite activarlo, ejecutar:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
.\.venv\Scripts\Activate.ps1
```

### 5. Instalar lo necesario

```powershell
python -m pip install -r requirements.txt
```

### 6. Aplicar las migraciones

```powershell
python manage.py migrate
```

### 7. Iniciar el proyecto

```powershell
python manage.py runserver
```

Después, abrir en el navegador:

```text
http://127.0.0.1:8000/api/
```

## Direcciones de la API

Desde la página principal se puede ingresar a las siguientes direcciones:

- `/api/permisos/`
- `/api/roles/`
- `/api/usuarios/`
- `/api/clientes/`
- `/api/direcciones/`
- `/api/contactos/`
- `/api/categorias/`
- `/api/productos/`
- `/api/inventarios/`
- `/api/ventas/`
- `/api/detalles-venta/`
- `/api/pagos/`
- `/api/proveedores/`
- `/api/compras/`
- `/api/detalles-compra/`

## Funcionamiento

La API permite:

- Consultar información.
- Agregar nuevos registros.
- Modificar registros.
- Aplicar la eliminación lógica.

## Migraciones

Se crearon las migraciones iniciales de las cinco aplicaciones.

También se realizó un cambio posterior en la aplicación de productos:

- Se agregó el campo `stock_maximo`.
- Se modificó el campo `precio`.

Para revisar las migraciones se puede utilizar:

```powershell
python manage.py showmigrations
```

## Comprobar el proyecto

Para comprobar que no existen errores:

```powershell
python manage.py check
```

Si aparece el siguiente mensaje, significa que todo está correcto:

```text
System check identified no issues (0 silenced).
```