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

def showAllRoom(conn):

    # get a cursor object. cursor object will help us run queries on the database
    cursor = conn.cursor()

    sql = """
    SELECT id, name, capacity
    FROM Room
    """

    cursor.execute(sql)

    ## create an HTML table for output:
    body = """
    <h2>Room List</h2>
    <p>
    <table border=1>
      <tr>
        <td><font size=+1"><b>id</b></font></td>
        <td><font size=+1"><b>name</b></font></td>
        <td><font size=+1"><b>capacity</b></font></td>
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
            '<input type="submit" name="deleteRoom" value="Delete">'
            "</form></td>"
            "</tr>\n"
        )
        count += 1

    body += "</table>" f"<p>Found {count} Rooms.</p>"

    return body

def showAllCourse(conn):

    # get a cursor object. cursor object will help us run queries on the database
    cursor = conn.cursor()

    sql = """
    SELECT name, start_time, end_time, room
    FROM Course
    """

    cursor.execute(sql)

    ## create an HTML table for output:
    body = """
    <h2>Course List</h2>
    <p>
    <table border=1>
      <tr>
        <td><font size=+1"><b>name</b></font></td>
        <td><font size=+1"><b>start_time</b></font></td>
        <td><font size=+1"><b>end_time</b></font></td>
        <td><font size=+1"><b>room</b></font></td>
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
            '<input type="submit" name="deleteCourse" value="Delete">'
            "</form></td>"
            "</tr>\n"
        )
        count += 1

    body += "</table>" f"<p>Found {count} Courses.</p>"

    return body


def showStudentPage(conn, idNum):

    body = """
    <a href="./university.py">Return to main page.</a>
    """

    # get a cursor object. cursor object will help us run queries on the database
    cursor = conn.cursor()

    sql = """
    SELECT *
    FROM Student
    WHERE id=%s
    """
    cursor.execute(sql, (int(idNum),))

    # get the data from the database:
    data = cursor.fetchall()

    ## show student information
    (idNum, name) = data[0]

    body += """
    <h2>%s %s's Student Page</h2>
    <p>
    <table border=1>
        <tr>
            <td>name</td>
            <td>%s</td>
        </tr>
    </table>
    """ % (
        name,
    )

    ## provide an update button:
    body += (
        """
    <FORM METHOD="POST" action="university.py">
    <INPUT TYPE="HIDDEN" NAME="idNum" VALUE="%s">
    <INPUT TYPE="SUBMIT" NAME="showUpdateStudentForm" VALUE="Update Student">
    </FORM>
    """
        % idNum
    )

def showRoomPage(conn, idNum):

    body = """
    <a href="./university.py">Return to main page.</a>
    """

    # get a cursor object. cursor object will help us run queries on the database
    cursor = conn.cursor()

    sql = """
    SELECT *
    FROM Room
    WHERE id=%s
    """
    cursor.execute(sql, (int(idNum),))

    # get the data from the database:
    data = cursor.fetchall()

    ## show student information
    (idNum, name, capacity) = data[0]

    body += """
    <h2>%s %s's Room Page</h2>
    <p>
    <table border=1>
        <tr>
            <td>name</td>
            <td>%s</td>
            <td>capacity</td>
            <td>%s</td>
        </tr>
    </table>
    """ % (
        name,
        capacity
    )

    ## provide an update button:
    body += (
        """
    <FORM METHOD="POST" action="university.py">
    <INPUT TYPE="HIDDEN" NAME="idNum" VALUE="%s">
    <INPUT TYPE="SUBMIT" NAME="showUpdateStudentForm" VALUE="Update Student">
    </FORM>
    """
        % idNum
    )

