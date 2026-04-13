import { useState, useEffect } from 'react'

const departments = [
  'Police', 'Water Supply', 'Electricity', 'Municipal Corporation', 'Health Department',
  'Education', 'Road & Highways', 'Transport', 'Revenue', 'Urban Development',
  'Agriculture', 'Labour', 'Social Welfare', 'Banking', 'RTO',
  'Postal', 'Fire Safety', 'Sanitation', 'Parks & Recreation', 'Taxation',
  'Food Safety', 'Consumer Protection', 'Housing', 'Telecom', 'Grievance Redressal',
  'Sports', 'Tourism', 'Community Development', 'Disability Services', 'Women Empowerment',
  'Child Welfare', 'Disaster Management', 'Environment', 'Wildlife', 'Flood Control',
  'Public Works', 'Minority Affairs', 'Veterans Affairs', 'Pension', 'Audit',
  'Cyber Crime', 'Traffic'
]

const issueCategories = [
  'Service Disruption',
  'Infrastructure Damage',
  'Safety Hazard',
  'Billing/Payment Issue',
  'Money/Financial Problem',
  'Documentation/Records',
  'Staff Misconduct',
  'Quality/Standard Violation',
  'Unauthorized Access/Trespassing',
  'Environmental Issue',
  'Security Issue',
  'Medical Help',
  'Links/Resources Help',
  'Suggestion/Feedback',
  'Complaint Review',
  'Fraud/Scam Report',
  'Accessibility Issue',
  'Discrimination',
  'Delayed Service',
  'Other'
]

const priorities = ['Low', 'Medium', 'High']

function ComplaintForm({ apiUrl, onSuccess }) {
  const [title, setTitle] = useState('')
  const [description, setDescription] = useState('')
  const [stateName, setStateName] = useState('')
  const [district, setDistrict] = useState('')
  const [department, setDepartment] = useState('Other')
  const [priority, setPriority] = useState('Medium')
  const [category, setCategory] = useState('Other')
  const [location, setLocation] = useState('')
  const [status, setStatus] = useState('Ready to submit')
  const [states, setStates] = useState([])
  const [districts, setDistricts] = useState([])
  const [allLocations, setAllLocations] = useState([])

  useEffect(() => {
    // Fetch locations from backend
    fetch(`${apiUrl}/dashboard/locations`)
      .then((res) => res.json())
      .then((data) => {
        setAllLocations(data.locations || [])
        const uniqueStates = [...new Set(data.locations.map(loc => loc.state))].sort()
        setStates(uniqueStates)
        if (uniqueStates.length > 0) {
          setStateName(uniqueStates[0])
          updateDistricts(uniqueStates[0], data.locations)
        }
      })
      .catch(() => console.warn('Could not load locations'))
  }, [apiUrl])

  const updateDistricts = (state, locations) => {
    const stateDistricts = locations
      .filter(loc => loc.state === state)
      .map(loc => loc.district)
      .filter((d, i, arr) => arr.indexOf(d) === i)
      .sort()
    setDistricts(stateDistricts)
    if (stateDistricts.length > 0) {
      setDistrict(stateDistricts[0])
    }
  }

  const handleStateChange = (newState) => {
    setStateName(newState)
    updateDistricts(newState, allLocations)
  }

  const handleSubmit = async (event) => {
    event.preventDefault()
    setStatus('Submitting complaint...')

    try {
      const response = await fetch(`${apiUrl}/complaints/`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          title,
          description,
          state: stateName,
          district,
          department,
          priority,
          issue_category: category,
          location,
        }),
      })
      if (!response.ok) {
        throw new Error('Unable to submit complaint')
      }
      const data = await response.json()
      setStatus(`Submitted! Ticket: ${data.ticket_id}`)
      setTitle('')
      setDescription('')
      if (states.length > 0) setStateName(states[0])
      if (districts.length > 0) setDistrict(districts[0])
      setDepartment('Electricity')
      setPriority('Medium')
      setCategory('Other')
      setLocation('')
      if (typeof onSuccess === 'function') {
        onSuccess((prev) => [data, ...(prev ?? [])])
      }
    } catch (error) {
      setStatus('Submission failed. Please check the backend and try again.')
    }
  }

  return (
    <form className="complaint-form" onSubmit={handleSubmit}>
      <label>
        Complaint Title
        <input value={title} onChange={(e) => setTitle(e.target.value)} placeholder="Enter complaint title" required />
      </label>
      <label>
        Description
        <textarea value={description} onChange={(e) => setDescription(e.target.value)} placeholder="Describe your grievance in detail" required />
      </label>
      <label>
        State
        <select value={stateName} onChange={(e) => handleStateChange(e.target.value)} required>
          {states.map((state) => (
            <option key={state} value={state}>{state}</option>
          ))}
        </select>
      </label>
      <label>
        District
        <select value={district} onChange={(e) => setDistrict(e.target.value)} required>
          {districts.map((dist) => (
            <option key={dist} value={dist}>{dist}</option>
          ))}
        </select>
      </label>
      <label>
        Department
        <select value={department} onChange={(e) => setDepartment(e.target.value)}>
          {departments.map((dept) => (
            <option key={dept} value={dept}>{dept}</option>
          ))}
        </select>
      </label>
      <label>
        Priority
        <select value={priority} onChange={(e) => setPriority(e.target.value)}>
          {priorities.map((prio) => (
            <option key={prio} value={prio}>{prio}</option>
          ))}
        </select>
      </label>
      <label>
        Issue Category
        <select value={category} onChange={(e) => setCategory(e.target.value)} required>
          {issueCategories.map((cat) => (
            <option key={cat} value={cat}>{cat}</option>
          ))}
        </select>
      </label>
      <label>
        Location / Landmark
        <input value={location} onChange={(e) => setLocation(e.target.value)} placeholder="e.g. Near Indira Nagar bus stand" />
      </label>
      <button type="submit">Submit Complaint</button>
      <p className="load-bar">{status}</p>
    </form>
  )
}

export default ComplaintForm
