# Assessment 01 - Biblioteca Digital

API REST básica desarrollada con TypeScript, Node.js y Express.

## Funcionalidades

- GET /books
- POST /books
- PUT /books/:id
- DELETE /books/:id
- GET /health/fitness

## Función de Aptitud

El endpoint:

GET /health/fitness

valida dos condiciones:

1. El total de libros no debe exceder 100.
2. La relación entre libros prestados y libros totales debe ser menor al 80%.

Si ambas condiciones se cumplen, responde:

200 OK

```json
{
  "estado": "Healthy"
}