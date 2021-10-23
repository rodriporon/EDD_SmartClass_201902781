const ENDPOINT = 'http://localhost:3000'

export default function login({ carnet, password }) {
  return fetch(`${ENDPOINT}/login`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ carnet, password }),
  })
    .then((res) => {
      if (!res.ok) {
        alert('Carnet o Password incorrecto')
        throw new Error('Response is not OK')
      }
      return res.json()
    })
    .then((res) => {
      //const { carnet } = res
      console.log(`${JSON.stringify(res)} inicio sesion`)
      return res
    })
}
