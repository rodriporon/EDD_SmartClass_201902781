const ENDPOINT = 'http://localhost:3000'

export default function graficarTablaHash() {
  return fetch(`${ENDPOINT}/graficar-tablahash`)
    .then((res) => {
      if (!res.ok) {
        alert('No se pudo generar la grafica')
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
