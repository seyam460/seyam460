import { useState } from 'react'
import { apiRequest } from './api'

const initialRideForm = {
  pickup_address: '',
  dropoff_address: '',
  pickup_lat: '',
  pickup_lng: '',
  dropoff_lat: '',
  dropoff_lng: '',
  distance_km: '',
  price_estimate: ''
}

function App() {
  const [token, setToken] = useState('')
  const [authForm, setAuthForm] = useState({ username: '', password: '', role: 'rider', email: '' })
  const [rideForm, setRideForm] = useState(initialRideForm)
  const [rides, setRides] = useState([])
  const [message, setMessage] = useState('')

  const updateAuthForm = (field) => (event) => {
    setAuthForm({ ...authForm, [field]: event.target.value })
  }

  const updateRideForm = (field) => (event) => {
    setRideForm({ ...rideForm, [field]: event.target.value })
  }

  const handleRegister = async () => {
    const payload = {
      username: authForm.username,
      password: authForm.password,
      email: authForm.email,
      role: authForm.role
    }
    const data = await apiRequest('/auth/register/', {
      method: 'POST',
      body: JSON.stringify(payload)
    })
    setToken(data.token)
    setMessage('Registration successful!')
  }

  const handleLogin = async () => {
    const payload = {
      username: authForm.username,
      password: authForm.password
    }
    const data = await apiRequest('/auth/login/', {
      method: 'POST',
      body: JSON.stringify(payload)
    })
    setToken(data.token)
    setMessage('Login successful!')
  }

  const handleRequestRide = async () => {
    const data = await apiRequest('/rides/request/', {
      method: 'POST',
      headers: { Authorization: `Token ${token}` },
      body: JSON.stringify(rideForm)
    })
    setRides([data, ...rides])
    setRideForm(initialRideForm)
    setMessage('Ride requested!')
  }

  const handleLoadRides = async () => {
    const data = await apiRequest('/rides/', {
      headers: { Authorization: `Token ${token}` }
    })
    setRides(data)
  }

  return (
    <div className="page">
      <header className="hero">
        <div>
          <p className="badge">RideShare Platform</p>
          <h1>All-in-one ride sharing software</h1>
          <p>Authenticate, request rides, match drivers, track trips, and capture payments.</p>
        </div>
        <div className="hero-card">
          <h2>Get Started</h2>
          <div className="form-grid">
            <input placeholder="Username" value={authForm.username} onChange={updateAuthForm('username')} />
            <input placeholder="Email" value={authForm.email} onChange={updateAuthForm('email')} />
            <input type="password" placeholder="Password" value={authForm.password} onChange={updateAuthForm('password')} />
            <select value={authForm.role} onChange={updateAuthForm('role')}>
              <option value="rider">Rider</option>
              <option value="driver">Driver</option>
            </select>
          </div>
          <div className="button-row">
            <button onClick={handleRegister}>Register</button>
            <button className="secondary" onClick={handleLogin}>Login</button>
          </div>
          {message && <p className="message">{message}</p>}
        </div>
      </header>

      <section className="panel">
        <h2>Request a ride</h2>
        <div className="form-grid">
          <input placeholder="Pickup address" value={rideForm.pickup_address} onChange={updateRideForm('pickup_address')} />
          <input placeholder="Dropoff address" value={rideForm.dropoff_address} onChange={updateRideForm('dropoff_address')} />
          <input placeholder="Pickup lat" value={rideForm.pickup_lat} onChange={updateRideForm('pickup_lat')} />
          <input placeholder="Pickup lng" value={rideForm.pickup_lng} onChange={updateRideForm('pickup_lng')} />
          <input placeholder="Dropoff lat" value={rideForm.dropoff_lat} onChange={updateRideForm('dropoff_lat')} />
          <input placeholder="Dropoff lng" value={rideForm.dropoff_lng} onChange={updateRideForm('dropoff_lng')} />
          <input placeholder="Distance (km)" value={rideForm.distance_km} onChange={updateRideForm('distance_km')} />
          <input placeholder="Price estimate" value={rideForm.price_estimate} onChange={updateRideForm('price_estimate')} />
        </div>
        <div className="button-row">
          <button onClick={handleRequestRide}>Request ride</button>
          <button className="secondary" onClick={handleLoadRides}>Load my rides</button>
        </div>
      </section>

      <section className="panel">
        <h2>Rides</h2>
        <div className="ride-grid">
          {rides.length === 0 ? (
            <p className="muted">No rides yet. Request one to see it listed here.</p>
          ) : (
            rides.map((ride) => (
              <article className="ride-card" key={ride.id}>
                <h3>{ride.pickup_address} → {ride.dropoff_address}</h3>
                <p>Status: {ride.status}</p>
                <p>Estimate: {ride.price_estimate || 'TBD'}</p>
                <p>Driver: {ride.driver ? ride.driver.username : 'Unassigned'}</p>
              </article>
            ))
          )}
        </div>
      </section>
    </div>
  )
}

export default App
