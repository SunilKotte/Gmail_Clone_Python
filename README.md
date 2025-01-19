# Gmail Clone Backend

This README explains the design and implementation of a basic backend system for a Gmail clone. The project focuses on key functionalities such as sending emails, uploading attachments, and scheduling meetings. We also adhere to **SOLID principles** for clean code design and use **Data Structures and Algorithms (DSA)** concepts for efficient functionality.

---

## **SOLID Principles**

### **1. Single Responsibility Principle (SRP)**
- **Definition:** Each class or module should have one responsibility and one reason to change.
- **Application in the Project:**
  - **MailSender**: Handles email-sending logic.
  - **FileUploader**: Manages file upload and storage.
  - **Scheduler**: Handles meeting scheduling based on user availability.

### **2. Open/Closed Principle (OCP)**
- **Definition:** Code should be open for extension but closed for modification.
- **Application in the Project:**
  - New features, like scheduling recurring emails, can be added without modifying the existing `MailSender` class. Instead, we extend it.

### **3. Liskov Substitution Principle (LSP)**
- **Definition:** Subclasses should be replaceable with their parent classes without breaking functionality.
- **Application in the Project:**
  - `BasicEmailSender` can be replaced by `ScheduledEmailSender`, ensuring compatibility with existing email-sending features.

### **4. Interface Segregation Principle (ISP)**
- **Definition:** Classes should not be forced to implement methods they do not use.
- **Application in the Project:**
  - Separate interfaces for `FileUploader` (file management) and `Scheduler` (meeting scheduling) avoid unnecessary coupling.

### **5. Dependency Inversion Principle (DIP)**
- **Definition:** High-level modules should depend on abstractions rather than low-level modules.
- **Application in the Project:**
  - Use a generic `StorageService` interface for file uploads, which can be implemented for local or cloud storage (e.g., AWS S3).

---

## **How DSA Concepts Are Used**

### **1. Queue (FIFO)**
- **Usage:**
  - Emails scheduled for future delivery are added to a queue and processed in order.
- **Implementation Example:**
  ```python
  email_queue = deque()
  email_queue.append((send_at, sender, recipient, subject, body))
  email_queue.popleft()
  ```

### **2. Hashing**
- **Usage:**
  - Generate unique IDs for file attachments to avoid collisions.
- **Implementation Example:**
  ```python
  file_hash = hashlib.sha256(file.read()).hexdigest()
  file_storage[file_hash] = file.filename
  ```

### **3. Graphs**
- **Usage:**
  - Represent user availability for meeting scheduling.
  - Nodes represent users, and edges represent shared availability slots.

### **4. Priority Queue (Heap)**
- **Usage:**
  - Emails or tasks can be prioritized based on urgency or deadlines.

### **5. Linked List**
- **Usage:**
  - Manage email draft history to enable undo/redo functionality.

---

## **Folder Structure**

Here is the recommended folder structure for the backend:

```
project_root/
|
|-- app.py                  # Main Flask application
|-- requirements.txt        # Dependencies
|-- README.md               # Project documentation (this file)
|
|-- modules/                # Application modules
|   |-- mail_sender.py      # Mail sending logic
|   |-- file_uploader.py    # File upload logic
|   |-- scheduler.py        # Meeting scheduling logic
|
|-- static/                 # Static files (if needed)
|
|-- templates/              # HTML templates (if needed)
|
|-- utils/                  # Utility functions
|   |-- hashing.py          # Hashing utility
|   |-- queue_handler.py    # Queue management logic
|
|-- tests/                  # Test cases
    |-- test_mail_sender.py # Tests for MailSender
    |-- test_scheduler.py   # Tests for Scheduler
```

---

## **Features and Implementation**

### **1. Sending Emails**
- **Route:** `/send_email`
- **Functionality:** Send an email by providing sender, recipient, subject, and body.
- **Example Code:**
  ```python
  @app.route('/send_email', methods=['POST'])
  def send_email():
      data = request.get_json()
      sender = data.get("sender")
      recipient = data.get("recipient")
      subject = data.get("subject")
      body = data.get("body")

      return jsonify({"message": f"Email sent to {recipient} by {sender}!"}), 200
  ```

### **2. Scheduling Emails**
- **Route:** `/schedule_email`
- **Functionality:** Add emails to a queue for future delivery.
- **Example Code:**
  ```python
  @app.route('/schedule_email', methods=['POST'])
  def schedule_email():
      email_queue.append((send_at, sender, recipient, subject, body))
      return jsonify({"message": "Email scheduled successfully!"}), 201
  ```

### **3. Uploading Attachments**
- **Route:** `/upload_file`
- **Functionality:** Upload a file and store it with a unique hash.
- **Example Code:**
  ```python
  @app.route('/upload_file', methods=['POST'])
  def upload_file():
      file = request.files.get("file")
      file_hash = hashlib.sha256(file.read()).hexdigest()
      file_storage[file_hash] = file.filename
      return jsonify({"message": "File uploaded successfully!", "file_id": file_hash}), 201
  ```

### **4. Scheduling Meetings**
- **Route:** `/schedule_meeting`
- **Functionality:** Schedule a meeting based on user availability.
- **Example Code:**
  ```python
  @app.route('/schedule_meeting', methods=['POST'])
  def schedule_meeting():
      data = request.get_json()
      user1 = data.get("user1")
      user2 = data.get("user2")
      time_slot = data.get("time_slot")

      if user_availability[user1][time_slot] == "available" and user_availability[user2][time_slot] == "available":
          user_availability[user1][time_slot] = "busy"
          user_availability[user2][time_slot] = "busy"
          return jsonify({"message": f"Meeting scheduled at {time_slot}!"}), 200

      return jsonify({"message": "Time slot not available"}), 409
  ```

---
