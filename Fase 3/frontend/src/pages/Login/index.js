import React, { useEffect, useState } from 'react'
import { useLocation } from 'wouter'
import useUser from '../../hooks/useUser'

import './index.css'

export default function Login() {
  const [carnet, setCarnet] = useState('')
  const [password, setPassword] = useState('')
  const [, navigate] = useLocation()
  const { login, isUser, isAdmin } = useUser()

  useEffect(() => {
    if (isAdmin) navigate('/admin')
    if (isUser) navigate('/usuario')
  }, [isUser, isAdmin, navigate])

  const handleSubmit = (e) => {
    e.preventDefault()
    login({ carnet, password })
  }
  return (
    <form onSubmit={handleSubmit}>
      <h3>Inicie Sesión</h3>
      <input
        placeholder="Carnet"
        onChange={(e) => setCarnet(e.target.value)}
        value={carnet}
      />
      <input
        type="password"
        placeholder="Password"
        onChange={(e) => setPassword(e.target.value)}
        value={password}
      />
      <button>Login</button>
    </form>
  )
}
