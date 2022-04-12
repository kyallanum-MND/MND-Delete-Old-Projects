### WS-Delete-Old-Projects

This is a tool created by WhiteSource Support, to easily delete all projects in an organization older than a certain amount of days. 

To run, you will need Python installed. From there you just need to:

```
$> pip install -r requirements.txt
$> python init.py
```

The concept behind this is that it will get every single product and project in your organization, and then delete every single project that has a creation date older than "x" amount of days.