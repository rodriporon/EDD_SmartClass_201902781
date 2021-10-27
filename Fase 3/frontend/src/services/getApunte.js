const ENDPOINT = 'http://localhost:3000'

export default function getApunte({ carnet, id }) {
  return fetch(`${ENDPOINT}/apunte/${carnet}/${id}`)
    .then((res) => {
      if (!res.ok) {
        alert('Error al consultar el apunte')
        throw new Error('Response is not OK')
      }
      return res.json()
    })
    .then((res) => {
      const apunte = res
      return apunte
    })
}
