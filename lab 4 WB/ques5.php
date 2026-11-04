<?php
require 'db.php';

$sql = "CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    enrollment_date DATE
)";

$pdo->exec($sql);

echo "Students table created successfully!";
?>s