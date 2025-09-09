-- Criação da base de dados para o projeto final
CREATE DATABASE cadastro_produtos;

-- Seleciona a base de dados criada
USE cadastro_produtos;

-- Criação da tabela produtos
CREATE TABLE produtos
(
    id      INT          NOT NULL AUTO_INCREMENT PRIMARY KEY,
    produto VARCHAR(100) NOT NULL,
    preco   FLOAT        NOT NULL,
    estoque INT          NOT NULL
);
