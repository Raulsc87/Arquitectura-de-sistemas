import express, { Request, Response } from "express";
import swaggerUi from "swagger-ui-express";
import swaggerJsdoc from "swagger-jsdoc";

const app = express();

const puerto = 3000;

app.use(express.json());
const opcionesSwagger = {
  definition: {
    openapi: "3.0.0",
    info: {
      title: "API de videojuegos",
      version: "1.0.0",
      description: "Documentación automática de la API de videojuegos"
    },
    servers: [
      {
        url: "http://localhost:3000"
      }
    ]
  },
  apis: ["./src/index.ts"]
};

const documentacionSwagger = swaggerJsdoc(opcionesSwagger);

app.use(
  "/docs",
  swaggerUi.serve,
  swaggerUi.setup(documentacionSwagger)
);

interface Juego {
  id: number;
  nombre: string;
  genero: string;
  precio: number;
}

let juegos: Juego[] = [
  {
    id: 1,
    nombre: "Minecraft",
    genero: "Aventura",
    precio: 250
  },
  {
    id: 2,
    nombre: "FIFA 26",
    genero: "Deportes",
    precio: 500
  }
];

// Ruta principal
app.get("/", (req: Request, res: Response) => {
  res.status(200).json({
    mensaje: "API de videojuegos funcionando"
  });
});

/**
 * @swagger
 * /juegos:
 *   get:
 *     summary: Obtener todos los videojuegos
 *     responses:
 *       200:
 *         description: Lista de videojuegos obtenida correctamente
 */
app.get("/juegos", (req: Request, res: Response) => {
  res.status(200).json(juegos);
});

/**
 * @swagger
 * /juegos/{id}:
 *   get:
 *     summary: Obtener un videojuego por ID
 *     parameters:
 *       - in: path
 *         name: id
 *         required: true
 *         schema:
 *           type: integer
 *     responses:
 *       200:
 *         description: Videojuego encontrado
 *       404:
 *         description: Videojuego no encontrado
 */
// GET: buscar un juego por ID
app.get("/juegos/:id", (req: Request, res: Response) => {
  const id = Number(req.params.id);

  const juego = juegos.find(juego => juego.id === id);

  if (!juego) {
    return res.status(404).json({
      mensaje: "Juego no encontrado"
    });
  }

  return res.status(200).json(juego);
});
/**
 * @swagger
 * /juegos:
 *   post:
 *     summary: Crear un videojuego
 *     requestBody:
 *       required: true
 *       content:
 *         application/json:
 *           schema:
 *             type: object
 *             required:
 *               - nombre
 *               - genero
 *               - precio
 *             properties:
 *               nombre:
 *                 type: string
 *                 example: Mortal Kombat 1
 *               genero:
 *                 type: string
 *                 example: Peleas
 *               precio:
 *                 type: number
 *                 example: 450
 *     responses:
 *       201:
 *         description: Videojuego creado correctamente
 *       400:
 *         description: Datos incompletos
 */
// POST: agregar un juego
app.post("/juegos", (req: Request, res: Response) => {
  const { nombre, genero, precio } = req.body;

  if (!nombre || !genero || precio === undefined) {
    return res.status(400).json({
      mensaje: "El nombre, género y precio son obligatorios"
    });
  }

  const nuevoJuego: Juego = {
    id: juegos.length + 1,
    nombre,
    genero,
    precio
  };

  juegos.push(nuevoJuego);

  return res.status(201).json({
    mensaje: "Juego creado correctamente",
    juego: nuevoJuego
  });
});
/**
 * @swagger
 * /juegos/{id}:
 *   put:
 *     summary: Actualizar un videojuego
 *     parameters:
 *       - in: path
 *         name: id
 *         required: true
 *         schema:
 *           type: integer
 *     requestBody:
 *       required: true
 *       content:
 *         application/json:
 *           schema:
 *             type: object
 *             required:
 *               - nombre
 *               - genero
 *               - precio
 *             properties:
 *               nombre:
 *                 type: string
 *               genero:
 *                 type: string
 *               precio:
 *                 type: number
 *     responses:
 *       200:
 *         description: Videojuego actualizado correctamente
 *       400:
 *         description: Datos incompletos
 *       404:
 *         description: Videojuego no encontrado
 */
// PUT: modificar un juego
app.put("/juegos/:id", (req: Request, res: Response) => {
  const id = Number(req.params.id);
  const { nombre, genero, precio } = req.body;

  const juego = juegos.find(juego => juego.id === id);

  if (!juego) {
    return res.status(404).json({
      mensaje: "Juego no encontrado"
    });
  }

  if (!nombre || !genero || precio === undefined) {
    return res.status(400).json({
      mensaje: "El nombre, género y precio son obligatorios"
    });
  }

  juego.nombre = nombre;
  juego.genero = genero;
  juego.precio = precio;

  return res.status(200).json({
    mensaje: "Juego actualizado correctamente",
    juego
  });
});
/**
 * @swagger
 * /juegos/{id}:
 *   delete:
 *     summary: Eliminar un videojuego
 *     parameters:
 *       - in: path
 *         name: id
 *         required: true
 *         schema:
 *           type: integer
 *     responses:
 *       200:
 *         description: Videojuego eliminado correctamente
 *       404:
 *         description: Videojuego no encontrado
 */
// DELETE: eliminar un juego
app.delete("/juegos/:id", (req: Request, res: Response) => {
  const id = Number(req.params.id);

  const posicion = juegos.findIndex(juego => juego.id === id);

  if (posicion === -1) {
    return res.status(404).json({
      mensaje: "Juego no encontrado"
    });
  }

  const juegoEliminado = juegos[posicion];

  juegos.splice(posicion, 1);

  return res.status(200).json({
    mensaje: "Juego eliminado correctamente",
    juego: juegoEliminado
  });
});

app.listen(puerto, () => {
  console.log(`Servidor funcionando en http://localhost:${puerto}`);
});