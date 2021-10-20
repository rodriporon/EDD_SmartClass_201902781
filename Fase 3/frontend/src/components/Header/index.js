import React from 'react'
import { Link } from 'wouter'

import useUser from '../../hooks/useUser'
import './index.css'

export default function Header() {
  const { isLogged, logout } = useUser()

  const handleClick = (e) => {
    e.preventDefault()
    logout()
  }

  return (
    <header className="gf-header">
      {isLogged ? (
        <button className="bt-header" onClick={handleClick}>
          Logout
        </button>
      ) : (
        <Link to="/login">Login</Link>
      )}
    </header>
  )
}
