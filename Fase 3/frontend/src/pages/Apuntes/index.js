import React, { useState, useEffect } from 'react'
import BotonApuntes from '../../components/BotonApuntes'
import Info from '../../components/Info'
import Card from 'react-bootstrap/Card'
import Button from 'react-bootstrap/Button'
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
        {apuntes.map((apunte) => {
          return (
            <Card bg="dark" key={apunte.id}>
              <Card.Header as="h5">{apunte.id}</Card.Header>
              <Card.Body>
                <Card.Title>{apunte.titulo}</Card.Title>
                <Card.Text>{apunte.contenido}</Card.Text>
                <Button variant="light">Ver</Button>
              </Card.Body>
            </Card>
          )
        })}
      </Container>
    </>
  )
}
