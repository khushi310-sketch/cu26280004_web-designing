<?php
require 'db.php';

if ($_SERVER["REQUEST_METHOD"] == "POST") {

    $username = $_POST['username'];
    $password = $_POST['password'];

    $hash = password_hash($password, PASSWORD_DEFAULT);

    $sql = "INSERT INTO users (username, password_hash)
            VALUES (?, ?)
            ON DUPLICATE KEY UPDATE password_hash = VALUES(password_hash)";

    $stmt = $pdo->prepare($sql);
    $stmt->execute([$username, $hash]);

    $check = $pdo->prepare(
        "SELECT password_hash FROM users WHERE username = ?"
    );

    $check->execute([$username]);
    $storedHash = $check->fetchColumn();

    if (password_verify($password, $storedHash)) {
        echo "Password verified successfully!";
    } else {
        echo "Password verification failed!";
    }
}
?>

<form method="post">
    Username: <input type="text" name="username" required><br><br>
    Password: <input type="password" name="password" required><br><br>
    <button type="submit">Save Password</button>
</form>