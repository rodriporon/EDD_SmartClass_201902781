import React from 'react'
//import getUser from './services/getUser'
import { Route } from 'wouter'
import Home from './components/Home'
import './App.css'
import Header from './components/Header'
import Login from './pages/Login'
import { UserContextProvider } from './context/UserContext'
import Register from './pages/Register'
import Admin from './pages/Admin'
import Apuntes from './pages/Apuntes'
import NuevoApunte from './pages/NuevoApunte'

function App() {
  /* useEffect(function () {
    getUser()
  }, []) */

  return (
    <UserContextProvider>
      <div className="App">
        <Header />
        <section className="App-content">
          <Route component={Home} path="/" />
          <Route component={Login} path="/login" />
          <Route component={Register} path="/register" />
          <Route component={Admin} path="/admin" />
          <Route component={Apuntes} path="/apuntes" />
          <Route component={NuevoApunte} path="/nuevo-apunte" />
        </section>
      </div>
    </UserContextProvider>
  )
}

export default App
