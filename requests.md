# Requests de la API

## GET

Obtiene todos los productos.

```http
GET http://127.0.0.1:5000/productos
```

## POST

Agrega un producto.

```http
POST http://127.0.0.1:5000/productos
```

Body JSON:

```json
{
  "nombre": "Monitor",
  "precio": 1200
}
```

## PUT

Modifica el producto con ID 3.

```http
PUT http://127.0.0.1:5000/productos/3
```

Body JSON:

```json
{
  "nombre": "Monitor Gamer",
  "precio": 1500
}
```

## DELETE

Elimina el producto con ID 3.

```http
DELETE http://127.0.0.1:5000/productos/3
```