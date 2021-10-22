import React from 'react'
import { Link } from 'wouter'

import useUser from '../../hooks/useUser'
import './index.css'

export default function Header() {
  const { isUser, isAdmin, logout } = useUser()

  const handleClick = (e) => {
    e.preventDefault()
    logout()
  }

  if (isUser) {
    return (
      <>
        <ul className="ul">
          <li className="li">
            <Link className="li-a" to="/">
              Inicio
            </Link>
          </li>
          <li className="li">
            <Link className="li-a" to="/apuntes">
              Apuntes
            </Link>
          </li>
          <li className="li">
            <Link className="li-a" to="/tareas">
              Tareas
            </Link>
          </li>
          <li className="li">
            <Link className="li-a" to="/redcursos">
              Red de Cursos
            </Link>
          </li>

          <li className="lg-header">
            <a href="/#" className="active" onClick={handleClick}>
              Logout
            </a>
          </li>
        </ul>
      </>
    )
  } else if (isAdmin) {
    return (
      <>
        <ul>
          <li className="lg-header">
            <a href="/#" className="active" onClick={handleClick}>
              Logout
            </a>
          </li>
        </ul>
      </>
    )
  } else {
    return (
      <>
        <ul>
          <li className="lg-header">
            <Link className="lk-header" to="/login">
              Login
            </Link>
          </li>
          <li className="lg-header">
            <Link className="lk-header" to="/register">
              Register
            </Link>
          </li>
        </ul>
      </>
    )
  }
}
