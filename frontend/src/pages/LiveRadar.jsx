import React, { useState, useEffect, useRef } from 'react';
import { 
  Radio, Play, Pause, ShieldAlert, 
  Terminal, ShieldCheck, Cpu, ArrowRight, Zap, Layers
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
  };

  const filteredLogs = activeTabFilter === 'threats' ? logs.filter(l => l.type === 'threat') : logs;

  return (
    <div className="p-6 space-y-5 max-w-7xl mx-auto">
      {/* Header & Controls */}
      <div className="flex flex-col md:flex-row md:items-center justify-between gap-4 pb-3 border-b border-zinc-800">
        <div>
          <h1 className="text-xl font-bold tracking-tight text-white flex items-center gap-2.5">
            <Radio className="w-5 h-5 text-emerald-400 animate-pulse" />
            LIVE TELEMETRY STREAM & AI RADAR
          </h1>
          <p className="text-xs text-zinc-400 font-mono mt-0.5">
            Real-time Log Stream • Automated RAG Threat Interception • Zero Delay Detection
          </p>
        </div>

        {/* Playback Controls */}
        <div className="flex items-center space-x-2.5">
          <button
            onClick={() => setIsPlaying(!isPlaying)}
            className="flex items-center space-x-1.5 px-3 py-1.5 rounded-lg text-xs font-semibold font-mono border border-zinc-700 bg-zinc-900 text-zinc-300 hover:text-white transition-all shadow-sm"
          >
            {isPlaying ? <Pause className="w-3.5 h-3.5 text-amber-400" /> : <Play className="w-3.5 h-3.5 text-emerald-400" />}
            <span>{isPlaying ? 'Pause Stream' : 'Resume Stream'}</span>
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

          {/* Trigger Attack Wave Button: NexBank Signature Crimson */}
          <button
            onClick={triggerAttackWave}
            className="flex items-center space-x-1.5 px-3.5 py-1.5 rounded-lg bg-[#C10230] hover:bg-[#9E0025] text-white border border-[#C10230] text-xs font-mono font-bold shadow-[0_0_15px_rgba(193,2,48,0.35)] active:scale-95 transition-all"
          >
            <Zap className="w-3.5 h-3.5 text-white" />
            <span>Simulate Attack Wave</span>
          </button>
        </div>
      </div>

      {/* Pictorial Threat Kill Chain / Attack Flow Diagram */}
      <div className="p-4 rounded-xl bg-[#111114] border border-zinc-800">
        <div className="text-[11px] font-mono uppercase text-zinc-400 font-bold mb-3 flex items-center justify-between">
          <span className="flex items-center gap-1.5 text-white">
            <Layers className="w-3.5 h-3.5 text-zinc-300" />
            Automated Threat Interception Architecture (Real-Time Pipeline)
          </span>
          <span className="text-[10px] text-emerald-400 font-mono">MITRE Grounding: Sub-15ms</span>
        </div>

        <div className="grid grid-cols-1 sm:grid-cols-4 gap-3 text-center text-xs font-mono">
          <div className="p-3 bg-[#09090b] rounded-lg border border-zinc-800 relative">
            <div className="text-[10px] text-zinc-500 font-semibold">STAGE 1: INGESTION</div>
            <div className="font-bold text-white mt-1">Raw Telemetry Stream</div>
            <div className="text-[10px] text-zinc-400 mt-0.5">Windows, Linux, Apache, FW</div>
            <div className="hidden sm:block absolute -right-2.5 top-1/2 -translate-y-1/2 text-zinc-600">➔</div>
          </div>

          <div className="p-3 bg-[#09090b] rounded-lg border border-zinc-800 relative">
            <div className="text-[10px] text-zinc-500 font-semibold">STAGE 2: NORMALIZATION</div>
            <div className="font-bold text-white mt-1">ECS Pydantic Parser</div>
            <div className="text-[10px] text-zinc-400 mt-0.5">Regex Signature Matching</div>
            <div className="hidden sm:block absolute -right-2.5 top-1/2 -translate-y-1/2 text-zinc-600">➔</div>
          </div>

          <div className="p-3 bg-[#09090b] rounded-lg border border-zinc-800 relative">
            <div className="text-[10px] text-zinc-500 font-semibold">STAGE 3: RAG VECTOR DB</div>
            <div className="font-bold text-white mt-1">ChromaDB MITRE v14</div>
            <div className="text-[10px] text-zinc-400 mt-0.5">Zero-Hallucination k-NN</div>
            <div className="hidden sm:block absolute -right-2.5 top-1/2 -translate-y-1/2 text-zinc-600">➔</div>
          </div>

          <div className="p-3 bg-[#09090b] rounded-lg border border-[#C10230]/40 bg-[#C10230]/5">
            <div className="text-[10px] text-[#ff4d6d] font-semibold">STAGE 4: CONTAINMENT</div>
            <div className="font-bold text-white mt-1">CVSS Risk & Playbook</div>
            <div className="text-[10px] text-[#ffb3c1] mt-0.5">NIST SP 800-61 PDF</div>
          </div>
        </div>
      </div>

      {/* Main Split Grid: Live Stream vs AI Interceptor */}
      <div className="grid grid-cols-1 lg:grid-cols-12 gap-5">
        {/* Left Column (7 Cols): Live Telemetry Stream */}
        <div className="lg:col-span-7 flex flex-col h-[520px] rounded-xl bg-[#09090b] border border-zinc-800 overflow-hidden shadow-2xl">
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
                className={`px-2.5 py-1 rounded text-[10px] font-bold transition-colors ${activeTabFilter === 'all' ? 'bg-white text-black' : 'bg-zinc-900 text-zinc-400 hover:text-white border border-zinc-800'}`}
              >
                All Telemetry ({logs.length})
              </button>
              <button
                onClick={() => setActiveTabFilter('threats')}
                className={`px-2.5 py-1 rounded text-[10px] font-bold transition-colors ${activeTabFilter === 'threats' ? 'bg-[#C10230] text-white shadow-sm' : 'bg-zinc-900 text-zinc-400 hover:text-white border border-zinc-800'}`}
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
              <div className="h-full flex items-center justify-center text-zinc-500 text-xs">
                Connecting to telemetry socket stream...
              </div>
            ) : (
              filteredLogs.map((log) => {
                const isThreat = log.type === 'threat';
                return (
                  <div
                    key={log.uniqueKey}
                    className={`p-2 rounded-lg border transition-all duration-300 animate-log-slide ${
                      isThreat
                        ? 'bg-[#C10230]/15 border-l-4 border-l-[#C10230] border-zinc-800 text-[#ffb3c1] shadow-[0_0_15px_rgba(193,2,48,0.2)]'
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
            <span className="text-emerald-400 font-semibold">Stream Status: ACTIVE</span>
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
            <span className="text-[10px] px-2 py-0.5 rounded bg-[#C10230]/20 text-[#ff4d6d] border border-[#C10230]/40 font-bold">
              {interceptedThreats.length} Interceptions
            </span>
          </div>

          {/* Intercepted Threats Feed */}
          <div className="flex-1 p-3.5 overflow-y-auto space-y-3 bg-[#050507]">
            {interceptedThreats.length === 0 ? (
              <div className="h-full flex flex-col items-center justify-center text-center p-6 text-zinc-500">
                <div className="w-12 h-12 rounded-full bg-[#111114] border border-zinc-800 flex items-center justify-center mb-3">
                  <Cpu className="w-6 h-6 text-zinc-500 animate-spin" />
                </div>
                <div className="text-xs font-mono text-zinc-400">Listening to Telemetry Stream...</div>
                <div className="text-[11px] text-zinc-600 font-mono mt-1">
                  Threat signatures will automatically trigger RAG reasoning cards here
                </div>
              </div>
            ) : (
              interceptedThreats.map((threat, idx) => (
                <div
                  key={idx}
                  className="p-3.5 rounded-xl bg-[#111114] border-l-4 border-l-[#C10230] border border-zinc-800 hover:border-zinc-700 transition-all shadow-[0_0_15px_rgba(193,2,48,0.15)] space-y-2 animate-log-slide"
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
              className="text-white hover:underline text-[11px] flex items-center gap-1 font-bold"
            >
              <span>View Full Incident Triage</span>
              <ArrowRight className="w-3 h-3" />
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}
