INSERT INTO productos_productos (nombre_producto, precio_producto, distribuidor_producto, descripcion_producto, stock, fk_restaurante_id) VALUES
-- Pescados agregados a la tabla de productos
('Tilapia 300-400 grs', 8.00, 'Distribuidor de Pescados del Norte', 'Filete de tilapia fresco, tamaño mediano.', 50, 1),
('Tilapia 400-500 grs', 9.00, 'Distribuidor de Pescados del Norte', 'Filete de tilapia fresco, tamaño mediano-grande.', 40, 1),
('Tilapia 500-600 grs', 10.00, 'Distribuidor de Pescados del Norte', 'Filete de tilapia fresco, tamaño grande.', 30, 1),
('Sierra', 12.00, 'Pescados del Caribe', 'Pescado fresco sierra, ideal para parrilla y sopas.', 25, 1),
('Salmón Caribeño', 15.00, 'Pescados del Caribe', 'Filete de salmón fresco estilo caribeño.', 20, 1),
('Salmón al Ajillo', 16.00, 'Pescados del Caribe', 'Salmón fresco preparado al ajillo.', 15, 1),
('Pargo Rojo', 13.00, 'Pescados del Caribe', 'Filete de pargo rojo, fresco y jugoso.', 18, 1),
('Bocachico', 7.00, 'Pescados del Caribe', 'Pescado fresco bocachico, ideal para frituras.', 30, 1),
('Filete de Baza', 9.00, 'Pescados del Caribe', 'Filete fresco de baza, suave y delicioso.', 22, 1),
('Carne Asada', 10.00, 'Carnes Selectas', 'Carne de res asada, jugosa y sazonada.', 40, 1),
('Churrasco', 12.00, 'Carnes Selectas', 'Churrasco de carne de res, cocinado a la perfección.', 35, 1),
('Pollo Asado', 8.00, 'Carnes Selectas', 'Pollo asado jugoso y bien sazonado.', 50, 1),
-- -----------------------------------------
('Patacones', 3.00, 'Snacks y Más', 'Papas fritas crujientes, recién hechas.', 60, 1),
('Tilapia 300-400 grs', 8.00, 'Distribuidor de Pescados del Norte', 'Filete de tilapia fresco, tamaño mediano.', 50, 1),
('Arroz blanco', 2.00, 'Granos del Sur', 'Arroz cocido, ideal como acompañamiento.', 100, 1),
('Arroz coco', 2.50, 'Granos del Sur', 'Arroz con coco, aromático y delicioso.', 80, 1),
('Ensalada de lechuga, pepino, sukini y cebolla', 3.00, 'Verduras Frescas', 'Mezcla de vegetales frescos con salsa vinagreta.', 30, 1),
('Frijoles', 2.00, 'Legumbres Selectas', 'Frijoles cocidos, sazonados al estilo casero.', 70, 1),
('Caldito de pescado', 1.50, 'Pescados del Norte', 'Sopa de pescado ligera y deliciosa.', 40, 1),
('Pepinos', 1.50, 'Frutas y Verduras Co', 'Pepinos frescos, cortados.', 50, 1),
('Sukinis', 2.00, 'Verduras del Huerto', 'Calabacines frescos, ideales para ensaladas.', 45, 1),
('Papas fritas', 3.00, 'Snacks y Más', 'Papas fritas crujientes, recién hechas.', 60, 1),
('Limonada de coco', 4.00, 'Bebidas Tropicales', 'Refrescante limonada con sabor a coco.', 30, 1),
('Limonada de tamarindo', 4.00, 'Bebidas Tropicales', 'Refrescante limonada con tamarindo.', 25, 1),
('Limonada de cereza', 4.00, 'Bebidas Tropicales', 'Limonada con un toque de cereza.', 20, 1),
('Limonada natural', 3.50, 'Bebidas Tropicales', 'Limonada clásica y refrescante.', 40, 1),
('Limonada de piña colada', 4.50, 'Bebidas Tropicales', 'Limonada con un toque tropical de piña colada.', 15, 1),
('Limonada de hierba buena', 3.50, 'Bebidas Tropicales', 'Refrescante limonada con hierba buena.', 25, 1),
('Limonada de mango biche', 4.00, 'Bebidas Tropicales', 'Limonada con sabor a mango biche.', 20, 1),
('Jugo de mango en agua', 3.50, 'Bebidas Naturales', 'Jugo de mango preparado en agua.', 30, 1),
('Jugo de mango en leche', 4.00, 'Bebidas Naturales', 'Jugo de mango preparado en leche.', 25, 1),
('Jugo de fresa en agua', 3.50, 'Bebidas Naturales', 'Jugo de fresa preparado en agua.', 20, 1),
('Jugo de fresa en leche', 4.00, 'Bebidas Naturales', 'Jugo de fresa preparado en leche.', 15, 1),
('Jugo de guanábana en agua', 3.50, 'Bebidas Naturales', 'Jugo de guanábana preparado en agua.', 20, 1),
('Jugo de guanábana en leche', 4.00, 'Bebidas Naturales', 'Jugo de guanábana preparado en leche.', 15, 1),
('Agua', 1.50, 'Bebidas Naturales', 'Botella de agua pura.', 100, 1),
('Leche', 2.00, 'Bebidas Naturales', 'Vaso de leche fresca.', 80, 1),
('Cerveza artesanal', 5.00, 'Cervezas Premium', 'Cerveza artesanal en botella.', 30, 1),
('Cerveza comercial', 4.00, 'Cervezas Locales', 'Cerveza comercial en botella.', 50, 1),
('Gaseosa cola', 2.50, 'Refrescos del País', 'Gaseosa cola en botella de vidrio.', 60, 1),
('Gaseosa naranja', 2.50, 'Refrescos del País', 'Gaseosa sabor naranja en botella de vidrio.', 50, 1);

