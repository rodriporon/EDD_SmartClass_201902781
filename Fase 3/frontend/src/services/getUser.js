const loginURL = " http://127.0.0.1:3000/login"

export default function getUser() {
  return fetch(loginURL)
    .then((res) => res.json())
    .then((response) => {
      const { data } = response
      const users = data.map((user) => user.username)
      console.log(users)
      return users
    })
}
