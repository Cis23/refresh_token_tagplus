<h1><strong>Job de automação do token do sistema TagPlus<strong></h1>
<p> Job para atualização automática do token de acesos do tagplus </p>

<h2>Passo a passo para o uso</h2>
<ul>
  <li>
    <p><strong> 1º Crie uma tabela no seu banco de dados </strong><p>
    <span>
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
    </span>
  </li>
</ul>