const ENDPOINT = 'http://localhost:3000'

export default function cargaEstudiantes() {
  return fetch(`${ENDPOINT}/reporte/estudiantes/desencriptado`)
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
