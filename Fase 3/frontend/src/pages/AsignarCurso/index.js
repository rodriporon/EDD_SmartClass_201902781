import React, { useState } from 'react'
import Info from '../../components/Info'
import Container from 'react-bootstrap/Container'
import Row from 'react-bootstrap/Row'
import Col from 'react-bootstrap/Col'
import Form from 'react-bootstrap/Form'
import Button from 'react-bootstrap/Button'
import useAsignarCurso from '../../hooks/useAsignarCurso'
import useUser from '../../hooks/useUser'

export default function AsignarCurso() {
  const [codigo, setCodigo] = useState('')

  const { carnet } = useUser()
  const { asignarCurso } = useAsignarCurso()

  const handleSubmitAsignacion = (e) => {
    e.preventDefault()
    asignarCurso({ codigo, carnet })
  }
  return (
    <>
      <Info />
      <Container>
        <Row>
          <Col md={{ span: 6, offset: 3 }}>
            <Form onSubmit={handleSubmitAsignacion}>
              <Form.Group className="mb-3">
                <Form.Label>Codigo del Curso</Form.Label>
                <Form.Control onChange={(e) => setCodigo(e.target.value)} />
              </Form.Group>

              <Button variant="primary" type="submit">
                Asignarme
              </Button>
            </Form>
          </Col>
        </Row>
      </Container>
    </>
  )
}
