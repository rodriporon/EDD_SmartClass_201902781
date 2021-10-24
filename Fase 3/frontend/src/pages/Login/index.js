import React, { useEffect, useState } from 'react'
import { useLocation } from 'wouter'
import useUser from '../../hooks/useUser'
import Form from 'react-bootstrap/Form'
import Button from 'react-bootstrap/Button'
import Container from 'react-bootstrap/Container'
import Col from 'react-bootstrap/Col'
import Row from 'react-bootstrap/Row'

export default function Login() {
  const [carnet, setCarnet] = useState('')
  const [password, setPassword] = useState('')
  const [, navigate] = useLocation()
  const { login, isUser, isAdmin } = useUser()

  useEffect(() => {
    if (isAdmin) navigate('/admin')
    if (isUser) navigate('/usuario')
  }, [isUser, isAdmin, navigate])

  const handleSubmit = (e) => {
    e.preventDefault()
    login({ carnet, password })
  }
  return (
    <Container>
      <Row>
        <Col md={{ span: 6, offset: 3 }}>
          <Form onSubmit={handleSubmit}>
            <Form.Group className="mb-3" controlId="formBasicEmail">
              <Form.Label>Carnet</Form.Label>
              <Form.Control
                onChange={(e) => setCarnet(e.target.value)}
                type="text"
                placeholder="Carnet"
                value={carnet}
              />
              <Form.Text className="text-muted">
                Sus datos son confidenciales
              </Form.Text>
            </Form.Group>

            <Form.Group className="mb-3" controlId="formBasicPassword">
              <Form.Label>Password</Form.Label>
              <Form.Control
                onChange={(e) => setPassword(e.target.value)}
                type="password"
                placeholder="Password"
                value={password}
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
