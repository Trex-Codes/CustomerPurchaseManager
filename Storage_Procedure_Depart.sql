DELIMITER //
CREATE PROCEDURE p_all_users(IN Depat_param VARCHAR(50))
BEGIN 
	SELECT * FROM usuarios WHERE departamento = Depat_param;
END // 