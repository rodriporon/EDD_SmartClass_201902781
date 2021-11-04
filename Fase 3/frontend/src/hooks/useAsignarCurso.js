import { useCallback } from 'react'
import asignarCursoService from '../services/asignarCurso'

export default function useAsignarCurso() {
  const asignarCurso = useCallback(({ codigo, carnet }) => {
    asignarCursoService({ codigo, carnet })
      .then((msg) => {
        console.log(msg)
      })
      .catch((err) => {
        console.error(err)
      })
  }, [])

  return {
    asignarCurso,
  }
}
