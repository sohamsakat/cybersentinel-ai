import React, { useEffect, useState } from 'react';
import { Upload, CheckCircle2, FileCode, Layers } from 'lucide-react';
import { getLogBatches } from '../api/client';

export default function LogAnalyzer({ onOpenUpload }) {
  const [batches, setBatches] = useState([]);
  const [loading, setLoading] = useState(true);
  const [mounted, setMounted] = useState(false);

  const fetchBatches = async () => {
    try {
      setLoading(true);
      const data = await getLogBatches();
      setBatches(data);
    } catch (err) {
      console.error('Failed to load log batches', err);
    } finally {
      setLoading(false);
      setTimeout(() => setMounted(true), 50);
    }
  };

  useEffect(() => {
    fetchBatches();
  }, []);

  const formats = [
    {
      name: 'Windows Event Viewer',
      ext: '.json',
      desc: 'Security channel events including 4625 (Logon Failure), 4624 (Logon Success), 4672 (Privilege Assignment).',
      badge: 'Active Parser',
    },
    {
      name: 'Linux Syslog / Auth',
      ext: '.log',
      desc: 'RFC 3164 auth.log telemetry capturing SSH invalid user password guessing, PAM failures, and sudo privilege escalation.',
      badge: 'Active Parser',
    },
    {
      name: 'Apache Web Access',
      ext: '.log',
      desc: 'NCSA Combined Log format detecting SQL Injection (UNION SELECT), Directory Traversal (../../), and XSS payload probes.',
      badge: 'Active Parser',
    },
    {
      name: 'Network Perimeter Firewall',
      ext: '.csv',
      desc: 'Tabular packet telemetry tracking TCP SYN flags, port scans across sequential/privileged ports, and DENY drop rules.',
      badge: 'Active Parser',
    },
  ];

  return (
    <div className={`p-6 space-y-6 max-w-7xl mx-auto transition-all duration-500 ${mounted ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-4'}`}>
      {/* Header */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 pb-2 border-b border-zinc-800">
        <div>
          <h1 className="text-xl font-bold tracking-tight text-white flex items-center gap-2 text-shimmer">
            <Layers className="w-5 h-5 text-white" />
            TELEMETRY INGESTION PIPELINE
          </h1>
          <p className="text-xs text-zinc-400 font-mono mt-0.5">
            Heterogeneous Log Normalization into Elastic Common Schema (ECS)
          </p>
        </div>
        <button
          onClick={onOpenUpload}
          className="flex items-center space-x-2 bg-white hover:bg-zinc-200 text-black text-xs font-bold px-4 py-2 rounded-lg transition-all duration-200 border border-white shadow-sm hover:scale-105 active:scale-95 hover:shadow-[0_0_15px_rgba(255,255,255,0.15)]"
        >
          <Upload className="w-3.5 h-3.5" />
          <span>Upload New Log Batch</span>
        </button>
      </div>

      {/* 4 Supported Formats Grid */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
        {formats.map((fmt, idx) => (
          <div
            key={idx}
            className="p-4 rounded-xl bg-[#111114] border border-zinc-800 hover:border-zinc-600 transition-all duration-300 flex flex-col justify-between card-hover animate-fade-in-up"
            style={{ animationDelay: `${idx * 80}ms` }}
          >
            <div>
              <div className="flex items-center justify-between mb-2">
                <span className="font-mono text-xs font-bold text-white flex items-center gap-1.5">
                  <FileCode className="w-3.5 h-3.5 text-zinc-400" />
                  {fmt.name}
                </span>
                <span className="text-[10px] font-mono px-1.5 py-0.5 rounded bg-zinc-900 text-zinc-300 border border-zinc-700">
                  {fmt.ext}
                </span>
              </div>
              <p className="text-[11px] text-zinc-400 leading-relaxed mb-3">
                {fmt.desc}
              </p>
            </div>
            <div className="text-[10px] font-mono text-emerald-400 flex items-center gap-1 font-semibold">
              <CheckCircle2 className="w-3 h-3 text-emerald-400 animate-pulse" />
              {fmt.badge}
            </div>
          </div>
        ))}
      </div>

      {/* Historical Batches Table */}
      <div className="p-5 rounded-xl bg-[#111114] border border-zinc-800 space-y-4 animate-fade-in-up delay-300">
        <div className="flex items-center justify-between">
          <h3 className="text-xs font-semibold text-white tracking-wide font-mono uppercase">
            HISTORICAL LOG INGESTION BATCHES
          </h3>
          <button
            onClick={fetchBatches}
            className="text-[11px] font-mono text-zinc-400 hover:text-white hover:underline font-semibold transition-colors"
          >
            Refresh List
          </button>
        </div>

        <div className="overflow-x-auto">
          <table className="w-full text-left text-xs">
            <thead>
              <tr className="border-b border-zinc-800 text-[11px] font-mono text-zinc-400 uppercase bg-[#09090b]">
                <th className="py-2.5 px-3">BATCH ID</th>
                <th className="py-2.5 px-3">FILENAME</th>
                <th className="py-2.5 px-3">PARSER TYPE</th>
                <th className="py-2.5 px-3">EVENTS PARSED</th>
                <th className="py-2.5 px-3">PIPELINE STATUS</th>
                <th className="py-2.5 px-3">TIMESTAMP</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-zinc-800/60 font-mono">
              {loading ? (
                <tr>
                  <td colSpan="6" className="py-8 text-center text-zinc-500">
                    <div className="flex items-center justify-center gap-2">
                      <span className="w-4 h-4 rounded-full border-2 border-white/20 border-t-white animate-spin" />
                      <span>Querying ingestion log registry...</span>
                    </div>
                  </td>
                </tr>
              ) : batches.length === 0 ? (
                <tr>
                  <td colSpan="6" className="py-6 text-center text-zinc-500">
                    No log batches uploaded yet. Click "Upload New Log Batch" or choose a Quick Demo Preset!
                  </td>
                </tr>
              ) : (
                batches.map((b, bIdx) => (
                  <tr
                    key={b.id}
                    className="hover:bg-[#18181c] transition-colors animate-slide-in-right"
                    style={{ animationDelay: `${bIdx * 50}ms` }}
                  >
                    <td className="py-3 px-3 text-zinc-400">#{b.id}</td>
                    <td className="py-3 px-3 text-white font-medium">{b.filename}</td>
                    <td className="py-3 px-3 text-zinc-300 font-semibold">{b.source_type}</td>
                    <td className="py-3 px-3 text-zinc-300">{b.raw_count} events</td>
                    <td className="py-3 px-3">
                      <span className="text-[10px] px-2 py-0.5 rounded bg-emerald-500/10 text-emerald-400 border border-emerald-500/20 font-bold">
                        {b.status}
                      </span>
                    </td>
                    <td className="py-3 px-3 text-zinc-400 text-[11px]">
                      {new Date(b.uploaded_at).toLocaleString()}
                    </td>
                  </tr>
                ))
              )}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}
