import React, { useState, useEffect, useRef } from 'react';
import { 
  Radio, Play, Pause, ShieldAlert, 
  Terminal, ShieldCheck, Cpu, ArrowRight, Zap, Layers, Activity, AlertTriangle
} from 'lucide-react';
import SeverityBadge from '../components/SeverityBadge';

// Rich pre-recorded stream telemetry simulating realistic enterprise traffic + active attack campaigns
const TELEMETRY_STREAM_DATABASE = [
  { id: 1, type: 'normal', source: 'APACHE', ip: '192.168.1.50', host: 'web-prod-01', msg: 'GET /index.html HTTP/1.1 200 OK - Mozilla/5.0' },
  { id: 2, type: 'normal', source: 'LINUX', ip: '10.0.0.12', host: 'srv-prod-01', msg: 'CRON[18421]: pam_unix(cron:session): session opened for user root by (uid=0)' },
  { id: 3, type: 'normal', source: 'FIREWALL', ip: '198.51.100.22', host: 'edge-fw-01', msg: 'TCP 443 ALLOW - TLS Handshake from benign client' },
  { id: 4, type: 'normal', source: 'LINUX', ip: '10.0.0.12', host: 'srv-prod-01', msg: 'CRON[18421]: pam_unix(cron:session): session closed for user root' },
  { id: 5, type: 'normal', source: 'WINDOWS', ip: '192.168.1.105', host: 'DC01.corp', msg: 'EventID 4624: Successful Logon for user jsmith (Domain: CORP)' },
  { id: 6, type: 'normal', source: 'APACHE', ip: '192.168.1.50', host: 'web-prod-01', msg: 'GET /assets/style.css HTTP/1.1 200 OK - cached' },
  // Attack Wave 1: SSH Brute Force
  { 
    id: 7, 
    type: 'threat', 
    severity: 'HIGH',
    source: 'LINUX', 
    ip: '198.51.100.45', 
    host: 'srv-prod-01', 
    msg: 'sshd[19001]: Failed password for invalid user admin from 198.51.100.45 port 41256',
    threatData: {
      title: 'SSH Authentication Brute Force Campaign',
      mitre: 'T1110 - Brute Force',
      tactic: 'Credential Access',
      riskScore: 78,
      action: 'Rate-limiting IP & monitoring auth threshold'
    }
  },
  { id: 8, type: 'threat', severity: 'HIGH', source: 'LINUX', ip: '198.51.100.45', host: 'srv-prod-01', msg: 'sshd[19003]: Failed password for invalid user root from 198.51.100.45 port 41258' },
  { id: 9, type: 'threat', severity: 'HIGH', source: 'LINUX', ip: '198.51.100.45', host: 'srv-prod-01', msg: 'sshd[19007]: Failed password for invalid user deploy from 198.51.100.45 port 41264' },
  { 
    id: 10, 
    type: 'threat', 
    severity: 'CRITICAL',
    source: 'LINUX', 
    ip: '198.51.100.45', 
    host: 'srv-prod-01', 
    msg: 'sudo: deploy : 3 incorrect password attempts ; USER=root ; COMMAND=/bin/cat /etc/shadow',
    threatData: {
      title: 'Root Privilege Escalation Probe on /etc/shadow',
      mitre: 'T1548 - Abuse Elevation Control',
      tactic: 'Privilege Escalation',
      riskScore: 95,
      action: 'Account locked. Sudo session terminated.'
    }
  },
  // Normal background
  { id: 11, type: 'normal', source: 'FIREWALL', ip: '10.0.0.8', host: 'edge-fw-01', msg: 'UDP 53 ALLOW - DNS Query resolving internal.corp' },
  { id: 12, type: 'normal', source: 'APACHE', ip: '172.16.0.4', host: 'web-prod-01', msg: 'GET /api/v1/health HTTP/1.1 200 OK - Health probe' },
  // Attack Wave 2: SQL Injection
  { 
    id: 13, 
    type: 'threat', 
    severity: 'CRITICAL',
    source: 'APACHE', 
    ip: '203.0.113.88', 
    host: 'web-prod-01', 
    msg: 'GET /products.php?category=1 UNION SELECT null,username,password,email FROM users-- HTTP/1.1 200 OK [sqlmap/1.7#stable]',
    threatData: {
      title: 'Automated SQL Injection Data Extraction (sqlmap)',
      mitre: 'T1190 - Exploit Public-Facing App',
      tactic: 'Initial Access',
      riskScore: 92,
      action: 'WAF Rule #403 applied. Attacker IP blacklisted.'
    }
  },
  { 
    id: 14, 
    type: 'threat', 
    severity: 'HIGH',
    source: 'APACHE', 
    ip: '203.0.113.88', 
    host: 'web-prod-01', 
    msg: 'GET /view.php?page=../../../../etc/passwd HTTP/1.1 200 OK - Path Traversal detected' 
  },
  // Attack Wave 3: Firewall Reconnaissance
  { 
    id: 15, 
    type: 'threat', 
    severity: 'MEDIUM',
    source: 'FIREWALL', 
    ip: '198.51.100.99', 
    host: 'edge-fw-01', 
    msg: 'TCP Port Scan SYN to ports 21, 22, 23, 80, 443, 3389 within 100ms - DENIED',
    threatData: {
      title: 'Reconnaissance TCP Port Scan (Nmap SYN)',
      mitre: 'T1046 - Network Service Discovery',
      tactic: 'Discovery',
      riskScore: 65,
      action: 'Dynamic firewall drop rule triggered.'
    }
  },
  { id: 16, type: 'normal', source: 'WINDOWS', ip: '192.168.1.185', host: 'DC01.corp', msg: 'EventID 4624: User Kerberos ticket renewed for svc-backup' },
  // Attack Wave 4: Windows Privilege Assignment
  { 
    id: 17, 
    type: 'threat', 
    severity: 'CRITICAL',
    source: 'WINDOWS', 
    ip: '192.168.1.185', 
    host: 'DC01.corp', 
    msg: 'EventID 4672: Special Privileges Assigned (SeDebugPrivilege, SeTakeOwnershipPrivilege)',
    threatData: {
      title: 'Special Privileges Assigned to Administrator SID',
      mitre: 'T1078 - Valid Accounts',
      tactic: 'Defense Evasion',
      riskScore: 90,
      action: 'Privileged audit alert dispatched to SOC Commander'
    }
  },
  { id: 18, type: 'normal', source: 'APACHE', ip: '192.168.1.50', host: 'web-prod-01', msg: 'GET /dashboard HTTP/1.1 200 OK - Authenticated session' },
];

