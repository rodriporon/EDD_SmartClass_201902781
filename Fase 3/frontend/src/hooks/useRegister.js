import { useCallback } from 'react'
import registerService from '../services/register'

export default function useRegister() {
  const register = useCallback(
    ({ carnet, DPI, nombre, carrera, correo, password, edad }) => {
      registerService({ carnet, DPI, nombre, carrera, correo, password, edad })
        .then((carnet) => {
          console.log(`${carnet} registrado`)
        })
        .catch((err) => {
          console.error(err)
        })
    },
    []
  )

  return {
    register,
  }
}
