<h1><strong>Job de automação de renovação de tokens do sistema TagPlus<strong></h1>
<p> O objetivo dessa job, é automatizar o processo de renovação de tokens solicitados pela API do tagplus: <a target="blank" title="DOC API TAGPLUS">https://developers.tagplus.com.br/apps</a> </p>

<h2>Passo a passo para o uso</h2>
<ul>
  <li>
    <p><strong> 1º Crie uma tabela no seu banco de dados, de preferência MySQL </strong><p>
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

  <li>
    <p>
      <strong> 
        2º Após a criação dos apps no sistema do tagplus na parte da documentação <a target="blank" title="DOC API TAGPLUS">https://developers.tagplus.com.br/apps</a> e documentar devidamente a API no POSTMAN
      </strong>
    <p>
    <span>
      Salve os dados na armazenados na tabela criada
    </span>
  </li>
  
</ul>