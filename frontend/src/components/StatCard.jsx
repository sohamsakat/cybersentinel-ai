import React from 'react';

export default function StatCard({ title, value, subtitle, icon: Icon, color = 'sky', alert = false }) {
  const colorMap = {
    sky: 'text-sky-400 bg-sky-500/10 border-sky-500/30 shadow-[0_0_15px_rgba(56,189,248,0.1)]',
    red: 'text-red-400 bg-red-500/10 border-red-500/30 shadow-[0_0_15px_rgba(239,68,68,0.15)]',
    orange: 'text-orange-400 bg-orange-500/10 border-orange-500/30 shadow-[0_0_15px_rgba(249,115,22,0.1)]',
    emerald: 'text-emerald-400 bg-emerald-500/10 border-emerald-500/30 shadow-[0_0_15px_rgba(16,185,129,0.1)]',
    purple: 'text-purple-400 bg-purple-500/10 border-purple-500/30 shadow-[0_0_15px_rgba(168,85,247,0.1)]',
  };

  const currentStyle = colorMap[color] || colorMap.sky;

  return (
    <div className={`p-4 rounded-xl bg-[#0f172a] border transition-all ${
      alert ? 'border-red-500/50 bg-red-950/10 animate-pulse' : 'border-slate-800 hover:border-slate-700'
    }`}>
      <div className="flex items-center justify-between mb-3">
        <span className="text-xs font-medium text-slate-400">{title}</span>
        <div className={`w-8 h-8 rounded-lg flex items-center justify-center border ${currentStyle}`}>
          {Icon && <Icon className="w-4 h-4" />}
        </div>
      </div>
      <div className="flex items-baseline space-x-2">
        <span className="text-2xl font-bold tracking-tight text-white font-mono">{value}</span>
      </div>
      {subtitle && (
        <div className="mt-1 text-[11px] text-slate-500 flex items-center gap-1 font-mono">
          {subtitle}
        </div>
      )}
    </div>
  );
}
