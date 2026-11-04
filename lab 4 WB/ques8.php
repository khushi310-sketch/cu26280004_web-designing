<?php
require 'db.php';

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $id = $_POST['id'];
    $email = $_POST['email'];

    $sql = "UPDATE students SET email = ? WHERE id = ?";
    $stmt = $pdo->prepare($sql);
    $stmt->execute([$email, $id]);

    echo "Student email updated successfully!";
}
?>

<form method="post">
    Student ID: <input type="number" name="id" required><br><br>
    New Email: <input type="email" name="email" required><br><br>
    <button type="submit">Update</button>
</form>