# refresh_token_tagplus
Job para atualização automática do token de acesos do tagplus

# Crie uma tabela tokens
CREATE TABLE tokens (
    id INT NOT NULL AUTO_INCREMENT,
    company VARCHAR(100) UNIQUE,
    access_token VARCHAR(100) UNIQUE,
    refresh_token VARCHAR(100) UNIQUE,
    expires_in INT,
    client_id VARCHAR(100) UNIQUE,
    client_secret VARCHAR(100) UNIQUE,
    expires_at DATETIME,
    created_at DATETIME,
    updated_at DATETIME,
    PRIMARY KEY (id)
) CHARACTER SET utf8;