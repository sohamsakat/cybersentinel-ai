/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        nexbank: {
          crimson: '#C10230',
          crimsonDark: '#9E0025',
          crimsonGlow: 'rgba(193, 2, 48, 0.35)',
          navy: '#154372',
          navyDark: '#0e2b4a',
          black: '#050507',
          canvas: '#09090b',
          surface: '#111114',
          card: '#18181b',
          border: '#27272a',
          borderHover: '#3f3f46',
        },
        cyber: {
          bg: '#050507',
          surface: '#09090b',
          card: '#111114',
          border: '#27272a',
          borderHover: '#3f3f46',
          text: '#fafafa',
          muted: '#a1a1aa',
          accent: '#ffffff',
          neonBlue: '#ffffff',
          critical: '#C10230',
          high: '#f59e0b',
          medium: '#154372',
          low: '#10b981',
          purple: '#a1a1aa',
        }
      },
      fontFamily: {
        mono: ['JetBrains Mono', 'Fira Code', 'monospace'],
        sans: ['Inter', 'system-ui', 'sans-serif'],
      }
    },
  },
  plugins: [],
}
