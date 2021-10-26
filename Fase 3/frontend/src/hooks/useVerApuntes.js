import { useCallback } from 'react'
import getApuntesService from '../services/getApuntes'

export default function useGetApuntes() {
  const getApuntes = useCallback(({ carnet }) => {
    getApuntesService({ carnet })
      .then((res) => {
        console.log(res)
      })
      .catch((err) => {
        console.error(err)
      })
  }, [])
  return {
    getApuntes,
  }
}
