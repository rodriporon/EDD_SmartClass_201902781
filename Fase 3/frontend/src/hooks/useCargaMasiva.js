import { useCallback } from 'react'

import cargaEstudiantesService from '../services/cargaEstudiantes'

export default function useCargaEstudiantes() {
  const cargaEstudiantes = useCallback((archivo) => {
    cargaEstudiantesService(archivo)
      .then((msg) => {
        console.log(msg)
      })
      .catch((err) => {
        console.log(err)
      })
  }, [])

  return {
    cargaEstudiantes,
  }
}
