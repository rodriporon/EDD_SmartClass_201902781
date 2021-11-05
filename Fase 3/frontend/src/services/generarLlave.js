const ENDPOINT = 'http://localhost:3000'

export default function generarLlave() {
  return fetch(`${ENDPOINT}/generar-llave`)
    .then((res) => {
      if (!res.ok) {
        alert('No se pudo generar la llave')
        throw new Error('Response is not OK')
      }
      return res.json()
    })
    .then((res) => {
      const { msg } = res
      alert(msg)
      return msg
    })
}
