CREATE DATABASE IF NOT EXISTS gamemaster;

CREATE USER IF NOT EXISTS 'gamemaster_user'@'localhost' IDENTIFIED BY 'GameMaster2026!';
GRANT ALL PRIVILEGES ON gamemaster.* TO 'gamemaster_user'@'localhost';
FLUSH PRIVILEGES;

USE gamemaster;

DROP TABLE IF EXISTS games;

CREATE TABLE games (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    platform VARCHAR(50) NOT NULL,
    price DECIMAL(6,2) NOT NULL,
    discount INT DEFAULT 0,
    image_url VARCHAR(500) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO games (name, platform, price, discount, image_url) VALUES
('ARC Raiders', 'PC (Steam)', 39.99, 31, 'https://i.ytimg.com/vi/Aivl1uvTGl0/hq720.jpg?sqp=-oaymwEhCK4FEIIDSFryq4qpAxMIARUAAAAAGAElAADIQj0AgKJD&rs=AOn4CLD-abFgf-0n3_G1Aw6c5WMyyXNx5w'),
('Quarantine Zone: The Last Check', 'PC (Steam)', 19.99, 33, 'https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/3419520/0e9ad1210bad7759be402611027b0039f8ac897a/capsule_616x353.jpg?t=1769849776'),
('Cult of the Lamb: Woolhaven', 'Nintendo', 16.99, 29, 'https://gaming-cdn.com/images/products/20252/orig/cult-of-the-lamb-woolhaven-pc-steam-cover.jpg?v=1769072654'),
('StarRupture', 'PC (Steam)', 19.99, 30, 'https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/1631270/header.jpg?t=1767955451'),
('Elden Ring', 'PC (Steam)', 59.99, 20, 'https://mountonline.org/wp-content/uploads/2022/04/elden-ring-cover-1.jpg'),
('Hogwarts Legacy', 'PC (Steam)', 59.99, 40, 'https://images.g2a.com/470x276/1x1x0/hogwarts-legacy-xbox-series-x-s-xbox-live-key-south-africa-i10000218808044/5f6dd91a46177c561331a902'),
('Cyberpunk 2077', 'PC (Steam)', 59.99, 50, 'https://cdn2.unrealengine.com/en-product-landscape-image-2560x1440-2560x1440-6dbb1ee2879a.jpg?resize=1&w=480&h=270&quality=hd'),
('God of War Ragnarök', 'PlayStation', 69.99, 25, 'https://www.lavanguardia.com/files/image_449_220/uploads/2018/08/03/5fa43c03d2bab.png'),
('The Legend of Zelda: TOTK', 'Nintendo', 69.99, 15, 'https://i.etsystatic.com/10064703/r/il/7a459d/4212246485/il_570xN.4212246485_aqhl.jpg'),
('Halo Infinite', 'Xbox', 59.99, 45, 'https://cdn.displate.com/artwork/380x270/2022-12-02/5420b53701bb4d4876c00fdcbcf27eeb_8d6f239a0a9e6907fa45879ba4427346.jpg'),
('Red Dead Redemption 2', 'PC (Steam)', 59.99, 60, 'https://www.lavanguardia.com/files/image_449_220/uploads/2018/09/20/5fa447fe8edd9.jpeg'),
('GTA V', 'PC (Steam)', 29.99, 50, 'https://www.mouse-sensitivity.com/uploads/monthly_2017_04/c42acec38aa8abd3226d2053578a7243.jpg.d9d92a37137139aa8bbedfc6ca0e8768.jpg');
