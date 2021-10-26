import React, { useState } from 'react'
import Stack from 'react-bootstrap/Stack'
import Button from 'react-bootstrap/Button'
import Form from 'react-bootstrap/Form'
import Container from 'react-bootstrap/esm/Container'
import Row from 'react-bootstrap/Row'
import Col from 'react-bootstrap/Col'
import useUser from '../../hooks/useUser'

export default function BotonApuntes() {
  const [verApuntes, setVerApuntes] = useState(true)
  const [titulo, setTitulo] = useState('')
  const [contenido, setContenido] = useState('')

  const { carnet } = useUser()

  const handleVerApuntes = () => {
    setVerApuntes(true)
  }

  const handleNuevoApunte = () => {
    setVerApuntes(false)
  }

  return (
    <>
      <Stack direction="horizontal" gap={3}>
        <Button
          onClick={handleVerApuntes}
          className="bg-dark border ms-auto"
          variant="outline-secondary"
        >
          Ver Apuntes
        </Button>
        <div className="vr" />
        <Button
          onClick={handleNuevoApunte}
          className="bg-dark border"
          variant="outline-secondary"
        >
          Nuevo Apunte
        </Button>{' '}
      </Stack>

      {verApuntes ? (
        <>
          <Container>
            <Form.Group className="mb-3">
              <Form.Label>Apuntes</Form.Label>
              <Form.Control placeholder="Disabled input" disabled />
            </Form.Group>
            <Form.Group className="mb-3">
              <Form.Label>Disabled select menu</Form.Label>
              <Form.Select disabled>
                <option>Disabled select</option>
              </Form.Select>
            </Form.Group>
            <Form.Group className="mb-3">
              <Form.Check type="checkbox" label="Can't check this" disabled />
            </Form.Group>
          </Container>
        </>
      ) : (
        <>
          <Container>
            <Row>
              <Col md={{ span: 6, offset: 3 }}>
                <Form.Group className="mb-3">
                  <Form.Label>Carnet</Form.Label>
                  <Form.Control placeholder={carnet} disabled />
                </Form.Group>
                <Form.Group className="mb-3">
                  <Form.Label>Titulo</Form.Label>
                </Form.Group>
                <Form.Control
                  onChange={(e) => setTitulo(e.target.value)}
                  placeholder="Titulo"
                  value={titulo}
                />
                <Form.Group className="mb-3">
                  <Form.Label>Contenido del Apunte</Form.Label>
                  <Form.Control
                    as="textarea"
                    rows={3}
                    onChange={(e) => setContenido(e.target.value)}
                    value={contenido}
                  />
                </Form.Group>
                <Button variant="primary" type="submit">
                  Enviar
                </Button>
              </Col>
            </Row>
          </Container>
        </>
      )}
    </>
  )
}
