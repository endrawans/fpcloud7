from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_mysqldb import MySQL
from werkzeug.security import check_password_hash, generate_password_hash
import os

app = Flask(__name__)

#konfigurasi MySQL
app.secret_key = 'bebasaja'
app.config['MYSQL_HOST'] = 'webfpccc.mysql.database.azure.com'
app.config['MYSQL_USER'] = 'fpccweb'
app.config['MYSQL_PASSWORD'] = 'Bidot_store'  
app.config['MYSQL_DB'] = 'tokotopup'
app.config['MYSQL_PORT'] = 3306
mysql = MySQL(app)

# Registrasi
@app.route('/registrasi', methods=('GET','POST'))
def registrasi():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        level = request.form['level']

        # Cek Username atau Email
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM tb_users WHERE username=%s OR email=%s',(username, email,))
        akun = cursor.fetchone()
        if akun is None:
            cursor.execute('INSERT INTO tb_users VALUES (NULL, %s, %s, %s, %s)', (username, email, generate_password_hash(password), level))
            mysql.connection.commit()
            flash('Registrasi Berhasil', 'success')
        else:
            flash('Username atau email sudah ada', 'danger')
    return render_template('registrasi.html')

# login
@app.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Cek data Username
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM tb_users WHERE email=%s', (email,))
        akun = cursor.fetchone()
        if akun is None:
            flash('Login Gagal, Cek Username Anda', 'danger')
        elif not check_password_hash(akun[3], password):
            flash('Login Gagal, Cek Password Anda', 'danger')
        else:
            session['loggedin'] = True
            session['username'] = akun[1]
            session['level'] = akun[4]

            # Cek level pengguna
            if akun[4] == 'Admin':  # Jika level admin
                return redirect(url_for('admin'))
            else:
                return redirect(url_for('index'))
    return render_template('login.html')

# Route Admin
@app.route('/admin')
def admin():
    # Cek apakah user sudah login dan levelnya admin
    if 'loggedin' in session and session['level'] == 'Admin':
        # Query untuk menampilkan data dari tb_transaksi
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM tb_transaksi ORDER BY id_transaksi DESC")
        datatampil = cursor.fetchall()
        cursor.close()
        return render_template('admin.html', datapemesan=datatampil)
    else:
        flash('Akses ditolak! Halaman ini hanya dapat diakses oleh admin.', 'danger')
        return redirect(url_for('index'))

# Update
@app.route('/update', methods=['POST'])
def update():
    if request.method == 'POST':
        id_transaksi = request.form['id_transaksi']
        jproduk = request.form['jproduk']
        userId = request.form['userId']
        item = request.form['item']
        price = request.form['price']
        jumlah = request.form['jumlah']
        email = request.form['email']
        metode = request.form['metode']
        status = request.form['status']

        cursor = mysql.connection.cursor()
        cursor.execute("UPDATE tb_transaksi SET jproduk=%s, userId=%s, item=%s, price=%s, jumlah=%s, email=%s, metode=%s, status=%s WHERE id_transaksi=%s", 
            (jproduk, userId, item, price, jumlah, email, metode, status, id_transaksi,))
        mysql.connection.commit()
        flash('Status transaksi berhasil diperbarui', 'success')  # Pesan sukses
        return redirect(url_for('admin'))


#Delete
@app.route('/hapus/<int:id_transaksi>', methods=["GET"])
def hapus(id_transaksi):
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM tb_transaksi WHERE id_transaksi=%s",(id_transaksi,))
    mysql.connection.commit()
    flash('Data Berhasil Di Hapus', 'success')  # Pesan sukses
    return redirect(url_for('admin'))



# index
@app.route('/')
def index():
    if 'loggedin' in session:
        return render_template('index.html')
    flash('Harap Login dulu', 'danger')
    return redirect(url_for('login'))

# Logout
@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('username', None)
    session.pop('level', None)
    return redirect(url_for('login'))

# Free Fire
@app.route('/free fire', methods=['GET', 'POST'])
def free_fire():
    if 'loggedin' not in session:  # Check if the user is logged in
        flash('Harap login terlebih dahulu', 'danger')  # Flash a message
        return redirect(url_for('login'))  # Redirect to the login page

    if request.method == 'POST':
        jproduk = request.form['jproduk']
        userId = request.form['userId']
        item = request.form['item']
        price = request.form['price']
        jumlah = request.form['jumlah']
        email = request.form['email']
        metode = request.form['metode']

        cursor = mysql.connection.cursor()
        cursor.execute(
            'INSERT INTO tb_transaksi (jproduk, userId, item, price, jumlah, email, metode) VALUES(%s, %s, %s, %s, %s, %s, %s)',
            (jproduk, userId, item, price, jumlah, email, metode)
        )
        mysql.connection.commit()
        flash('Transaksi berhasil ditambahkan', 'success')  # Optional success message
        return redirect(url_for('free_fire'))

    return render_template('ff.html')

