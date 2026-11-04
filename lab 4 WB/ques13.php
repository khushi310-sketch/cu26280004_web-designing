<?php
if (isset($_FILES['photo'])) {

    $file = $_FILES['photo'];

    $allowed = ['jpg', 'jpeg', 'png'];
    $extension = strtolower(
        pathinfo($file['name'], PATHINFO_EXTENSION)
    );

    if ($file['error'] !== UPLOAD_ERR_OK) {
        echo "File upload failed!";
    }
    elseif ($file['size'] > 2 * 1024 * 1024) {
        echo "File size must be below 2 MB!";
    }
    elseif (!in_array($extension, $allowed)) {
        echo "Only JPG and PNG files are allowed!";
    }
    else {
        $folder = "uploads/";

        if (!is_dir($folder)) {
            mkdir($folder, 0755, true);
        }

        $filename = bin2hex(random_bytes(12)) . "." . $extension;

        if (move_uploaded_file($file['tmp_name'], $folder . $filename)) {
            echo "Image uploaded successfully!";
        } else {
            echo "Unable to save image!";
        }
    }
}
?>

<form method="post" enctype="multipart/form-data">
    Select Image:
    <input type="file" name="photo" required>
    <button type="submit">Upload</button>
</form>