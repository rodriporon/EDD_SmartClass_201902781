import React from 'react'
import { Link } from 'wouter'
import Stack from 'react-bootstrap/Stack'
import Button from 'react-bootstrap/Button'

export default function BotonApuntes() {
  return (
    <>
      <Stack direction="horizontal" gap={3}>
        <Button
          as={Link}
          to="/apuntes"
          className="bg-dark border ms-auto"
          variant="outline-secondary"
        >
          Ver Apuntes
        </Button>
        <div className="vr" />
        <Button
          as={Link}
          to="/nuevo-apunte"
          className="bg-dark border"
          variant="outline-secondary"
        >
          Nuevo Apunte
        </Button>{' '}
      </Stack>
    </>
  )
}
