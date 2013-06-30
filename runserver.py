from app import App
import config
app = App(config)

if __name__ == "__main__":
    app.run(debug=True)
