import { useCallback } from 'react'
import generarLlaveService from '../services/generarLlave'

export default function useGenerarLlave() {
  const generarLlave = useCallback(() => {
    generarLlaveService()
      .then((msg) => {
        console.log(msg)
      })
      .catch((err) => console.log(err))
  }, [])

  return {
    generarLlave,
  }
}
