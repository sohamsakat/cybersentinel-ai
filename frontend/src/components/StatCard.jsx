import React, { useEffect, useState } from 'react';

function useCountUp(target, duration = 900) {
  const [count, setCount] = useState(0);
  useEffect(() => {
    if (target === 0) { setCount(0); return; }
    let start = 0;
    const step = Math.ceil(target / (duration / 16));
    const timer = setInterval(() => {
      start += step;
      if (start >= target) { setCount(target); clearInterval(timer); }
      else setCount(start);
    }, 16);
    return () => clearInterval(timer);
  }, [target, duration]);
  return count;
}

export default function StatCard({ title, value, subtitle, icon: Icon, color = 'white', alert = false, delay = 0 }) {
  const animated = useCountUp(typeof value === 'number' ? value : 0);

  const colorMap = {
    white:   'text-white bg-white/10 border-white/20',
    sky:     'text-zinc-200 bg-zinc-900 border-zinc-700',
    red:     'text-[#ff4d6d] bg-[#C10230]/15 border-[#C10230]/40 shadow-[0_0_12px_rgba(193,2,48,0.25)]',
    orange:  'text-amber-400 bg-amber-500/10 border-amber-500/30 shadow-[0_0_12px_rgba(245,158,11,0.15)]',
    emerald: 'text-emerald-400 bg-emerald-500/10 border-emerald-500/30 shadow-[0_0_12px_rgba(16,185,129,0.15)]',
    purple:  'text-zinc-300 bg-zinc-900 border-zinc-700',
  };

  const currentStyle = colorMap[color] || colorMap.white;

  return (
    <div
      className={`p-4 rounded-xl bg-[#111114] border transition-all duration-300 card-hover animate-fade-in-up ${
        alert
          ? 'border-[#C10230]/60 bg-[#C10230]/5 animate-border-pulse'
          : 'border-zinc-800 hover:border-zinc-600 shadow-sm animate-glow-pulse-white'
      }`}
      style={{ animationDelay: `${delay}ms` }}
    >
      <div className="flex items-center justify-between mb-3">
        <span className="text-xs font-semibold tracking-wider text-zinc-400 font-mono uppercase">{title}</span>
        <div className={`w-8 h-8 rounded-lg flex items-center justify-center border transition-transform duration-300 hover:scale-110 hover:rotate-6 ${currentStyle}`}>
          {Icon && <Icon className="w-4 h-4" />}
        </div>
      </div>
      <div className="flex items-baseline space-x-2">
        <span className="text-2xl font-bold tracking-tight text-white font-mono animate-count-up" style={{ animationDelay: `${delay + 100}ms` }}>
          {typeof value === 'number' ? animated : value}
        </span>
      </div>
      {subtitle && (
        <div className="mt-1 text-[11px] text-zinc-400 flex items-center gap-1 font-mono">
          {subtitle}
        </div>
      )}
    </div>
  );
}
