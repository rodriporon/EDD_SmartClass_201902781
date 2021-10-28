import React, { useState } from 'react'
import Container from 'react-bootstrap/Container'
import Form from 'react-bootstrap/Form'
import Button from 'react-bootstrap/Button'

import './index.css'
import useCargaEstudiantes from '../../hooks/useCargaMasiva'

export default function Admin() {
  const [estudiantes, setEstudiantes] = useState('')

  const { cargaEstudiantes } = useCargaEstudiantes()

  const handleArchivoEstudiantes = (e) => {
    const fileReader = new FileReader()
    fileReader.readAsText(e.target.files[0], 'UTF-8')
    fileReader.onload = (e) => {
      console.log('e.target.result', e.target.result)
      setEstudiantes(e.target.result)
    }
  }

  const handleSubmitEstudiantes = (e) => {
    e.preventDefault()
    console.log(`handleSubmitEstudiantes: ${estudiantes}`)
    cargaEstudiantes(estudiantes)
  }

  console.log(estudiantes)
  return (
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
  )
}
