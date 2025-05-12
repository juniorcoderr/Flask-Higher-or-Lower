## 🔢 Flask "Higher or Lower" Number Guessing Game 🎯

This is a fun and interactive web-based game built using **Python Flask**. The idea is simple: the server picks a **random number between 0 and 9**, and you try to guess it by typing a number in the URL. Depending on your guess, the app tells you whether it's **too low**, **too high**, or **correct**—all with amusing GIF responses!

This project is ideal for **beginners in Python and Flask**, and it demonstrates the core concepts of **web routing, dynamic URL parameters, HTML response handling**, and **random number generation**.

---

## 📌 How the Game Works

1. When you visit the root URL (`/`), you're prompted to guess a number between **0 and 9**.
2. You make a guess by appending the number to the URL.
   Example: `http://localhost:5000/5`
3. The Flask server checks the guessed number against a randomly generated number.
4. It responds with:

   * 📉 `Too low!` — if your guess is less than the target number
   * 📈 `Too high!` — if your guess is more than the target number
   * 🎉 `You found it!` — if your guess is correct
5. Each response is presented in HTML format with a fun GIF.

---

## 🚀 Live Demo

> Coming soon (if deployed)

---

## 🧠 Concepts and Features Explained

### 🔹 Flask Basics

* **Flask** is a lightweight web framework for Python.
* The `Flask` class is used to create the application instance:

  ```python
  app = Flask(__name__)
  ```

### 🔹 Routing and View Functions

* Flask uses the `@app.route()` decorator to define routes (URLs) and bind them to Python functions.

  ```python
  @app.route("/")
  def home():
      ...
  ```

* The route `"/<int:number>"` is a **dynamic route** which captures the number directly from the URL and passes it as an argument to the function.

  ```python
  @app.route("/<int:number>")
  def user_number(number):
      ...
  ```

### 🔹 Random Number Generation

* A number between 0 and 9 is generated when the server starts using:

  ```python
  random_number = random.randint(0, 9)
  ```

> ❗ Note: This number stays the same until the server restarts. It doesn’t change per request or user.

### 🔹 HTML in Flask Responses

* The game returns **HTML content directly as strings** from the route functions. It uses basic HTML tags and includes `<img>` tags for GIFs.

  Example:

  ```python
  return "<h1>Too low!</h1><img src='some_url'/>"
  ```

### 🔹 GIFs for User Engagement

* GIFs are included from online sources (Giphy) to make the game more engaging and enjoyable for users.

---

## 📂 Project Structure

```text
flask-number-guessing-game/
│
├── server.py          # Main Flask application
├── README.md          # Project documentation
├── requirements.txt   # (Optional) Python dependencies
```

---

## 🛠️ How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/juniorcoderr/flask-number-guessing-game.git
cd flask-number-guessing-game
```

### 2. (Optional) Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install flask
```

### 4. Run the Flask App

```bash
python server.py
```

### 5. Open in Browser

Navigate to:

```
http://127.0.0.1:5000/
```

Then try:

```
http://127.0.0.1:5000/3
```

---

## 📸 Screenshots

| Route             | Description              | Example                                                             |
| ----------------- | ------------------------ | ------------------------------------------------------------------- |
| `/`               | Prompt to guess a number | ![Prompt](https://media3.giphy.com/media/v1.Y2lk.../giphy.gif)      |
| `/2`              | Too Low                  | ![Low](https://media3.giphy.com/media/v1.Y2lk.../giphy.gif)         |
| `/8`              | Too High                 | ![High](https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif) |
| `/correct_number` | You found it!            | ![Win](https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif)       |

---

## 🔧 Possible Improvements

* 🔁 Add a reset feature for random number generation without restarting the server
* 🧠 Use session or cookies to maintain game state per user
* 🎨 Improve UI using templates (`Flask render_template`)
* 🌐 Deploy the game online using platforms like Render, Vercel, or Heroku

---

## 🤝 Contributing

Pull requests and suggestions are welcome! If you want to improve this game (UI, logic, or new features), feel free to fork the repo and open a PR.
