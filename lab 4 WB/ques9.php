<?php
require 'db.php';

if (isset($_GET['id'])) {
    $id = filter_var($_GET['id'], FILTER_VALIDATE_INT);

    if ($id) {
        $stmt = $pdo->prepare("DELETE FROM students WHERE id = ?");
        $stmt->execute([$id]);

        echo "Student deleted successfully!";
    } else {
        echo "Invalid student ID.";
    }
}
?>

<h2>Delete Student</h2>

<a href="?id=1">Delete Student ID 1</a>s