export default function LiveRadar({ onSelectIncident }) {
  const [streamIndex, setStreamIndex] = useState(0);
  const [logs, setLogs] = useState([]);
  const [interceptedThreats, setInterceptedThreats] = useState([]);
  const [isPlaying, setIsPlaying] = useState(true);
  const [speed, setSpeed] = useState(1800); // ms per log line
  const [activeTabFilter, setActiveTabFilter] = useState('all'); // 'all' or 'threats'
  const [attackWaveActive, setAttackWaveActive] = useState(false);
  const [radarAngle, setRadarAngle] = useState(0);

  const scrollRef = useRef(null);

  // Streaming Engine: Emulates real-time SIEM syslog tail
  useEffect(() => {
    if (!isPlaying) return;

    const timer = setInterval(() => {
      setStreamIndex((prevIdx) => {
        const nextItem = TELEMETRY_STREAM_DATABASE[prevIdx % TELEMETRY_STREAM_DATABASE.length];
        const timestamp = new Date().toLocaleTimeString();
        const logWithTime = { ...nextItem, streamTime: timestamp, uniqueKey: `${Date.now()}-${Math.random()}` };

        setLogs((prevLogs) => [...prevLogs.slice(-45), logWithTime]);

        // If this line is a threat with threat data, intercept it!
        if (nextItem.type === 'threat' && nextItem.threatData) {
          setInterceptedThreats((prevThreats) => [
            { ...nextItem.threatData, id: nextItem.id, timestamp, ip: nextItem.ip, host: nextItem.host, severity: nextItem.severity },
            ...prevThreats.slice(0, 7)
          ]);
        }

        return prevIdx + 1;
      });
    }, speed);

    return () => clearInterval(timer);
  }, [isPlaying, speed]);

  // Autoscroll live terminal
  useEffect(() => {
    if (scrollRef.current) {
      scrollRef.current.scrollTop = scrollRef.current.scrollHeight;
    }
  }, [logs]);

  // Trigger Instant Attack Wave button
  const triggerAttackWave = () => {
    setStreamIndex(6);
    setIsPlaying(true);
    setAttackWaveActive(true);
    setTimeout(() => setAttackWaveActive(false), 8000);
  };

  const filteredLogs = activeTabFilter === 'threats' ? logs.filter(l => l.type === 'threat') : logs;
  const hasActiveThreat = attackWaveActive || (logs.length > 0 && logs[logs.length - 1]?.type === 'threat');

  return (
    <div className="p-6 space-y-5 max-w-7xl mx-auto">
      {/* Emergency Flash Banner on Attack Wave */}
      {attackWaveActive && (
        <div className="p-3.5 rounded-xl border border-[#ff4d6d] bg-[#C10230]/20 animate-strobe-alert flex items-center justify-between text-white font-mono text-xs shadow-2xl">
          <div className="flex items-center gap-3">
            <span className="w-3 h-3 rounded-full bg-[#ff4d6d] animate-ping" />
            <AlertTriangle className="w-5 h-5 text-[#ff4d6d] animate-bounce" />
            <div>
              <span className="font-bold tracking-wider text-sm">CRITICAL THREAT INJECTION IN PROGRESS:</span>
              <span className="text-zinc-200 ml-2">MITRE T1110 (Brute Force) &amp; T1548 (Privilege Escalation)</span>
            </div>
          </div>
          <span className="px-2 py-0.5 rounded bg-[#C10230] text-white font-bold tracking-widest text-[10px] animate-pulse">
            DEFCON 1 • CONTAINMENT ACTIVE
          </span>
        </div>
      )}

      {/* Header & Controls */}
      <div className="flex flex-col md:flex-row md:items-center justify-between gap-4 pb-3 border-b border-zinc-800">
        <div>
          <h1 className="text-xl font-bold tracking-tight text-white flex items-center gap-2.5">
            <Radio className={`w-5 h-5 ${hasActiveThreat ? 'text-[#ff4d6d] animate-ping' : 'text-emerald-400 animate-pulse'}`} />
            LIVE TELEMETRY STREAM &amp; AI RADAR
          </h1>
          <p className="text-xs text-zinc-400 font-mono mt-0.5">
            Real-time Log Stream • Automated RAG Threat Interception • Zero Delay Detection
          </p>
        </div>

        {/* Live Packet Waveform & Playback Controls */}
        <div className="flex items-center space-x-3 flex-wrap gap-y-2">
          {/* Animated Audio-style Equalizer Bars */}
          <div className="hidden sm:flex items-center gap-1 bg-[#111114] px-3 py-1.5 rounded-lg border border-zinc-800">
            <Activity className="w-3.5 h-3.5 text-emerald-400 mr-1 animate-pulse" />
            <div className="flex items-end gap-0.5 h-4 w-16">
              {[60, 100, 45, 80, 30, 90, 70, 40, 95, 55, 85, 35].map((h, i) => (
                <span
                  key={i}
                  className={`w-1 rounded-sm ${hasActiveThreat ? 'bg-[#ff4d6d]' : 'bg-emerald-400'} transition-all`}
                  style={{
                    height: `${isPlaying ? h : 20}%`,
                    animation: isPlaying ? `eqBounce 0.${6 + (i % 5)}s ease-in-out infinite alternate` : 'none',
                    animationDelay: `${i * 70}ms`
                  }}
                />
              ))}
            </div>
            <span className="text-[10px] font-mono text-zinc-400 ml-1">1,840 pkts/s</span>
          </div>

          <button
            onClick={() => setIsPlaying(!isPlaying)}
            className="flex items-center space-x-1.5 px-3 py-1.5 rounded-lg text-xs font-semibold font-mono border border-zinc-700 bg-zinc-900 text-zinc-300 hover:text-white transition-all shadow-sm active:scale-95"
          >
            {isPlaying ? <Pause className="w-3.5 h-3.5 text-amber-400" /> : <Play className="w-3.5 h-3.5 text-emerald-400" />}
            <span>{isPlaying ? 'Pause' : 'Resume'}</span>
          </button>

          {/* Speed Buttons */}
          <div className="flex items-center bg-[#09090b] border border-zinc-800 rounded-lg p-0.5">
            <button
              onClick={() => setSpeed(2400)}
              className={`px-2 py-1 text-[11px] font-mono rounded transition-colors ${speed === 2400 ? 'bg-white text-black font-bold' : 'text-zinc-400 hover:text-white'}`}
            >
              1x
            </button>
            <button
              onClick={() => setSpeed(1400)}
              className={`px-2 py-1 text-[11px] font-mono rounded transition-colors ${speed === 1400 ? 'bg-white text-black font-bold' : 'text-zinc-400 hover:text-white'}`}
            >
              2x
            </button>
            <button
              onClick={() => setSpeed(600)}
              className={`px-2 py-1 text-[11px] font-mono rounded transition-colors ${speed === 600 ? 'bg-white text-black font-bold' : 'text-zinc-400 hover:text-white'}`}
            >
              Rapid
            </button>
          </div>

          {/* Trigger Attack Wave Button */}
          <button
            onClick={triggerAttackWave}
            className="flex items-center space-x-1.5 px-3.5 py-1.5 rounded-lg bg-[#C10230] hover:bg-[#9E0025] text-white border border-[#C10230] text-xs font-mono font-bold shadow-[0_0_15px_rgba(193,2,48,0.35)] active:scale-95 transition-all hover:scale-105"
          >
            <Zap className="w-3.5 h-3.5 text-white animate-pulse" />
            <span>Simulate Attack Wave</span>
          </button>
        </div>
      </div>

      {/* Cyber Radar HUD + Animated Pipeline Strip */}
      <div className="grid grid-cols-1 lg:grid-cols-12 gap-5">
        {/* Visual Circular Radar Scope (4 cols) */}
        <div className="lg:col-span-4 p-4 rounded-xl bg-[#111114] border border-zinc-800 flex flex-col items-center justify-between relative overflow-hidden card-hover">
          <div className="w-full flex items-center justify-between text-[11px] font-mono text-zinc-400 mb-2">
            <span className="flex items-center gap-1.5 text-white font-bold">
              <Radio className={`w-3.5 h-3.5 ${hasActiveThreat ? 'text-[#ff4d6d]' : 'text-emerald-400'}`} />
              CIRCULAR SONAR SCOPE
            </span>
            <span className={`px-1.5 py-0.5 rounded text-[10px] font-bold ${hasActiveThreat ? 'bg-[#C10230]/20 text-[#ff4d6d] border border-[#C10230]/40' : 'bg-emerald-500/10 text-emerald-400 border border-emerald-500/30'}`}>
              {hasActiveThreat ? 'THREAT IN RANGE' : 'SECTOR CLEAR'}
            </span>
          </div>

          {/* Circular Radar Screen */}
          <div className="relative w-48 h-48 my-2 rounded-full border border-emerald-500/30 bg-[#050507] flex items-center justify-center overflow-hidden shadow-[inset_0_0_20px_rgba(16,185,129,0.15)]">
            {/* Concentric Sonar Rings */}
            <div className="absolute w-36 h-36 rounded-full border border-emerald-500/20" />
            <div className="absolute w-24 h-24 rounded-full border border-emerald-500/20" />
            <div className="absolute w-12 h-12 rounded-full border border-emerald-500/25" />

            {/* Crosshairs */}
            <div className="absolute inset-x-0 top-1/2 h-px bg-emerald-500/20" />
            <div className="absolute inset-y-0 left-1/2 w-px bg-emerald-500/20" />

            {/* Rotating Radar Sweep Beam */}
            <div
              className={`absolute inset-0 ${hasActiveThreat ? 'radar-sweep-beam-crimson animate-radar-spin-fast' : 'radar-sweep-beam animate-radar-spin'}`}
            />

            {/* Pulsing center ping */}
            <div className={`w-2 h-2 rounded-full relative z-10 ${hasActiveThreat ? 'bg-[#ff4d6d] animate-ping' : 'bg-emerald-400 animate-ping'}`} />

            {/* Simulated Target Blips */}
            <div className="absolute top-10 left-12 flex items-center justify-center">
              <span className="w-2 h-2 rounded-full bg-emerald-400 shadow-[0_0_8px_#10b981]" />
              <span className="absolute w-4 h-4 rounded-full border border-emerald-400 animate-radar-ping-ring" />
            </div>

            <div className="absolute bottom-12 right-14 flex items-center justify-center">
              <span className="w-2 h-2 rounded-full bg-emerald-400 shadow-[0_0_8px_#10b981]" />
              <span className="absolute w-4 h-4 rounded-full border border-emerald-400 animate-radar-ping-ring delay-300" />
            </div>

            {hasActiveThreat && (
              <div className="absolute top-8 right-10 flex items-center justify-center">
                <span className="w-2.5 h-2.5 rounded-full bg-[#ff4d6d] shadow-[0_0_12px_#ff4d6d]" />
                <span className="absolute w-6 h-6 rounded-full border border-[#ff4d6d] animate-threat-ping-ring" />
                <span className="absolute -top-3 text-[9px] font-mono text-[#ff4d6d] font-bold">T1110</span>
              </div>
            )}
          </div>

          {/* Radar Telemetry Readout */}
          <div className="w-full grid grid-cols-2 gap-2 text-[10px] font-mono text-zinc-400 pt-2 border-t border-zinc-800/80">
            <div>SWEEP: <span className="text-white font-bold">360° CONTINUOUS</span></div>
            <div className="text-right">TARGETS: <span className={hasActiveThreat ? 'text-[#ff4d6d] font-bold' : 'text-emerald-400 font-bold'}>{interceptedThreats.length > 0 ? interceptedThreats.length : 2} NODES</span></div>
          </div>
        </div>

        {/* Animated Interception Pipeline (8 cols) */}
        <div className="lg:col-span-8 p-4 rounded-xl bg-[#111114] border border-zinc-800 flex flex-col justify-between card-hover">
          <div className="text-[11px] font-mono uppercase text-zinc-400 font-bold mb-3 flex items-center justify-between">
            <span className="flex items-center gap-1.5 text-white">
              <Layers className="w-3.5 h-3.5 text-zinc-300" />
              Real-Time Automated Threat Interception Architecture
            </span>
            <span className="text-[10px] text-emerald-400 font-mono flex items-center gap-1">
              <span className="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-ping inline-block" />
              MITRE Grounding: Sub-15ms
            </span>
          </div>

          {/* 4 Pipeline Stages with Animated Data Cables */}
          <div className="grid grid-cols-1 sm:grid-cols-4 gap-3 text-center text-xs font-mono relative my-auto">
            {/* Stage 1 */}
            <div className="p-3 bg-[#09090b] rounded-lg border border-zinc-800 relative group hover:border-zinc-600 transition-colors">
              <div className="flex items-center justify-between text-[10px] text-zinc-500 font-semibold mb-1">
                <span>STAGE 1</span>
                <span className="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-pulse" />
              </div>
              <div className="font-bold text-white">Ingestion</div>
              <div className="text-[10px] text-zinc-400 mt-0.5">Raw Telemetry Tail</div>
              <div className="text-[9px] text-emerald-400/80 mt-1 font-mono">Win/Lin/Apache/FW</div>

              {/* Animated Data Wire to Stage 2 */}
              <div className="hidden sm:block absolute -right-3 top-1/2 -translate-y-1/2 w-3 h-0.5 bg-zinc-800 z-10 overflow-hidden">
                <span className="absolute top-0 bottom-0 w-2 bg-emerald-400 rounded-full animate-packet-travel" style={{ animation: 'packetTravel 1.4s ease-in-out infinite' }} />
              </div>
            </div>

            {/* Stage 2 */}
            <div className="p-3 bg-[#09090b] rounded-lg border border-zinc-800 relative group hover:border-zinc-600 transition-colors">
              <div className="flex items-center justify-between text-[10px] text-zinc-500 font-semibold mb-1">
                <span>STAGE 2</span>
                <span className="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-pulse delay-100" />
              </div>
              <div className="font-bold text-white">Normalization</div>
              <div className="text-[10px] text-zinc-400 mt-0.5">ECS Schema Engine</div>
              <div className="text-[9px] text-zinc-500 mt-1 font-mono">Regex Filters</div>

              {/* Animated Data Wire to Stage 3 */}
              <div className="hidden sm:block absolute -right-3 top-1/2 -translate-y-1/2 w-3 h-0.5 bg-zinc-800 z-10 overflow-hidden">
                <span className="absolute top-0 bottom-0 w-2 bg-emerald-400 rounded-full" style={{ animation: 'packetTravel 1.4s ease-in-out infinite 0.35s' }} />
              </div>
            </div>

            {/* Stage 3 */}
            <div className="p-3 bg-[#09090b] rounded-lg border border-zinc-800 relative group hover:border-zinc-600 transition-colors">
              <div className="flex items-center justify-between text-[10px] text-zinc-500 font-semibold mb-1">
                <span>STAGE 3</span>
                <span className="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-pulse delay-200" />
              </div>
              <div className="font-bold text-white">Vector RAG</div>
              <div className="text-[10px] text-zinc-400 mt-0.5">ChromaDB MITRE v14</div>
              <div className="text-[9px] text-zinc-500 mt-1 font-mono">600+ TTPs Indexed</div>

              {/* Animated Data Wire to Stage 4 */}
              <div className="hidden sm:block absolute -right-3 top-1/2 -translate-y-1/2 w-3 h-0.5 bg-zinc-800 z-10 overflow-hidden">
                <span className="absolute top-0 bottom-0 w-2 bg-[#ff4d6d] rounded-full" style={{ animation: 'packetTravel 1.4s ease-in-out infinite 0.7s' }} />
              </div>
            </div>

            {/* Stage 4 */}
            <div className={`p-3 bg-[#09090b] rounded-lg border transition-all ${hasActiveThreat ? 'border-[#C10230] bg-[#C10230]/15 glow-crimson animate-border-pulse' : 'border-[#C10230]/40 bg-[#C10230]/5'}`}>
              <div className="flex items-center justify-between text-[10px] text-[#ff4d6d] font-semibold mb-1">
                <span>STAGE 4</span>
                <span className="w-1.5 h-1.5 rounded-full bg-[#ff4d6d] animate-ping" />
              </div>
              <div className="font-bold text-white">Containment</div>
              <div className="text-[10px] text-[#ffb3c1] mt-0.5">CVSS &amp; Auto-Block</div>
              <div className="text-[9px] text-[#ff4d6d] mt-1 font-mono">NIST SP 800-61</div>
            </div>
          </div>

          <div className="mt-3 pt-2 border-t border-zinc-800/80 flex justify-between items-center text-[10px] font-mono text-zinc-400">
            <span>Edge Filter Efficiency: <strong className="text-white">99.2% Benign Discarded</strong></span>
            <span>Zero-Hallucination Rate: <strong className="text-emerald-400">0.0% Verified</strong></span>
          </div>
        </div>
      </div>

      {/* Main Split Grid: Live Stream vs AI Interceptor */}
      <div className="grid grid-cols-1 lg:grid-cols-12 gap-5">
        {/* Left Column (7 Cols): Live Telemetry Stream */}
        <div className="lg:col-span-7 flex flex-col h-[520px] rounded-xl bg-[#09090b] border border-zinc-800 overflow-hidden shadow-2xl relative">
          {/* Scanning Laser Beam */}
          <div className="absolute left-0 right-0 h-0.5 bg-gradient-to-r from-transparent via-emerald-400 to-transparent pointer-events-none z-20 animate-laser-sweep opacity-70" />

          {/* Stream Header */}
          <div className="px-4 py-2.5 bg-[#111114] border-b border-zinc-800 flex justify-between items-center text-xs font-mono">
            <div className="flex items-center space-x-2">
              <Terminal className="w-4 h-4 text-zinc-300" />
              <span className="font-bold text-white">LIVE TELEMETRY STREAM</span>
              <span className="w-2 h-2 rounded-full bg-emerald-400 animate-ping" />
            </div>

            {/* Filter Pills */}
            <div className="flex items-center space-x-1.5">
              <button
                onClick={() => setActiveTabFilter('all')}
                className={`px-2.5 py-1 rounded text-[10px] font-bold transition-all active:scale-95 ${activeTabFilter === 'all' ? 'bg-white text-black' : 'bg-zinc-900 text-zinc-400 hover:text-white border border-zinc-800'}`}
              >
                All Telemetry ({logs.length})
              </button>
              <button
                onClick={() => setActiveTabFilter('threats')}
                className={`px-2.5 py-1 rounded text-[10px] font-bold transition-all active:scale-95 ${activeTabFilter === 'threats' ? 'bg-[#C10230] text-white shadow-sm' : 'bg-zinc-900 text-zinc-400 hover:text-white border border-zinc-800'}`}
              >
                Threats Only ({logs.filter(l => l.type === 'threat').length})
              </button>
            </div>
          </div>

          {/* Terminal Logs Window */}
          <div
            ref={scrollRef}
            className="flex-1 p-3.5 overflow-y-auto space-y-2 font-mono text-xs select-text scroll-smooth bg-[#050507]"
          >
            {filteredLogs.length === 0 ? (
              <div className="h-full flex items-center justify-center text-zinc-500 text-xs gap-2">
                <span className="w-4 h-4 rounded-full border-2 border-emerald-400/30 border-t-emerald-400 animate-spin" />
                <span>Connecting to telemetry socket stream...</span>
              </div>
            ) : (
              filteredLogs.map((log) => {
                const isThreat = log.type === 'threat';
                return (
                  <div
                    key={log.uniqueKey}
                    className={`p-2 rounded-lg border transition-all duration-300 animate-log-slide ${
                      isThreat
                        ? 'bg-[#C10230]/20 border-l-4 border-l-[#C10230] border-zinc-800 text-[#ffb3c1] shadow-[0_0_18px_rgba(193,2,48,0.35)]'
                        : 'bg-[#0e0e11] border-zinc-900 text-zinc-300 hover:bg-[#16161a]'
                    }`}
                  >
                    <div className="flex items-center justify-between text-[10px] mb-1 opacity-90">
                      <div className="flex items-center space-x-2">
                        <span className="text-zinc-500">[{log.streamTime}]</span>
                        <span className={`px-1.5 py-0.2 rounded font-bold ${
                          log.source === 'LINUX' ? 'bg-zinc-800 text-zinc-200' :
                          log.source === 'WINDOWS' ? 'bg-zinc-800 text-zinc-200' :
                          log.source === 'APACHE' ? 'bg-zinc-800 text-zinc-200' : 'bg-zinc-800 text-zinc-200'
                        }`}>
                          {log.source}
                        </span>
                        <span className="text-zinc-400">{log.ip}</span>
                        <span className="text-zinc-600">➔</span>
                        <span className="text-zinc-400">{log.host}</span>
                      </div>

                      {isThreat && (
                        <span className="px-1.5 py-0.2 rounded bg-[#C10230] text-white font-bold tracking-wider animate-pulse text-[9px] shadow-sm">
                          ⚡ THREAT DETECTED
                        </span>
                      )}
                    </div>

                    <div className={`text-[11px] leading-snug break-all ${isThreat ? 'font-bold text-[#ffccd5]' : 'text-zinc-300'}`}>
                      {log.msg}
                    </div>
                  </div>
                );
              })
            )}
          </div>

          <div className="px-3.5 py-1.5 bg-[#111114] border-t border-zinc-800 flex justify-between items-center text-[10px] font-mono text-zinc-400">
            <span>Buffer: 45 events (Auto-pruned)</span>
            <span className="text-emerald-400 font-semibold flex items-center gap-1.5">
              <span className="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-ping inline-block" />
              Stream Status: ACTIVE
            </span>
          </div>
        </div>

        {/* Right Column (5 Cols): AI Cognitive Threat Interceptor */}
        <div className="lg:col-span-5 flex flex-col h-[520px] rounded-xl bg-[#09090b] border border-zinc-800 overflow-hidden shadow-2xl">
          {/* Radar Header */}
          <div className="px-4 py-2.5 bg-[#111114] border-b border-zinc-800 flex justify-between items-center text-xs font-mono">
            <div className="flex items-center space-x-2">
              <ShieldAlert className="w-4 h-4 text-[#ff4d6d]" />
              <span className="font-bold text-white">AI THREAT INTERCEPTOR</span>
            </div>
            <span className="text-[10px] px-2 py-0.5 rounded bg-[#C10230]/20 text-[#ff4d6d] border border-[#C10230]/40 font-bold flex items-center gap-1">
              <span className="w-1.5 h-1.5 rounded-full bg-[#ff4d6d] animate-ping" />
              {interceptedThreats.length} Interceptions
            </span>
          </div>

          {/* Intercepted Threats Feed */}
          <div className="flex-1 p-3.5 overflow-y-auto space-y-3 bg-[#050507]">
            {interceptedThreats.length === 0 ? (
              <div className="h-full flex flex-col items-center justify-center text-center p-6 text-zinc-500">
                <div className="w-14 h-14 rounded-full bg-[#111114] border border-zinc-800 flex items-center justify-center mb-3 relative">
                  <span className="absolute inset-0 rounded-full border border-zinc-700 animate-ping opacity-30" />
                  <Cpu className="w-6 h-6 text-zinc-400 animate-spin" />
                </div>
                <div className="text-xs font-mono text-zinc-300 font-bold">Listening to Telemetry Stream...</div>
                <div className="text-[11px] text-zinc-500 font-mono mt-1 max-w-xs">
                  Threat signatures automatically trigger RAG reasoning cards and NIST containment playbooks
                </div>
              </div>
            ) : (
              interceptedThreats.map((threat, idx) => (
                <div
                  key={idx}
                  className="p-3.5 rounded-xl bg-[#111114] border-l-4 border-l-[#C10230] border border-zinc-800 hover:border-zinc-700 transition-all shadow-[0_0_20px_rgba(193,2,48,0.25)] space-y-2 animate-log-slide card-hover"
                >
                  <div className="flex items-start justify-between">
                    <div>
                      <div className="flex items-center gap-1.5">
                        <span className="w-2 h-2 rounded-full bg-[#ff4d6d] animate-ping" />
                        <span className="text-[10px] font-mono text-zinc-500">[{threat.timestamp}]</span>
                        <SeverityBadge severity={threat.severity || 'CRITICAL'} />
                      </div>
                      <h4 className="text-xs font-bold text-white mt-1">{threat.title}</h4>
                    </div>
                    <div className="text-right font-mono">
                      <div className="text-[10px] text-zinc-400 font-semibold">CVSS RISK</div>
                      <div className="text-sm font-bold text-[#ff4d6d]">{threat.riskScore}/100</div>
                    </div>
                  </div>

                  {/* MITRE ATT&CK Attribution Badge */}
                  <div className="p-2 rounded-lg bg-[#09090b] border border-zinc-800 flex items-center justify-between text-[11px] font-mono">
                    <span className="text-white font-bold">{threat.mitre}</span>
                    <span className="text-zinc-400">{threat.tactic}</span>
                  </div>

                  {/* Automated Action */}
                  <div className="text-[10px] text-emerald-400 font-mono flex items-center gap-1 font-semibold">
                    <ShieldCheck className="w-3 h-3 shrink-0" />
                    <span>{threat.action}</span>
                  </div>
                </div>
              ))
            )}
          </div>

          <div className="p-3 bg-[#111114] border-t border-zinc-800 flex justify-between items-center text-xs font-mono">
            <span className="text-zinc-500 text-[10px]">ChromaDB Index: T1110, T1548, T1190</span>
            <button
              onClick={() => onSelectIncident(1)}
              className="text-white hover:underline text-[11px] flex items-center gap-1 font-bold group"
            >
              <span>View Full Incident Triage</span>
              <ArrowRight className="w-3 h-3 transition-transform group-hover:translate-x-1" />
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}
