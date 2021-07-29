<!DOCTYPE html>

% rebase('layout.tpl', title='Home Page', year=year)
<html>
<head>
    <link rel="stylesheet" type="text/css" href="/static/content/bootstrap.min.css" />
    <link rel="stylesheet" type="text/css" href="/static/content/site.css" />


      <title>New User</title>
</head>
<body>
<!--New user form for them to sign up with us -->
<h2>New User</h2>
    <form method="post">
        <label for="firstName">First Name</label>
        <input type="text" id="firstName" name="firstName">

        <label for="lastName">Last Name</label>
        <input type="text" id="lastName" name="lastName">

        <label for="password">Password</label>
        <input type="text" id="password" name="password">

        <label for="email">Email</label>
        <input type="email" id="email" name="email"><br>

        <button type="submit">Submit</button>

    </form>

</body>
</html>