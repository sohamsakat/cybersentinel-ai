import React from 'react';
import { LayoutDashboard, AlertTriangle, FileUp, MessageSquareCode, ShieldCheck, Database, Radio, Activity } from 'lucide-react';

export default function Sidebar({ activeTab, setActiveTab }) {
  const navItems = [
    { id: 'radar', label: 'Live Cyber Radar', icon: Radio, badge: 'LIVE' },
    { id: 'dashboard', label: 'SOC Dashboard', icon: LayoutDashboard },
    { id: 'incidents', label: 'Incidents & Triage', icon: AlertTriangle },
    { id: 'logs', label: 'Log Ingestion', icon: FileUp },
    { id: 'copilot', label: 'SecOps AI Copilot', icon: MessageSquareCode },
  ];

  return (
    <aside className="w-64 bg-[#09090b] border-r border-zinc-800/80 flex flex-col justify-between p-4 min-h-[calc(100vh-4rem)] select-none">
      <div className="space-y-6">
        <div className="text-[11px] font-mono tracking-wider text-zinc-400 uppercase px-3 font-semibold flex items-center justify-between">
          <span>SOC Operations</span>
          <span className="w-1.5 h-1.5 rounded-full bg-emerald-500 animate-ping" />
        </div>

        <nav className="space-y-1.5">
          {navItems.map((item, idx) => {
            const Icon = item.icon;
            const isActive = activeTab === item.id;
            return (
              <button
                key={item.id}
                onClick={() => setActiveTab(item.id)}
                className={`w-full flex items-center space-x-3 px-3.5 py-2.5 rounded-lg text-xs font-medium transition-all duration-200 group relative overflow-hidden active:scale-95 ${
                  isActive
                    ? 'bg-zinc-900 text-white border border-zinc-700 font-semibold shadow-sm'
                    : 'text-zinc-400 hover:text-white hover:bg-zinc-900/60 hover:translate-x-1 border border-transparent'
                }`}
                style={{ animationDelay: `${idx * 60}ms` }}
              >
                {/* Active indicator bar on left edge */}
                {isActive && (
                  <span className="absolute left-0 top-1.5 bottom-1.5 w-1 bg-[#C10230] rounded-r animate-fade-in" />
                )}

                <Icon className={`w-4 h-4 transition-transform duration-200 group-hover:scale-110 ${
                  isActive ? 'text-white' : 'text-zinc-500 group-hover:text-zinc-300'
                }`} />

                <span className="flex-1 text-left tracking-wide">{item.label}</span>

                {item.badge && (
                  <span className="relative flex items-center">
                    <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-[#C10230] opacity-40" />
                    <span className="px-1.5 py-0.5 rounded text-[9px] font-mono font-bold bg-[#C10230]/20 text-[#ff4d6d] border border-[#C10230]/40 relative z-10">
                      {item.badge}
                    </span>
                  </span>
                )}
              </button>
            );
          })}
        </nav>

        <div className="pt-4 border-t border-zinc-800/80">
          <div className="text-[11px] font-mono tracking-wider text-zinc-400 uppercase px-3 mb-2 font-semibold">
            Threat Intelligence
          </div>
          <div className="px-3 py-2.5 rounded-lg bg-[#111114] border border-zinc-800 text-xs space-y-2 card-hover transition-all duration-300">
            <div className="flex items-center justify-between text-zinc-300 group">
              <span className="flex items-center gap-1.5 text-[11px]">
                <ShieldCheck className="w-3.5 h-3.5 text-emerald-400 transition-transform group-hover:rotate-12" />
                MITRE ATT&CK
              </span>
              <span className="font-mono text-[10px] text-emerald-400 font-semibold px-1.5 py-0.2 rounded bg-emerald-500/10 border border-emerald-500/20">
                v14 Active
              </span>
            </div>
            <div className="flex items-center justify-between text-zinc-300 group">
              <span className="flex items-center gap-1.5 text-[11px]">
                <Database className="w-3.5 h-3.5 text-zinc-300 transition-transform group-hover:scale-110" />
                ChromaDB Vector
              </span>
              <span className="font-mono text-[10px] text-zinc-300 font-semibold px-1.5 py-0.2 rounded bg-white/5 border border-white/10">
                Ready
              </span>
            </div>
          </div>
        </div>
      </div>

      <div className="p-3 bg-[#111114] rounded-lg border border-zinc-800 text-[11px] text-zinc-400 hover:border-zinc-700 transition-colors">
        <div className="flex justify-between items-center text-zinc-300 mb-1">
          <span className="flex items-center gap-1.5">
            <Activity className="w-3.5 h-3.5 text-emerald-400 animate-pulse" />
            Engine Status
          </span>
          <span className="text-emerald-400 font-mono font-semibold flex items-center gap-1">
            <span className="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-ping inline-block" />
            NOMINAL
          </span>
        </div>
        <div className="text-[10px] font-mono text-zinc-500 flex justify-between">
          <span>Latency: 14ms</span>
          <span>Memory: 32MB</span>
        </div>
      </div>
    </aside>
  );
}
