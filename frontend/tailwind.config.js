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
        cyber: {
          bg: '#080c14',
          surface: '#0f172a',
          card: '#131d31',
          border: '#1e293b',
          borderHover: '#334155',
          text: '#f8fafc',
          muted: '#94a3b8',
          accent: '#0284c7',
          neonBlue: '#38bdf8',
          critical: '#ef4444',
          high: '#f97316',
          medium: '#f59e0b',
          low: '#10b981',
          purple: '#8b5cf6',
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
