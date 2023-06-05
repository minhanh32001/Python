/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.html",
    "./node_modules/flowbite/**/*.js",
    "node_modules/preline/dist/*.js",
  ],
  theme: {
    colors: {
      "primary-color": "#f7ab0a",
      "primary-hover-color": "#F7CC0A",
      "gray-color": "#242424",
      "gray-hover-color": "#4F4F4F",
    },
    extend: {},
  },
  plugins: [require("flowbite/plugin"), require("preline/plugin"), require("daisyui")],
};
