import React, { useEffect, useState } from 'react';
import { AlertOctagon, Flame, ShieldAlert, CheckCircle2, ArrowUpRight, Activity, Cpu, Radio } from 'lucide-react';
import { getIncidentStats } from '../api/client';
import StatCard from '../components/StatCard';
import SeverityBadge from '../components/SeverityBadge';

export default function Dashboard({ onSelectIncident, onOpenUpload }) {
  const [stats, setStats] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const fetchStats = async () => {
    try {
      const data = await getIncidentStats();
      setStats(data);
      setError(null);
    } catch (err) {
      setError('Unable to load telemetry metrics.');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchStats();
    const interval = setInterval(fetchStats, 10000); // 10s auto-refresh
    return () => clearInterval(interval);
  }, []);

  if (loading) {
    return (
      <div className="p-8 flex items-center justify-center min-h-[60vh]">
        <div className="flex items-center space-x-3 text-sky-400 font-mono text-sm">
          <Radio className="w-5 h-5 animate-spin" />
          <span>Polling SOC Telemetry Stream...</span>
        </div>
      </div>
    );
  }

  return (
    <div className="p-6 space-y-6 max-w-7xl mx-auto">
      {/* Top Banner */}
      <div className="flex flex-col md:flex-row md:items-center justify-between gap-4 pb-2 border-b border-slate-800">
        <div>
          <h1 className="text-xl font-bold tracking-tight text-white flex items-center gap-2">
            SOC SITUATIONAL AWARENESS
          </h1>
          <p className="text-xs text-slate-400 font-mono mt-0.5">
            Real-time Threat Correlation • RAG Intelligence • Zero Hallucination Triage
          </p>
        </div>
        <div className="flex items-center space-x-3">
          <button
            onClick={fetchStats}
            className="px-3 py-1.5 rounded-lg bg-slate-900 border border-slate-800 hover:border-slate-700 text-xs font-mono text-slate-300 transition-colors"
          >
            Auto-Refresh: 10s
          </button>
        </div>
      </div>

      {/* Top 4 Stat Cards */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
        <StatCard
          title="TOTAL CORRELATED INCIDENTS"
          value={stats?.total_incidents || 0}
          subtitle="Processed across all log streams"
          icon={Activity}
          color="sky"
        />
        <StatCard
          title="CRITICAL THREATS"
          value={stats?.critical_count || 0}
          subtitle="Immediate containment required"
          icon={Flame}
          color="red"
          alert={(stats?.critical_count || 0) > 0}
        />
        <StatCard
          title="HIGH SEVERITY ALERTS"
          value={stats?.high_count || 0}
          subtitle="Active credential / web probes"
          icon={AlertOctagon}
          color="orange"
        />
        <StatCard
          title="CONTAINED / RESOLVED"
          value={stats?.resolved_count || 0}
          subtitle="Mitigated via NIST playbooks"
          icon={CheckCircle2}
          color="emerald"
        />
      </div>

      {/* Middle Grid: Threat Breakdown & MITRE Intelligence */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        {/* Severity Distribution */}
        <div className="p-5 rounded-xl bg-[#0f172a] border border-slate-800 space-y-4">
          <div className="flex items-center justify-between">
            <h3 className="text-xs font-semibold text-slate-200 tracking-wide font-mono uppercase">
              SEVERITY SPECTRUM
            </h3>
            <span className="text-[11px] text-slate-500 font-mono">CVSS Weighted</span>
          </div>

          <div className="space-y-3 pt-1">
            <div>
              <div className="flex justify-between text-xs font-mono mb-1">
                <span className="text-red-400">CRITICAL</span>
                <span className="text-slate-300">{stats?.critical_count || 0}</span>
              </div>
              <div className="w-full bg-slate-900 h-2 rounded-full overflow-hidden">
                <div
                  className="bg-red-500 h-full rounded-full transition-all duration-500"
                  style={{ width: `${stats?.total_incidents ? (stats.critical_count / stats.total_incidents) * 100 : 0}%` }}
                />
              </div>
            </div>

            <div>
              <div className="flex justify-between text-xs font-mono mb-1">
                <span className="text-orange-400">HIGH</span>
                <span className="text-slate-300">{stats?.high_count || 0}</span>
              </div>
              <div className="w-full bg-slate-900 h-2 rounded-full overflow-hidden">
                <div
                  className="bg-orange-500 h-full rounded-full transition-all duration-500"
                  style={{ width: `${stats?.total_incidents ? (stats.high_count / stats.total_incidents) * 100 : 0}%` }}
                />
              </div>
            </div>

            <div>
              <div className="flex justify-between text-xs font-mono mb-1">
                <span className="text-amber-400">MEDIUM</span>
                <span className="text-slate-300">{stats?.medium_count || 0}</span>
              </div>
              <div className="w-full bg-slate-900 h-2 rounded-full overflow-hidden">
                <div
                  className="bg-amber-500 h-full rounded-full transition-all duration-500"
                  style={{ width: `${stats?.total_incidents ? (stats.medium_count / stats.total_incidents) * 100 : 0}%` }}
                />
              </div>
            </div>

            <div>
              <div className="flex justify-between text-xs font-mono mb-1">
                <span className="text-emerald-400">LOW</span>
                <span className="text-slate-300">{stats?.low_count || 0}</span>
              </div>
              <div className="w-full bg-slate-900 h-2 rounded-full overflow-hidden">
                <div
                  className="bg-emerald-500 h-full rounded-full transition-all duration-500"
                  style={{ width: `${stats?.total_incidents ? (stats.low_count / stats.total_incidents) * 100 : 0}%` }}
                />
              </div>
            </div>
          </div>
        </div>

        {/* Top MITRE ATT&CK Techniques */}
        <div className="lg:col-span-2 p-5 rounded-xl bg-[#0f172a] border border-slate-800 space-y-4">
          <div className="flex items-center justify-between">
            <h3 className="text-xs font-semibold text-slate-200 tracking-wide font-mono uppercase">
              TOP MITRE ATT&CK TECHNIQUES DETECTED
            </h3>
            <span className="text-[11px] text-sky-400 font-mono">Vector Retrievable</span>
          </div>

          <div className="grid grid-cols-1 sm:grid-cols-3 gap-3 pt-1">
            {stats?.top_techniques?.length > 0 ? (
              stats.top_techniques.map((item, idx) => {
                const [tech, count] = Object.entries(item)[0];
                return (
                  <div key={idx} className="p-3 bg-slate-900/80 rounded-lg border border-slate-800 hover:border-sky-500/40 transition-colors">
                    <div className="flex items-center justify-between mb-1">
                      <span className="text-xs font-mono font-bold text-sky-400">{tech}</span>
                      <span className="text-[11px] font-mono px-1.5 py-0.5 rounded bg-sky-500/10 text-sky-300 border border-sky-500/20">
                        {count} hits
                      </span>
                    </div>
                    <div className="text-[11px] text-slate-400">
                      {tech === 'T1110' ? 'Brute Force' :
                       tech === 'T1548' ? 'Abuse Elevation Control' :
                       tech === 'T1190' ? 'Exploit Public App' :
                       tech === 'T1046' ? 'Network Service Discovery' : 'Enterprise Technique'}
                    </div>
                  </div>
                );
              })
            ) : (
              <div className="col-span-3 text-xs text-slate-500 font-mono py-4 text-center">
                No MITRE technique triggers logged yet.
              </div>
            )}
          </div>
        </div>
      </div>

      {/* Real-time Recent Alerts Feed Table */}
      <div className="p-5 rounded-xl bg-[#0f172a] border border-slate-800 space-y-4">
        <div className="flex items-center justify-between">
          <div>
            <h3 className="text-xs font-semibold text-slate-200 tracking-wide font-mono uppercase">
              RECENT CORRELATED SECURITY INCIDENTS
            </h3>
            <p className="text-[11px] text-slate-500 font-mono">Click any incident row to inspect deep forensic evidence</p>
          </div>
        </div>

        <div className="overflow-x-auto">
          <table className="w-full text-left text-xs">
            <thead>
              <tr className="border-b border-slate-800 text-[11px] font-mono text-slate-400 uppercase">
                <th className="py-2.5 px-3">ID</th>
                <th className="py-2.5 px-3">SEVERITY</th>
                <th className="py-2.5 px-3">INCIDENT TITLE</th>
                <th className="py-2.5 px-3">MITRE TECHNIQUE</th>
                <th className="py-2.5 px-3">SOURCE ACTOR</th>
                <th className="py-2.5 px-3">RISK SCORE</th>
                <th className="py-2.5 px-3">STATUS</th>
                <th className="py-2.5 px-3 text-right">ACTION</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-slate-800/60 font-mono">
              {stats?.recent_alerts?.map((inc) => (
                <tr
                  key={inc.id}
                  onClick={() => onSelectIncident(inc.id)}
                  className="hover:bg-slate-800/40 cursor-pointer transition-colors group"
                >
                  <td className="py-3 px-3 text-slate-400">#{inc.id}</td>
                  <td className="py-3 px-3">
                    <SeverityBadge severity={inc.severity} />
                  </td>
                  <td className="py-3 px-3 font-sans font-medium text-white group-hover:text-sky-400 transition-colors">
                    {inc.title}
                  </td>
                  <td className="py-3 px-3">
                    <span className="px-2 py-0.5 rounded bg-sky-500/10 text-sky-400 border border-sky-500/20 text-[11px]">
                      {inc.mitre_technique_id || 'T1110'}
                    </span>
                  </td>
                  <td className="py-3 px-3 text-slate-300 text-[11px]">
                    {inc.source_ip || 'Internal'}
                  </td>
                  <td className="py-3 px-3">
                    <div className="flex items-center space-x-2">
                      <span className={`text-[11px] font-bold ${
                        inc.risk_score >= 80 ? 'text-red-400' :
                        inc.risk_score >= 60 ? 'text-orange-400' : 'text-amber-400'
                      }`}>
                        {inc.risk_score}/100
                      </span>
                    </div>
                  </td>
                  <td className="py-3 px-3">
                    <span className="text-[11px] px-2 py-0.5 rounded bg-slate-900 text-slate-300 border border-slate-700">
                      {inc.status}
                    </span>
                  </td>
                  <td className="py-3 px-3 text-right">
                    <button
                      onClick={(e) => {
                        e.stopPropagation();
                        onSelectIncident(inc.id);
                      }}
                      className="text-slate-400 hover:text-sky-400 p-1 rounded hover:bg-slate-800"
                    >
                      <ArrowUpRight className="w-4 h-4" />
                    </button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}