-- Platos
INSERT INTO platos_platos (nombre_plato, descripcion_plato, precio, fk_restaurante_id, ingresado_en) VALUES
('Tilapia Económica', 'Tilapia de 300-400 grs con arroz coco, ensalada de pepino, sukini, cebolla, salsa vinagreta, caldito de pescado y patacones.', 15.00, 1),
('Tilapia Mediana', 'Tilapia de 400-500 grs con arroz coco, ensalada de pepino, sukini, cebolla, salsa vinagreta, caldito de pescado y patacones.', 18.00, 1),
('Tilapia Grande', 'Tilapia de 500-600 grs con arroz coco, ensalada de pepino, sukini, cebolla, salsa vinagreta, caldito de pescado y patacones.', 20.00, 1),
('Sierra', 'Pescado sierra con arroz coco, ensalada de pepino, sukini, cebolla, salsa vinagreta, caldito de pescado y patacones.', 22.00, 1),
('Salmón Caribeño', 'Salmón al estilo caribeño con arroz coco, ensalada de pepino, sukini, cebolla, salsa vinagreta, caldito de pescado y patacones.', 25.00, 1),
('Salmón al Ajillo', 'Salmón al ajillo con arroz coco, ensalada de pepino, sukini, cebolla, salsa vinagreta, caldito de pescado y patacones.', 26.00, 1),
('Pargo Rojo', 'Pargo rojo con arroz coco, ensalada de pepino, sukini, cebolla, salsa vinagreta, caldito de pescado y patacones.', 24.00, 1),
('Bocachico', 'Bocachico con arroz coco, ensalada de pepino, sukini, cebolla, salsa vinagreta, caldito de pescado y patacones.', 18.00, 1),
('Filete de Baza', 'Filete de baza con arroz coco, ensalada de pepino, sukini, cebolla, salsa vinagreta, caldito de pescado y patacones.', 17.00, 1),
('Carne Asada', 'Carne asada con arroz blanco, ensalada de pepino, sukini y cebolla, frijoles y papas fritas.', 15.00, 1),
('Churrasco', 'Churrasco con arroz blanco, ensalada de pepino, sukini y cebolla, frijoles y papas fritas.', 20.00, 1),
('Pollo Asado', 'Pollo asado con arroz blanco, ensalada de pepino, sukini y cebolla, frijoles y papas fritas.', 12.00, 1),
('Vegetales al Vapor', 'Sukinis y pepinos al vapor, acompañados de papas fritas.', 9.00, 1);



