import express, { Request, Response } from "express";

const app = express();
const puerto = 3000;

app.use(express.json());

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

// GET: mostrar todos los juegos
app.get("/juegos", (req: Request, res: Response) => {
  res.status(200).json(juegos);
});

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