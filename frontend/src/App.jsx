import React, { useState, useEffect } from 'react';
import Navbar from './components/Navbar';
import Sidebar from './components/Sidebar';
import LogUploadModal from './components/LogUploadModal';
import Login from './pages/Login';
import Dashboard from './pages/Dashboard';
import Incidents from './pages/Incidents';
import IncidentDetail from './pages/IncidentDetail';
import LogAnalyzer from './pages/LogAnalyzer';
import CopilotChat from './pages/CopilotChat';
import LiveRadar from './pages/LiveRadar';

export default function App() {
  const [currentUser, setCurrentUser] = useState(() => {
    const saved = localStorage.getItem('cybersentinel_user');
    return saved ? JSON.parse(saved) : null;
  });

  const [activeTab, setActiveTab] = useState('radar');
  const [selectedIncidentId, setSelectedIncidentId] = useState(null);
  const [isUploadModalOpen, setIsUploadModalOpen] = useState(false);
  const [copilotIncidentContext, setCopilotIncidentContext] = useState(null);

  const handleLoginSuccess = (userData) => {
    setCurrentUser(userData);
    setActiveTab('dashboard');
  };

  const handleLogout = () => {
    localStorage.removeItem('cybersentinel_token');
    localStorage.removeItem('cybersentinel_user');
    setCurrentUser(null);
    setSelectedIncidentId(null);
  };

  const handleSelectIncident = (id) => {
    setSelectedIncidentId(id);
  };

  const handleBackFromDetail = () => {
    setSelectedIncidentId(null);
  };

  const handleOpenCopilotForIncident = (id) => {
    setCopilotIncidentContext(id);
    setSelectedIncidentId(null);
    setActiveTab('copilot');
  };

  const handleUploadSuccess = () => {
    // Return to dashboard and refresh data
    setActiveTab('dashboard');
  };

  if (!currentUser) {
    return <Login onLoginSuccess={handleLoginSuccess} />;
  }

  return (
    <div className="min-h-screen bg-cyber-bg text-cyber-text flex flex-col">
      <Navbar
        currentUser={currentUser}
        onLogout={handleLogout}
        onOpenUpload={() => setIsUploadModalOpen(true)}
      />

      <div className="flex flex-1">
        <Sidebar activeTab={activeTab} setActiveTab={(tab) => {
          setActiveTab(tab);
          setSelectedIncidentId(null);
        }} />

        <main className="flex-1 overflow-y-auto bg-[#080c14]">
          {selectedIncidentId ? (
            <IncidentDetail
              incidentId={selectedIncidentId}
              onBack={handleBackFromDetail}
              onOpenCopilotForIncident={handleOpenCopilotForIncident}
            />
          ) : activeTab === 'radar' ? (
            <LiveRadar
              onSelectIncident={handleSelectIncident}
            />
          ) : activeTab === 'dashboard' ? (
            <Dashboard
              onSelectIncident={handleSelectIncident}
              onOpenUpload={() => setIsUploadModalOpen(true)}
            />
          ) : activeTab === 'incidents' ? (
            <Incidents onSelectIncident={handleSelectIncident} />
          ) : activeTab === 'logs' ? (
            <LogAnalyzer onOpenUpload={() => setIsUploadModalOpen(true)} />
          ) : activeTab === 'copilot' ? (
            <CopilotChat activeIncidentId={copilotIncidentContext} />
          ) : null}
        </main>
      </div>

      <LogUploadModal
        isOpen={isUploadModalOpen}
        onClose={() => setIsUploadModalOpen(false)}
        onUploadSuccess={handleUploadSuccess}
      />
    </div>
  );
}
