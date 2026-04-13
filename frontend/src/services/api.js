export async function getHealth(apiUrl) {
  const response = await fetch(`${apiUrl}/health`)
  if (!response.ok) throw new Error('Health check failed')
  return response.json()
}

export async function fetchComplaints(apiUrl) {
  const response = await fetch(`${apiUrl}/complaints/`)
  if (!response.ok) return []
  return response.json()
}

export async function fetchDashboard(apiUrl) {
  const response = await fetch(`${apiUrl}/dashboard/summary`)
  if (!response.ok) return null
  return response.json()
}

export async function fetchLocations(apiUrl) {
  const response = await fetch(`${apiUrl}/dashboard/locations`)
  if (!response.ok) return { locations: [] }
  return response.json()
}
