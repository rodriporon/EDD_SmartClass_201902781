const ENDPOINT = 'http://localhost:3000'

export default function register({
  carnet,
  DPI,
  nombre,
  carrera,
  correo,
  password,
  edad,
}) {
  return fetch(`${ENDPOINT}/register`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      carnet,
      DPI,
      nombre,
      carrera,
      correo,
      password,
      edad,
    }),
  })
    .then((res) => {
      if (!res.ok) {
        alert('Ingrese datos correctos')
        throw new Error('Response is not OK')
      }
      return res.json()
    })
    .then((res) => {
      const { carnet } = res
      alert(`El carnet ${carnet} ha sido creado`)
      return carnet
    })
}
