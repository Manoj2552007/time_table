# Ex03 Time Table
# Date:23-04-2025
# AIM
To write a html webpage page to display your slot timetable.

# ALGORITHM
## STEP 1
Create a Django-admin Interface.

## STEP 2
Create a static folder and inert HTML code.

## STEP 3
Create a simple table using `<table>` tag in html.

## STEP 4
Add header row using `<th>` tag.

## STEP 5
Add your timetable using `<td>` tag.

## STEP 6
Execute the program using runserver command.

# PROGRAM
``` html
<html>
<head>
<title> Course Schedule </title>
</head>
<body>
<br>
<table align="center" width="540" cellspacing="2" cellpadding="4" border="5" bgcolor="cyan">
<caption><b>SCHEDULE OF ALL COURSES - ABDUL RAWOOF  (212224230003)</b></caption>
<tr align="center">
<th bgcolor="yellow">Day/Time</th>
<th bgcolor="yellow">Monday</th>
<th bgcolor="yellow">Tuesday</th>
<th bgcolor="yellow">Wednesday</th>
<th bgcolor="yellow">Thursday</th>
<th bgcolor="yellow">Friday</th>
</tr>
<tr align="center">
<th bgcolor="yellow">8-10</th>
<td >FREE SLOT</td>
<td>FREE SLOT</td>
<td>FREE SLOT</td>
<td>FREE SLOT</td>
<td>FREE SLOT</td>
</tr>
<tr align="center">
<th bgcolor="yellow">10-12</th>
<td>MATHS</td>
<td> OPERATING SYSTEMS</td>
<td>OPERATING SYSTEMS</td>
<td>STATISTICS</td>
<td>FUNDAMENTALS OF WEB</td>
</tr>
<tr>
<th bgcolor="yellow">12-1</th>
<td colspan="5" align="center">L U N C H</td>
</tr>
<tr align="center">
<th bgcolor="yellow">1-3</th>
<td >STATISTICS</td>
<td>DBMS</td>
<td>MENTOR MEET</td>
<td>EMPD</td>
<td>EMPD</td>
</tr>
<tr align="center">
<th bgcolor="yellow">3-5</th>
<td>FREE SLOT</td>
<td>FREE SLOT</td>
<td>FUNDAMENTALS OF WEB</td>
<td>CN</td>
<td>MATHS</td>
</tr>
</table>
<br>
<table align="center" cellspacing="2" cellpadding="4" border="2">
<tr align="center">
<th>S. No.</th>
<th>Subject Code</th>
<th>Subject Name</th>
</tr>
<tr>
<td align="center">1.</td>
<td align="center">19AI414</td>
<td>FUNDAMENTALS OF WEB APPLICATION DEVELOPMENT (FWAD)</td>
</tr>
<tr>
<td align="center">2.</td>
<td align="center">19AI304</td>
<td>FUNDAMENTALS OF C PROGRAMMING (C PROGRAM)</td>
</tr>
<tr>
<td align="center">3.</td>
<td align="center"></td>
<td> ENGINEERING MECHANICS AND PRODUCT(EMPD)</td>
</tr>
<tr>
<td align="center">4.</td>
<td align="center">19CS405</td>
<td>OPERATING SYSTEMS (OS)</td>
</tr>
<tr>
<td align="center">5.</td>
<td align="center">19MA211</td>
<td>STATISTICS AND NUMERICAL METHODS (MAT)</td>
</tr>
<tr>
<td align="center">6.</td>
<td align="center">19CS404</td>
<td>DATABASE MANAGEMENT SYSTEMS AND ITS APPLICATIONS (DBMS)</td>
</tr>
<td align="center">7.</td>
<td align="center">19CS406</td>
<td>COMPUTER NETWORKS(CN)</td>
</tr>
<td align="center">8.</td>
<td align="center">19EE305</td>
<td>MATHS FOR ARTIFICIAL INTELLIGENCE (MATHS FOR AI)</td>
</table>
</body>
</html>
```
# OUTPUT
![OUTPUT](./Screenshot%202025-04-22%20204420.png)
# RESULT
The program for creating slot timetable using basic HTML tags is executed successfully.
