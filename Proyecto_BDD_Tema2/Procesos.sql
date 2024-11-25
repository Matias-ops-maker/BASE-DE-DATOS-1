DELIMITER $$

CREATE PROCEDURE RegistrarOrden(
    IN p_id_cliente INT,
    IN p_id_producto INT,
    IN p_cantidad INT
)
BEGIN
    DECLARE stock_actual INT;

    SELECT cantidad_stock INTO stock_actual 
    FROM Productos 
    WHERE id_producto = p_id_producto;

    IF stock_actual >= p_cantidad THEN
        INSERT INTO Ordenes (id_cliente, id_producto, fecha, cantidad_unidades) 
        VALUES (p_id_cliente, p_id_producto, CURDATE(), p_cantidad);

        UPDATE Productos 
        SET cantidad_stock = cantidad_stock - p_cantidad 
        WHERE id_producto = p_id_producto;

        SELECT 'Orden registrada con exito';
    ELSE
        SELECT 'Stock insuficiente para completar la orden-solicitud';
    END IF;
END$$

DELIMITER ;