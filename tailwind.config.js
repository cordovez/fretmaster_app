/** @type {import('tailwindcss').Config} */
const defaultTheme = require('tailwindcss/defaultTheme')
module.exports = {
  content: ["templates/**/*.html"],
  theme: {
    extend: {
     
      fontFamily: {
        Playfair: ['"Playfair Display"', defaultTheme.fontFamily.serif],
        Music: ['"Noto Music"', defaultTheme.fontFamily.sans]
}
    },
  },
  plugins: [],
};