# Mobile Legends
@app.route('/mlbb', methods=['GET', 'POST'])
def mobile_legends():
    if 'loggedin' not in session:  # Check if the user is logged in
        flash('Harap login terlebih dahulu', 'danger')  # Flash a message
        return redirect(url_for('login'))  # Redirect to the login page

    if request.method == 'POST':
        jproduk = request.form['jproduk']
        userId = request.form['userId']
        item = request.form['item']
        price = request.form['price']
        jumlah = request.form['jumlah']
        email = request.form['email']
        metode = request.form['metode']

        cursor = mysql.connection.cursor()
        cursor.execute(
            'INSERT INTO tb_transaksi (jproduk, userId, item, price, jumlah, email, metode) VALUES(%s, %s, %s, %s, %s, %s, %s)',
            (jproduk, userId, item, price, jumlah, email, metode)
        )
        mysql.connection.commit()
        flash('Transaksi berhasil ditambahkan', 'success')  # Optional success message
        return redirect(url_for('mobile_legends'))

    return render_template('mlbb.html')

# Valorant
@app.route('/Valorant', methods=['GET', 'POST'])
def valorant():
    if 'loggedin' not in session:  # Check if the user is logged in
        flash('Harap login terlebih dahulu', 'danger')  # Flash a message
        return redirect(url_for('login'))  # Redirect to the login page

    if request.method == 'POST':
        jproduk = request.form['jproduk']
        userId = request.form['userId']
        item = request.form['item']
        price = request.form['price']
        jumlah = request.form['jumlah']
        email = request.form['email']
        metode = request.form['metode']

        cursor = mysql.connection.cursor()
        cursor.execute(
            'INSERT INTO tb_transaksi (jproduk, userId, item, price, jumlah, email, metode) VALUES(%s, %s, %s, %s, %s, %s, %s)',
            (jproduk, userId, item, price, jumlah, email, metode)
        )
        mysql.connection.commit()
        flash('Transaksi berhasil ditambahkan', 'success')  # Optional success message
        return redirect(url_for('valorant'))

    return render_template('valo.html')

# Call of Dutty Mobile
@app.route('/Call of Dutty Mobile', methods=['GET', 'POST'])
def codm():
    if 'loggedin' not in session:  # Check if the user is logged in
        flash('Harap login terlebih dahulu', 'danger')  # Flash a message
        return redirect(url_for('login'))  # Redirect to the login page

    if request.method == 'POST':
        jproduk = request.form['jproduk']
        userId = request.form['userId']
        item = request.form['item']
        price = request.form['price']
        jumlah = request.form['jumlah']
        email = request.form['email']
        metode = request.form['metode']

        cursor = mysql.connection.cursor()
        cursor.execute(
            'INSERT INTO tb_transaksi (jproduk, userId, item, price, jumlah, email, metode) VALUES(%s, %s, %s, %s, %s, %s, %s)',
            (jproduk, userId, item, price, jumlah, email, metode)
        )
        mysql.connection.commit()
        flash('Transaksi berhasil ditambahkan', 'success')  # Optional success message
        return redirect(url_for('codm'))

    return render_template('codm.html')

# PUBG
@app.route('/PUBG', methods=['GET', 'POST'])
def pubg():
    if 'loggedin' not in session:  # Check if the user is logged in
        flash('Harap login terlebih dahulu', 'danger')  # Flash a message
        return redirect(url_for('login'))  # Redirect to the login page

    if request.method == 'POST':
        jproduk = request.form['jproduk']
        userId = request.form['userId']
        item = request.form['item']
        price = request.form['price']
        jumlah = request.form['jumlah']
        email = request.form['email']
        metode = request.form['metode']

        cursor = mysql.connection.cursor()
        cursor.execute(
            'INSERT INTO tb_transaksi (jproduk, userId, item, price, jumlah, email, metode) VALUES(%s, %s, %s, %s, %s, %s, %s)',
            (jproduk, userId, item, price, jumlah, email, metode)
        )
        mysql.connection.commit()
        flash('Transaksi berhasil ditambahkan', 'success')  # Optional success message
        return redirect(url_for('pubg'))

    return render_template('pubg.html')


# Genshin
@app.route('/Genshin Impact', methods=['GET', 'POST'])
def genshin():
    if 'loggedin' not in session:  # Check if the user is logged in
        flash('Harap login terlebih dahulu', 'danger')  # Flash a message
        return redirect(url_for('login'))  # Redirect to the login page

    if request.method == 'POST':
        jproduk = request.form['jproduk']
        userId = request.form['userId']
        item = request.form['item']
        price = request.form['price']
        jumlah = request.form['jumlah']
        email = request.form['email']
        metode = request.form['metode']

        cursor = mysql.connection.cursor()
        cursor.execute(
            'INSERT INTO tb_transaksi (jproduk, userId, item, price, jumlah, email, metode) VALUES(%s, %s, %s, %s, %s, %s, %s)',
            (jproduk, userId, item, price, jumlah, email, metode)
        )
        mysql.connection.commit()
        flash('Transaksi berhasil ditambahkan', 'success')  # Optional success message
        return redirect(url_for('genshin'))

    return render_template('genshin.html')

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