-- Relación de platos con productos corregida
INSERT INTO platos_platos_productos (fk_plato_id, fk_producto_id, fk_restaurante_id) VALUES
-- Platos de pescado
(1, 1, 1),  -- Tilapia 300-400 grs -> Filete de tilapia
(1, 16, 1), -- Tilapia 300-400 grs -> Arroz coco
(1, 17, 1), -- Tilapia 300-400 grs -> Ensalada de lechuga, pepino, sukini y cebolla
(1, 19, 1), -- Tilapia 300-400 grs -> Caldito de pescado
(1, 13, 1), -- Tilapia 300-400 grs -> Patacones
(3, 3, 1),  -- Tilapia 500-600 grs -> Filete de tilapia
(3, 16, 1), -- Tilapia 500-600 grs -> Arroz coco
(3, 17, 1), -- Tilapia 500-600 grs -> Ensalada de lechuga, pepino, sukini y cebolla
(3, 19, 1), -- Tilapia 500-600 grs -> Caldito de pescado
(3, 13, 1), -- Tilapia 500-600 grs -> Patacones
(4, 4, 1), -- Sierra -> Pescado sierra
(4, 16, 1), -- Sierra -> Arroz coco
(4, 17, 1), -- Sierra -> Ensalada de lechuga, pepino, sukini y cebolla
(4, 19, 1), -- Sierra -> Caldito de pescado
(4, 13, 1), -- Sierra -> Patacones
(5, 5, 1), -- Salmón Caribeño -> Filete de salmón
(5, 16, 1), -- Salmón Caribeño -> Arroz coco
(5, 17, 1), -- Salmón Caribeño -> Ensalada de lechuga, pepino, sukini y cebolla
(5, 19, 1), -- Salmón Caribeño -> Caldito de pescado
(5, 13, 1), -- Salmón Caribeño -> Patacones
(6, 6, 1), -- Salmón al Ajillo -> Filete de salmón
(6, 16, 1), -- Salmón al Ajillo -> Arroz coco
(6, 17, 1), -- Salmón al Ajillo -> Ensalada de lechuga, pepino, sukini y cebolla
(6, 19, 1), -- Salmón al Ajillo -> Caldito de pescado
(6, 13, 1), -- Salmón al Ajillo -> Patacones
(7, 7, 1), -- Pargo Rojo -> Filete de pargo
(7, 16, 1), -- Pargo Rojo -> Arroz coco
(7, 17, 1), -- Pargo Rojo -> Ensalada de lechuga, pepino, sukini y cebolla
(7, 19, 1), -- Pargo Rojo -> Caldito de pescado
(7, 13, 1), -- Pargo Rojo -> Patacones
(8, 8, 1),  -- Bocachico -> Pescado bocachico
(8, 16, 1), -- Bocachico -> Arroz coco
(8, 17, 1), -- Bocachico -> Ensalada de lechuga, pepino, sukini y cebolla
(8, 19, 1), -- Bocachico -> Caldito de pescado
(8, 13, 1), -- Bocachico -> Patacones
(9, 9, 1),  -- Filete de Baza -> Filete de basa
(9, 16, 1), -- Filete de Baza -> Arroz coco
(9, 17, 1), -- Filete de Baza -> Ensalada de lechuga, pepino, sukini y cebolla
(9, 19, 1), -- Filete de Baza -> Caldito de pescado
(9, 13, 1), -- Filete de Baza -> Patacones
-- Platos de carne
(10, 10, 1), -- Carne Asada -> Carne asada
(10, 15, 1), -- Carne Asada -> Arroz blanco
(10, 17, 1), -- Carne Asada -> Ensalada de lechuga, pepino, sukini y cebolla
(10, 18, 1), -- Carne Asada -> Frijoles
(10, 22, 1), -- Carne Asada -> Papas fritas
(11, 11, 1), -- Churrasco -> Carne de churrasco
(11, 15, 1), -- Churrasco -> Arroz blanco
(11, 17, 1), -- Churrasco -> Ensalada de lechuga, pepino, sukini y cebolla
(11, 18, 1), -- Churrasco -> Frijoles
(11, 22, 1), -- Churrasco -> Papas fritas
(12, 12, 1),  -- Pollo Asado -> Pollo asado
(12, 15, 1), -- Pollo Asado -> Arroz blanco
(12, 17, 1), -- Pollo Asado -> Ensalada de lechuga, pepino, sukini y cebolla
(12, 18, 1), -- Pollo Asado -> Frijoles
(12, 22, 1); -- Pollo Asado -> Papas fritas

