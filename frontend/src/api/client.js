import axios from 'axios';

const API_BASE_URL = 'http://127.0.0.1:8000/api/v1';

const apiClient = axios.create({
  baseURL: API_BASE_URL,
});

// Request interceptor to attach JWT bearer token
apiClient.interceptors.request.use((config) => {
  const token = localStorage.getItem('cybersentinel_token');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

// Authentication APIs
export const loginUser = async (username, password) => {
  const params = new URLSearchParams();
  params.append('username', username);
  params.append('password', password);
  const response = await apiClient.post('/auth/login', params, {
    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
  });
  return response.data;
};

export const getCurrentUser = async () => {
  const response = await apiClient.get('/auth/me');
  return response.data;
};

// Incident APIs
export const getIncidentStats = async () => {
  const response = await apiClient.get('/incidents/stats/summary');
  return response.data;
};

export const getIncidents = async (filters = {}) => {
  const params = {};
  if (filters.severity) params.severity = filters.severity;
  if (filters.status) params.status = filters.status;
  const response = await apiClient.get('/incidents', { params });
  return response.data;
};

export const getIncidentDetail = async (id) => {
  const response = await apiClient.get(`/incidents/${id}`);
  return response.data;
};

export const updateIncidentStatus = async (id, updateData) => {
  const response = await apiClient.patch(`/incidents/${id}`, updateData);
  return response.data;
};

// Log Ingestion APIs
export const uploadLogFile = async (file, sourceType = null) => {
  const formData = new FormData();
  formData.append('file', file);
  if (sourceType) {
    formData.append('source_type', sourceType);
  }
  const response = await apiClient.post('/logs/upload', formData, {
    headers: { 'Content-Type': 'multipart/form-data' },
  });
  return response.data;
};

export const getLogBatches = async () => {
  const response = await apiClient.get('/logs/batches');
  return response.data;
};

// SecOps AI Copilot API
export const sendCopilotMessage = async (message, incidentId = null) => {
  const response = await apiClient.post('/chat', {
    message,
    incident_id: incidentId,
  });
  return response.data;
};

// PDF Report Download
export const downloadIncidentPdf = async (incidentId) => {
  const response = await apiClient.get(`/reports/incident/${incidentId}/pdf`, {
    responseType: 'blob',
  });
  const url = window.URL.createObjectURL(new Blob([response.data], { type: 'application/pdf' }));
  const link = document.createElement('a');
  link.href = url;
  link.setAttribute('download', `CyberSentinel_Incident_${incidentId}_Report.pdf`);
  document.body.appendChild(link);
  link.click();
  link.parentNode.removeChild(link);
};

export default apiClient;
