import { useCallback } from 'react'

import reporteEstudiantesEncriptadoService from '../services/reporteEstudiantesEncriptado'
import reporteEstudiantesDesencriptadoService from '../services/reporteEstudiantesDesencriptado'
import reporteCursosAsignadosService from '../services/reporteCursosAsignados'

export default function useReportes() {
  const reporteEstudiantesEncriptado = useCallback(() => {
    reporteEstudiantesEncriptadoService()
      .then((msg) => {
        console.log(msg)
      })
      .catch((err) => {
        console.log(err)
      })
  }, [])

  const reporteEstudiantesDesencriptado = useCallback(() => {
    reporteEstudiantesDesencriptadoService()
      .then((msg) => {
        console.log(msg)
      })
      .catch((err) => {
        console.log(err)
      })
  }, [])

  const reporteCursosAsignados = useCallback((carnet) => {
    reporteCursosAsignadosService(carnet)
      .then((msg) => {
        console.log(msg)
      })
      .catch((err) => {
        console.log(err)
      })
  }, [])

  return {
    reporteEstudiantesEncriptado,
    reporteEstudiantesDesencriptado,
    reporteCursosAsignados,
  }
}
