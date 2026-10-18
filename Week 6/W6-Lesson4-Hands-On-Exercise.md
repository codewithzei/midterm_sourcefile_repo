# W6 - Lesson 4 - Activity: Mini Student Profile App

#### Prepared by: Jackson S. Soriano, MIT

### Objectives

Create a simple console program that behaves like a very small web application. The program will use Flask-inspired names and structure, but **Flask is not required**.

Your program will have:

- An `app` object
- Route paths such as `/` and `/profile`
- HTML-like strings as page responses
- An `app.run()` method

The activity applies the important OOP concepts from the lesson: classes, objects, attributes, methods, `self`, constructors, multiple classes, and inheritance.

---

## Program Scenario

Develop a **Mini Student Profile App** that displays a home page and an IT student profile.

The program must use three classes:

1. `Student` - parent class containing basic student information
2. `ITStudent` - child class containing an additional programming skill
3. `StudentApp` - application class that handles route paths and displays page content

---

## Program Requirements

### Part A: Student Parent Class - 7 points

Create a class named `Student`.

1. Add a constructor with the following parameters:

   - `name`
   - `course`
   - `year_level`

2. Store each value in an instance attribute using `self`.
3. Add a method named `get_profile()`.
4. The method must return an HTML-like student profile.

Example return value:

```html
<h2>Ana Cruz</h2>
<p>Course: BS Information Technology</p>
<p>Year Level: 2</p>
```

### Part B: ITStudent Child Class - 5 points

Create a child class named `ITStudent` that inherits from `Student`.

1. Add a class attribute named `skill` with a programming skill as its value.
2. Add a method named `get_skill()`.
3. The method must return the skill using an HTML-like paragraph.

Example:

```html
<p>Programming Skill: Python</p>
```

The child object must be able to use both:

- The inherited `get_profile()` method
- Its own `get_skill()` method

### Part C: StudentApp Class - 8 points

Create a class named `StudentApp`.

1. Its constructor must receive:

   - `title`
   - `student`

2. Create a method named `route(path)`.
3. Use an `if-elif-else` statement to process these routes:

| Route | Returned content |
| --- | --- |
| `/` | Application title inside an `<h1>` tag |
| `/profile` | Student profile and programming skill |
| Any other route | `<h1>404 - Page Not Found</h1>` |

4. Create a method named `run()` that prints the application name and the content returned by the routes.

### Part D: Object Creation and Execution - 5 points

1. Create one `ITStudent` object.
2. Create one `StudentApp` object named `app`.
3. Pass the student object to the application object.
4. Call `app.run()`.

The final portion of your program should resemble this Flask-style structure:

```python
student = ITStudent("Ana Cruz", "BS Information Technology", 2)
app = StudentApp("PSU Student Profile App", student)
app.run()
```

### Part E: Code Quality and Output - 5 points

- Use meaningful class, method, and variable names.
- Apply correct indentation.
- Add short comments to important code blocks.
- Produce complete and readable output.
- Run the program without syntax or runtime errors.

---

## Starter Code

Complete the missing parts marked with `TODO`.

```python
# Parent class for basic student information.
class Student:
    def __init__(self, name, course, year_level):
        # TODO: Store the three values in instance attributes.
        pass

    def get_profile(self):
        # TODO: Return the student's information using HTML-like tags.
        pass


# Child class for an IT student.
class ITStudent(Student):
    # TODO: Create a class attribute named skill.
    pass

    def get_skill(self):
        # TODO: Return the programming skill using a <p> tag.
        pass


# Application class with Flask-inspired routes.
class StudentApp:
    def __init__(self, title, student):
        # TODO: Store the title and student object.
        pass

    def route(self, path):
        # TODO: Return the correct content for /, /profile, or an invalid route.
        pass

    def run(self):
        # TODO: Print the app title and test the required routes.
        pass


# Create the student and application objects.
# TODO: Replace the sample information with your own information.
student = ITStudent("Your Name", "BS Information Technology", 2)
app = StudentApp("Student Profile App", student)

# Start the application.
app.run()
```

---

## Expected Output Format

Your exact student information may be different, but the program should produce an output similar to this:

```text
Running: PSU Student Profile App

GET /
<h1>PSU Student Profile App</h1>

GET /profile
<h2>Ana Cruz</h2>
<p>Course: BS Information Technology</p>
<p>Year Level: 2</p>
<p>Programming Skill: Python</p>

GET /unknown
<h1>404 - Page Not Found</h1>
```

---

## Scoring Rubric

| Criterion | Points |
| --- | ---: |
| `Student` class, constructor, attributes, and `get_profile()` | 7 |
| `ITStudent` inheritance, `skill`, and `get_skill()` | 5 |
| `StudentApp` constructor, routes, and `run()` | 8 |
| Correct object creation and `app.run()` execution | 5 |
| Code quality, comments, correct output, and error-free execution | 5 |
| **Total** | **30** |

---

## Turn-In Rquirements

1. Save the program as `fullname_student_profile_app.py` or `.txt`.
2. Screenshot showing the complete console output (1-3 pictures)
3. Youtube Link of Video Demo (max of 3 minutes)
4. A short reflection the challenges and learnings in accomplishing the exercise.

---

