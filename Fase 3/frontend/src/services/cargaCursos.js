const ENDPOINT = 'http://localhost:3000'

export default function cargaCursosEstudiante(cursos) {
  return fetch(`${ENDPOINT}/carga-cursos-estudiante`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(cursos),
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
