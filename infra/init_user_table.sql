CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO users (username, email, created_at) VALUES 
('user1', 'user1@example.com', CURRENT_TIMESTAMP),
('user2', 'user2@example.com', CURRENT_TIMESTAMP),
('user3', 'user3@example.com', CURRENT_TIMESTAMP);