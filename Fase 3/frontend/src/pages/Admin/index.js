import React, { useState } from 'react'
import Container from 'react-bootstrap/Container'
import Form from 'react-bootstrap/Form'
import Button from 'react-bootstrap/Button'

import useCargaMasiva from '../../hooks/useCargaMasiva'

export default function Admin() {
  const [estudiantes, setEstudiantes] = useState('')
  const [apuntes, setApuntes] = useState('')
  const [pensum, setPensum] = useState('')

  const { cargaEstudiantes, cargaApuntes, cargaPensum } = useCargaMasiva()

  const handleArchivoEstudiantes = (e) => {
    const fileReader = new FileReader()
    fileReader.readAsText(e.target.files[0], 'UTF-8')
    fileReader.onload = (e) => {
      console.log('e.target.result', e.target.result)
      setEstudiantes(e.target.result)
    }
  }

  const handleArchivoPensum = (e) => {
    const fileReader = new FileReader()
    fileReader.readAsText(e.target.files[0], 'UTF-8')
    fileReader.onload = (e) => {
      console.log('e.target.result', e.target.result)
      setPensum(e.target.result)
    }
  }

  const handleArchivoApuntes = (e) => {
    const fileReader = new FileReader()
    fileReader.readAsText(e.target.files[0], 'UTF-8')
    fileReader.onload = (e) => {
      console.log('e.target.result', e.target.result)
      setApuntes(e.target.result)
    }
  }

  const handleSubmitEstudiantes = (e) => {
    e.preventDefault()
    cargaEstudiantes(estudiantes)
  }

  const handleSubmitApuntes = (e) => {
    e.preventDefault()
    cargaApuntes(apuntes)
  }

  const handleSubmitPensum = (e) => {
    e.preventDefault()
    cargaPensum(pensum)
  }
  return (
    <>
      <Container>
        <Form type="submit">
          <p className="p-admin">Usuario Admin</p>
          <Form.Group controlId="formFile" className="mb-3">
            <Form.Label>Carga masiva estudiantes</Form.Label>
            <Form.Control onChange={handleArchivoEstudiantes} type="file" />
            <Button variant="light" onClick={handleSubmitEstudiantes}>
              Cargar
            </Button>
          </Form.Group>
        </Form>
      </Container>
      <Container>
        <Form type="submit">
          <Form.Group controlId="formFile" className="mb-3">
            <Form.Label>Carga masiva apuntes</Form.Label>
            <Form.Control onChange={handleArchivoApuntes} type="file" />
            <Button variant="light" onClick={handleSubmitApuntes}>
              Cargar
            </Button>
          </Form.Group>
        </Form>
      </Container>
      <Container>
        <Form type="submit">
          <Form.Group controlId="formFile" className="mb-3">
            <Form.Label>Carga masiva cursos de pensum</Form.Label>
            <Form.Control onChange={handleArchivoPensum} type="file" />
            <Button variant="light" onClick={handleSubmitPensum}>
              Cargar
            </Button>
          </Form.Group>
        </Form>
      </Container>
    </>
  )
}