def showCoursePage(conn, idNum):

    body = """
    <a href="./university.py">Return to main page.</a>
    """

    # get a cursor object. cursor object will help us run queries on the database
    cursor = conn.cursor()

    sql = """
    SELECT *
    FROM Course
    WHERE id=%s
    """
    cursor.execute(sql, (int(idNum),))

    # get the data from the database:
    data = cursor.fetchall()

    ## show student information
    (idNum, name, start_time, end_time, room) = data[0]

    body += """
    <h2>%s %s's Course Page</h2>
    <p>
    <table border=1>
        <tr>
            <td>name</td>
            <td>start_time</td>
            <td>end_time</td>
            <td>room</td>
            <td>%s</td>
        </tr>
    </table>
    """ % (
        name, 
        start_time, 
        end_time,
        room


    )

    ## provide an update button:
    body += (
        """
    <FORM METHOD="POST" action="university.py">
    <INPUT TYPE="HIDDEN" NAME="idNum" VALUE="%s">
    <INPUT TYPE="SUBMIT" NAME="showUpdateCourseForm" VALUE="Update Course">
    </FORM>
    """
        % idNum
    )

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
            <input type="submit" name="addStudent" value="Add!">
            </td>
        </tr>
    </table>
    </FORM>
    """

def showAddRoomForm():

    return """
    <h2>Add A Room</h2>
    <p>
    <FORM METHOD="POST">
    <table>
        <tr>
            <td>name</td>
            <td><INPUT TYPE="TEXT" NAME="name" VALUE=""></td>
            <td>capacity</td>
            <td><INPUT TYPE="TEXT" NAME="capacity" VALUE=""></td>
        </tr>
        <tr>
            <td></td>
            <td>
            <input type="submit" name="addRoom" value="Add!">
            </td>
        </tr>
    </table>
    </FORM>
    """
################################################################################
def showAddCourseForm():

    return """
    <h2>Add A Course</h2>
    <p>
    <FORM METHOD="POST">
    <table>
        <tr>
            <td>name</td>
            <td><INPUT TYPE="TEXT" NAME="name" VALUE=""></td>
            <td>start time</td>
            <td><INPUT TYPE="TEXT" NAME="start_time" VALUE=""></td>
            <td>end time</td>
            <td><INPUT TYPE="TEXT" NAME="end_time" VALUE=""></td>
            <td>room</td>
            <td><INPUT TYPE="TEXT" NAME="room" VALUE=""></td>
        </tr>
        <tr>
            <td></td>
            <td>
            <input type="submit" name="addCourse" value="Add!">
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

def getUpdateRoomForm(conn, idNum):
    ## FIRST, get current data for this profile

    # get a cursor object. cursor object will help us run queries on the database
    cursor = conn.cursor()

    sql = """
    SELECT *
    FROM Room
    WHERE id=%s
    """
    cursor.execute(sql, (idNum,))

    # get the data from the database:
    data = cursor.fetchall()

    ## CREATE A FORM TO UPDATE THIS PROFILE
    (idNum, name, capacity) = data[0]

    return """
    <h2>Update Room Page</h2>
    <p>
    <FORM METHOD="POST">
    <table>
        <tr>
            <td>Name</td>
            <td><INPUT TYPE="TEXT" NAME="name" VALUE="%s"></td>
            <td>Capacity</td>
            <td><INPUT TYPE="TEXT" NAME="capacity" VALUE="%s"></td>
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
        capacity,
        idNum,
    )

################################################################################
def getUpdateCourseForm(conn, idNum):
    ## FIRST, get current data for this profile

    # get a cursor object. cursor object will help us run queries on the database
    cursor = conn.cursor()

    sql = """
    SELECT *
    FROM Course
    WHERE id=%s
    """
    cursor.execute(sql, (idNum,))

    # get the data from the database:
    data = cursor.fetchall()

    ## CREATE A FORM TO UPDATE THIS PROFILE
    (name, start_time, end_time, room) = data[0]

    return """
    <h2>Update Your Profile Page</h2>
    <p>
    <FORM METHOD="POST">
    <table>
        <tr>
            <td>name</td>
            <td><INPUT TYPE="TEXT" NAME="name" VALUE="%s"></td>
            <td>start_time</td>
            <td><INPUT TYPE="TEXT" NAME="start_time" VALUE="%s"></td>
            <td>end_time</td>
            <td><INPUT TYPE="TEXT" NAME="end_time" VALUE="%s"></td>
            <td>room</td>
            <td><INPUT TYPE="TEXT" NAME="room" VALUE="%s"></td>
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
        start_time,
        end_time,
        room,
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

    sql = "INSERT INTO Student VALUES (%s,%s)"
    params = (nextID, name)

    cursor.execute(sql, params)
    conn.commit()

    body = ""
    if cursor.rowcount > 0:
        body = "Add Student Succeeded."
    else:
        body = "Add Student Failed."

    return body, nextID

