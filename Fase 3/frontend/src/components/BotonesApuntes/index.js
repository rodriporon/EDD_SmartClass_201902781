import React from 'react'
import { Link } from 'wouter'

import './index.css'

export default function BotonesApuntes() {
  return (
    <div className="dv-apuntes">
      <ul className="ul-apuntes">
        <li className="li-apuntes">
          <Link className="li-a-apuntes" to="/ver-apuntes">
            Ver Apuntes
          </Link>
        </li>
        <li className="li-apuntes">
          <Link className="li-a-apuntes" to="/nuevo-apunte">
            Nuevo Apunte
          </Link>
        </li>
      </ul>
    </div>
  )
}
