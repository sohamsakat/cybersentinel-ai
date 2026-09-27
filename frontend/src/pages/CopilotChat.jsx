import React, { useState } from 'react';
import { Send, Bot, User, BookOpen, Loader2 } from 'lucide-react';
import { sendCopilotMessage } from '../api/client';

export default function CopilotChat({ activeIncidentId = null }) {
  const [messages, setMessages] = useState([
    {
      role: 'assistant',
      content: `Hello Analyst. I am **CyberSentinel Copilot**, an AI SOC assistant strictly grounded in the **MITRE ATT&CK Framework (v14)**, **OWASP Top 10**, and verified incident logs.\n\nI can assist with:\n- Investigating active incident telemetry & IoCs\n- Formulating NIST SP 800-61 containment playbooks\n- Explaining adversary tactics, techniques, and procedures (TTPs)\n- Synthesizing firewall/WAF defensive rule configurations\n\nHow can I support your investigation today?`,
      cited_sources: ['MITRE ATT&CK v14', 'NIST SP 800-61'],
    },
  ]);
  const [inputQuery, setInputQuery] = useState('');
  const [incidentContextId, setIncidentContextId] = useState(activeIncidentId || '');
  const [isLoading, setIsLoading] = useState(false);

  const quickPrompts = [
    'How do I mitigate MITRE technique T1110 Brute Force?',
    'What is the difference between MITRE T1110 and T1078 Valid Accounts?',
    'Explain the attack progression in Incident #1',
    'Generate iptables rules to drop traffic from 198.51.100.45',
  ];

  const handleSendMessage = async (queryText = null) => {
    const textToSend = queryText || inputQuery;
    if (!textToSend.trim() || isLoading) return;

    const userMessage = { role: 'user', content: textToSend };
    setMessages(prev => [...prev, userMessage]);
    setInputQuery('');
    setIsLoading(true);

    try {
      const response = await sendCopilotMessage(
        textToSend,
        incidentContextId ? parseInt(incidentContextId, 10) : null
      );
      const assistantMessage = {
        role: 'assistant',
        content: response.answer,
        cited_sources: response.cited_sources || [],
      };
      setMessages(prev => [...prev, assistantMessage]);
    } catch (err) {
      setMessages(prev => [
        ...prev,
        {
          role: 'assistant',
          content: 'Error: Unable to retrieve intelligence from vector database. Please ensure backend is running.',
          cited_sources: [],
        },
      ]);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="p-6 max-w-5xl mx-auto h-[calc(100vh-5rem)] flex flex-col space-y-4">
      {/* Header Banner */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between pb-3 border-b border-zinc-800 gap-2">
        <div>
          <h1 className="text-xl font-bold tracking-tight text-white flex items-center gap-2">
            <Bot className="w-5 h-5 text-white" />
            SECOPS AI COPILOT
          </h1>
          <p className="text-xs text-zinc-400 font-mono mt-0.5">
            RAG-Grounded Incident Advisory • Zero Hallucination Guarantee
          </p>
        </div>

        {/* Incident Context Selector */}
        <div className="flex items-center space-x-2 bg-[#111114] border border-zinc-800 px-3 py-1.5 rounded-lg">
          <span className="text-[11px] font-mono text-zinc-400 font-semibold">Context:</span>
          <input
            type="number"
            placeholder="Global (or Incident #)"
            value={incidentContextId}
            onChange={(e) => setIncidentContextId(e.target.value)}
            className="w-24 bg-transparent text-xs font-mono text-white placeholder-zinc-600 focus:outline-none"
          />
        </div>
      </div>

      {/* Messages Scroll Area */}
      <div className="flex-1 overflow-y-auto space-y-4 pr-2">
        {messages.map((msg, idx) => {
          const isUser = msg.role === 'user';
          return (
            <div
              key={idx}
              className={`flex space-x-3 ${isUser ? 'justify-end' : 'justify-start'}`}
            >
              {!isUser && (
                <div className="w-8 h-8 rounded-lg bg-white/10 border border-white/20 flex items-center justify-center text-white shrink-0">
                  <Bot className="w-4 h-4" />
                </div>
              )}

              <div
                className={`max-w-2xl rounded-xl p-4 text-xs leading-relaxed ${
                  isUser
                    ? 'bg-white text-black font-medium shadow-sm'
                    : 'bg-[#111114] border border-zinc-800 text-zinc-200'
                }`}
              >
                <div className="whitespace-pre-wrap font-sans">{msg.content}</div>

                {/* Grounding Attribution & Cited Sources */}
                {!isUser && msg.cited_sources?.length > 0 && (
                  <div className="mt-3 pt-2.5 border-t border-zinc-800/80">
                    <div className="text-[10px] font-mono text-zinc-400 uppercase mb-1.5 flex items-center gap-1 font-semibold">
                      <BookOpen className="w-3 h-3 text-emerald-400" />
                      Grounded Citations:
                    </div>
                    <div className="flex flex-wrap gap-1.5">
                      {msg.cited_sources.map((src, sIdx) => (
                        <span
                          key={sIdx}
                          className="px-2 py-0.5 rounded bg-[#09090b] border border-zinc-800 text-[10px] font-mono text-zinc-300 font-semibold"
                        >
                          {src}
                        </span>
                      ))}
                    </div>
                  </div>
                )}
              </div>

              {isUser && (
                <div className="w-8 h-8 rounded-lg bg-zinc-900 border border-zinc-800 flex items-center justify-center text-zinc-300 shrink-0">
                  <User className="w-4 h-4" />
                </div>
              )}
            </div>
          );
        })}

        {isLoading && (
          <div className="flex items-center space-x-3 text-xs font-mono text-zinc-400 pl-11">
            <Loader2 className="w-4 h-4 animate-spin text-white" />
            <span>Querying ChromaDB vector store & formulating grounded answer...</span>
          </div>
        )}
      </div>

      {/* Suggested Query Chips */}
      <div className="flex flex-wrap gap-2 pt-1">
        {quickPrompts.map((prompt, pIdx) => (
          <button
            key={pIdx}
            disabled={isLoading}
            onClick={() => handleSendMessage(prompt)}
            className="text-[11px] font-mono px-3 py-1.5 rounded-lg bg-[#111114] border border-zinc-800 hover:border-zinc-600 text-zinc-300 hover:text-white transition-colors text-left"
          >
            {prompt}
          </button>
        ))}
      </div>

      {/* Input Form */}
      <form
        onSubmit={(e) => {
          e.preventDefault();
          handleSendMessage();
        }}
        className="relative"
      >
        <input
          type="text"
          value={inputQuery}
          onChange={(e) => setInputQuery(e.target.value)}
          disabled={isLoading}
          placeholder="Ask Copilot about IoCs, MITRE techniques, or incident mitigation..."
          className="w-full pl-4 pr-12 py-3 bg-[#111114] border border-zinc-800 rounded-xl text-xs text-white placeholder-zinc-500 focus:outline-none focus:border-white font-sans shadow-lg"
        />
        <button
          type="submit"
          disabled={isLoading || !inputQuery.trim()}
          className="absolute right-2 top-2 p-2 bg-white hover:bg-zinc-200 text-black disabled:opacity-40 rounded-lg transition-colors"
        >
          <Send className="w-3.5 h-3.5" />
        </button>
      </form>
    </div>
  );
}
