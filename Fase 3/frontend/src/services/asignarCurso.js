const ENDPOINT = 'http://localhost:3000'

export default function asignarCurso({ codigo, carnet }) {
  return fetch(`${ENDPOINT}/asignar-curso/${carnet}`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ codigo }),
  })
    .then((res) => {
      if (!res.ok) {
        alert('No se pudo cargar el archivo')
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
