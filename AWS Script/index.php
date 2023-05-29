<!DOCTYPE html>
<html>
<head>
  <!-- Add Bootstrap CSS link -->
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
  <div class="container">
    <form method="POST">
      <div class="form-group">
        <label for="keyInput">Enter Key:</label>
        <input type="text" name=ids class="form-control" id="keyInput" placeholder="Enter your key">
      </div>
      <button type="submit" class="btn btn-primary">Submit</button>
    </form>
<?php if(isset($_POST['ids']))
{
$parameter[]=$_POST['ids'];
$parameter[]='JIGS';
$output=shell_exec('python3 /var/app/current/aws-check/check_file.py '. escapeshellarg(' '.implode("|",array_values($parameter)).' ').' 2>&1');

echo $output;

}
?>
  </div>

  <!-- Add Bootstrap JS link (required for certain functionality) -->
  <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
</body>
</html>


