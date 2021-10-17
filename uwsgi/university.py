import os
import time
from urllib.parse import parse_qs
from html import escape

import psycopg2

def wrapBody(body, title="Blank Title"):

    return (
        "<html>\n"
        "<head>\n"
        f"<title>{title}</title>\n"
        "</head>\n"
        "<body>\n"
        f"{body}\n"
        "<hr>\n"
        f"<p>This page was generated at {time.ctime()}.</p>\n"
        "</body>\n"
        "</html>\n"
    )
def showAllStudents(conn):

    # get a cursor object. cursor object will help us run queries on the database
    cursor = conn.cursor()

    sql = """
    SELECT id, name
    FROM Student
    """

    cursor.execute(sql)

    ## create an HTML table for output:
    body = """
    <h2>Student List</h2>
    <p>
    <table border=1>
      <tr>
        <td><font size=+1"><b>id</b></font></td>
        <td><font size=+1"><b>name</b></font></td>
        <td><font size=+1"><b>delete</b></font></td>
      </tr>
    """

    count = 0
    # each iteration of this loop creates on row of output:
    for idNum, name in cursor:
        body += (
            "<tr>"
            f"<td><a href='?idNum={idNum}'>{name}</a></td>"
            "<td><form method='post' action='university.py'>"
            f"<input type='hidden' NAME='idNum' VALUE='{idNum}'>"
            '<input type="submit" name="deleteStudent" value="Delete">'
            "</form></td>"
            "</tr>\n"
        )
        count += 1

    body += "</table>" f"<p>Found {count} Students.</p>"

    return body

    ################################################################################
def showAddStudentForm():

    return """
    <h2>Add A Student</h2>
    <p>
    <FORM METHOD="POST">
    <table>
        <tr>
            <td>name</td>
            <td><INPUT TYPE="TEXT" NAME="name" VALUE=""></td>
        </tr>
        <tr>
            <td></td>
            <td>
            <input type="submit" name="addProfile" value="Add!">
            </td>
        </tr>
    </table>
    </FORM>
    """


################################################################################
def getUpdateStudentForm(conn, idNum):
    ## FIRST, get current data for this profile

    # get a cursor object. cursor object will help us run queries on the database
    cursor = conn.cursor()

    sql = """
    SELECT *
    FROM Student
    WHERE id=%s
    """
    cursor.execute(sql, (idNum,))

    # get the data from the database:
    data = cursor.fetchall()

    ## CREATE A FORM TO UPDATE THIS PROFILE
    (idNum, name) = data[0]

    return """
    <h2>Update Your Profile Page</h2>
    <p>
    <FORM METHOD="POST">
    <table>
        <tr>
            <td>Last Name</td>
            <td><INPUT TYPE="TEXT" NAME="name" VALUE="%s"></td>
        </tr>
        <tr>
            <td></td>
            <td>
            <input type="hidden" name="idNum" value="%s">
            <input type="submit" name="completeUpdate" value="Update!">
            </td>
        </tr>
    </table>
    </FORM>
    """ % (
        name,
        idNum,
    )


################################################################################
def addStudent(conn, name):

    # get a cursor object. cursor object will help us run queries on the database
    cursor = conn.cursor()

    sql = "SELECT max(ID) FROM Student"
    try:
        cursor.execute(sql)
        data = cursor.fetchone()
        nextID = int(data[0]) + 1
    except:
        nextID = 1

    sql = "INSERT INTO Student VALUES (%s,%s,%s,%s,%s)"
    params = (nextID, name)

    cursor.execute(sql, params)
    conn.commit()

    body = ""
    if cursor.rowcount > 0:
        body = "Add Student Succeeded."
    else:
        body = "Add Student Failed."

    return body, nextID



################################################################################
def updateStudent(conn, idNum, name):

    # get a cursor object. cursor object will help us run queries on the database
    cursor = conn.cursor()

    sql = "UPDATE Student SET name=%s WHERE id = %s"
    params = (name, idNum)

    cursor.execute(sql, params)
    conn.commit()

    if cursor.rowcount > 0:
        return "Update Student Succeeded."
    else:
        return "Update Student Failed."


