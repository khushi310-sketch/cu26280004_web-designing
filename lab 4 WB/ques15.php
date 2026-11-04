<?php
session_start();

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $username = $_POST['username'];
    $password = $_POST['password'];

    if ($username == "admin" && $password == "12345") {
        session_regenerate_id(true);
        $_SESSION['username'] = $username;

        header("Location: Q15_Session_Dashboard.php");
        exit;
    } else {
        echo "Invalid login!";
    }
}
?>

<form method="post">
    Username: <input type="text" name="username" required><br><br>
    Password: <input type="password" name="password" required><br><br>
    <button type="submit">Login</button>
</form>