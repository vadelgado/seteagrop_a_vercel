from application import create_app

app = create_app()
app.config['WTF_CSRF_ENABLED'] = False

if __name__ == '__main__':
    try:
        port = 8000
        app.run(port=port, debug=True)
        print(f"La aplicación se está ejecutando en el puerto {port}")
    except ImportError as e:
        print(f"Error al ejecutar la aplicación: {str(e)}")
    finally:
        print("La aplicación ha finalizado.")

