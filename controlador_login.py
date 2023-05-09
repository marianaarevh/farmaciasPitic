from bd import obtener_conexion
from flask import Flask, render_template, request, redirect, flash, session



def login():
    conexion = obtener_conexion()
    if 'conectado' in session:
        return render_template('dashboard.html')
    else:
        msg = ''
        if request.method == 'POST' and 'username' in request.form and 'contrasena' in request.form:
            username = request.form['username']
            contrasena = request.form['contrasena']
            
            # Comprobando si existe una cuenta
            cursor = conexion.cursor(dictionary=True)
            cursor.execute("SELECT * FROM login_python WHERE username = %s", [username])
            account = cursor.fetchone()

            if account:
                if (account['contrasena']==contrasena):
                    # Crear datos de sesión, para poder acceder a estos datos en otras rutas 
                    session['conectado']        = True
                    session['id']               = account['id']
                    session['username']        = account['username']
                    session['nombre']           = account['nombre']
                    session['apellido']         = account['apellido']

                    msg = "Ha iniciado sesión correctamente."
                    return render_template('dashboard.html', msjAlert = msg, typeAlert=1)                    
                else:
                    msg = 'Datos incorrectos, por favor verfique!'
                    return render_template('login.html', msjAlert = msg, typeAlert=0)
            else:
                return render_template('login.html', msjAlert = msg, typeAlert=0)
    return render_template('login.html', msjAlert = 'Debe iniciar sesión.', typeAlert=0)