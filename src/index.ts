import express, { Request, Response } from "express";

const app = express();
const puerto = 3000;

app.use(express.json());

interface Libro {
  id: number;
  titulo: string;
  autor: string;
  prestado: boolean;
}

let libros: Libro[] = [
  {
    id: 1,
    titulo: "Dracula",
    autor: "Bram Stoker",
    prestado: false
  },
  {
    id: 2,
    titulo: "Frankenstein",
    autor: "Mary Shelley",
    prestado: true
  },
  {
    id: 3,
    titulo: "El Resplandor",
    autor: "Stephen King",
    prestado: false
  },
  {
    id: 4,
    titulo: "It",
    autor: "Stephen King",
    prestado: true
  }
];


// Ruta principal
app.get("/", (req: Request, res: Response) => {
  res.status(200).json({
    mensaje: "API de Biblioteca Digital funcionando"
  });
});


// GET: listar todos los libros
app.get("/books", (req: Request, res: Response) => {
  res.status(200).json(libros);
});


// POST: agregar un libro
app.post("/books", (req: Request, res: Response) => {

  if (!req.is("application/json")) {
    return res.status(400).json({
      mensaje: "El cuerpo debe enviarse en formato JSON"
    });
  }

  const { titulo, autor, prestado } = req.body;

  if (!titulo || !autor || typeof prestado !== "boolean") {
    return res.status(400).json({
      mensaje: "Titulo, autor y prestado son obligatorios"
    });
  }

  const nuevoLibro: Libro = {
    id: libros.length + 1,
    titulo: titulo,
    autor: autor,
    prestado: prestado
  };

  libros.push(nuevoLibro);

  return res.status(201).json({
    mensaje: "Libro agregado correctamente",
    libro: nuevoLibro
  });
});


// PUT: modificar un libro
app.put("/books/:id", (req: Request, res: Response) => {

  const id = Number(req.params.id);

  const libro = libros.find(
    libro => libro.id === id
  );

  if (!libro) {
    return res.status(404).json({
      mensaje: "Libro no encontrado"
    });
  }

  if (!req.is("application/json")) {
    return res.status(400).json({
      mensaje: "El cuerpo debe enviarse en formato JSON"
    });
  }

  const { titulo, autor, prestado } = req.body;

  if (!titulo || !autor || typeof prestado !== "boolean") {
    return res.status(400).json({
      mensaje: "Titulo, autor y prestado son obligatorios"
    });
  }

  libro.titulo = titulo;
  libro.autor = autor;
  libro.prestado = prestado;

  return res.status(200).json({
    mensaje: "Libro actualizado correctamente",
    libro: libro
  });
});


// DELETE: eliminar un libro
app.delete("/books/:id", (req: Request, res: Response) => {

  const id = Number(req.params.id);

  const posicion = libros.findIndex(
    libro => libro.id === id
  );

  if (posicion === -1) {
    return res.status(404).json({
      mensaje: "Libro no encontrado"
    });
  }

  const libroEliminado = libros[posicion];

  libros.splice(posicion, 1);

  return res.status(200).json({
    mensaje: "Libro eliminado correctamente",
    libro: libroEliminado
  });
});


// GET: funcion de aptitud
app.get("/health/fitness", (req: Request, res: Response) => {

  const totalLibros = libros.length;

  const librosPrestados = libros.filter(
    libro => libro.prestado === true
  ).length;

  let ratioPrestados = 0;

  if (totalLibros > 0) {
    ratioPrestados = librosPrestados / totalLibros;
  }

  const capacidadCorrecta = totalLibros <= 100;
  const ratioCorrecto = ratioPrestados < 0.80;

  if (capacidadCorrecta && ratioCorrecto) {

    return res.status(200).json({
      estado: "Healthy",
      totalLibros: totalLibros,
      librosPrestados: librosPrestados,
      ratioPrestados: ratioPrestados
    });
  }

  return res.status(503).json({
    estado: "Degradacion de Calidad",
    totalLibros: totalLibros,
    librosPrestados: librosPrestados,
    ratioPrestados: ratioPrestados
  });
});


app.listen(puerto, () => {
  console.log(`Servidor funcionando en http://localhost:${puerto}`);
});