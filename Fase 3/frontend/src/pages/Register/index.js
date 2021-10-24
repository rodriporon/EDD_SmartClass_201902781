import React, { useState } from 'react'
import useRegister from '../../hooks/useRegister'
import Form from 'react-bootstrap/Form'
import Button from 'react-bootstrap/Button'
import Container from 'react-bootstrap/Container'
import Col from 'react-bootstrap/Col'
import Row from 'react-bootstrap/Row'

export default function Register() {
  const [carnet, setCarnet] = useState('')
  const [DPI, setDPI] = useState('')
  const [nombre, setNombre] = useState('')
  const [carrera, setCarrera] = useState('')
  const [correo, setCorreo] = useState('')
  const [password, setPassword] = useState('')
  const [edad, setEdad] = useState('')

  const { register } = useRegister()

  const handleSubmit = (e) => {
    e.preventDefault()
    register({ carnet, DPI, nombre, carrera, correo, password, edad })
    setCarnet('')
    setDPI('')
    setNombre('')
    setCarrera('')
    setCorreo('')
    setPassword('')
    setEdad('')
  }
  return (
    <Container>
      <Row>
        <Col md={{ span: 6, offset: 3 }}>
          <Form onSubmit={handleSubmit}>
            <Form.Group className="mb-3">
              <Form.Label>Carnet</Form.Label>
              <Form.Control
                onChange={(e) => setCarnet(e.target.value)}
                type="text"
                placeholder="Carnet"
                value={carnet}
              />
            </Form.Group>

            <Form.Group className="mb-3">
              <Form.Label>DPI</Form.Label>
              <Form.Control
                onChange={(e) => setDPI(e.target.value)}
                type="text"
                placeholder="DPI"
                value={DPI}
              />
            </Form.Group>

            <Form.Group className="mb-3">
              <Form.Label>Nombre</Form.Label>
              <Form.Control
                onChange={(e) => setNombre(e.target.value)}
                type="text"
                placeholder="Nombre"
                value={nombre}
              />
            </Form.Group>

            <Form.Group className="mb-3">
              <Form.Label>Carrera</Form.Label>
              <Form.Control
                onChange={(e) => setCarrera(e.target.value)}
                type="text"
                placeholder="Carrera"
                value={carrera}
              />
            </Form.Group>

            <Form.Group className="mb-3">
              <Form.Label>Correo</Form.Label>
              <Form.Control
                onChange={(e) => setCorreo(e.target.value)}
                type="text"
                placeholder="Correo"
                value={correo}
              />
            </Form.Group>

            <Form.Group className="mb-3">
              <Form.Label>Password</Form.Label>
              <Form.Control
                onChange={(e) => setPassword(e.target.value)}
                type="password"
                placeholder="Password"
                value={password}
              />
            </Form.Group>

            <Form.Group className="mb-3">
              <Form.Label>Edad</Form.Label>
              <Form.Control
                onChange={(e) => setEdad(e.target.value)}
                type="text"
                placeholder="Edad"
                value={edad}
              />
            </Form.Group>

            <Button variant="primary" type="submit">
              Login
            </Button>
          </Form>
        </Col>
      </Row>
    </Container>
  )
}
