-- Seleciona a base de dados cadastro_produtos
USE cadastro_produtos;

-- Seleciona todos os dados da tabela produtos
SELECT
    *
FROM
    produtos;

-- Deletando todos os dados da tabela produtos
DELETE FROM produtos WHERE id = 2;