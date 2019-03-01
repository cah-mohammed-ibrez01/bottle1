<!DOCTYPE html>
<html lang="en">
<head>
  <title>Bootstrap Example</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/js/bootstrap.min.js"></script>
</head>
<body>

<div class="container">

% if name != '':
  <div class="alert alert-warning alert-dismissable">
    <a href="#" class="close" data-dismiss="alert" aria-label="close">×</a>
    <strong>Warning! {{name}} </strong>
  </div>
% else:

% end

  <h1>My First Bootstrap Page</h1>

<p>Add a new task to the ToDo list:</p>


<div class="form-group">
<form action="/new" method="POST">
  <input type="text" size="20" maxlength="20" name="task" class="form-control" id="usr">
  <input type="submit" name="save" value="save" class="btn">
</form>
</div>


</div>

</body>
</html>
