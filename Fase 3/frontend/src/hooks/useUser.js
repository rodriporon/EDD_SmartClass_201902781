import { useCallback, useContext } from 'react'
import Context from '../context/UserContext'
import loginService from '../services/login'
import { useLocation } from 'wouter'

export default function useUser() {
  const {
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
  } = useContext(Context)
  const [, navigate] = useLocation()

  const login = useCallback(
    ({ carnet, password }) => {
      loginService({ carnet, password })
        .then((res) => {
          if (res.carnet === 'admin') {
            setAdmin(res.carnet)
          } else {
            setCarnet(res.carnet)
            setDPI(res.DPI)
            setNombre(res.nombre)
            setCarrera(res.carrera)
            setCorreo(res.correo)
            setPassword(res.password)
            setEdad(res.edad)
          }
        })
        .catch((err) => {
          console.error(err)
        })
    },
    [
      setCarnet,
      setDPI,
      setNombre,
      setCarrera,
      setCorreo,
      setPassword,
      setEdad,
      setAdmin,
    ]
  )

  const logout = useCallback(() => {
    setCarnet(null)
    setAdmin(null)
    navigate('/')
  }, [setCarnet, setAdmin, navigate])

  return {
    carnet,
    DPI,
    nombre,
    carrera,
    correo,
    password,
    edad,
    isUser: Boolean(carnet),
    isAdmin: Boolean(admin),
    login,
    logout,
  }
}
