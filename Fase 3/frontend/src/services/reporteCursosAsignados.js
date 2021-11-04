const ENDPOINT = 'http://localhost:3000'

export default function reporteCursosAsignados(carnet) {
  return fetch(`${ENDPOINT}/reporte/cursos-asignados/${carnet}`)
    .then((res) => {
      if (!res.ok) {
        alert('No se pudo generar el reporte')
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
