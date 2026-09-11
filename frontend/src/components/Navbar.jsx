import React from 'react';
import { Shield, ShieldAlert, LogOut, User as UserIcon, Upload, Terminal } from 'lucide-react';

export default function Navbar({ currentUser, onLogout, onOpenUpload }) {
  return (
    <header className="h-16 bg-[#0c121e] border-b border-cyber-border px-6 flex items-center justify-between sticky top-0 z-30">
      {/* Brand & SOC Status */}
      <div className="flex items-center space-x-4">
        <div className="flex items-center space-x-2.5">
          <div className="w-9 h-9 rounded-lg bg-sky-500/10 border border-sky-500/30 flex items-center justify-center text-sky-400 shadow-[0_0_15px_rgba(56,189,248,0.25)]">
            <Shield className="w-5 h-5" />
          </div>
          <div>
            <span className="font-bold text-base tracking-wide text-white flex items-center gap-1.5">
              CYBERSENTINEL <span className="text-xs px-1.5 py-0.5 rounded bg-sky-500/20 text-sky-400 font-mono border border-sky-500/30">AI SOC</span>
            </span>
            <span className="text-[10px] text-slate-400 block -mt-0.5 font-mono">MITRE ATT&CK Grounded Engine</span>
          </div>
        </div>

        <div className="hidden md:flex items-center space-x-2 bg-slate-900/80 px-3 py-1 rounded-full border border-slate-800 text-xs text-slate-300">
          <span className="w-2 h-2 rounded-full bg-emerald-500 animate-ping" />
          <span className="font-mono text-emerald-400">TELEMETRY STREAM: LIVE</span>
        </div>
      </div>

      {/* Actions & User Profile */}
      <div className="flex items-center space-x-4">
        <button
          onClick={onOpenUpload}
          className="flex items-center space-x-2 bg-sky-600 hover:bg-sky-500 text-white text-xs font-semibold px-3.5 py-2 rounded-lg transition-all shadow-[0_0_15px_rgba(2,132,199,0.3)] border border-sky-400/30 active:scale-95"
        >
          <Upload className="w-3.5 h-3.5" />
          <span>Ingest Logs</span>
        </button>

        <div className="h-6 w-px bg-slate-800" />

        <div className="flex items-center space-x-3">
          <div className="w-8 h-8 rounded-full bg-slate-800 border border-slate-700 flex items-center justify-center text-slate-300">
            <UserIcon className="w-4 h-4" />
          </div>
          <div className="hidden sm:block text-left">
            <div className="text-xs font-semibold text-white leading-tight">
              {currentUser?.username || 'Analyst'}
            </div>
            <div className="text-[10px] text-sky-400 font-mono capitalize">
              {currentUser?.role?.replace('_', ' ') || 'Tier-1 Analyst'}
            </div>
          </div>
        </div>

        <button
          onClick={onLogout}
          title="Logout"
          className="text-slate-400 hover:text-red-400 p-2 rounded-lg hover:bg-slate-800/50 transition-colors"
        >
          <LogOut className="w-4 h-4" />
        </button>
      </div>
    </header>
  );
}
