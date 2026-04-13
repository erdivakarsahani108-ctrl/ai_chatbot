function Dashboard({ summary, locations }) {
  return (
    <div className="dashboard-panel">
      <h3>State & Department Dashboard</h3>
      <div className="dashboard-grid">
        <div className="dashboard-card">
          <strong>Total Complaints</strong>
          <p>{summary?.total_complaints ?? 0}</p>
        </div>
        <div className="dashboard-card">
          <strong>Top Department</strong>
          <p>{summary?.department_breakdown?.[0]?.name ?? 'N/A'}</p>
        </div>
        <div className="dashboard-card">
          <strong>Top State</strong>
          <p>{summary?.state_breakdown?.[0]?.name ?? 'N/A'}</p>
        </div>
      </div>
      <div className="dashboard-section">
        <h4>Status Breakdown</h4>
        <ul>
          {summary?.status_breakdown.map((item) => (
            <li key={item.name}>
              {item.name}: {item.value}
            </li>
          ))}
        </ul>
      </div>
      <div className="dashboard-section">
        <h4>State / District Locations</h4>
        <div className="location-grid">
          {locations?.slice(0, 12).map((item) => (
            <span key={`${item.state}-${item.district}`}>{item.state} / {item.district}</span>
          ))}
        </div>
      </div>
    </div>
  )
}

export default Dashboard
