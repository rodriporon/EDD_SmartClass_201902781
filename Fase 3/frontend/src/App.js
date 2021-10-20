import React from 'react'
//import getUser from './services/getUser'
import { Route } from 'wouter'
import Home from './components/Home'
import './App.css'
import Header from './components/Header'
import Login from './pages/Login'
import { UserContextProvider } from './context/UserContext'

function App() {
  /* useEffect(function () {
    getUser()
  }, []) */

  return (
    <UserContextProvider>
      <div className="App">
        <section className="App-content">
          <Header />
          <Route component={Home} path="/" />
          <Route component={Login} path="/login" />
        </section>
      </div>
    </UserContextProvider>
  )
}

export default App
