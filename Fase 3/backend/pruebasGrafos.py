from estructuras.ListaPensum.listaPensum import ListaPensum

lista = ListaPensum()

cursos = {
    "Cursos": [
        {
            "Codigo": "0017",
            "Nombre": "Social Humanistica 1",
            "Creditos": 4,
            "Prerequisitos": "",
            "Obligatorio": True
        },
        {
            "Codigo": "0101",
            "Nombre": "Matematica Basica 1",
            "Creditos": 7,
            "Prerequisitos": "",
            "Obligatorio": True
        },
        {
            "Codigo": "0039",
            "Nombre": "Deportes 1",
            "Creditos": 1,
            "Prerequisitos": "",
            "Obligatorio": False
        },
        {
            "Codigo": "0348",
            "Nombre": "Quimica General 1",
            "Creditos": 3,
            "Prerequisitos": "",
            "Obligatorio": True
        },
        {
            "Codigo": "0006",
            "Nombre": "Idioma tecnico 1",
            "Creditos": 2,
            "Prerequisitos": "",
            "Obligatorio": False
        },
        {
            "Codigo": "0019",
            "Nombre": "Social Humanistica 2",
            "Creditos": 4,
            "Prerequisitos": "0017",
            "Obligatorio": True
        },
        {
            "Codigo": "0103",
            "Nombre": "Matematica Basica 2",
            "Creditos": 7,
            "Prerequisitos": "0101",
            "Obligatorio": True
        },
        {
            "Codigo": "0005",
            "Nombre": "Tecnicas de estudio y de investigacion",
            "Creditos": 3,
            "Prerequisitos": "",
            "Obligatorio": True
        },
        {
            "Codigo": "0147",
            "Nombre": "Fisica basica",
            "Creditos": 5,
            "Prerequisitos": "0101",
            "Obligatorio": True
        },
        {
            "Codigo": "0008",
            "Nombre": "Idioma tecnico 2",
            "Creditos": 2,
            "Prerequisitos": "0006",
            "Obligatorio": False
        },
        {
            "Codigo": "0795",
            "Nombre": "Logica de sistemas",
            "Creditos": 2,
            "Prerequisitos": "0103",
            "Obligatorio": True
        },
        {
            "Codigo": "0960",
            "Nombre": "Matematica computo 1",
            "Creditos": 5,
            "Prerequisitos": "0103",
            "Obligatorio": True
        },
        {
            "Codigo": "0770",
            "Nombre": "Introduccion a la programacion y computacion 1",
            "Creditos": 4,
            "Prerequisitos": "0103",
            "Obligatorio": True
        },
        {
            "Codigo": "0107",
            "Nombre": "Matematica intermedia 1",
            "Creditos": 10,
            "Prerequisitos": "0103",
            "Obligatorio": True
        },
        {
            "Codigo": "0150",
            "Nombre": "Fisica 1",
            "Creditos": 10,
            "Prerequisitos": "0103,0147",
            "Obligatorio": True
        },
        {
            "Codigo": "0009",
            "Nombre": "Idioma tecnico 3",
            "Creditos": 10,
            "Prerequisitos": "0008",
            "Obligatorio": False
        },
        {
            "Codigo": "0732",
            "Nombre": "Estadistica 1",
            "Creditos": 5,
            "Prerequisitos": "0107,0005",
            "Obligatorio": True
        },
        {
            "Codigo": "0796",
            "Nombre": "Lenguajes formales y de programacion",
            "Creditos": 3,
            "Prerequisitos": "0770,0795,0960",
            "Obligatorio": True
        },
        {
            "Codigo": "0962",
            "Nombre": "Matematica computo 2",
            "Creditos": 5,
            "Prerequisitos": "0770,0795,0960",
            "Obligatorio": True
        },
        {
            "Codigo": "0771",
            "Nombre": "Introduccion a la programacion y computacion 2",
            "Creditos": 5,
            "Prerequisitos": "0107,0770,0795,0960",
            "Obligatorio": True
        },
        {
            "Codigo": "0112",
            "Nombre": "Matematica intermedia 2",
            "Creditos": 5,
            "Prerequisitos": "0107",
            "Obligatorio": True
        },
        {
            "Codigo": "0114",
            "Nombre": "Matematica intermedia 3",
            "Creditos": 5,
            "Prerequisitos": "0107",
            "Obligatorio": True
        },
        {
            "Codigo": "0152",
            "Nombre": "Fisica 2",
            "Creditos": 6,
            "Prerequisitos": "0107,0150",
            "Obligatorio": True
        },
        {
            "Codigo": "0011",
            "Nombre": "Idioma tecnico 4",
            "Creditos": 2,
            "Prerequisitos": "0009",
            "Obligatorio": False
        },
        {
            "Codigo": "2025",
            "Nombre": "Practica inicial",
            "Creditos": 0,
            "Prerequisitos": "0103,0770",
            "Obligatorio": True
        },
        {
            "Codigo": "0736",
            "Nombre": "Analisis probabilistico",
            "Creditos": 4,
            "Prerequisitos": "0732",
            "Obligatorio": True
        },
        {
            "Codigo": "0777",
            "Nombre": "Organizacion de lenguajes y compiladores 1",
            "Creditos": 4,
            "Prerequisitos": "0771,0796,0962",
            "Obligatorio": True
        },
        {
            "Codigo": "0964",
            "Nombre": "Organizacion computacional",
            "Creditos": 3,
            "Prerequisitos": "0152,0771,0962",
            "Obligatorio": True
        },
        {
            "Codigo": "0772",
            "Nombre": "Estructura de datos",
            "Creditos": 5,
            "Prerequisitos": "0771,0796,0962",
            "Obligatorio": True
        },
        {
            "Codigo": "0018",
            "Nombre": "Filosofia de la ciencia",
            "Creditos": 3,
            "Prerequisitos": "0019",
            "Obligatorio": False
        },
        {
            "Codigo": "0116",
            "Nombre": "Matematica aplicada 3",
            "Creditos": 5,
            "Prerequisitos": "0112,0114",
            "Obligatorio": True
        },
        {
            "Codigo": "0118",
            "Nombre": "Matematica aplicada 1",
            "Creditos": 6,
            "Prerequisitos": "0112,0114",
            "Obligatorio": True
        },
        {
            "Codigo": "0722",
            "Nombre": "Teoria de sistemas 1",
            "Creditos": 5,
            "Prerequisitos": "0732,0772,0116,0118",
            "Obligatorio": True
        },
        {
            "Codigo": "0601",
            "Nombre": "Investigacion de operaciones 1",
            "Creditos": 5,
            "Prerequisitos": "0771,0732",
            "Obligatorio": True
        },
        {
            "Codigo": "0014",
            "Nombre": "Economia",
            "Creditos": 4,
            "Prerequisitos": "0732",
            "Obligatorio": True
        },
        {
            "Codigo": "0781",
            "Nombre": "Organizacion de lenguajes y compiladores 2",
            "Creditos": 5,
            "Prerequisitos": "0777,0772",
            "Obligatorio": True
        },
        {
            "Codigo": "0778",
            "Nombre": "Arquitectura de computadores y ensambladores 1",
            "Creditos": 5,
            "Prerequisitos": "0796,0964",
            "Obligatorio": True
        },
        {
            "Codigo": "0773",
            "Nombre": "Manejo e implementacion de archivos",
            "Creditos": 4,
            "Prerequisitos": "0772,0796",
            "Obligatorio": True
        },
        {
            "Codigo": "0724",
            "Nombre": "Teoria de sistemas 2",
            "Creditos": 5,
            "Prerequisitos": "0722,0601,0736",
            "Obligatorio": True
        },
        {
            "Codigo": "0603",
            "Nombre": "Investigacion de operaciones 2",
            "Creditos": 5,
            "Prerequisitos": "0601",
            "Obligatorio": True
        },
        {
            "Codigo": "0281",
            "Nombre": "Sistemas operativos 1",
            "Creditos": 5,
            "Prerequisitos": "0781,0778",
            "Obligatorio": True
        },
        {
            "Codigo": "0779",
            "Nombre": "Arquitectura de computadores y ensambladores 2",
            "Creditos": 4,
            "Prerequisitos": "0778",
            "Obligatorio": True
        },
        {
            "Codigo": "0970",
            "Nombre": "Redes de computadoras 1",
            "Creditos": 4,
            "Prerequisitos": "0773,0778",
            "Obligatorio": True
        },
        {
            "Codigo": "0771",
            "Nombre": "Sistemas de bases de datos 1",
            "Creditos": 5,
            "Prerequisitos": "0773",
            "Obligatorio": True
        },
        {
            "Codigo": "2036",
            "Nombre": "Practica intermedia",
            "Creditos": 0,
            "Prerequisitos": "0778,0777,0773,2025",
            "Obligatorio": True
        },
        {
            "Codigo": "0285",
            "Nombre": "Sistemas operativos 2",
            "Creditos": 4,
            "Prerequisitos": "0281",
            "Obligatorio": True
        },
        {
            "Codigo": "0975",
            "Nombre": "Redes de computadoras 2",
            "Creditos": 4,
            "Prerequisitos": "0970",
            "Obligatorio": True
        },
        {
            "Codigo": "0775",
            "Nombre": "Sistemas de bases de datos 2",
            "Creditos": 4,
            "Prerequisitos": "0281,0774",
            "Obligatorio": True
        },
        {
            "Codigo": "0283",
            "Nombre": "Analisis y diseño de sistemas 1",
            "Creditos": 5,
            "Prerequisitos": "0774",
            "Obligatorio": True
        },
        {
            "Codigo": "0797",
            "Nombre": "Seminario de sistemas 1",
            "Creditos": 3,
            "Prerequisitos": "0724",
            "Obligatorio": True
        },
        {
            "Codigo": "0729",
            "Nombre": "Modelacion y simulacion 1",
            "Creditos": 5,
            "Prerequisitos": "0724,0603",
            "Obligatorio": True
        },
        {
            "Codigo": "0786",
            "Nombre": "Sistemas organizacionales y gerenciales 1",
            "Creditos": 4,
            "Prerequisitos": "0283,0722",
            "Obligatorio": True
        },
        {
            "Codigo": "0972",
            "Nombre": "Sistemas organizacionales y gerenciales 1",
            "Creditos": 4,
            "Prerequisitos": "0781,0775,0724",
            "Obligatorio": True
        },
        {
            "Codigo": "0785",
            "Nombre": "Analisis y diseño de sistemas 2",
            "Creditos": 5,
            "Prerequisitos": "0283",
            "Obligatorio": True
        },
        {
            "Codigo": "0798",
            "Nombre": "Seminario de sistemas 2",
            "Creditos": 3,
            "Prerequisitos": "0797",
            "Obligatorio": True
        },
        {
            "Codigo": "2009",
            "Nombre": "Practica final",
            "Creditos": 0,
            "Prerequisitos": "2036",
            "Obligatorio": True
        },
        {
            "Codigo": "0787",
            "Nombre": "Sistemas organizacionales y gerenciales 2",
            "Creditos": 4,
            "Prerequisitos": "0786",
            "Obligatorio": True
        },
        {
            "Codigo": "0720",
            "Nombre": "Modelacion y simulacion 2",
            "Creditos": 5,
            "Prerequisitos": "0729",
            "Obligatorio": True
        },
        {
            "Codigo": "0780",
            "Nombre": "Software avanzado",
            "Creditos": 6,
            "Prerequisitos": "0785",
            "Obligatorio": True
        },
        {
            "Codigo": "0799",
            "Nombre": "Seminario de investigacion",
            "Creditos": 3,
            "Prerequisitos": "0798",
            "Obligatorio": True
        }
    ]
}

for curso in cursos["Cursos"]:
    codigo = curso['Codigo']
    nombre = curso['Nombre']
    creditos = curso['Creditos']
    prerequisitos = curso['Prerequisitos']
    obligatorio = curso['Obligatorio']

    lista.insertar(codigo, nombre, creditos, prerequisitos, obligatorio)

lista.graficarRedCursos()