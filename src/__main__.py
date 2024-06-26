from uvicorn import run

from triple_des.create_app import create_app

if __name__ == "__main__":
    app = create_app()

    run(app, host="0.0.0.0")
