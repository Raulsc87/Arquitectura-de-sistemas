# Tarea 02 - Documentación de API con Swagger

API de videojuegos desarrollada con TypeScript, Node.js y Express.

Esta versión agrega documentación automática con Swagger.

## Requisitos

- Node.js
- npm

## Instalación

Instalar dependencias:

```bash
npm install
```

Ejecutar el proyecto:

```bash
npm run dev
```

## Direcciones

API:

```text
http://localhost:3000
```

Documentación Swagger:

```text
http://localhost:3000/docs
```

## Endpoints

| Método | Ruta | Descripción |
|---|---|---|
| GET | `/juegos` | Mostrar todos los juegos |
| GET | `/juegos/:id` | Buscar un juego |
| POST | `/juegos` | Crear un juego |
| PUT | `/juegos/:id` | Actualizar un juego |
| DELETE | `/juegos/:id` | Eliminar un juego |

## Autor

José Raúl Soto Cal  
Carné: 202308084