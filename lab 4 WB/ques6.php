<?php
require 'db.php';

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name = $_POST['name'];
    $email = $_POST['email'];
    $date = $_POST['enrollment_date'];

    $sql = "INSERT INTO students (name, email, enrollment_date)
            VALUES (?, ?, ?)";

    $stmt = $pdo->prepare($sql);
    $stmt->execute([$name, $email, $date]);

    echo "Student inserted successfully!";
}
?>

<form method="post">
    Name: <input type="text" name="name" required><br><br>
    Email: <input type="email" name="email" required><br><br>
    Date: <input type="date" name="enrollment_date" required><br><br>
    <button type="submit">Insert Student</button>
</form>