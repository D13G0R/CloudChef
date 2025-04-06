CREATE DATABASE restaurante;

USE restaurante;

-- Tabla de roles
CREATE TABLE roles (
    id SERIAL PRIMARY KEY, -- Django usa IntegerField o AutoField para claves primarias automáticas
    nombre VARCHAR(150) NOT NULL UNIQUE -- Django TextField corresponde a VARCHAR por defecto en PostgreSQL
);

-- Tabla de usuarios
CREATE TABLE usuarios (pedidos_pedidos
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(150) NOT NULL, -- Usar VARCHAR con un límite razonable
    correo VARCHAR(254) UNIQUE NOT NULL, -- Django EmailField acepta hasta 254 caracteres
    telefono VARCHAR(15), -- Django CharField con un límite para teléfonos
    fk_id_rol INTEGER REFERENCES roles(id) ON DELETE SET NULL -- Similar a ForeignKey(null=True)
);

-- Tabla de productos
CREATE TABLE productos (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(150) NOT NULL, -- Un límite razonable para nombres de productos
    descripcion TEXT, -- TextField mapea directamente a TEXT en PostgreSQL
    precio DECIMAL(10, 2) NOT NULL -- DecimalField en Django con precisión y escala
);

-- Tabla de platos
CREATE TABLE platos (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(150) NOT NULL,
    descripcion TEXT,
    precio DECIMAL(10, 2) NOT NULL
);

-- Tabla de pedidos
CREATE TABLE pedidos (
    id SERIAL PRIMARY KEY,
    fk_id_usuario INTEGER REFERENCES usuarios(id) ON DELETE CASCADE, -- ForeignKey con cascade delete
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Django DateTimeField(auto_now_add=True)
    total DECIMAL(10, 2) NOT NULL
);

-- Tabla intermedia: pedido_productos
CREATE TABLE pedido_productos (
    fk_id_pedido INTEGER REFERENCES pedidos(id) ON DELETE CASCADE,
    fk_id_producto INTEGER REFERENCES productos(id) ON DELETE CASCADE,
    cantidad INTEGER NOT NULL,
    PRIMARY KEY (fk_id_pedido, fk_id_producto) -- Clave compuesta
);

-- Tabla intermedia: pedido_platos
CREATE TABLE pedido_platos (
    fk_id_pedido INTEGER REFERENCES pedidos(id) ON DELETE CASCADE,
    fk_id_plato INTEGER REFERENCES platos(id) ON DELETE CASCADE,
    cantidad INTEGER NOT NULL,
    PRIMARY KEY (fk_id_pedido, fk_id_plato)
);

-- Tabla intermedia: plato_productos
CREATE TABLE plato_productos (
    fk_id_plato INTEGER REFERENCES platos(id) ON DELETE CASCADE,
    fk_id_producto INTEGER REFERENCES productos(id) ON DELETE CASCADE,
    cantidad INTEGER NOT NULL,
    PRIMARY KEY (fk_id_plato, fk_id_producto)
);