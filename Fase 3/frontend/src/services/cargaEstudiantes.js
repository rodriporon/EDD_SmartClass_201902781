const ENDPOINT = 'http://localhost:3000'

export default function cargaEstudiantes(estudiantes) {
  console.log(`desde SERVICES archivo: ${JSON.stringify(estudiantes)}`)
  return fetch(`${ENDPOINT}/carga-estudiantes`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(estudiantes),
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
