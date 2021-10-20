import React, { useState } from 'react'

export default function Register() {
  const [carnet, setCarnet] = useState('')
  const [DPI, setDPI] = useState('')
  const [nombre, setNombre] = useState('')
  const [carrera, setCarrera] = useState('')
  const [correo, setCorreo] = useState('')
  const [password, setPassword] = useState('')
  const [edad, setEdad] = useState('')

  const handleSubmit = (e) => {
    e.preventDefault()
  }
  return (
    <form onSubmit={handleSubmit}>
      <h3>Registro</h3>
      <input
        placeholder="Carnet"
        onChange={(e) => setCarnet(e.target.value)}
        value={carnet}
      />
      <input
        placeholder="DPI"
        onChange={(e) => setDPI(e.target.value)}
        value={DPI}
      />
      <input
        placeholder="Nombre"
        onChange={(e) => setNombre(e.target.value)}
        value={nombre}
      />
      <input
        placeholder="Carrera"
        onChange={(e) => setCarrera(e.target.value)}
        value={carrera}
      />
      <input
        placeholder="Correo"
        onChange={(e) => setCorreo(e.target.value)}
        value={correo}
      />
      <input
        type="password"
        placeholder="Password"
        onChange={(e) => setPassword(e.target.value)}
        value={password}
      />
      <input
        placeholder="Edad"
        onChange={(e) => setEdad(e.target.value)}
        value={edad}
      />
      <button>Register</button>
    </form>
  )
}
