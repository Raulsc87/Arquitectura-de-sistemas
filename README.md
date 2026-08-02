# Tarea 01 - API de videojuegos en TypeScript

API sencilla desarrollada con TypeScript, Node.js y Express.

## Métodos implementados

- GET
- POST
- PUT
- DELETE

## Requisitos

- Node.js
- npm

## Instalación

Instalar las dependencias:

```bash
npm install
```

Ejecutar el proyecto:

```bash
npm run dev
```

La API estará disponible en:

```text
http://localhost:3000
```

## Endpoints

| Método | Ruta | Descripción |
|---|---|---|
| GET | `/juegos` | Mostrar todos los juegos |
| GET | `/juegos/:id` | Buscar un juego por ID |
| POST | `/juegos` | Crear un juego |
| PUT | `/juegos/:id` | Actualizar un juego |
| DELETE | `/juegos/:id` | Eliminar un juego |

## Ejemplo para POST

```json
{
  "nombre": "Mortal Kombat 1",
  "genero": "Peleas",
  "precio": 450
}
```

## Códigos de respuesta

- `200`: operación correcta.
- `201`: juego creado.
- `400`: datos incompletos.
- `404`: juego no encontrado.

## Autor

José Raúl Soto Cal  
Carné: 202308084
