# Abstraction in Python (Two Small Projects)

This project shows how **abstraction** works in Python using two simple examples.

---

## 1. Notification Sender (`abstraction_1.py`)

This program sends notifications in two ways:

- Email
- SMS

Each class has:

- One public method: `send_notification(message)`
- Other steps like connecting and formatting are hidden using private methods

### Example Output:

connecting to smtp server
preparing email
hello
message sent

------------SMS----------
Connecting to SMS gateway
Formatting SMS: Hi, your OTP is 101010
SMS sent

---

## 2. Shape Area Calculator (`abstraction_2.py`)

This program calculates the area of:

- A Circle
- A Rectangle

It uses an **abstract class** so every shape must have a method called `calculate_area()`.

### Example Output:

area of a circle is : 78.53981633974483
Area of a Rectangle is : 50
