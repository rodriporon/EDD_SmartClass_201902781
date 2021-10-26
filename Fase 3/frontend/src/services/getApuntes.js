const ENDPOINT = 'http://localhost:3000'

export default function getApuntes({ carnet }) {
  return fetch(`${ENDPOINT}/obtener-apuntes/${carnet}`)
    .then((res) => {
      if (!res.ok) {
        alert('Error al consultar los apuntes')
        throw new Error('Response is not OK')
      }
      return res.json()
    })
    .then((res) => {
      const { data = [] } = res
      if (Array.isArray(data)) {
        const apuntes = data.map((apunte) => apunte.titulo)
        return apuntes
      }
    })
}