def addRoom(conn, name, capacity):

    # get a cursor object. cursor object will help us run queries on the database
    cursor = conn.cursor()

    sql = "SELECT max(ID) FROM Room"
    try:
        cursor.execute(sql)
        data = cursor.fetchone()
        nextID = int(data[0]) + 1
    except:
        nextID = 1

    sql = "INSERT INTO Room VALUES (%s,%s,%s)"
    params = (nextID, name, capacity)

    cursor.execute(sql, params)
    conn.commit()

    body = ""
    if cursor.rowcount > 0:
        body = "Add Room Succeeded."
    else:
        body = "Add Room Failed."

    return body, nextID
    ################################################################################
def addCourse(conn, name, start_time, end_time, room):

    # get a cursor object. cursor object will help us run queries on the database
    cursor = conn.cursor()

    sql = "SELECT max(ID) FROM Course"
    try:
        cursor.execute(sql)
        data = cursor.fetchone()
        nextID = int(data[0]) + 1
    except:
        nextID = 1

    sql = "INSERT INTO Course VALUES (%s,%s,%s,%s)"
    params = (nextID, name, start_time, end_time, room)

    cursor.execute(sql, params)
    conn.commit()

    body = ""
    if cursor.rowcount > 0:
        body = "Add Course Succeeded."
    else:
        body = "Add Course Failed."

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

def updateRoom(conn, idNum, name, capacity):
    # get a cursor object. cursor object will help us run queries on the database
    cursor = conn.cursor()

    sql = "UPDATE Room SET name=%s WHERE id = %s"
    params = (name, capacity, idNum)

    cursor.execute(sql, params)
    conn.commit()

    if cursor.rowcount > 0:
        return "Update Room Succeeded."
    else:
        return "Update Room Failed."

################################################################################
def updateCourse(conn, idNum, name, start_time, end_time, room):

    # get a cursor object. cursor object will help us run queries on the database
    cursor = conn.cursor()

    sql = "UPDATE Course SET name=%s WHERE id = %s"
    params = (name, idNum, start_time, end_time, room)

    cursor.execute(sql, params)
    conn.commit()

    if cursor.rowcount > 0:
        return "Update Course Succeeded."
    else:
        return "Update Course Failed."

################################################################################
def deleteStudent(conn, idNum):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Student WHERE id = %s", (idNum,))
    conn.commit()
    if cursor.rowcount > 0:
        return "Delete Student Succeeded."
    else:
        return "Delete Student Failed."

def deleteRoom(conn, idNum):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Room WHERE id = %s", (idNum,))
    conn.commit()
    if cursor.rowcount > 0:
        return "Delete Room Succeeded."
    else:
        return "Delete Room Failed."

################################################################################
def deleteCourse(conn, idNum):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Course WHERE id = %s", (idNum,))
    conn.commit()
    if cursor.rowcount > 0:
        return "Delete Course Succeeded."
    else:
        return "Delete Course Failed."

def get_qs_post(env):
    """
    :param env: WSGI environment
    :returns: A tuple (qs, post), containing the query string and post data,
              respectively
    """
    # the environment variable CONTENT_LENGTH may be empty or missing
    try:
        request_body_size = int(env.get("CONTENT_LENGTH", 0))
    except (ValueError):
        request_body_size = 0
    # When the method is POST the variable will be sent
    # in the HTTP request body which is passed by the WSGI server
    # in the file like wsgi.input environment variable.
    request_body = env["wsgi.input"].read(request_body_size).decode("utf-8")
    post = parse_qs(request_body)
    return parse_qs(env["QUERY_STRING"]), post

