/** @type {import('tailwindcss').Config} */
module.exports = {
    content: [
      "./src/**/*.{html,ts}",
    ],
    theme: {
      extend: {
        animation: {
          
        },
        colors: {
          'primary': '#93cba3',
          'secondary':'#333333',
          'orange': '#f5bc62',
          'gray': '#aaaaaa',
          'dark': '#111111',
          'goldish': '#946515'
        },
        backgroundImage: {
          'hero-pattern': "url('/assets/business-analyst-background.png')"
        }
      },
    },
    plugins: [],
  }