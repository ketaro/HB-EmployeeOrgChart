HB-EmployeeOrgChart
===================

Hackbright example, printing an employee org chart as a tree.
http://www.hackbrightacademy.com/

So now that we know Dictionaries, Classes, Trees and Recursion, let's put them all together in a little data modeling example.

With Classes, we've shown how we can represent our data in the computer using objects.  We've also shown how inheritance lets us extend our new classes based on existing ones (so we don't have to keep re-inventing the wheel).

With Dictionaries, we've shown how we can use a key to easily retreive a piece of information (our value).

We've learned that Trees are a way we can organize our data in a meaningful way.

Now lets put all that together in a simple example of an Employee directory.  A company is organized with a "CEO" at the top.  She has a level of direct reports (maybe VPs), who then have reports on down to the individual employees.  It's a natural structure for a tree!  Our CEO is the "root" node, managers with direct reports are the branch nodes and the employees are the leaves.

