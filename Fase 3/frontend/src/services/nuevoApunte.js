const ENDPOINT = 'http://localhost:3000'

export default function NuevoApunte({ carnet, titulo, contenido }) {
  return fetch(`${ENDPOINT}/nuevo-apunte`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      carnet,
      titulo,
      contenido,
    }),
  })
    .then((res) => {
      if (!res.ok) {
        alert('Ingrese los datos que se le solicitan')
        throw new Error('Response of nuevo-apunte is not OK')
      }
      return res.json()
    })
    .then((res) => {
      const { titulo } = res
      alert(`Apunte con titulo: ${titulo} creado`)
      return titulo
    })
}
