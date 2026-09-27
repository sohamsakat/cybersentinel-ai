import React from 'react';

export default function SeverityBadge({ severity }) {
  const upper = (severity || 'LOW').toUpperCase();

  const styles = {
    CRITICAL: 'bg-[#C10230]/15 text-[#ff4d6d] border-[#C10230]/50 shadow-[0_0_12px_rgba(193,2,48,0.25)] hover:shadow-[0_0_18px_rgba(193,2,48,0.4)]',
    HIGH: 'bg-amber-950/30 text-amber-400 border-amber-800/50 shadow-[0_0_10px_rgba(245,158,11,0.15)] hover:shadow-[0_0_16px_rgba(245,158,11,0.3)]',
    MEDIUM: 'bg-[#154372]/25 text-sky-300 border-[#154372]/60 hover:shadow-[0_0_12px_rgba(21,67,114,0.3)]',
    LOW: 'bg-emerald-950/30 text-emerald-400 border-emerald-800/50 hover:shadow-[0_0_12px_rgba(16,185,129,0.25)]',
    INFO: 'bg-zinc-900 text-zinc-300 border-zinc-700',
  };

  const badgeClass = styles[upper] || styles.LOW;

  return (
    <span className={`inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-semibold font-mono tracking-wider border transition-all duration-300 hover:scale-105 cursor-default ${badgeClass}`}>
      <span className={`w-1.5 h-1.5 rounded-full mr-1.5 transition-all ${
        upper === 'CRITICAL' ? 'bg-[#ff4d6d] animate-ping' :
        upper === 'HIGH' ? 'bg-amber-400 animate-pulse' :
        upper === 'MEDIUM' ? 'bg-sky-400' : 'bg-emerald-400'
      }`} />
      {upper}
    </span>
  );
}
