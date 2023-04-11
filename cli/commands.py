# cli/commands.py
import click
from uvicorn import run
import code
import subprocess
import os
import signal

from app.main import app

DEFAULT_HOST = '127.0.0.1'
DEFAULT_PORT = 8000

@click.group()
def cli():
    pass

@cli.command()
@click.option('--host', default=DEFAULT_HOST, help='Host to bind the server to.')
@click.option('--port', default=DEFAULT_PORT, help='Port to bind the server to.')
def runserver(host: str, port: int):
    click.echo(f'Starting server on http://{host}:{port}')
    run(app, host=host, port=port)

@cli.command()
def shell():
    from app.core.config import settings
    
    shell_locals = dict(globals(), **locals())
    shell_locals['settings'] = settings
    
    try:
        import IPython
        IPython.start_ipython(argv=[], user_ns=shell_locals)
    except ImportError:
        code.interact(local=dict(globals(), **locals()))


@cli.command()
def initdb():
    from app.db.session import engine
    from app.db.models import Base
    click.echo("Creating database tables...")
    Base.metadata.create_all(bind=engine)
    click.echo("Database tables created.")

@cli.group()
def alembic():
    pass

@alembic.command()
def revision():
    subprocess.run(['alembic', 'revision', '--autogenerate'])

@alembic.command()
def upgrade():
    subprocess.run(['alembic', 'upgrade', 'head'])

@alembic.command()
def downgrade():
    subprocess.run(['alembic', 'downgrade', '-1'])

@cli.command()
def test():
    click.echo("Running tests...")
    result = subprocess.run(['pytest'])
    if result.returncode != 0:
        click.echo(click.style("Tests failed.", fg="red"))
    else:
        click.echo(click.style("All tests passed.", fg="green"))

@cli.command()
@click.option('--host', default=DEFAULT_HOST, help='Host to bind the server to.')
@click.option('--port', default=DEFAULT_PORT, help='Port to bind the server to.')
def profile(host: str, port: int):
    click.echo(f'Profiling server on http://{host}:{port}')

    server_process = subprocess.Popen(
        ['uvicorn', 'app.main:app', f'--host={host}', f'--port={port}']
    )
    profiler_process = subprocess.Popen(['py-spy', 'top', f'--pid={server_process.pid}'])

    try:
        profiler_process.wait()
    except KeyboardInterrupt:
        pass
    finally:
        os.kill(server_process.pid, signal.SIGTERM)
        server_process.wait()

if __name__ == '__main__':
    cli()
