import React, { useState } from 'react';
import { Shield, Lock, User, ArrowRight, AlertCircle, Sparkles, Terminal } from 'lucide-react';
import { loginUser } from '../api/client';

export default function Login({ onLoginSuccess }) {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleSubmit = async (e) => {
    e?.preventDefault();
    setIsLoading(true);
    setError(null);
    try {
      const data = await loginUser(username, password);
      localStorage.setItem('cybersentinel_token', data.access_token);
      localStorage.setItem('cybersentinel_user', JSON.stringify({ username: data.username, role: data.role }));
      onLoginSuccess({ username: data.username, role: data.role });
    } catch (err) {
      setError(err.response?.data?.detail || 'Authentication failed. Please check credentials.');
    } finally {
      setIsLoading(false);
    }
  };

  const handleQuickLogin = async (user, pass) => {
    setUsername(user);
    setPassword(pass);
    setIsLoading(true);
    setError(null);
    try {
      const data = await loginUser(user, pass);
      localStorage.setItem('cybersentinel_token', data.access_token);
      localStorage.setItem('cybersentinel_user', JSON.stringify({ username: data.username, role: data.role }));
      onLoginSuccess({ username: data.username, role: data.role });
    } catch (err) {
      setError('Quick login failed. Ensure the backend server is running.');
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-[#080c14] flex flex-col justify-center items-center px-4 relative overflow-hidden">
      {/* Background Cyber Grid Lines */}
      <div className="absolute inset-0 bg-[linear-gradient(to_right,#1e293b15_1px,transparent_1px),linear-gradient(to_bottom,#1e293b15_1px,transparent_1px)] bg-[size:4rem_4rem] pointer-events-none" />
      <div className="absolute w-96 h-96 bg-sky-500/10 rounded-full blur-3xl pointer-events-none -top-20 -left-20" />
      <div className="absolute w-96 h-96 bg-indigo-500/10 rounded-full blur-3xl pointer-events-none -bottom-20 -right-20" />

      <div className="w-full max-w-md relative z-10">
        {/* Brand Header */}
        <div className="text-center mb-8">
          <div className="inline-flex items-center justify-center w-14 h-14 rounded-2xl bg-sky-500/10 border border-sky-500/30 text-sky-400 mb-4 shadow-[0_0_30px_rgba(56,189,248,0.25)]">
            <Shield className="w-8 h-8" />
          </div>
          <h1 className="text-2xl font-bold tracking-tight text-white flex items-center justify-center gap-2">
            CYBERSENTINEL <span className="text-xs px-2 py-0.5 rounded bg-sky-500/20 text-sky-400 font-mono border border-sky-500/30">AI SOC</span>
          </h1>
          <p className="text-xs text-slate-400 mt-1 font-mono">
            Intelligent SOC Assistant using RAG & LLMs
          </p>
        </div>

        {/* Login Card */}
        <div className="bg-[#0f172a]/90 backdrop-blur-md border border-slate-800 p-8 rounded-2xl shadow-[0_0_40px_rgba(0,0,0,0.6)]">
          <form onSubmit={handleSubmit} className="space-y-4">
            <div>
              <label className="text-xs font-medium text-slate-300 block mb-1.5 font-mono">
                OPERATOR USERNAME
              </label>
              <div className="relative">
                <div className="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none text-slate-500">
                  <User className="w-4 h-4" />
                </div>
                <input
                  type="text"
                  required
                  value={username}
                  onChange={(e) => setUsername(e.target.value)}
                  placeholder="analyst or admin"
                  className="w-full pl-9 pr-3 py-2.5 bg-slate-900/80 border border-slate-800 rounded-xl text-xs text-white placeholder-slate-500 focus:outline-none focus:border-sky-500 font-mono transition-colors"
                />
              </div>
            </div>

            <div>
              <label className="text-xs font-medium text-slate-300 block mb-1.5 font-mono">
                SECURITY PASSPHRASE
              </label>
              <div className="relative">
                <div className="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none text-slate-500">
                  <Lock className="w-4 h-4" />
                </div>
                <input
                  type="password"
                  required
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                  placeholder="••••••••"
                  className="w-full pl-9 pr-3 py-2.5 bg-slate-900/80 border border-slate-800 rounded-xl text-xs text-white placeholder-slate-500 focus:outline-none focus:border-sky-500 font-mono transition-colors"
                />
              </div>
            </div>

            {error && (
              <div className="p-3 bg-red-950/40 border border-red-800/60 rounded-xl text-xs text-red-300 flex items-center gap-2">
                <AlertCircle className="w-4 h-4 shrink-0 text-red-400" />
                <span>{error}</span>
              </div>
            )}

            <button
              type="submit"
              disabled={isLoading}
              className="w-full py-2.5 px-4 rounded-xl bg-sky-600 hover:bg-sky-500 text-white text-xs font-semibold tracking-wide transition-all shadow-[0_0_20px_rgba(2,132,199,0.3)] flex items-center justify-center space-x-2 disabled:opacity-50 active:scale-[0.98]"
            >
              <span>{isLoading ? 'Authenticating...' : 'Authenticate Operator'}</span>
              <ArrowRight className="w-3.5 h-3.5" />
            </button>
          </form>

          {/* 1-Click Demo Login Shortcuts */}
          <div className="mt-6 pt-5 border-t border-slate-800/80">
            <div className="text-[11px] font-mono text-slate-400 mb-2.5 flex items-center gap-1.5">
              <Sparkles className="w-3.5 h-3.5 text-amber-400" />
              1-Click Demo Credentials:
            </div>
            <div className="grid grid-cols-2 gap-2">
              <button
                type="button"
                onClick={() => handleQuickLogin('analyst', 'analyst123')}
                className="px-3 py-2 rounded-lg bg-slate-900 border border-slate-800 hover:border-sky-500/40 text-left transition-colors text-slate-300"
              >
                <div className="text-[11px] font-semibold text-sky-400">Tier-1 Analyst</div>
                <div className="text-[10px] font-mono text-slate-500">analyst / analyst123</div>
              </button>

              <button
                type="button"
                onClick={() => handleQuickLogin('admin', 'admin123')}
                className="px-3 py-2 rounded-lg bg-slate-900 border border-slate-800 hover:border-purple-500/40 text-left transition-colors text-slate-300"
              >
                <div className="text-[11px] font-semibold text-purple-400">SOC Admin</div>
                <div className="text-[10px] font-mono text-slate-500">admin / admin123</div>
              </button>
            </div>
          </div>
        </div>

        {/* Academic & Framework Accreditation Footer */}
        <div className="mt-6 text-center text-[11px] text-slate-500 font-mono space-y-1">
          <div>MITRE ATT&CK v14 • NIST SP 800-61 • OWASP Top 10 Grounded</div>
          <div>B.Tech Final Year Engineering Project • CyberSentinel AI</div>
        </div>
      </div>
    </div>
  );
}
