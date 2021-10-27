import React, { useState } from 'react'
import BotonApuntes from '../../components/BotonApuntes'
import Info from '../../components/Info'
import useNuevoApunte from '../../hooks/useNuevoApunte'
import useUser from '../../hooks/useUser'

import Button from 'react-bootstrap/Button'
import Form from 'react-bootstrap/Form'
import Container from 'react-bootstrap/esm/Container'
import Row from 'react-bootstrap/Row'
import Col from 'react-bootstrap/Col'

export default function NuevoApunte() {
  const [titulo, setTitulo] = useState('')
  const [contenido, setContenido] = useState('')
  const { carnet } = useUser()
  const { nuevoApunte } = useNuevoApunte()
  const handleSubmitApunte = (e) => {
    e.preventDefault()
    nuevoApunte({ carnet, titulo, contenido })
  }
  return (
    <>
      <Info />
      <BotonApuntes />
      <Container>
        <Row>
          <Col md={{ span: 6, offset: 3 }}>
            <Form onSubmit={handleSubmitApunte}>
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
            </Form>
          </Col>
        </Row>
      </Container>
    </>
  )
}
