import { useCallback, useContext } from 'react'
import Context from '../context/UserContext'
import loginService from '../services/login'
import { useLocation } from 'wouter'

export default function useUser() {
  const { user, setUser, admin, setAdmin } = useContext(Context)
  const [, navigate] = useLocation()

  const login = useCallback(
    ({ carnet, password }) => {
      loginService({ carnet, password })
        .then((carnet) => {
          if (carnet === 'admin') {
            setAdmin(carnet)
          }
          setUser(carnet)
        })
        .catch((err) => {
          console.error(err)
        })
    },
    [setUser, setAdmin]
  )

  const logout = useCallback(() => {
    setUser(null)
    setAdmin(null)
    navigate('/')
  }, [setUser, setAdmin, navigate])

  return {
    isLogged: Boolean(user),
    isAdmin: Boolean(admin),
    login,
    logout,
  }
}
