import React from 'react'
import useUser from '../../hooks/useUser'

import './index.css'

export default function Info() {
  const { nombre } = useUser()
  return <div className="dv-info">Usuario: {nombre}</div>
}
