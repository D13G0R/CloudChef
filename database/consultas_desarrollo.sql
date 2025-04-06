INSERT INTO users_roles(nombre_rol, fk_restaurante_id) 
VALUES ("Administrador",1),("Cocinero",1), ("Mesero",1), ("Ayudante",1);

SET SQL_SAFE_UPDATES = 0;
SET SQL_SAFE_UPDATES = 1;

ALTER TABLE productos_productos
MODIFY COLUMN ingresado_en DATETIME(6) DEFAULT CURRENT_TIMESTAMP(6);

UPDATE productos_productos
SET ingresado_en = CURRENT_TIMESTAMP(6)
WHERE ingresado_en = '0000-00-00 00:00:00.000000';

UPDATE platos_platos
SET ingresado_en = CURRENT_TIMESTAMP
WHERE ingresado_en = '0000-00-00 00:00:00.000000';

INSERT INTO users_restaurantes (
    numero_identificacion_tributaria,
    rues,
    contraseña_restaurante,
    direccion_restaurante,
    tipo_restaurante,
    estado,
    cedula_propietario
) VALUES (
    '123456789', -- Número de identificación tributaria
    'Cevichon', -- RUES del restaurante
    'Cevichon123', -- Contraseña del restaurante
    'Calle 123, Ciudad', -- Dirección del restaurante
    'Comida Rápida', -- Tipo de restaurante
    'Activo', -- Estado del restaurante
    '987654321' -- Cédula del propietario
);


DELETE FROM users_users WHERE id=1;

UPDATE users_users SET fk_id_rol_id = 2 WHERE id=2;

INSERT INTO users_restaurantes (
    numero_identificacion_tributaria,
    rues,
    contraseña_restaurante,
    direccion_restaurante,
    tipo_restaurante,
    estado,
    cedula_propietario
) VALUES (
    '111111111', -- Número de identificación tributaria
    'FrutCevCam', -- RUES del restaurante
    'contraseñaSegura123', -- Contraseña del restaurante
    'Calle 51  47-42', -- Dirección del restaurante
    'Frutas y Ceviches de camaron', -- Tipo de restaurante
    'Activo', -- Estado del restaurante
    '1013367781' -- Cédula del propietario
);




INSERT INTO users_users (
    id, 
    password, 
    last_login, 
    is_superuser, 
    username, 
    first_name, 
    last_name, 
    email, 
    is_staff, 
    is_active, 
    date_joined, 
    fk_id_rol_id
)
VALUES (
    1,  -- ID único para el usuario
    'pbkdf2_sha256$870000$N2eueXbXUh7MtJjAlX4K1t$bHKG+PMpjbnpEYGLm/vjpf+cIhYikqx3UhFcwoB2hKg=',  -- Contraseña cifrada
    NULL,  -- Último inicio de sesión, NULL si nunca ha iniciado
    1,  -- is_superuser (1 para True)
    'admin',  -- Nombre de usuario
    'Admin',  -- Nombre
    'User',  -- Apellido
    'admin@example.com',  -- Correo electrónico
    1,  -- is_staff (1 para True)
    1,  -- is_active (1 para True)
    '2025-01-01 12:00:00',  -- Fecha de registro
    4   -- fk_id_rol_id (ID del rol "Administrador" en la tabla roles)
);