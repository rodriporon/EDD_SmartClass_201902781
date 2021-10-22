import React from 'react'
import { Link } from 'wouter'
import Navbar from 'react-bootstrap/Navbar'
import Container from 'react-bootstrap/Container'
import Nav from 'react-bootstrap/Nav'
import useUser from '../../hooks/useUser'

export default function Header() {
  const { isUser, isAdmin, logout } = useUser()

  const handleClick = (e) => {
    e.preventDefault()
    logout()
  }

  if (isUser) {
    return (
      <>
        <Navbar bg="dark" variant="dark">
          <Container>
            <Navbar.Brand>
              <Link to="/">Inicio</Link>
            </Navbar.Brand>
            <Nav className="me-auto">
              <Nav.Link>
                <Link to="/apuntes">Apuntes</Link>
              </Nav.Link>
              <Nav.Link>
                <Link to="/tareas">Tareas</Link>
              </Nav.Link>
              <Nav.Link>
                <Link to="/red-cursos">Red de Cursos</Link>
              </Nav.Link>
            </Nav>
            <Navbar.Collapse className="justify-content-end">
              <Navbar.Text>
                <a href="/#" onClick={handleClick}>
                  Logout
                </a>
              </Navbar.Text>
            </Navbar.Collapse>
          </Container>
        </Navbar>
      </>
    )
  } else if (isAdmin) {
    return (
      <>
        <Navbar bg="dark" variant="dark">
          <Container>
            <Navbar.Brand>
              <Link className="p5" to="/">
                Inicio
              </Link>
            </Navbar.Brand>
            <Nav className="me-auto"></Nav>
            <Navbar.Collapse className="justify-content-end">
              <Navbar.Text>
                <a href="/#" onClick={handleClick}>
                  Logout
                </a>
              </Navbar.Text>
            </Navbar.Collapse>
          </Container>
        </Navbar>
      </>
    )
  } else {
    return (
      <>
        <Navbar bg="dark" variant="dark">
          <Container>
            <Nav className="me-auto"></Nav>
            <Navbar.Collapse className="justify-content-end">
              <Nav.Link>
                <Link to="/login">Login</Link>
              </Nav.Link>
              <Nav.Link>
                <Link to="/register">Register</Link>
              </Nav.Link>
            </Navbar.Collapse>
          </Container>
        </Navbar>
      </>
    )
  }
}
