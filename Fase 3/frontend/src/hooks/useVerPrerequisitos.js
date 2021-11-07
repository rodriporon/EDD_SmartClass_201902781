import { useCallback } from 'react'
import verPrerequisitosService from '../services/verPrerequisitos'

export default function useVerPrerequisitos() {
  const verPrerequisitos = useCallback(({ codigo }) => {
    verPrerequisitosService({ codigo })
      .then((msg) => {
        console.log(msg)
      })
      .catch((err) => {
        console.error(err)
      })
  }, [])

  return {
    verPrerequisitos,
  }
}
