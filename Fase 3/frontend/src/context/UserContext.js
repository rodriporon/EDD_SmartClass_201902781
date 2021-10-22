import React, { useState } from 'react'

const Context = React.createContext({})

export function UserContextProvider({ children }) {
  const [carnet, setCarnet] = useState(null)
  const [DPI, setDPI] = useState(null)
  const [nombre, setNombre] = useState(null)
  const [carrera, setCarrera] = useState(null)
  const [correo, setCorreo] = useState(null)
  const [password, setPassword] = useState(null)
  const [edad, setEdad] = useState(null)

  const [admin, setAdmin] = useState(null)

  return (
    <Context.Provider
      value={{
        carnet,
        setCarnet,
        DPI,
        setDPI,
        nombre,
        setNombre,
        carrera,
        setCarrera,
        correo,
        setCorreo,
        password,
        setPassword,
        edad,
        setEdad,
        admin,
        setAdmin,
      }}
    >
      {children}
    </Context.Provider>
  )
}

export default Context
