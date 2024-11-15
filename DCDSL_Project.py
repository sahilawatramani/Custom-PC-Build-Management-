from flask import Flask, render_template, request, redirect, url_for, flash, session
import mysql.connector

app = Flask(__name__)

app.secret_key = "your_secret_key"  

def get_db_connection():
    conn = mysql.connector.connect(
        host='localhost',           
        user='root',                
        password='Sahil@02022005',  
        database='custom_pc_builder' 
    )
    return conn

@app.route('/')
def index():
    if 'username' not in session:
        return redirect(url_for('login'))  

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM pc_build')
    builds = cursor.fetchall()
    cursor.close()
    conn.close()
    
    return render_template('index.html', builds=builds)

@app.route('/create_build', methods=('GET', 'POST'))
def create_build():
    if 'username' not in session:
        return redirect(url_for('login'))  
    
    if request.method == 'POST':
        cpu_id = request.form['cpu_id']
        gpu_id = request.form['gpu_id']
        ram_id = request.form['ram_id']
        psu_id = request.form['psu_id']
        mon_id = request.form['mon_id']
        mb_id = request.form['mb_id']
        str_id = request.form['str_id']
        total_price = request.form['total_price']

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO pc_build (cpu_id, gpu_id, ram_id, psu_id, mon_id, mb_id, str_id, total_price) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)',
            (cpu_id, gpu_id, ram_id, psu_id, mon_id, mb_id, str_id, total_price)
        )
        conn.commit()
        cursor.close()
        conn.close()
        flash('PC Build created successfully!', 'success')
        return redirect(url_for('index'))  

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute('SELECT * FROM cpu')
    cpus = cursor.fetchall()

    cursor.execute('SELECT * FROM gpu')
    gpus = cursor.fetchall()

    cursor.execute('SELECT * FROM ram')
    rams = cursor.fetchall()

    cursor.execute('SELECT * FROM power_supply')
    psus = cursor.fetchall()

    cursor.execute('SELECT * FROM monitor')
    monitors = cursor.fetchall()

    cursor.execute('SELECT * FROM motherboard')
    motherboards = cursor.fetchall()

    cursor.execute('SELECT * FROM storage')
    storages = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template('create_build.html', cpus=cpus, gpus=gpus, rams=rams, psus=psus, monitors=monitors, motherboards=motherboards, storages=storages)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute('SELECT * FROM users WHERE username = %s AND password = %s', (username, password))
        user = cursor.fetchone()
        cursor.close()
        conn.close()

        if user:
            session['username'] = username  
            flash('Login successful!', 'success')
            return redirect(url_for('index'))  
        else:
            flash('Invalid username or password', 'error')
            return redirect(url_for('login'))  

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)  
    flash('You have been logged out.', 'info')
    return redirect(url_for('login'))  

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute('SELECT * FROM users WHERE username = %s', (username,))
        user = cursor.fetchone()

        if user:
            flash('Username already exists. Please choose a different username.', 'error')
        else:
            
            cursor.execute('INSERT INTO users (username, password) VALUES (%s, %s)', (username, password))
            conn.commit()
            cursor.close()
            conn.close()
            flash('Account created successfully! Please log in.', 'success')
            return redirect(url_for('login'))

    return render_template('register.html')


if __name__ == '__main__':
    app.run(debug=True)
