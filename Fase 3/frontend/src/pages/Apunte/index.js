import React, { useEffect, useState } from 'react'
import Container from 'react-bootstrap/esm/Container'
import Card from 'react-bootstrap/Card'
import getApunte from '../../services/getApunte'

export default function Apunte({ params }) {
  const { carnet, id } = params
  const [titulo, setTitulo] = useState()
  const [contenido, setContenido] = useState()

  useEffect(function () {
    getApunte({ carnet, id }).then((apunte) => {
      setTitulo(apunte.titulo)
      setContenido(apunte.contenido)
    })
  })

  return (
    <>
      <Container>
        <Card bg="dark">
          <Card.Body>
            <Card.Title>{titulo}</Card.Title>
            <Card.Text>{contenido}</Card.Text>
          </Card.Body>
        </Card>
      </Container>
    </>
  )
}
