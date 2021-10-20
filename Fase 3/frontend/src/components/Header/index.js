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
    <>
      <header className="gf-header">
        {isLogged ? (
          <button className="bt-header" onClick={handleClick}>
            Logout
          </button>
        ) : (
          <div>
            <Link className="lk-header" to="/login">
              Login
            </Link>
            <Link className="lk-header" to="/register">
              Register
            </Link>
          </div>
        )}
      </header>
    </>
  )
}
