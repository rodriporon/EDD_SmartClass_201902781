import React, { useState, useEffect } from 'react'
import BotonApuntes from '../../components/BotonApuntes'
import Info from '../../components/Info'
import Form from 'react-bootstrap/Form'
import Container from 'react-bootstrap/esm/Container'
import getApuntes from '../../services/getApuntes'
import useUser from '../../hooks/useUser'

export default function Apuntes() {
  const [apuntes, setApuntes] = useState([])

  const { carnet } = useUser()

  useEffect(
    function () {
      getApuntes({ carnet }).then((apuntes) => setApuntes(apuntes))
    },
    [carnet]
  )

  console.log(apuntes)
  return (
    <>
      <Info />
      <BotonApuntes />
      <Container>
        <Form.Group className="mb-3">
          <Form.Label>Apuntes</Form.Label>
          <Form.Control placeholder="Disabled input" disabled />
        </Form.Group>
        <Form.Group className="mb-3">
          <Form.Label>Disabled select menu</Form.Label>
          <Form.Select>
            <option>Disabled select</option>
          </Form.Select>
        </Form.Group>
        <Form.Group className="mb-3">
          <Form.Check type="checkbox" label="Can't check this" disabled />
        </Form.Group>
      </Container>
    </>
  )
}
