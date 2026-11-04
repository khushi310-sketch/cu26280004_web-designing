<?php
if (isset($_POST['theme'])) {

    $theme = $_POST['theme'];

    setcookie("theme", $theme, time() + 86400, "/");

    header("Location: Q16_Cookies_Theme.php");
    exit;
}

$theme = $_COOKIE['theme'] ?? 'light';
?>

<h2>Theme Preference</h2>

<p>Selected Theme: <?php echo htmlspecialchars($theme); ?></p>

<form method="post">
    <select name="theme">
        <option value="light">Light</option>
        <option value="dark">Dark</option>
    </select>

    <button type="submit">Save Theme</button>