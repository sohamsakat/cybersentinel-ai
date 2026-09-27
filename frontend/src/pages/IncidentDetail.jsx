import React, { useEffect, useState } from 'react';
import { ArrowLeft, Download, Shield, Cpu, Terminal, CheckCircle2, CheckSquare, Square, MessageSquare } from 'lucide-react';
import { getIncidentDetail, updateIncidentStatus, downloadIncidentPdf } from '../api/client';
import SeverityBadge from '../components/SeverityBadge';

export default function IncidentDetail({ incidentId, onBack, onOpenCopilotForIncident }) {
  const [incident, setIncident] = useState(null);
  const [loading, setLoading] = useState(true);
  const [statusUpdating, setStatusUpdating] = useState(false);
  const [completedSteps, setCompletedSteps] = useState({});
  const [mounted, setMounted] = useState(false);

  useEffect(() => {
    const fetchDetail = async () => {
      try {
        setLoading(true);
        const data = await getIncidentDetail(incidentId);
        setIncident(data);
      } catch (err) {
        console.error('Failed to load incident detail', err);
      } finally {
        setLoading(false);
        setTimeout(() => setMounted(true), 50);
      }
    };
    fetchDetail();
  }, [incidentId]);

  const handleStatusChange = async (newStatus) => {
    try {
      setStatusUpdating(true);
      const updated = await updateIncidentStatus(incidentId, { status: newStatus });
      setIncident(updated);
    } catch (err) {
      console.error('Failed to update status', err);
    } finally {
      setStatusUpdating(false);
    }
  };

  const toggleStep = (idx) => {
    setCompletedSteps(prev => ({ ...prev, [idx]: !prev[idx] }));
  };

  if (loading) {
    return (
      <div className="p-16 flex flex-col items-center justify-center text-center font-mono text-xs text-zinc-500 space-y-3">
        <span className="w-6 h-6 rounded-full border-2 border-white/20 border-t-white animate-spin" />
        <span className="typewriter">Decrypting incident forensic profile...</span>
      </div>
    );
  }

  if (!incident) {
    return (
      <div className="p-8 text-center text-[#ff4d6d] font-mono text-xs animate-shake">
        Incident #{incidentId} could not be retrieved.
      </div>
    );
  }

  const playbookSteps = (incident.recommended_mitigation || '')
    .split('\n')
    .map(s => s.trim())
    .filter(s => s.length > 0 && !s.startsWith('Immediate Containment'));

  return (
    <div className={`p-6 space-y-6 max-w-6xl mx-auto transition-all duration-500 ${mounted ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-4'}`}>
      {/* Top Header & Actions */}
      <div className="flex flex-col md:flex-row md:items-center justify-between gap-4 pb-4 border-b border-zinc-800">
        <div className="flex items-center space-x-3">
          <button
            onClick={onBack}
            className="p-2 rounded-lg bg-[#111114] border border-zinc-800 hover:border-zinc-700 text-zinc-400 hover:text-white transition-all duration-200 hover:scale-105 active:scale-95"
          >
            <ArrowLeft className="w-4 h-4" />
          </button>
          <div>
            <div className="flex items-center gap-2">
              <span className="text-xs font-mono text-zinc-400 font-semibold">INCIDENT #{incident.id}</span>
              <SeverityBadge severity={incident.severity} />
            </div>
            <h1 className="text-lg font-bold text-white mt-0.5">{incident.title}</h1>
          </div>
        </div>

        <div className="flex items-center space-x-3 flex-wrap gap-y-2">
          {/* Status Dropdown */}
          <div className="flex items-center space-x-2 bg-[#111114] border border-zinc-800 hover:border-zinc-700 px-3 py-1.5 rounded-lg transition-colors">
            <span className="text-[11px] font-mono text-zinc-400 font-semibold">Status:</span>
            <select
              value={incident.status}
              disabled={statusUpdating}
              onChange={(e) => handleStatusChange(e.target.value)}
              className="bg-transparent text-xs font-mono font-bold text-white focus:outline-none cursor-pointer"
            >
              <option value="OPEN" className="bg-[#111114] text-white">OPEN</option>
              <option value="INVESTIGATING" className="bg-[#111114] text-white">INVESTIGATING</option>
              <option value="CONTAINED" className="bg-[#111114] text-white">CONTAINED</option>
              <option value="RESOLVED" className="bg-[#111114] text-white">RESOLVED</option>
            </select>
          </div>

          <button
            onClick={() => onOpenCopilotForIncident(incident.id)}
            className="flex items-center space-x-2 bg-[#111114] hover:bg-[#1c1c20] text-white text-xs font-semibold px-3.5 py-2 rounded-lg transition-all duration-200 border border-zinc-700 shadow-sm hover:scale-[1.02] active:scale-95"
          >
            <MessageSquare className="w-3.5 h-3.5" />
            <span>Ask Copilot</span>
          </button>

          <button
            onClick={() => downloadIncidentPdf(incident.id)}
            className="flex items-center space-x-2 bg-white hover:bg-zinc-200 text-black text-xs font-bold px-3.5 py-2 rounded-lg transition-all duration-200 border border-white shadow-sm hover:scale-[1.02] active:scale-95 hover:shadow-[0_0_15px_rgba(255,255,255,0.2)]"
          >
            <Download className="w-3.5 h-3.5" />
            <span>NIST PDF Report</span>
          </button>
        </div>
      </div>

      {/* Main Grid: Forensic Details & Playbook */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        {/* Left 2 Cols: Threat Profile & Evidence */}
        <div className="lg:col-span-2 space-y-6">
          {/* Key Metrics Strip */}
          <div className="grid grid-cols-3 gap-3 p-4 bg-[#111114] rounded-xl border border-zinc-800 card-hover animate-fade-in-up">
            <div className="group">
              <div className="text-[11px] font-mono text-zinc-400 font-semibold">CALCULATED RISK</div>
              <div className="text-xl font-bold font-mono text-[#ff4d6d] mt-0.5 animate-count-up">
                {incident.risk_score} <span className="text-xs text-zinc-500">/ 100</span>
              </div>
            </div>
            <div>
              <div className="text-[11px] font-mono text-zinc-400 font-semibold">SOURCE ACTOR IP</div>
              <div className="text-xs font-mono font-bold text-white mt-1">
                {incident.source_ip || 'Internal Network'}
              </div>
            </div>
            <div>
              <div className="text-[11px] font-mono text-zinc-400 font-semibold">TARGET ASSET</div>
              <div className="text-xs font-mono font-bold text-white mt-1">
                {incident.target_host || 'Endpoint Host'}
              </div>
            </div>
          </div>

          {/* Executive Summary */}
          <div className="p-5 bg-[#111114] rounded-xl border border-zinc-800 space-y-2 card-hover animate-fade-in-up delay-100">
            <h3 className="text-xs font-mono uppercase text-zinc-400 font-bold flex items-center gap-2">
              <Shield className="w-3.5 h-3.5 text-zinc-300" />
              Executive Triage Summary
            </h3>
            <p className="text-xs text-zinc-300 leading-relaxed">
              {incident.summary}
            </p>
          </div>

          {/* MITRE ATT&CK Mapping Card */}
          <div className="p-5 bg-[#111114] rounded-xl border border-zinc-800 space-y-3 card-hover animate-fade-in-up delay-200">
            <div className="flex items-center justify-between">
              <h3 className="text-xs font-mono uppercase text-zinc-400 font-bold flex items-center gap-2">
                <Cpu className="w-3.5 h-3.5 text-emerald-400" />
                MITRE ATT&CK Enterprise Grounding
              </h3>
              <span className="text-[10px] font-mono px-2 py-0.5 rounded bg-emerald-500/10 text-emerald-400 border border-emerald-500/30 font-semibold">
                Confidence: {Math.round((incident.confidence_score || 0.85) * 100)}%
              </span>
            </div>

            <div className="p-3 bg-[#09090b] rounded-lg border border-zinc-800 flex items-center justify-between">
              <div>
                <div className="text-sm font-bold text-white">
                  {incident.mitre_technique_id} - {incident.mitre_technique_name}
                </div>
                <div className="text-[11px] text-zinc-400 font-mono mt-0.5">
                  Tactic: <span className="text-white font-semibold">{incident.attack_category}</span>
                </div>
              </div>
              <a
                href={`https://attack.mitre.org/techniques/${incident.mitre_technique_id?.replace('.', '/')}/`}
                target="_blank"
                rel="noreferrer"
                className="text-[11px] font-mono text-zinc-300 hover:text-white hover:underline px-2.5 py-1 rounded bg-zinc-900 border border-zinc-700 transition-all hover:scale-105"
              >
                View MITRE Docs ↗
              </a>
            </div>
          </div>

          {/* Forensic Log Timeline */}
          <div className="p-5 bg-[#111114] rounded-xl border border-zinc-800 space-y-3 card-hover animate-fade-in-up delay-300">
            <h3 className="text-xs font-mono uppercase text-zinc-400 font-bold flex items-center gap-2">
              <Terminal className="w-3.5 h-3.5 text-amber-400" />
              Chronological Forensic Evidence
            </h3>
            <pre className="p-4 bg-[#050507] rounded-lg border border-zinc-800 text-[11px] font-mono text-zinc-300 overflow-x-auto whitespace-pre-wrap leading-relaxed scanline-overlay relative">
              {incident.technical_details}
            </pre>
          </div>
        </div>

        {/* Right Col: NIST Remediation Playbook */}
        <div className="space-y-6 animate-fade-in-up delay-200">
          <div className="p-5 bg-[#111114] rounded-xl border border-zinc-800 space-y-4 card-hover">
            <div>
              <h3 className="text-xs font-mono uppercase text-zinc-400 font-bold flex items-center gap-2">
                <CheckCircle2 className="w-4 h-4 text-emerald-400" />
                NIST SP 800-61 Remediation Playbook
              </h3>
              <p className="text-[11px] text-zinc-400 font-mono mt-0.5">
                Check off actions as your containment progresses
              </p>
            </div>

            <div className="space-y-2.5">
              {playbookSteps.length > 0 ? (
                playbookSteps.map((step, idx) => {
                  const isChecked = !!completedSteps[idx];
                  return (
                    <div
                      key={idx}
                      onClick={() => toggleStep(idx)}
                      className={`p-3 rounded-lg border cursor-pointer transition-all duration-200 flex items-start space-x-2.5 text-xs active:scale-[0.98] ${
                        isChecked
                          ? 'bg-emerald-950/20 border-emerald-800/40 text-zinc-400 line-through'
                          : 'bg-[#09090b] border-zinc-800 text-zinc-200 hover:border-zinc-700 hover:bg-[#141418]'
                      }`}
                    >
                      {isChecked ? (
                        <CheckSquare className="w-4 h-4 text-emerald-400 shrink-0 mt-0.5 transition-transform scale-110" />
                      ) : (
                        <Square className="w-4 h-4 text-zinc-600 shrink-0 mt-0.5 transition-transform" />
                      )}
                      <span className="leading-snug">{step}</span>
                    </div>
                  );
                })
              ) : (
                <div className="text-xs text-zinc-500 font-mono">
                  Standard containment rules apply.
                </div>
              )}
            </div>

            <div className="pt-2 border-t border-zinc-800/80 flex justify-between text-[11px] font-mono text-zinc-400">
              <span>Playbook Completion:</span>
              <span className="text-emerald-400 font-bold">
                {Object.values(completedSteps).filter(Boolean).length} / {playbookSteps.length}
              </span>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
