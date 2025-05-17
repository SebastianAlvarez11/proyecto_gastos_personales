CREATE TABLE usuarios(
    id SERIAL PRIMARY KEY,
    nombre TEXT,
    tipo_documento TEXT,
    numero_documento INT UNIQUE,
    contrasena TEXT,
    correo TEXT,
    fecha_nacimiento DATE
);

CREATE TABLE transacciones(
    id SERIAL PRIMARY KEY,
    cantidad_dinero DECIMAL,
    categoria TEXT,
    fecha TIMESTAMP,
    id_usuario INT,
    CONSTRAINT id_foreign_key FOREIGN KEY (id_usuario) REFERENCES usuarios (id)
);


INSERT INTO usuarios(nombre, tipo_documento, numero_documento, contrasena, correo, fecha_nacimiento)
VALUES
('Luis', 'cédula', 1029315667, 'Luis.1000', 'luis10@gmail.com', '02/02/2001'),
('Luisa', 'cédula', 1029315660, 'Luisa.1000', 'luisa10@gmail.com', '12/12/2000');


INSERT INTO transacciones(id_usuario, cantidad_dinero, categoria, fecha)
VALUES
(1, 1500000, 'pago', '02-02-2025  9:00'),
(1, -20000, 'comida', '05-02-2025  12:00'),
(2, 2000000, 'pago', '02-02-2025  9:00'),
(2, 50000, 'rifa', '07-02-2025  5:00');
