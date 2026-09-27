import React, { useEffect, useState } from 'react';
import { Search, Download, ShieldAlert, Filter } from 'lucide-react';
import { getIncidents, downloadIncidentPdf } from '../api/client';
import SeverityBadge from '../components/SeverityBadge';

export default function Incidents({ onSelectIncident }) {
  const [incidents, setIncidents] = useState([]);
  const [loading, setLoading] = useState(true);
  const [searchTerm, setSearchTerm] = useState('');
  const [severityFilter, setSeverityFilter] = useState('');
  const [statusFilter, setStatusFilter] = useState('');
  const [mounted, setMounted] = useState(false);

  const fetchIncidentsList = async () => {
    try {
      setLoading(true);
      const data = await getIncidents({
        severity: severityFilter || null,
        status: statusFilter || null,
      });
      setIncidents(data);
    } catch (err) {
      console.error('Failed to load incidents', err);
    } finally {
      setLoading(false);
      setTimeout(() => setMounted(true), 50);
    }
  };

  useEffect(() => {
    fetchIncidentsList();
  }, [severityFilter, statusFilter]);

  const filteredIncidents = incidents.filter((inc) => {
    const term = searchTerm.toLowerCase();
    return (
      inc.title.toLowerCase().includes(term) ||
      (inc.source_ip && inc.source_ip.toLowerCase().includes(term)) ||
      (inc.mitre_technique_id && inc.mitre_technique_id.toLowerCase().includes(term)) ||
      (inc.attack_category && inc.attack_category.toLowerCase().includes(term))
    );
  });

  return (
    <div className="p-6 space-y-6 max-w-7xl mx-auto">
      {/* Header */}
      <div className={`flex flex-col sm:flex-row sm:items-center justify-between gap-4 pb-2 border-b border-zinc-800 transition-all duration-500 ${mounted ? 'opacity-100 translate-y-0' : 'opacity-0 -translate-y-3'}`}>
        <div>
          <h1 className="text-xl font-bold tracking-tight text-white flex items-center gap-2 text-shimmer">
            <ShieldAlert className="w-5 h-5 text-white" />
            INCIDENT TRIAGE & CORRELATION
          </h1>
          <p className="text-xs text-zinc-400 font-mono mt-0.5">
            Audit-grade security records mapped to MITRE ATT&CK & NIST SP 800-61
          </p>
        </div>
      </div>

      {/* Controls Bar: Search & Filters */}
      <div className={`flex flex-col md:flex-row gap-4 justify-between items-stretch md:items-center bg-[#111114] p-4 rounded-xl border border-zinc-800 transition-all duration-500 delay-100 card-hover ${mounted ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-3'}`}>
        {/* Search */}
        <div className="relative flex-1 max-w-md group">
          <Search className="w-4 h-4 absolute left-3 top-3 text-zinc-500 group-focus-within:text-white transition-colors" />
          <input
            type="text"
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
            placeholder="Search by IP, technique, title, or tactic..."
            className="w-full pl-9 pr-4 py-2 bg-[#09090b] border border-zinc-800 rounded-lg text-xs text-white placeholder-zinc-500 focus:outline-none focus:border-white focus:ring-1 focus:ring-white/10 font-mono transition-all duration-200"
          />
        </div>

        {/* Severity Filter */}
        <div className="flex items-center space-x-1.5 flex-wrap gap-y-1">
          <span className="text-[11px] font-mono text-zinc-400 font-semibold mr-1 flex items-center gap-1">
            <Filter className="w-3 h-3 text-zinc-500" />
            Severity:
          </span>
          {['', 'CRITICAL', 'HIGH', 'MEDIUM', 'LOW'].map((sev) => (
            <button
              key={sev}
              onClick={() => setSeverityFilter(sev)}
              className={`px-2.5 py-1 rounded text-xs font-mono font-bold transition-all duration-200 active:scale-95 ${
                severityFilter === sev
                  ? (sev === 'CRITICAL' ? 'bg-[#C10230] text-white shadow-[0_0_12px_rgba(193,2,48,0.35)]' : 'bg-white text-black shadow-sm')
                  : 'bg-[#09090b] text-zinc-400 hover:text-white hover:bg-zinc-800 border border-zinc-800'
              }`}
            >
              {sev || 'ALL'}
            </button>
          ))}
        </div>

        {/* Status Filter */}
        <div className="flex items-center space-x-1.5 flex-wrap gap-y-1">
          <span className="text-[11px] font-mono text-zinc-400 font-semibold mr-1">Status:</span>
          {['', 'OPEN', 'INVESTIGATING', 'RESOLVED'].map((st) => (
            <button
              key={st}
              onClick={() => setStatusFilter(st)}
              className={`px-2.5 py-1 rounded text-xs font-mono font-bold transition-all duration-200 active:scale-95 ${
                statusFilter === st
                  ? 'bg-white text-black shadow-sm'
                  : 'bg-[#09090b] text-zinc-400 hover:text-white hover:bg-zinc-800 border border-zinc-800'
              }`}
            >
              {st || 'ALL'}
            </button>
          ))}
        </div>
      </div>

      {/* Incidents Table */}
      <div className={`rounded-xl bg-[#111114] border border-zinc-800 overflow-hidden shadow-sm transition-all duration-500 delay-200 ${mounted ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-4'}`}>
        <table className="w-full text-left text-xs">
          <thead>
            <tr className="border-b border-zinc-800 text-[11px] font-mono text-zinc-400 uppercase bg-[#09090b]">
              <th className="py-3 px-4">INCIDENT ID</th>
              <th className="py-3 px-4">SEVERITY</th>
              <th className="py-3 px-4">TITLE & IMPACT</th>
              <th className="py-3 px-4">MITRE MAPPING</th>
              <th className="py-3 px-4">ACTOR / HOST</th>
              <th className="py-3 px-4">RISK</th>
              <th className="py-3 px-4">STATUS</th>
              <th className="py-3 px-4 text-right">PDF REPORT</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-zinc-800/60 font-mono">
            {loading ? (
              <tr>
                <td colSpan="8" className="py-12 text-center text-zinc-500 font-mono">
                  <div className="flex flex-col items-center justify-center gap-2">
                    <span className="w-5 h-5 rounded-full border-2 border-white/20 border-t-white animate-spin" />
                    <span>Loading incident registry...</span>
                  </div>
                </td>
              </tr>
            ) : filteredIncidents.length === 0 ? (
              <tr>
                <td colSpan="8" className="py-12 text-center text-zinc-500 font-mono">
                  No incidents matching criteria found.
                </td>
              </tr>
            ) : (
              filteredIncidents.map((inc, idx) => (
                <tr
                  key={inc.id}
                  onClick={() => onSelectIncident(inc.id)}
                  className="hover:bg-[#18181c] cursor-pointer transition-all duration-200 group animate-slide-in-right"
                  style={{ animationDelay: `${idx * 40}ms` }}
                >
                  <td className="py-3.5 px-4 text-zinc-400 font-mono group-hover:text-white transition-colors">#{inc.id}</td>
                  <td className="py-3.5 px-4">
                    <SeverityBadge severity={inc.severity} />
                  </td>
                  <td className="py-3.5 px-4 font-sans font-medium text-white group-hover:underline group-hover:text-[#ff4d6d] transition-colors">
                    <div>{inc.title}</div>
                    <div className="text-[11px] text-zinc-500 font-mono mt-0.5">
                      {new Date(inc.created_at).toLocaleString()}
                    </div>
                  </td>
                  <td className="py-3.5 px-4">
                    <span className="px-2 py-0.5 rounded bg-zinc-900 text-zinc-300 border border-zinc-800 text-[11px] font-bold group-hover:border-zinc-600 transition-colors">
                      {inc.mitre_technique_id || 'T1110'}
                    </span>
                    <span className="text-[11px] text-zinc-400 block mt-0.5 truncate max-w-[140px]">
                      {inc.mitre_technique_name}
                    </span>
                  </td>
                  <td className="py-3.5 px-4 text-zinc-300 text-[11px]">
                    <div>{inc.source_ip || '127.0.0.1'}</div>
                    <div className="text-zinc-500 text-[10px]">Host: {inc.target_host}</div>
                  </td>
                  <td className="py-3.5 px-4 font-bold">
                    <span className={`transition-colors ${
                      inc.risk_score >= 80 ? 'text-[#ff4d6d]' :
                      inc.risk_score >= 60 ? 'text-amber-400' : 'text-zinc-300'
                    }`}>
                      {inc.risk_score}/100
                    </span>
                  </td>
                  <td className="py-3.5 px-4">
                    <span className="text-[11px] px-2 py-0.5 rounded bg-[#09090b] text-zinc-300 border border-zinc-800 group-hover:border-zinc-700 transition-colors">
                      {inc.status}
                    </span>
                  </td>
                  <td className="py-3.5 px-4 text-right">
                    <button
                      onClick={(e) => {
                        e.stopPropagation();
                        downloadIncidentPdf(inc.id);
                      }}
                      title="Download NIST Report PDF"
                      className="p-1.5 rounded-lg bg-[#09090b] border border-zinc-800 hover:border-white hover:text-white text-zinc-400 transition-all duration-200 hover:scale-110 active:scale-95 hover:shadow-[0_0_12px_rgba(255,255,255,0.15)]"
                    >
                      <Download className="w-3.5 h-3.5" />
                    </button>
                  </td>
                </tr>
              ))
            )}
          </tbody>
        </table>
      </div>
    </div>
  );
}
