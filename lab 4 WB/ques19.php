<?php
require 'db.php';

try {
    $pdo->beginTransaction();

    $sql = "INSERT INTO students
            (name, email, enrollment_date)
            VALUES (?, ?, ?)";

    $stmt = $pdo->prepare($sql);

    $stmt->execute([
        "Demo Student",
        "demo" . time() . "@example.com",
        date("Y-m-d")
    ]);

    $pdo->commit();

    echo "Transaction committed successfully!";
}
catch (Exception $e) {

    if ($pdo->inTransaction()) {
        $pdo->rollBack();
    }

    echo "Transaction rolled back!";
}
?>