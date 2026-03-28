CREATE DATABASE loja_jogos;
USE loja_jogos;

CREATE TABLE clientes (
    id INT PRIMARY KEY,
    nome VARCHAR(50),
    cidade VARCHAR(50)
);

INSERT INTO clientes VALUES
(1, 'Ana', 'São Paulo'),
(2, 'Bruno', 'Rio de Janeiro'),
(3, 'Carla', 'São Paulo'),
(4, 'Diego', 'Belo Horizonte'),
(5, 'Thomas', 'São Paulo');

CREATE TABLE produtos (
    id INT PRIMARY KEY,
    nome VARCHAR(100),
    preco DECIMAL(10,2),
    categoria VARCHAR(50)
);

INSERT INTO produtos VALUES
(1, 'Elden Ring', 249.90, 'RPG'),
(2, 'Minecraft', 99.90, 'Sandbox'),
(3, 'Hollow Knight', 46.99, 'Aventura'),
(4, 'GTA V', 79.90, 'Aventura'),
(5, 'Cyberpunk 2077', 199.90, 'RPG');

CREATE TABLE pedidos (
    id INT PRIMARY KEY,
    cliente_id INT,
    produto_id INT,
    quantidade INT,
    FOREIGN KEY (cliente_id) REFERENCES clientes(id),
    FOREIGN KEY (produto_id) REFERENCES produtos(id)
);

INSERT INTO pedidos VALUES
(1, 1, 1, 2),
(2, 1, 3, 1),
(3, 2, 5, 1),
(4, 3, 1, 3),
(5, 3, 2, 2),
(6, 5, 4, 1),
(7, 5, 3, 4);

SELECT nome, preco
FROM produtos
WHERE categoria = 'RPG'
ORDER BY preco DESC;

SELECT c.nome, p.id AS pedido_id
FROM clientes c
LEFT JOIN pedidos p ON c.id = p.cliente_id;

SELECT 
    c.nome,
    SUM(pr.preco * pe.quantidade) AS total_gasto
FROM clientes c
JOIN pedidos pe ON c.id = pe.cliente_id
JOIN produtos pr ON pe.produto_id = pr.id
GROUP BY c.nome;

SELECT 
    categoria,
    AVG(preco) AS preco_medio
FROM produtos
GROUP BY categoria
HAVING AVG(preco) > 100;

SELECT 
    pr.nome,
    COUNT(pe.id) AS total_pedidos
FROM produtos pr
LEFT JOIN pedidos pe ON pr.id = pe.produto_id
GROUP BY pr.nome;
