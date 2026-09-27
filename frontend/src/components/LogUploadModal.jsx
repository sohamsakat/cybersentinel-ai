import React, { useState } from 'react';
import { X, UploadCloud, FileText, AlertCircle, Loader2, Sparkles, Server } from 'lucide-react';
import { uploadLogFile } from '../api/client';

export default function LogUploadModal({ isOpen, onClose, onUploadSuccess }) {
  const [selectedFile, setSelectedFile] = useState(null);
  const [sourceType, setSourceType] = useState('');
  const [isUploading, setIsUploading] = useState(false);
  const [uploadProgress, setUploadProgress] = useState('');
  const [error, setError] = useState(null);

  if (!isOpen) return null;

  // Sample datasets for quick demo testing
  const samplePresets = [
    {
      name: 'Linux SSH Attack',
      type: 'linux_syslog',
      filename: 'sample_linux_ssh_attack.log',
      content: `Oct 14 03:14:15 srv-prod-01 sshd[19001]: Failed password for invalid user admin from 198.51.100.45 port 41256 ssh2
Oct 14 03:14:18 srv-prod-01 sshd[19003]: Failed password for invalid user admin from 198.51.100.45 port 41258 ssh2
Oct 14 03:14:21 srv-prod-01 sshd[19005]: Failed password for invalid user root from 198.51.100.45 port 41260 ssh2
Oct 14 03:14:50 srv-prod-01 sshd[19022]: Accepted password for deploy from 198.51.100.45 port 41286 ssh2
Oct 14 03:15:20 srv-prod-01 sudo:   deploy : 3 incorrect password attempts ; TTY=pts/0 ; PWD=/home/deploy ; USER=root ; COMMAND=/bin/cat /etc/shadow`,
    },
    {
      name: 'Windows Brute Force',
      type: 'windows',
      filename: 'sample_windows_event_log.json',
      content: JSON.stringify([
        {
          EventID: 4625,
          TimeCreated: new Date().toISOString(),
          Computer: 'DC01.corp.internal',
          Channel: 'Security',
          EventData: { TargetUserName: 'Administrator', IpAddress: '192.168.1.185', SubStatus: '0xC000006A' }
        },
        {
          EventID: 4625,
          TimeCreated: new Date().toISOString(),
          Computer: 'DC01.corp.internal',
          Channel: 'Security',
          EventData: { TargetUserName: 'Administrator', IpAddress: '192.168.1.185', SubStatus: '0xC000006A' }
        },
        {
          EventID: 4672,
          TimeCreated: new Date().toISOString(),
          Computer: 'DC01.corp.internal',
          Channel: 'Security',
          EventData: { SubjectUserName: 'Administrator', PrivilegeList: 'SeDebugPrivilege\nSeTakeOwnershipPrivilege' }
        }
      ], null, 2),
    },
    {
      name: 'Apache SQL Injection',
      type: 'apache',
      filename: 'sample_apache_sqli.log',
      content: `203.0.113.88 - - [11/Sep/2026:10:15:02 +0000] "GET /products.php?category=electronics' OR '1'='1 HTTP/1.1" 200 15230 "-" "sqlmap/1.7#stable"
203.0.113.88 - - [11/Sep/2026:10:15:05 +0000] "GET /products.php?category=1 UNION SELECT null,username,password,email FROM users-- HTTP/1.1" 200 18450 "-" "sqlmap/1.7#stable"
203.0.113.88 - - [11/Sep/2026:10:15:15 +0000] "GET /view.php?page=../../../../etc/passwd HTTP/1.1" 200 2400 "-" "Mozilla/5.0"`,
    },
  ];

  const handleFileChange = (e) => {
    if (e.target.files && e.target.files[0]) {
      setSelectedFile(e.target.files[0]);
      setError(null);
    }
  };

  const handleLoadSample = (sample) => {
    const blob = new Blob([sample.content], { type: 'text/plain' });
    const file = new File([blob], sample.filename, { type: 'text/plain' });
    setSelectedFile(file);
    setSourceType(sample.type);
    setError(null);
  };

  const handleUpload = async () => {
    if (!selectedFile) {
      setError('Please select a file or choose a demo sample log.');
      return;
    }

    setIsUploading(true);
    setError(null);

    try {
      setUploadProgress('Normalizing security telemetry events...');
      await new Promise(r => setTimeout(r, 600));

      setUploadProgress('Executing ChromaDB MITRE ATT&CK vector search...');
      await new Promise(r => setTimeout(r, 600));

      setUploadProgress('Synthesizing CVSS Risk Score & Mitigation Playbook...');
      const response = await uploadLogFile(selectedFile, sourceType || null);

      setUploadProgress('Analysis complete!');
      await new Promise(r => setTimeout(r, 400));

      setIsUploading(false);
      onUploadSuccess(response);
      onClose();
    } catch (err) {
      setIsUploading(false);
      setError(err.response?.data?.detail || 'Log analysis failed. Please verify format.');
    }
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/80 backdrop-blur-sm animate-fadeIn">
      <div className="bg-[#111114] border border-zinc-800 rounded-2xl w-full max-w-xl overflow-hidden shadow-2xl">
        {/* Header */}
        <div className="px-6 py-4 border-b border-zinc-800 flex justify-between items-center bg-[#09090b]">
          <div className="flex items-center space-x-2.5">
            <div className="w-8 h-8 rounded-lg bg-white/10 border border-white/20 flex items-center justify-center text-white">
              <UploadCloud className="w-4 h-4" />
            </div>
            <div>
              <h3 className="text-sm font-semibold text-white">Ingest Security Logs</h3>
              <p className="text-[11px] text-zinc-400">Multi-format parser & AI RAG Threat Correlation</p>
            </div>
          </div>
          <button
            onClick={onClose}
            disabled={isUploading}
            className="text-zinc-400 hover:text-white p-1 rounded-lg hover:bg-zinc-800 transition-colors"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Body */}
        <div className="p-6 space-y-5 bg-[#111114]">
          {/* Quick Demo Presets */}
          <div>
            <label className="text-[11px] font-mono uppercase text-zinc-400 block mb-2 flex items-center gap-1.5 font-semibold">
              <Sparkles className="w-3.5 h-3.5 text-amber-400" />
              Quick Demo Presets (1-Click Viva Demonstration)
            </label>
            <div className="grid grid-cols-3 gap-2">
              {samplePresets.map((preset) => (
                <button
                  key={preset.name}
                  type="button"
                  onClick={() => handleLoadSample(preset)}
                  className="px-2.5 py-2 rounded-lg bg-[#09090b] border border-zinc-800 hover:border-zinc-600 hover:bg-[#18181c] text-[11px] font-medium text-zinc-300 transition-all text-left flex items-center gap-2 group"
                >
                  <Server className="w-3.5 h-3.5 text-zinc-400 group-hover:scale-110 transition-transform" />
                  <span className="truncate">{preset.name}</span>
                </button>
              ))}
            </div>
          </div>

          {/* Upload Area */}
          <div className="border-2 border-dashed border-zinc-800 hover:border-zinc-600 rounded-xl p-6 text-center transition-colors bg-[#09090b]">
            <input
              type="file"
              id="logFileInput"
              className="hidden"
              accept=".log,.json,.csv,.txt"
              onChange={handleFileChange}
              disabled={isUploading}
            />
            <label htmlFor="logFileInput" className="cursor-pointer block">
              <div className="w-12 h-12 rounded-full bg-[#111114] border border-zinc-700 flex items-center justify-center mx-auto mb-3 text-zinc-300">
                <FileText className="w-6 h-6 text-white" />
              </div>
              <p className="text-xs font-semibold text-white mb-1">
                {selectedFile ? selectedFile.name : 'Click to browse or drop security logs here'}
              </p>
              <p className="text-[11px] text-zinc-500 font-mono">
                Supports: Windows Event (JSON), Linux Syslog (.log), Apache Web, Firewall (CSV)
              </p>
            </label>
          </div>

          {/* Source Type Override */}
          <div className="grid grid-cols-2 gap-4">
            <div>
              <label className="text-[11px] font-mono text-zinc-400 block mb-1 font-semibold">
                Log Format Parser
              </label>
              <select
                value={sourceType}
                onChange={(e) => setSourceType(e.target.value)}
                className="w-full bg-[#09090b] border border-zinc-800 rounded-lg px-3 py-2 text-xs text-zinc-200 focus:outline-none focus:border-white font-mono"
              >
                <option value="">Auto-Detect Format</option>
                <option value="windows">Windows Event (JSON)</option>
                <option value="linux_syslog">Linux Syslog / Auth</option>
                <option value="apache">Apache Web Access</option>
                <option value="firewall">Firewall Telemetry (CSV)</option>
              </select>
            </div>

            <div>
              <label className="text-[11px] font-mono text-zinc-400 block mb-1 font-semibold">
                Analysis Engine
              </label>
              <div className="bg-[#09090b] border border-zinc-800 rounded-lg px-3 py-2 text-xs text-zinc-400 font-mono flex items-center justify-between">
                <span>RAG + ChromaDB</span>
                <span className="text-emerald-400 font-bold text-[10px]">ACTIVE</span>
              </div>
            </div>
          </div>

          {/* Error message */}
          {error && (
            <div className="p-3 bg-[#C10230]/10 border border-[#C10230]/40 rounded-lg text-xs text-[#ff4d6d] flex items-center gap-2">
              <AlertCircle className="w-4 h-4 shrink-0 text-[#ff4d6d]" />
              <span>{error}</span>
            </div>
          )}

          {/* Uploading progress status */}
          {isUploading && (
            <div className="p-3.5 bg-zinc-900 border border-zinc-800 rounded-lg text-xs text-zinc-200 space-y-2">
              <div className="flex items-center gap-2 font-mono">
                <Loader2 className="w-4 h-4 animate-spin text-white" />
                <span>{uploadProgress}</span>
              </div>
              <div className="w-full bg-[#09090b] h-1.5 rounded-full overflow-hidden">
                <div className="bg-white h-full rounded-full animate-pulse w-3/4" />
              </div>
            </div>
          )}
        </div>

        {/* Footer */}
        <div className="px-6 py-3.5 border-t border-zinc-800 bg-[#09090b] flex justify-end space-x-3">
          <button
            type="button"
            onClick={onClose}
            disabled={isUploading}
            className="px-4 py-2 rounded-lg text-xs font-semibold text-zinc-400 hover:text-white hover:bg-zinc-800 transition-colors"
          >
            Cancel
          </button>
          <button
            type="button"
            onClick={handleUpload}
            disabled={isUploading || !selectedFile}
            className="px-5 py-2 rounded-lg text-xs font-bold bg-white hover:bg-zinc-200 disabled:opacity-40 text-black transition-all border border-white shadow-sm flex items-center gap-2 active:scale-95"
          >
            {isUploading ? (
              <>
                <Loader2 className="w-3.5 h-3.5 animate-spin" />
                <span>Analyzing Telemetry...</span>
              </>
            ) : (
              <>
                <Sparkles className="w-3.5 h-3.5 text-black" />
                <span>Trigger AI Triage</span>
              </>
            )}
          </button>
        </div>
      </div>
    </div>
  );
}
