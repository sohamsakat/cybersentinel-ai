import React from 'react';

export default function SeverityBadge({ severity }) {
  const upper = (severity || 'LOW').toUpperCase();

  const styles = {
    CRITICAL: 'bg-red-950/80 text-red-400 border-red-800/60 shadow-[0_0_10px_rgba(239,68,68,0.2)]',
    HIGH: 'bg-orange-950/80 text-orange-400 border-orange-800/60 shadow-[0_0_10px_rgba(249,115,22,0.2)]',
    MEDIUM: 'bg-amber-950/80 text-amber-400 border-amber-800/60 shadow-[0_0_10px_rgba(245,158,11,0.2)]',
    LOW: 'bg-emerald-950/80 text-emerald-400 border-emerald-800/60',
    INFO: 'bg-sky-950/80 text-sky-400 border-sky-800/60',
  };

  const badgeClass = styles[upper] || styles.LOW;

  return (
    <span className={`inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-semibold border ${badgeClass}`}>
      <span className={`w-1.5 h-1.5 rounded-full mr-1.5 ${
        upper === 'CRITICAL' ? 'bg-red-400 animate-pulse' :
        upper === 'HIGH' ? 'bg-orange-400' :
        upper === 'MEDIUM' ? 'bg-amber-400' : 'bg-emerald-400'
      }`} />
      {upper}
    </span>
  );
}
