import React, { useState } from 'react'

const Context = React.createContext({})

export function UserContextProvider({ children }) {
  const [user, setUser] = useState(null)
  const [admin, setAdmin] = useState(null)

  return (
    <Context.Provider value={{ user, setUser, admin, setAdmin }}>
      {children}
    </Context.Provider>
  )
}

export default Context
