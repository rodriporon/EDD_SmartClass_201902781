import { useCallback } from 'react'

import cargaEstudiantesService from '../services/cargaEstudiantes'
import cargaApuntesService from '../services/cargaApuntes'
import cargaPensumService from '../services/cargaPensum'
import cargaCursosEstudianteService from '../services/cargaCursos'

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

  const cargaCursosEstudiante = useCallback((archivo) => {
    cargaCursosEstudianteService(archivo)
      .then((msg) => {
        console.log(msg)
      })
      .catch((err) => {
        console.log(err)
      })
  }, [])

  const cargaPensum = useCallback((archivo) => {
    cargaPensumService(archivo)
      .then((msg) => {
        console.log(msg)
      })
      .catch((err) => {
        console.log(err)
      })
  }, [])

  const cargaApuntes = useCallback((archivo) => {
    cargaApuntesService(archivo)
      .then((msg) => {
        console.log(msg)
      })
      .catch((err) => {
        console.log(err)
      })
  }, [])

  return {
    cargaEstudiantes,
    cargaApuntes,
    cargaPensum,
    cargaCursosEstudiante,
  }
}
