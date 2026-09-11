import React from 'react';
import { LayoutDashboard, AlertTriangle, FileUp, MessageSquareCode, ShieldCheck, Database, Radio } from 'lucide-react';

export default function Sidebar({ activeTab, setActiveTab }) {
  const navItems = [
    { id: 'radar', label: 'Live Cyber Radar', icon: Radio, badge: 'LIVE' },
    { id: 'dashboard', label: 'SOC Dashboard', icon: LayoutDashboard },
    { id: 'incidents', label: 'Incidents & Triage', icon: AlertTriangle },
    { id: 'logs', label: 'Log Ingestion', icon: FileUp },
    { id: 'copilot', label: 'SecOps AI Copilot', icon: MessageSquareCode },
  ];

  return (
    <aside className="w-64 bg-[#0a0f1a] border-r border-cyber-border flex flex-col justify-between p-4 min-h-[calc(100vh-4rem)]">
      <div className="space-y-6">
        <div className="text-[11px] font-mono tracking-wider text-slate-500 uppercase px-3">
          SOC Operations
        </div>

        <nav className="space-y-1.5">
          {navItems.map((item) => {
            const Icon = item.icon;
            const isActive = activeTab === item.id;
            return (
              <button
                key={item.id}
                onClick={() => setActiveTab(item.id)}
                className={`w-full flex items-center space-x-3 px-3.5 py-2.5 rounded-lg text-xs font-medium transition-all ${
                  isActive
                    ? 'bg-sky-500/10 text-sky-400 border border-sky-500/30 font-semibold shadow-[0_0_12px_rgba(56,189,248,0.15)]'
                    : 'text-slate-400 hover:text-slate-200 hover:bg-slate-900/60 border border-transparent'
                }`}
              >
                <Icon className={`w-4 h-4 ${isActive ? 'text-sky-400' : 'text-slate-400'}`} />
                <span className="flex-1 text-left">{item.label}</span>
                {item.badge && (
                  <span className="px-1.5 py-0.2 rounded text-[9px] font-mono font-bold bg-emerald-500/20 text-emerald-400 border border-emerald-500/30 animate-pulse">
                    {item.badge}
                  </span>
                )}
              </button>
            );
          })}
        </nav>

        <div className="pt-4 border-t border-slate-800/80">
          <div className="text-[11px] font-mono tracking-wider text-slate-500 uppercase px-3 mb-2">
            Threat Intelligence
          </div>
          <div className="px-3 py-2.5 rounded-lg bg-[#0f172a] border border-slate-800/80 text-xs space-y-2">
            <div className="flex items-center justify-between text-slate-300">
              <span className="flex items-center gap-1.5 text-[11px]">
                <ShieldCheck className="w-3.5 h-3.5 text-emerald-400" />
                MITRE ATT&CK
              </span>
              <span className="font-mono text-[10px] text-emerald-400 font-semibold">v14 Active</span>
            </div>
            <div className="flex items-center justify-between text-slate-300">
              <span className="flex items-center gap-1.5 text-[11px]">
                <Database className="w-3.5 h-3.5 text-sky-400" />
                ChromaDB Vector
              </span>
              <span className="font-mono text-[10px] text-sky-400 font-semibold">Ready</span>
            </div>
          </div>
        </div>
      </div>

      <div className="p-3 bg-slate-900/40 rounded-lg border border-slate-800 text-[11px] text-slate-500">
        <div className="flex justify-between items-center text-slate-400 mb-1">
          <span>Engine Status</span>
          <span className="text-emerald-400 font-mono">NOMINAL</span>
        </div>
        <div className="text-[10px] font-mono text-slate-500">
          Latency: 14ms | Memory: 32MB
        </div>
      </div>
    </aside>
  );
}
