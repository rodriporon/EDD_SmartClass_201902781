import { useCallback } from 'react'
import nuevoApunteService from '../services/nuevoApunte'

export default function useNuevoApunte() {
  const nuevoApunte = useCallback(({ carnet, titulo, contenido }) => {
    nuevoApunteService({ carnet, titulo, contenido })
      .then((carnet) => {
        console.log(`apunte del carnet: ${carnet} creado`)
      })
      .catch((err) => {
        console.error(err)
      })
  }, [])
  return {
    nuevoApunte,
  }
}
