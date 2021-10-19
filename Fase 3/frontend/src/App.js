import React, { useEffect } from "react"
import getUser from "./services/getUser"
import { Route } from "wouter"
import "./App.css"
import Home from "./components/Home"

function App() {
  useEffect(function () {
    getUser()
  }, [])
  return (
    <div className="App">
      <section className="App-content">
        <Route component={Home} path="/" />
      </section>
    </div>
  )
}

export default App
