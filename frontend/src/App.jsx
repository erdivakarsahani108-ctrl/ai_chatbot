import { useEffect, useState } from 'react'
import ComplaintForm from './components/ComplaintForm'
import ChatBot from './components/ChatBot'
import Dashboard from './components/Dashboard'
import { fetchComplaints, fetchDashboard, fetchLocations, getHealth } from './services/api'

const getApiUrl = async () => {
  const defaultUrl =
    import.meta.env.VITE_API_BASE_URL ||
    'https://ai-chatbot-1-z5wf.onrender.com'

  try {
    const res = await fetch(`${defaultUrl}/health`)
    if (res.ok) return defaultUrl
  } catch (e) {}

  return defaultUrl
}

let apiUrl =
  import.meta.env.VITE_API_BASE_URL ||
  'https://ai-chatbot-1-z5wf.onrender.com'

function App() {
  const [complaints, setComplaints] = useState([])
  const [health, setHealth] = useState(null)
  const [dashboard, setDashboard] = useState(null)
  const [locations, setLocations] = useState([])
  const [message, setMessage] = useState('Loading portal...')
  const [currentApiUrl, setCurrentApiUrl] = useState(apiUrl)

  useEffect(() => {
    const detectApi = async () => {
      const detectedUrl = await getApiUrl()
      console.log('Detected API URL:', detectedUrl)

      setCurrentApiUrl(detectedUrl)
      apiUrl = detectedUrl

      getHealth(detectedUrl)
        .then((data) => {
          console.log('Health check passed:', data)
          setHealth(data)
          setMessage('GovTech Grievance Portal connected.')
        })
        .catch((err) => {
          console.error('Health check failed:', err)
          setMessage('Backend not reachable. Start the API and refresh.')
        })
    }

    detectApi()
  }, [])

  useEffect(() => {
    if (currentApiUrl) {
      fetchComplaints(currentApiUrl)
        .then(setComplaints)
        .catch(() => setComplaints([]))

      fetchDashboard(currentApiUrl)
        .then(setDashboard)
        .catch(() => setDashboard(null))

      fetchLocations(currentApiUrl)
        .then((data) => setLocations(data.locations || []))
        .catch(() => setLocations([]))
    }
  }, [currentApiUrl])

  return (
    <div className="app-shell">
      <header className="app-header">
        <div>
          <h1>GovTech Grievance Portal</h1>
          <p>{message}</p>
        </div>

        {health && (
          <div className="status-chip">
            <strong>API:</strong> {health.status} | <strong>DB:</strong>{' '}
            {health.database}
          </div>
        )}
      </header>

      <main className="app-grid">
        <section className="panel panel-left">
          <h2>Submit a grievance</h2>
          <ComplaintForm apiUrl={currentApiUrl} onSuccess={setComplaints} />
          <div className="panel-divider" />
          <ChatBot apiUrl={currentApiUrl} />
        </section>

        <section className="panel panel-right">
          <Dashboard summary={dashboard} locations={locations} />
          <div className="panel-divider" />

          <h2>Recent complaints</h2>

          {complaints.length === 0 ? (
            <p>No complaints yet.</p>
          ) : (
            <div className="complaint-list">
              {complaints.map((item) => (
                <article key={item.ticket_id} className="complaint-card">
                  <div className="complaint-header">
                    <span>{item.ticket_id}</span>
                    <strong>{item.status}</strong>
                  </div>

                  <h3>{item.title}</h3>
                  <p>{item.description}</p>

                  <div className="complaint-meta">
                    <span>{item.department}</span>
                    <span>{item.priority}</span>
                  </div>
                </article>
              ))}
            </div>
          )}
        </section>
      </main>
    </div>
  )
}

export default App