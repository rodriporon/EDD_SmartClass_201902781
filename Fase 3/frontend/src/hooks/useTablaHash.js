import { useCallback } from 'react'
import { useLocation } from 'wouter'
import graficarTablaHashService from '../services/graficarTablaHash'

export default function useTablaHash() {
  const [, navigate] = useLocation()
  const graficarTablaHash = useCallback(() => {
    graficarTablaHashService()
      .then((msg) => {
        console.log(msg)
        navigate('ver-tabla-hash')
      })
      .catch((err) => console.log(err))
  }, [navigate])

  return {
    graficarTablaHash,
  }
}
