import React, { useState } from 'react'
import Info from '../../components/Info'
import Container from 'react-bootstrap/Container'
import Row from 'react-bootstrap/Row'
import Col from 'react-bootstrap/Col'
import Form from 'react-bootstrap/Form'
import Button from 'react-bootstrap/Button'
import useVerPrerequisitos from '../../hooks/useVerPrerequisitos'

export default function RedCursos() {
  const [codigo, setCodigo] = useState('')

  const { verPrerequisitos } = useVerPrerequisitos()

  const handleSubmitVerPrerequisitos = (e) => {
    e.preventDefault()
    verPrerequisitos({ codigo })
  }
  return (
    <>
      <Info />
      <Container>
        <Row>
          <Col md={{ span: 6, offset: 3 }}>
            <Form onSubmit={handleSubmitVerPrerequisitos}>
              <Form.Group className="mb-3">
                <Form.Label>
                  Codigo del Curso para ver sus Prerequisitos
                </Form.Label>
                <Form.Control onChange={(e) => setCodigo(e.target.value)} />
              </Form.Group>

              <Button variant="primary" type="submit">
                Ver prerequisitos
              </Button>
            </Form>
          </Col>
        </Row>
      </Container>
    </>
  )
}
