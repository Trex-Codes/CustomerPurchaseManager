CREATE TABLE email_history (
	email_history_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    DNI VARCHAR (100) NULL
);

DELIMITER // 

CREATE TRIGGER tg_dni 
AFTER UPDATE ON usuarios
FOR EACH ROW 
BEGIN
	IF OLD.DNI <> NEW.DNI THEN
    INSERT INTO dni_history(user_id, DNI)
    VALUES (OLD.codigo_usuarios_id, OLD.DNI);
END IF;

END //

UPDATE usuarios SET DNI = "36.181.667" WHERE codigo_usuarios_id = 1;