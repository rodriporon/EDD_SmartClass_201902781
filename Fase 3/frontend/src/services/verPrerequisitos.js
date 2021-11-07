const ENDPOINT = 'http://localhost:3000'

export default function verPrerequisitos({ codigo }) {
  return fetch(`${ENDPOINT}/ver-prerequisitos`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ codigo }),
  })
    .then((res) => {
      if (!res.ok) {
        alert('No se pudo obtener informacion del curso')
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
