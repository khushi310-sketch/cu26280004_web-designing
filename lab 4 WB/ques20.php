<?php
echo "<h2>PHP Extension Status</h2>";

$extensions = [
    'mysqli',
    'pdo_mysql',
    'mbstring',
    'curl'
];

foreach ($extensions as $extension) {

    if (extension_loaded($extension)) {
        echo $extension . " is Enabled<br>";
    } else {
        echo $extension . " is Disabled<br>";
    }
}
?>