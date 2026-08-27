/** @type {import('tailwindcss').Config} */
export default {
  // Le decimos a Tailwind en qué archivos buscar clases de estilo.
  content: ["./index.html", "./src/**/*.{ts,tsx}"],
  theme: {
    extend: {
      // Paleta del juego (los colores que pediste).
      colors: {
        verde: "#2e7d5b",
        azul: "#3a6ea5",
        madera: "#6b5b3a",
        maderaOscura: "#7a5c2e",
        crema: "#efe6d0",
        crema2: "#e5d8b8",
        facil: "#2e7d5b",
        media: "#d98a2b",
        dificil: "#c0392b",
        tinta: "#2b2b2b",
      },
    },
  },
  plugins: [],
};
