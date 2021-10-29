import { useCallback } from 'react'

import reporteEstudiantesEncriptadoService from '../services/reporteEstudiantesEncriptado'

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

  return {
    reporteEstudiantesEncriptado,
  }
}
