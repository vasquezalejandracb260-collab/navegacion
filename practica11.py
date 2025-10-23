import tkinter as tk

def abrir_login(ventana_inicio):
    ventana_inicio.withdraw()
    login = tk.Toplevel()
    login.title("Login")
    login.geometry("300x250")

    tk.Label(login, text="Usuario:").pack()
    entrada_usuario = tk.Entry(login)
    entrada_usuario.pack()

    tk.Label(login, text="Contraseña:").pack()
    entrada_contra = tk.Entry(login, show="*")
    entrada_contra.pack()

    mensaje = tk.Label(login, text="")
    mensaje.pack()

    def iniciar_sesion():
        usuario = entrada_usuario.get()
        contra = entrada_contra.get()
        if usuario == "" :
            mensaje.config(text="Por favor completa todos los campos")
        else:
            mensaje.config(text="Inicio de sesión en proceso")

    def recuperar_contra():
        mensaje.config(text="Te ayudaremos a recuperar tu contraseña")

    tk.Button(login, text="Iniciar Sesion", command=iniciar_sesion).pack(pady=5)
    tk.Button(login, text="¿Olvidaste tu contraseña?", command=recuperar_contra).pack()

    tk.Button(login, text="Volver", command=lambda: volver(ventana_inicio, login)).pack(pady=10)

def abrir_contacto(ventana_inicio):
    ventana_inicio.withdraw()
    contacto = tk.Toplevel()
    contacto.title("Contacto")
    contacto.geometry("300x350")

    tk.Label(contacto, text="Tu nombre o correo:").pack()
    entrada_nombre = tk.Entry(contacto)
    entrada_nombre.pack()

    tk.Label(contacto, text="Tu mensaje:").pack()
    entrada_mensaje = tk.Text(contacto, height=5, width=30)
    entrada_mensaje.pack()

    mensaje = tk.Label(contacto, text="")
    mensaje.pack()

    def enviar():
        nombre = entrada_nombre.get()
        texto = entrada_mensaje.get("1.0", tk.END).strip()
        if nombre == "" :
            mensaje.config(text="Por favor completa todos los campos")
        else:
            mensaje.config(text="Mensaje enviado")
            entrada_nombre.delete(0, tk.END)
            entrada_mensaje.delete("1.0", tk.END)

    tk.Button(contacto, text="Enviar", command=enviar).pack(pady=5)

    tk.Label(contacto, text="Soporte Tecnico").pack()
    tk.Label(contacto, text="Email: FoodVibe_Soporte@gnail.com").pack()
    tk.Label(contacto, text="Tel: 1345678902").pack()

    tk.Button(contacto, text="Volver", command=lambda: volver(ventana_inicio, contacto)).pack(pady=10)

def volver(ventana_anterior, ventana_actual):
    ventana_actual.destroy()
    ventana_anterior.deiconify()

def main():
    ventana = tk.Tk()
    ventana.title("Empresa XYZ")
    ventana.geometry("400x400")

    tk.Label(ventana, text="Misión").pack()
    tk.Label(ventana, text="Ayudar a las personas con comidas de calidad y precios accesibles.").pack()

    tk.Label(ventana, text="Visión").pack()
    tk.Label(ventana, text="Ser un restaurante confiable y util.").pack()

    tk.Label(ventana, text="Correo: FoodVibe@gmail.com").pack()
    tk.Label(ventana, text="Av. 117 Pte. 706, Guadalupe Hidalgo").pack()

    tk.Label(ventana, text="Codigo Postal:").pack()
    entrada_cp = tk.Entry(ventana)
    entrada_cp.pack()

    mensaje_cp = tk.Label(ventana, text="")
    mensaje_cp.pack()

    def mostrar_cp():
        cp = entrada_cp.get()
        if cp == "":
            mensaje_cp.config(text="Escribe tu código postal")
        else:
            mensaje_cp.config(text="Codigo postal guardado")

    tk.Button(ventana, text="Guardar Codigo Postal", command=mostrar_cp).pack(pady=5)
    tk.Button(ventana, text="Ir a Login", command=lambda: abrir_login(ventana)).pack(pady=5)
    tk.Button(ventana, text="Formulario de Contacto", command=lambda: abrir_contacto(ventana)).pack()

    ventana.mainloop()

if __name__ == "__main__":
    main()