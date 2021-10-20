const ENDPOINT = 'http://localhost:3000'

export default function login({ username, password }) {
  return fetch(`${ENDPOINT}/login`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ username, password }),
  })
    .then((res) => {
      if (!res.ok) throw new Error('Response is not OK')
      return res.json()
    })
    .then((res) => {
      const { username } = res
      console.log(username)
      return username
    })
}
