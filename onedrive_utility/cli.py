import os
import click
from .client import Client

class Context(object):
    def __init__(self):
        self.verbose = False
        self.home = os.getcwd()
        self.session_cache = os.path.expanduser('~/.li_onedrive_session')
        self.config = os.path.expanduser('~/.li_onedrive')

    def get_client(self):
        with open(self.config) as file:
            tokens = file.read().split('\n')
            return {'client_id': tokens[0], 'client_secret': tokens[1]}


pass_context = click.make_pass_decorator(Context, ensure=True)


@click.group(context_settings=dict(help_option_names=['-h', '--help']))
@pass_context
def cli(ctx):
    pass


@cli.command()
@click.option('--client-secret', required=True, help='Application secret')
@click.option('--client-id', required=True, help='Application id')
@pass_context
def init(ctx, client_id, client_secret):
    with open(ctx.config, 'w') as file:
        file.write('{client_id}\n{client_secret}'.format(client_id=client_id, client_secret=client_secret))

    client = Client(client_id, client_secret)
    client.authenticate(cache=ctx.session_cache)


@cli.command()
@pass_context
def authenticate(ctx):
    client_info = ctx.get_client()
    client = Client(client_info['client_id'], client_info['client_secret'])
    client.authenticate(cache=ctx.session_cache)


@cli.command()
@click.option('--out', required=False, default="file.out", help='Output file name')
@click.option('-p', required=False, default=False, is_flag=True, help='Print data to output stream')
@click.argument('path', required=True)
@pass_context
def download(ctx, path, out, p):
    client_info = ctx.get_client()
    client = Client(client_info['client_id'], client_info['client_secret'])
    client.load_session(ctx.session_cache)
    onedrive_client = client.get_onedrive_client()
    onedrive_client.item(drive='me', path=path).download(out)

    if p:
        with open(out) as file:
            click.echo(file.read())


def main():
    cli()


if __name__ == "__main__":
    cli()
