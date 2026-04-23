from flask import Flask, request, redirect, render_template
import sqlite3
import string
import random
import os

app = Flask(__name__)

# -------------------------------
# DATABASE PATH FIX (IMPORTANT)
# -------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(app.instance_path, "urls.db")

# -------------------------------
# DATABASE SETUP
# -------------------------------
def init_db():
    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    # 🔥 IMPORTANT: NO UNIQUE constraint now
    c.execute('''
        CREATE TABLE IF NOT EXISTS URL (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            original_url TEXT,
            short_code TEXT,
            clicks INTEGER DEFAULT 0
        )
    ''')

    conn.commit()
    conn.close()
init_db()

# -------------------------------
# GENERATE SHORT CODE
# -------------------------------
def generate_code(length=6):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

# -------------------------------
# HOME ROUTE
# -------------------------------
@app.route('/', methods=['GET', 'POST'])
def index():
    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    short_url = None

    if request.method == 'POST':
        original_url = request.form['url']

        code = generate_code()

        # 🔥 ALWAYS INSERT (NO FAILURE NOW)
        c.execute("INSERT INTO URL (original_url, short_code) VALUES (?, ?)",
                  (original_url, code))
        conn.commit()

        print("Inserted:", original_url, code)  # DEBUG

        short_url = request.host_url + code

    # Fetch last 5 links
    c.execute("SELECT short_code FROM URL ORDER BY id DESC LIMIT 5")
    rows = c.fetchall()

    history = []
    for row in rows:
        history.append({
            "short": request.host_url + row[0]
        })

    conn.close()

    return render_template("index.html", short_url=short_url, history=history)

# -------------------------------
# REDIRECT ROUTE
# -------------------------------
@app.route('/<code>')
def redirect_url(code):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    c.execute("""
        SELECT id, original_url, clicks 
        FROM URL 
        WHERE short_code=? 
        ORDER BY id DESC LIMIT 1
    """, (code,))

    result = c.fetchone()

    if result is None:
        conn.close()
        return "URL not found"

    row_id, original_url, clicks = result

    # 🔥 FIX: handle NULL clicks
    if clicks is None:
        clicks = 0

    # 🔥 FIX: ensure valid URL
    if not original_url.startswith("http"):
        original_url = "http://" + original_url

    # update clicks
    c.execute("UPDATE URL SET clicks=? WHERE id=?", (clicks + 1, row_id))

    conn.commit()
    conn.close()

    return redirect(original_url)

# -------------------------------
# RUN APP
# -------------------------------
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)