def application(env, start_response):
    qs, post = get_qs_post(env)

    body = ""
    try:
        conn = psycopg2.connect(
            host="postgres",
            dbname=os.environ["POSTGRES_DB"],
            user=os.environ["POSTGRES_USER"],
            password=os.environ["POSTGRES_PASSWORD"],
        )
    except psycopg2.Warning as e:
        print(f"Database warning: {e}")
        body += "Check logs for DB warning"
    except psycopg2.Error as e:
        print(f"Database error: {e}")
        body += "Check logs for DB error"

    idNum = None
    if "idNum" in post:
        idNum = post["idNum"][0]
        ## handle case of starting to do an update -- show the form
        if "showUpdateStudentForm" in post and "idNum" in post:
            body += getUpdateStudentForm(conn, post["idNum"][0])
        ## handle case of completing an update
        elif "completeUpdate" in post:
            body += updateStudent(
                conn,
                idNum,
                post["name"][0],
            )
        ## handle case of showing a profile page
        if "updateStudent" in post:
            name = post["name"][0]
            body += updateStudent(conn, idNum, name)
        elif "deleteStudent" in post:
            body += deleteStudent(conn, idNum)
            idNum = None
    ## handle case of adding a profile page:
    elif "addStudent" in post:
        b, idNum = addStudent(
            conn,
            post["name"][0],
        )
        body += b
    elif "idNum" in qs:
        idNum = qs.get("idNum")[0]
    if idNum:
        # Finish by showing the profile page
        body += showStudentPage(conn, idNum)
    # default case: show all profiles
    else:
        body += showAllStudents(conn)
        body += showAddStudentForm()
        ######################################################### ROOM ###################################
    if "idNum" in post:
        idNum = post["idNum"][0]
        ## handle case of starting to do an update -- show the form
        if "showUpdateRoomForm" in post and "idNum" in post:
            body += getUpdateRoomForm(conn, post["idNum"][0])
        ## handle case of completing an update
        elif "completeUpdate" in post:
            body += updateRoom(
                conn,
                idNum,
                post["name"][0],
                post["capacity"][0],
            )
        ## handle case of showing a profile page
        if "updateRoom" in post:
            name = post["name"][0]
            capacity = post["capacity"][0]
            body += updateRoom(conn, idNum, name, capacity)
        elif "deleteRoom" in post:
            body += deleteRoom(conn, idNum)
            idNum = None
    ## handle case of adding a profile page:
    elif "addRoom" in post:
        b, idNum = addRoom(
            conn,
            post["name"][0],
            post["capacity"][0],
        )
        body += b
    elif "idNum" in qs:
        idNum = qs.get("idNum")[0]
    if idNum:
        # Finish by showing the profile page
        body += showRoomPage(conn, idNum)
    # default case: show all profiles
    else:
        body += showAllRoom(conn)
        body += showAddRoomForm()

        ######################################################### COURSE ###################################
    if "idNum" in post:
        idNum = post["idNum"][0]
        ## handle case of starting to do an update -- show the form
        if "showUpdateCourseForm" in post and "idNum" in post:
            body += getUpdateCourseForm(conn, post["idNum"][0])
        ## handle case of completing an update
        elif "completeUpdate" in post:
            body += updateCourse(
                conn,
                idNum,
                post["name"][0],
                post["start_time"][0],
                post["end_time"][0],
                post["room"][0],
            )
        ## handle case of showing a profile page
        if "updateCourse" in post:
            name = post["name"][0]
            start_time = post["start_time"][0]
            end_time = post["end_time"][0]
            room = post["room"][0]
            body += updateCourse(conn, idNum, name, start_time, end_time, room)
        elif "deleteCourse" in post:
            body += deleteCourse(conn, idNum)
            idNum = None
    ## handle case of adding a profile page:
    elif "addCourse" in post:
        b, idNum = addCourse(
            conn,
            post["name"][0],
            post["start_time"][0],
            post["end_time"][0],
            post["room"][0],
        )
        body += b
    elif "idNum" in qs:
        idNum = qs.get("idNum")[0]
    if idNum:
        # Finish by showing the profile page
        body += showCoursePage(conn, idNum)
    # default case: show all profiles
    else:
        body += showAllCourse(conn)
        body += showAddCourseForm()


    start_response("200 OK", [("Content-Type", "text/html")])
    return [wrapBody(body, title="University App").encode("utf-8")]

if __name__ == "__main__":
    main()
