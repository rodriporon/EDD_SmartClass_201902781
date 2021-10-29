import React from 'react'
import { Link } from 'wouter'
import Navbar from 'react-bootstrap/Navbar'
import Container from 'react-bootstrap/Container'
import NavDropdown from 'react-bootstrap/NavDropdown'
import Nav from 'react-bootstrap/Nav'
import useUser from '../../hooks/useUser'
import useReportes from '../../hooks/useReportes'

export default function Header() {
  const { isUser, isAdmin, logout } = useUser()
  const { reporteEstudiantesEncriptado, reporteEstudiantesDesencriptado } =
    useReportes()

  const handleReporteEstudiantesEncriptado = (e) => {
    e.preventDefault()
    reporteEstudiantesEncriptado()
  }

  const handleReporteEstudiantesDesencriptado = (e) => {
    e.preventDefault()
    reporteEstudiantesDesencriptado()
  }

  const handleClick = (e) => {
    e.preventDefault()
    logout()
  }

  if (isUser) {
    return (
      <>
        <Navbar bg="dark" variant="dark">
          <Container>
            <Navbar.Brand as={Link} to="/">
              Inicio
            </Navbar.Brand>
            <Nav className="me-auto">
              <Nav.Link as={Link} to="/apuntes">
                Apuntes
              </Nav.Link>
              <Nav.Link as={Link} to="/tareas">
                Tareas
              </Nav.Link>
              <Nav.Link as={Link} to="/red-cursos">
                Red de Cursos
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
            <Navbar.Brand as={Link} to="/admin">
              Inicio
            </Navbar.Brand>
            <Nav className="me-auto">
              <Nav.Link as={Link} to="/generar-llave">
                Generar Llave
              </Nav.Link>
              <NavDropdown title="Reportes" id="basic-nav-dropdown">
                <NavDropdown.Item onClick={handleReporteEstudiantesEncriptado}>
                  Estudiantes Encriptado
                </NavDropdown.Item>
                <NavDropdown.Item
                  onClick={handleReporteEstudiantesDesencriptado}
                >
                  Estudiantes Desencriptado
                </NavDropdown.Item>
                <NavDropdown.Item as={Link} to="/carga-apuntes">
                  Apuntes
                </NavDropdown.Item>
              </NavDropdown>
              <Nav.Link as={Link} to="/tareas">
                Cargas Masivas
              </Nav.Link>
              <Nav.Link as={Link} to="/red-cursos">
                Red de Cursos
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
  } else {
    return (
      <>
        <Navbar bg="dark" variant="dark">
          <Container>
            <Nav className="me-auto"></Nav>
            <Navbar.Collapse className="justify-content-end">
              <Nav.Link as={Link} to="/login">
                Login
              </Nav.Link>
              <Nav.Link as={Link} to="/register">
                Register
              </Nav.Link>
            </Navbar.Collapse>
          </Container>
        </Navbar>
      </>
    )
  }
}
