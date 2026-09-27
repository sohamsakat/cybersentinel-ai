import React, { useState, useEffect } from 'react';
import { Shield, Lock, User, ArrowRight, AlertCircle, Sparkles } from 'lucide-react';
import { loginUser } from '../api/client';

export default function Login({ onLoginSuccess }) {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);
  const [mounted, setMounted] = useState(false);

  useEffect(() => {
    // Trigger entrance animation after mount
    const t = setTimeout(() => setMounted(true), 50);
    return () => clearTimeout(t);
  }, []);

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
    <div className="min-h-screen bg-[#050507] flex flex-col justify-center items-center px-4 relative overflow-hidden">
      {/* Animated Background Grid */}
      <div className="absolute inset-0 bg-[linear-gradient(to_right,#27272a25_1px,transparent_1px),linear-gradient(to_bottom,#27272a25_1px,transparent_1px)] bg-[size:4rem_4rem] pointer-events-none" />

      {/* Animated Glow Blobs */}
      <div className="absolute w-96 h-96 bg-[#C10230]/8 rounded-full blur-3xl pointer-events-none -top-20 -left-20 animate-float" />
      <div className="absolute w-72 h-72 bg-white/5 rounded-full blur-3xl pointer-events-none -bottom-20 -right-20 animate-float delay-300" style={{ animationDuration: '4s' }} />
      <div className="absolute w-48 h-48 bg-[#C10230]/5 rounded-full blur-2xl pointer-events-none bottom-1/3 left-1/4 animate-float delay-500" style={{ animationDuration: '5s' }} />

      {/* Subtle animated scan line */}
      <div
        className="absolute left-0 right-0 h-px bg-gradient-to-r from-transparent via-white/10 to-transparent pointer-events-none"
        style={{ animation: 'scanline 6s linear infinite', top: 0 }}
      />

      <div
        className={`w-full max-w-md relative z-10 transition-all duration-700 ease-out ${
          mounted ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-8'
        }`}
      >
        {/* Brand Header */}
        <div className="text-center mb-8">
          {/* Floating animated shield */}
          <div className="inline-flex items-center justify-center w-16 h-16 rounded-2xl bg-white/10 border border-white/20 text-white mb-4 shadow-sm animate-float relative"
               style={{ animationDuration: '3.5s' }}>
            <Shield className="w-9 h-9" />
            {/* Radar ping around shield */}
            <span className="absolute inset-0 rounded-2xl animate-radar-ping border border-white/20" />
          </div>

          <h1
            className={`text-2xl font-bold tracking-tight text-white flex items-center justify-center gap-2 transition-all duration-700 delay-100 ${
              mounted ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-4'
            }`}
          >
            CYBERSENTINEL{' '}
            <span className="text-xs px-2 py-0.5 rounded bg-[#C10230]/20 text-[#ff4d6d] font-mono border border-[#C10230]/40 animate-border-pulse">
              AI SOC
            </span>
          </h1>
          <p
            className={`text-xs text-zinc-400 mt-1 font-mono transition-all duration-700 delay-200 ${
              mounted ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-4'
            }`}
          >
            Intelligent SOC Assistant using RAG &amp; LLMs
          </p>
        </div>

        {/* Login Card */}
        <div
          className={`bg-[#111114]/95 backdrop-blur-md border border-zinc-800 p-8 rounded-2xl shadow-2xl transition-all duration-700 delay-200 card-hover ${
            mounted ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-6'
          }`}
        >
          <form onSubmit={handleSubmit} className="space-y-4">
            <div className={`transition-all duration-500 delay-300 ${mounted ? 'opacity-100 translate-x-0' : 'opacity-0 -translate-x-4'}`}>
              <label className="text-xs font-semibold text-zinc-300 block mb-1.5 font-mono">
                OPERATOR USERNAME
              </label>
              <div className="relative group">
                <div className="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none text-zinc-500 group-focus-within:text-white transition-colors">
                  <User className="w-4 h-4" />
                </div>
                <input
                  type="text"
                  required
                  value={username}
                  onChange={(e) => setUsername(e.target.value)}
                  placeholder="analyst or admin"
                  className="w-full pl-9 pr-3 py-2.5 bg-[#09090b] border border-zinc-800 rounded-xl text-xs text-white placeholder-zinc-500 focus:outline-none focus:border-white focus:ring-1 focus:ring-white/10 font-mono transition-all duration-200"
                />
              </div>
            </div>

            <div className={`transition-all duration-500 delay-400 ${mounted ? 'opacity-100 translate-x-0' : 'opacity-0 -translate-x-4'}`}>
              <label className="text-xs font-semibold text-zinc-300 block mb-1.5 font-mono">
                SECURITY PASSPHRASE
              </label>
              <div className="relative group">
                <div className="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none text-zinc-500 group-focus-within:text-white transition-colors">
                  <Lock className="w-4 h-4" />
                </div>
                <input
                  type="password"
                  required
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                  placeholder="••••••••"
                  className="w-full pl-9 pr-3 py-2.5 bg-[#09090b] border border-zinc-800 rounded-xl text-xs text-white placeholder-zinc-500 focus:outline-none focus:border-white focus:ring-1 focus:ring-white/10 font-mono transition-all duration-200"
                />
              </div>
            </div>

            {error && (
              <div className="p-3 bg-[#C10230]/10 border border-[#C10230]/40 rounded-xl text-xs text-[#ff4d6d] flex items-center gap-2 animate-slide-in-right">
                <AlertCircle className="w-4 h-4 shrink-0 text-[#ff4d6d]" />
                <span>{error}</span>
              </div>
            )}

            <div className={`transition-all duration-500 delay-500 ${mounted ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-3'}`}>
              <button
                type="submit"
                disabled={isLoading}
                className="w-full py-2.5 px-4 rounded-xl bg-white hover:bg-zinc-200 text-black text-xs font-bold tracking-wide transition-all duration-200 shadow-sm flex items-center justify-center space-x-2 disabled:opacity-50 active:scale-[0.97] hover:scale-[1.01] hover:shadow-[0_0_20px_rgba(255,255,255,0.15)]"
              >
                <span>{isLoading ? 'Authenticating...' : 'Authenticate Operator'}</span>
                <ArrowRight className={`w-3.5 h-3.5 transition-transform ${isLoading ? 'animate-spin' : 'group-hover:translate-x-1'}`} />
              </button>
            </div>
          </form>

          {/* 1-Click Demo Login Shortcuts */}
          <div className={`mt-6 pt-5 border-t border-zinc-800/80 transition-all duration-500 delay-600 ${mounted ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-3'}`}>
            <div className="text-[11px] font-mono text-zinc-400 mb-2.5 flex items-center gap-1.5 font-semibold">
              <Sparkles className="w-3.5 h-3.5 text-amber-400 animate-float" style={{ animationDuration: '2s' }} />
              1-Click Demo Credentials:
            </div>
            <div className="grid grid-cols-2 gap-2">
              <button
                type="button"
                onClick={() => handleQuickLogin('analyst', 'analyst123')}
                className="px-3 py-2 rounded-lg bg-[#09090b] border border-zinc-800 hover:border-zinc-500 hover:bg-[#111114] text-left transition-all duration-200 text-zinc-300 hover:scale-[1.02] active:scale-95 card-hover"
              >
                <div className="text-[11px] font-semibold text-white">Tier-1 Analyst</div>
                <div className="text-[10px] font-mono text-zinc-500">analyst / analyst123</div>
              </button>

              <button
                type="button"
                onClick={() => handleQuickLogin('admin', 'admin123')}
                className="px-3 py-2 rounded-lg bg-[#09090b] border border-zinc-800 hover:border-zinc-500 hover:bg-[#111114] text-left transition-all duration-200 text-zinc-300 hover:scale-[1.02] active:scale-95 card-hover"
              >
                <div className="text-[11px] font-semibold text-zinc-300">SOC Admin</div>
                <div className="text-[10px] font-mono text-zinc-500">admin / admin123</div>
              </button>
            </div>
          </div>
        </div>

        {/* Footer */}
        <div className={`mt-6 text-center text-[11px] text-zinc-500 font-mono space-y-1 transition-all duration-500 delay-700 ${mounted ? 'opacity-100' : 'opacity-0'}`}>
          <div>MITRE ATT&CK v14 • NIST SP 800-61 • OWASP Top 10 Grounded</div>
          <div>B.Tech Final Year Engineering Project • CyberSentinel AI</div>
        </div>
      </div>
    </div>
  );
}
