class Contacto:
    def __init__(self, nombre, telefono, email):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email

class Agenda:
    def __init__(self):
        self.contactos = []

    def agregar_contacto(self, nombre, telefono, email):
        contacto = Contacto(nombre, telefono, email)
        self.contactos.append(contacto)

    def mostrar_contactos(self):
        if not self.contactos:
            print("La agenda está vacía.")
        else:
            print("Lista de contactos:")
            for i, contacto in enumerate(self.contactos, start=1):
                print(f"{i}. Nombre: {contacto.nombre}, Teléfono: {contacto.telefono}, Email: {contacto.email}")

    def buscar_contacto(self, nombre):
        for contacto in self.contactos:
            if contacto.nombre == nombre:
                print(f"Contacto encontrado - Nombre: {contacto.nombre}, Teléfono: {contacto.telefono}, Email: {contacto.email}")
                return
        print(f"Contacto no encontrado: {nombre}")

    def editar_contacto(self, nombre, nuevo_nombre, nuevo_telefono, nuevo_email):
        for contacto in self.contactos:
            if contacto.nombre == nombre:
                contacto.nombre = nuevo_nombre
                contacto.telefono = nuevo_telefono
                contacto.email = nuevo_email
                print(f"Contacto editado correctamente.")
                return
        print(f"Contacto no encontrado: {nombre}")

    def menu(self):
        while True:
            print("\nMenú de Agenda:")
            print("1. Añadir contacto")
            print("2. Lista de contactos")
            print("3. Buscar contacto")
            print("4. Editar contacto")
            print("5. Cerrar agenda")

            opcion = input("Ingrese el número de la opción deseada: ")

            if opcion == "1":
                nombre = input("Nombre: ")
                telefono = input("Teléfono: ")
                email = input("Email: ")
                self.agregar_contacto(nombre, telefono, email)
            elif opcion == "2":
                self.mostrar_contactos()
            elif opcion == "3":
                nombre = input("Nombre a buscar: ")
                self.buscar_contacto(nombre)
            elif opcion == "4":
                nombre = input("Nombre a editar: ")
                nuevo_nombre = input("Nuevo nombre: ")
                nuevo_telefono = input("Nuevo teléfono: ")
                nuevo_email = input("Nuevo email: ")
                self.editar_contacto(nombre, nuevo_nombre, nuevo_telefono, nuevo_email)
            elif opcion == "5":
                print("Agenda cerrada.")
                break
            else:
                print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    agenda = Agenda()
    agenda.menu()
