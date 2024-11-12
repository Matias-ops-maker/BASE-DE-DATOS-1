# Esquema de Base de Datos para Programas de Radio

## Tablas y Relaciones

### Radios
- **radio** (clave primaria)
- **año** (clave primaria)
- **frecuencia_radio**
- **gerente** (clave foránea que referencia a Gerentes)

### Gerentes
- **gerente** (clave primaria)

### Programas
- **radio** (clave foránea que referencia a Radios)
- **año** (clave foránea que referencia a Radios)
- **programa**
- **conductor**
- Clave primaria compuesta: **radio, año, programa**

## Diagrama del Esquema

![Diagrama del Esquema](ruta_al_diagrama)