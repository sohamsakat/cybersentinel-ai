import React from 'react';
import { Shield, LogOut, User as UserIcon, Upload } from 'lucide-react';

export default function Navbar({ currentUser, onLogout, onOpenUpload }) {
  return (
    <header className="h-16 bg-[#050507] border-b border-zinc-800/80 px-6 flex items-center justify-between sticky top-0 z-30">
      {/* Brand & SOC Status */}
      <div className="flex items-center space-x-4">
        <div className="flex items-center space-x-2.5">
          <div className="w-9 h-9 rounded-lg bg-white/10 border border-white/20 flex items-center justify-center text-white shadow-sm">
            <Shield className="w-5 h-5" />
          </div>
          <div>
            <span className="font-bold text-base tracking-wide text-white flex items-center gap-1.5">
              CYBERSENTINEL <span className="text-xs px-1.5 py-0.5 rounded bg-[#C10230]/20 text-[#ff4d6d] font-mono border border-[#C10230]/40">AI SOC</span>
            </span>
            <span className="text-[10px] text-zinc-400 block -mt-0.5 font-mono">MITRE ATT&CK Grounded Engine</span>
          </div>
        </div>

        <div className="hidden md:flex items-center space-x-2 bg-zinc-900/90 px-3 py-1 rounded-full border border-zinc-800 text-xs text-zinc-300">
          <span className="w-2 h-2 rounded-full bg-emerald-500 animate-ping" />
          <span className="font-mono text-emerald-400">TELEMETRY STREAM: LIVE</span>
        </div>
      </div>

      {/* Actions & User Profile */}
      <div className="flex items-center space-x-4">
        <button
          onClick={onOpenUpload}
          className="flex items-center space-x-2 bg-white hover:bg-zinc-200 text-black text-xs font-semibold px-3.5 py-2 rounded-lg transition-all border border-white shadow-sm active:scale-95"
        >
          <Upload className="w-3.5 h-3.5" />
          <span>Ingest Logs</span>
        </button>

        <div className="h-6 w-px bg-zinc-800" />

        <div className="flex items-center space-x-3">
          <div className="w-8 h-8 rounded-full bg-zinc-900 border border-zinc-800 flex items-center justify-center text-zinc-300">
            <UserIcon className="w-4 h-4" />
          </div>
          <div className="hidden sm:block text-left">
            <div className="text-xs font-semibold text-white leading-tight">
              {currentUser?.username || 'Analyst'}
            </div>
            <div className="text-[10px] text-zinc-400 font-mono capitalize">
              {currentUser?.role?.replace('_', ' ') || 'Tier-1 Analyst'}
            </div>
          </div>
        </div>

        <button
          onClick={onLogout}
          title="Logout"
          className="text-zinc-400 hover:text-[#ff4d6d] p-2 rounded-lg hover:bg-zinc-900 transition-colors"
        >
          <LogOut className="w-4 h-4" />
        </button>
      </div>
    </header>
  );
}
